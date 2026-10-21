---
url: https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-domains/
title: Restrict identities with domain-restricted sharing \u00a0|\u00a0 Organization Policy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:31:11.039165+00:00
---

# Restrict identities with domain-restricted sharing  |  Organization Policy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-domains/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Organization Policy ](https://docs.cloud.google.com/organization-policy)
  * [ Guides ](https://docs.cloud.google.com/organization-policy/overview)



Send feedback 

#  Restrict identities with domain-restricted sharing Stay organized with collections  Save and categorize content based on your preferences. 

Domain-restricted sharing lets you limit resource sharing based on a domain or organization resource. When domain-restricted sharing is active, only principals that belong to allowed domains or organizations can be granted IAM roles in your Google Cloud organization.

**Note** : If your organization was created on or after May 3, 2024, then the `iam.allowedPolicyMemberDomains` legacy managed constraint is enforced by default, with your domain listed as the only allowed value. 

There are three types of organization policies that you can use to restrict identities by domain:

  * The `iam.managed.allowedPolicyMembers` managed constraint
  * Custom organization policies referencing the `iam.googleapis.com/AllowPolicy` resource
  * The `iam.allowedPolicyMemberDomains` legacy managed constraint



## Before you begin

Choose which method you will use to implement domain-restricted sharing. To learn more about the benefits and drawbacks of each method, see [Methods for restricting sharing by domain](https://docs.cloud.google.com/organization-policy/domain-restricted-sharing#drs-methods).

### Required roles

To get the permissions that you need to enforce domain-restricted sharing, ask your administrator to grant you the [Organization policy administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/orgpolicy#orgpolicy.policyAdmin) (`roles/orgpolicy.policyAdmin`) IAM role on the organization. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Use the `iam.managed.allowedPolicyMembers` constraint to implement domain-restricted sharing

###  Console 

  1. In the Google Cloud console, go to the **Organization policies** page.

[Go to Organization policies](https://console.cloud.google.com/iam-admin/orgpolicies)

  2. From the project picker, select the project, folder, or organization for which you want to edit the organization policy. The **Organization policies** page that appears displays a filterable list of organization policy constraints that are available for this resource.

  3. From the list, select the **Restrict allowed policy members in IAM allow policies** managed constraint.

  4. On the **Policy details** page, click **Manage policy**.

  5. On the **Edit policy** page, select **Override parent's policy**.

  6. Select **Add a rule** and then update the organization policy rule.

  7. Under **Enforcement** , select **On**.

  8. Optionally, to make the organization policy conditional on a tag, click **Add condition**. If you add a conditional rule to an organization policy, you must add at least one unconditional rule or the policy cannot be saved. For more details, see [Scope organization policies with tags](https://docs.cloud.google.com/organization-policy/scope-policies).

  9. In the **Parameters** section, configure the members and principal sets that you want to grant roles to in your organization, and then click **Save**.

  10. Optionally, to preview the effect of your organization policy change before it is enforced, click **Test changes**. For more information about testing organization policy changes, see [Test organization policy changes with Policy Simulator](https://docs.cloud.google.com/policy-intelligence/docs/test-organization-policies).

  11. To enforce the organization policy in dry-run mode, click **Set dry run policy**. For more information, see [Test organization policies](https://docs.cloud.google.com/organization-policy/test-policies).

  12. After you verify that the organization policy in dry-run mode works as intended, set the live policy by clicking **Set policy**.




###  gcloud 

  1. Create a YAML file to define the organization policy:
         
         name: organizations/ORG_ID/policies/iam.managed.allowedPolicyMembers
         spec:
         rules:
          - enforce: true
            parameters:
              allowedMemberSubjects:
                - ALLOWED_MEMBER_1
                - ALLOWED_MEMBER_2
              allowedPrincipalSets:
                - ALLOWED_PRINCIPAL_SET_1
                - ALLOWED_PRINCIPAL_SET_2
         

Replace the following:

     * `ORG_ID`: the numeric ID of your Google Cloud organization.

     * `ALLOWED_MEMBER_1`, `ALLOWED_MEMBER_2`: The members that you want to grant roles to in your organization—for example, `user:example-user@example.com`.

     * `ALLOWED_PRINCIPAL_SET_1`, `ALLOWED_PRINCIPAL_SET_2`: The principal sets that you want to grant roles to in your organization. For example, `//cloudresourcemanager.googleapis.com/organizations/0123456789012`.

Optionally, to make the organization policy conditional on a tag, add a `condition` block to the `rules`. If you add a conditional rule to an organization policy, you must add at least one unconditional rule or the policy cannot be saved. For more details, see [Scope organization policies with tags](https://docs.cloud.google.com/organization-policy/scope-policies).

  2. Set the policy with the `org-policies set-policy` command and the `spec` flag:
         
         gcloud org-policies set-policy POLICY_PATH \
           --update-mask=spec
         

Replace `POLICY_PATH` with the full path to your organization policy YAML file.




To learn how to test the policy in dry-run mode before applying it, see [Test organization policies](https://docs.cloud.google.com/organization-policy/test-policies).

To learn how to simulate the policy before you enforce it, see [Test organization policy changes with Policy Simulator](https://docs.cloud.google.com/policy-intelligence/docs/test-organization-policies).

###  REST 

To set the organization policy, use the [`organizations.policies.create`](https://docs.cloud.google.com/resource-manager/docs/reference/orgpolicy/rest/v2/organizations.policies/create) method.
    
    
    POST https://orgpolicy.googleapis.com/v2/{parent=organizations/ORGANIZATION_ID}/policies
    

The request JSON body contains the definition of an organization policy. If this constraint doesn't support parameters, omit the `parameters` block under `rules`.
    
    
    {
      "name": "organizations/ORG_ID/policies/CONSTRAINT_NAME",
      "spec": {
        "rules": [
          {
            "enforce": true,
            "parameters": {
              "allowedMemberSubjects": [
                "ALLOWED_MEMBER_1",
                "ALLOWED_MEMBER_2"
              ],
              "allowedPrincipalSets": [
                "ALLOWED_PRINCIPAL_SET_1",
                "ALLOWED_PRINCIPAL_SET_2"
              ]
            }
          }
        ]
      }
    }
    

Replace the following:

  * `ORG_ID`: the numeric ID of your Google Cloud organization.

  * `CONSTRAINT_NAME`: the name of the constraint that you want to set.

  * `ALLOWED_MEMBER_1`, `ALLOWED_MEMBER_2`: The members that you want to grant roles to in your organization—for example, `user:example-user@example.com`.

  * `ALLOWED_PRINCIPAL_SET_1`, `ALLOWED_PRINCIPAL_SET_2`: The principal sets that you want to grant roles to in your organization. For example, `//cloudresourcemanager.googleapis.com/organizations/0123456789012`.




Optionally, to make the organization policy conditional on a tag, add a `condition` block to the `rules`. If you add a conditional rule to an organization policy, you must add at least one unconditional rule or the policy cannot be saved. For more details, see [Scope organization policies with tags](https://docs.cloud.google.com/organization-policy/scope-policies).

To learn how to test the policy in dry-run mode before applying it, see [Test organization policies](https://docs.cloud.google.com/organization-policy/test-policies).

To learn how to simulate the policy before you enforce it, see [Test organization policy changes with Policy Simulator](https://docs.cloud.google.com/policy-intelligence/docs/test-organization-policies).

## Use custom organization policies to implement domain-restricted sharing

  1. Create a custom constraint that restricts which principals can be granted roles in your organization:

     1. Use the [`memberInPrincipalSet` CEL function](https://docs.cloud.google.com/iam/docs/org-policy-custom-constraints#member-in-principal-set) with your organization principal set to restrict role grants to members in your organization. To learn how to find your organization ID, see Retrieving an organization principal set.

For example, the following constraint restricts role grants to members in your organization:
            
            name: organizations/ORG_ID/customConstraints/custom.allowInternalIdentitiesOnly
            resourceTypes: iam.googleapis.com/AllowPolicy
            methodTypes:
              - CREATE
              - UPDATE
            condition:
              "resource.bindings.all(
                binding,
                binding.members.all(member,
                  MemberInPrincipalSet(member, ['//cloudresourcemanager.googleapis.com/organizations/ORG_ID'])
                )
              )"
            actionType: ALLOW
            displayName: Only allow organization members to be granted roles
            

     2. Optionally, refine the constraint by adding additional CEL functions, joined with logical operators (`&&`, `||`, or `!`). You can add any of the following functions:

        * [`memberInPrincipalSet`](https://docs.cloud.google.com/iam/docs/org-policy-custom-constraints#member-in-principal-set)
        * [`memberTypeMatches`](https://docs.cloud.google.com/iam/docs/org-policy-custom-constraints#member-type-matches)
        * [`memberSubjectMatches`](https://docs.cloud.google.com/iam/docs/org-policy-custom-constraints#member-subject-matches)

For example, the following constraint restricts role grants to members in your organization and to `admin@example.com`:
    
    name: organizations/ORG_ID/customConstraints/custom.allowInternalIdentitiesOnly
    resourceTypes: iam.googleapis.com/AllowPolicy
    methodTypes:
      - CREATE
      - UPDATE
    condition:
      "resource.bindings.all(
        binding,
        binding.members.all(member,
          (
            MemberInPrincipalSet(member, ['//cloudresourcemanager.googleapis.com/organizations/ORG_ID'])
            ||
            MemberSubjectMatches(member, ['user:admin@example.com'])
          )
        )
      )"
    actionType: ALLOW
    displayName: Only allow organization members and service agents to be granted roles
    

  2. Set up the custom constraint:

### Console

To create a custom constraint, do the following: 

     1. In the Google Cloud console, go to the **Organization policies** page. 

[Go to Organization policies](https://console.cloud.google.com/iam-admin/orgpolicies)

     2. From the project picker, select the project that you want to set the organization policy for. 
     3. Click add **Custom constraint**. 
     4. In the **Display name** box, enter a human-readable name for the constraint. This name is used in error messages and can be used for identification and debugging. Don't use personally identifiable information (PII) or sensitive data in display names because this name could be exposed in error messages. This field can contain up to 200 characters. 
     5. In the **Constraint ID** box, enter the ID that you want for your new custom constraint. A custom constraint can only contain letters (including upper and lowercase) or numbers, for example `custom.allowInternalIdentitiesOnly`. This field can contain up to 70 characters, not counting the prefix (`custom.`), for example, `organizations/123456789/customConstraints/custom`. Don't include PII or sensitive data in your constraint ID, because it could be exposed in error messages. 
     6. In the **Description** box, enter a human-readable description of the constraint. This description is used as an error message when the policy is violated. Include details about why the policy violation occurred and how to resolve the policy violation. Don't include PII or sensitive data in your description, because it could be exposed in error messages. This field can contain up to 2000 characters. 
     7. In the **Resource type** box, select the name of the Google Cloud REST resource containing the object and field that you want to restrict—for example, `container.googleapis.com/NodePool`. Most resource types support up to 20 custom constraints. If you attempt to create more custom constraints, the operation fails. 
     8. This constraint can only be enforced on the REST `CREATE` method. 

To see supported methods for each service, find the service in [ Services that support custom constraints](https://docs.cloud.google.com/organization-policy/reference/custom-constraint-supported-services). 

     9. To define a condition, click edit **Edit condition**. 
        1. In the **Add condition** panel, create a CEL condition that refers to a supported service resource, for example, `resource.management.autoUpgrade == false`. This field can contain up to 1000 characters. For details about CEL usage, see [ Common Expression Language](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-custom-constraints#common_expression_language). For more information about the service resources you can use in your custom constraints, see [ Custom constraint supported services](https://docs.cloud.google.com/resource-manager/docs/organization-policy/custom-constraint-supported-services). 
        2. Click **Save**. 
     10. Under **Action** , select whether to allow or deny the evaluated method if the condition is met. 

The deny action means that the operation to create or update the resource is blocked if the condition evaluates to true. 

The allow action means that the operation to create or update the resource is permitted only if the condition evaluates to true. Every other case except those explicitly listed in the condition is blocked. 

     11. Click **Create constraint**. 

When you have entered a value into each field, the equivalent YAML configuration for this custom constraint appears on the right. 

### gcloud

     1. To create a custom constraint, create a YAML file using the following format: 
    
    name: organizations/ORGANIZATION_ID/customConstraints/CONSTRAINT_NAME
    resourceTypes: RESOURCE_NAME
    methodTypes:
      - CREATE
    condition: "CONDITION"
    actionType: ACTION
    displayName: DISPLAY_NAME
    description: DESCRIPTION

Replace the following: 

        * `ORGANIZATION_ID`: your organization ID, such as `123456789`. 
        * `CONSTRAINT_NAME`: the name that you want for your new custom constraint. A custom constraint can only contain letters (including upper and lowercase) or numbers, for example, `custom.allowInternalIdentitiesOnly`. This field can contain up to 70 characters, not counting the prefix (`custom.`)— for example, `organizations/123456789/customConstraints/custom`. Don't include PII or sensitive data in your constraint ID, because it could be exposed in error messages. 
        * `RESOURCE_NAME`: the fully qualified name of the Google Cloud resource containing the object and field that you want to restrict. For example, `iam.googleapis.com/AllowPolicy`. Most resource types support up to 20 custom constraints. If you attempt to create more custom constraints, the operation fails. 
        * `methodTypes`: the REST methods that the constraint is enforced on. Can only be `CREATE`. 

To see the supported methods for each service, find the service in [ Services that support custom constraints](https://docs.cloud.google.com/organization-policy/reference/custom-constraint-supported-services). 

        * `CONDITION`: a [ CEL condition](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-custom-constraints#common_expression_language) that is written against a representation of a supported service resource. This field can contain up to 1000 characters. For example, `"resource.bindings.all( binding, binding.members.all(member, MemberInPrincipalSet(member, ['//cloudresourcemanager.googleapis.com/organizations/ORG_ID']) ) )"`. 

For more information about the resources available to write conditions against, see Supported resources. 

        * `ACTION`: the action to take if the `condition` is met. Can only be `ALLOW`. 

The allow action means that if the condition evaluates to true, the operation to create or update the resource is permitted. This also means that every other case except the one explicitly listed in the condition is blocked. 

        * `DISPLAY_NAME`: a human-readable name for the constraint. This name is used in error messages and can be used for identification and debugging. Don't use PII or sensitive data in display names because this name could be exposed in error messages. This field can contain up to 200 characters. 
        * `DESCRIPTION`: a human-friendly description of the constraint to display as an error message when the policy is violated. This field can contain up to 2000 characters. 
     2. After you have created the YAML file for a new custom constraint, you must set it up to make it available for organization policies in your organization. To set up a custom constraint, use the [ `gcloud org-policies set-custom-constraint`](https://docs.cloud.google.com/sdk/gcloud/reference/org-policies/set-custom-constraint) command: 
    
    gcloud org-policies set-custom-constraint CONSTRAINT_PATH

Replace `CONSTRAINT_PATH` with the full path to your custom constraint file. For example, `/home/user/customconstraint.yaml`. 

After this operation is complete, your custom constraints are available as organization policies in your list of Google Cloud organization policies. 

     3. To verify that the custom constraint exists, use the [ `gcloud org-policies list-custom-constraints`](https://docs.cloud.google.com/sdk/gcloud/reference/org-policies/list-custom-constraints) command: 
    
    gcloud org-policies list-custom-constraints --organization=ORGANIZATION_ID

Replace `ORGANIZATION_ID` with the ID of your organization resource. 

For more information, see [ Viewing organization policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies#viewing_organization_policies). 

  3. Enforce the custom organization policy:

You can enforce a constraint by creating an organization policy that references it, and then applying that organization policy to a Google Cloud resource. 

### Console

     1. In the Google Cloud console, go to the **Organization policies** page. 

[Go to Organization policies](https://console.cloud.google.com/iam-admin/orgpolicies)

     2. From the project picker, select the project that you want to set the organization policy for. 
     3. From the list on the **Organization policies** page, select your constraint to view the **Policy details** page for that constraint. 
     4. To configure the organization policy for this resource, click **Manage policy**. 
     5. On the **Edit policy** page, select **Override parent's policy**. 
     6. Click **Add a rule**. 
     7. In the **Enforcement** section, select whether this organization policy is enforced or not. 
     8. Optional: To make the organization policy conditional on a tag, click **Add condition**. Note that if you add a conditional rule to an organization policy, you must add at least one unconditional rule or the policy cannot be saved. For more information, see [ Scope organization policies with tags](https://docs.cloud.google.com/organization-policy/scope-policies). 
     9. Click **Test changes** to simulate the effect of the organization policy. For more information, see [ Test organization policy changes with Policy Simulator](https://docs.cloud.google.com/policy-intelligence/docs/test-organization-policies). 
     10. To enforce the organization policy in dry-run mode, click **Set dry run policy**. For more information, see [ Test organization policies](https://docs.cloud.google.com/organization-policy/test-policies). 
     11. After you verify that the organization policy in dry-run mode works as intended, set the live policy by clicking **Set policy**. 

### gcloud

     1. To create an organization policy with boolean rules, create a policy YAML file that references the constraint: 
    
    name: projects/PROJECT_ID/policies/CONSTRAINT_NAME
    spec:
      rules:
      - enforce: true
    
    dryRunSpec:
      rules:
      - enforce: true

Replace the following: 

        * `PROJECT_ID`: the project that you want to enforce your constraint on. 
        * `CONSTRAINT_NAME`: the name you defined for your custom constraint. For example, `custom.allowInternalIdentitiesOnly`. 
     2. To enforce the organization policy in [dry-run mode](https://docs.cloud.google.com/organization-policy/test-policies), run the following command with the `dryRunSpec` flag: 
    
    gcloud org-policies set-policy POLICY_PATH --update-mask=dryRunSpec

Replace `POLICY_PATH` with the full path to your organization policy YAML file. The policy requires up to 15 minutes to take effect. 

     3. After you verify that the organization policy in dry-run mode works as intended, set the live policy with the `org-policies set-policy` command and the `spec` flag: 
    
    gcloud org-policies set-policy POLICY_PATH --update-mask=spec

Replace `POLICY_PATH` with the full path to your organization policy YAML file. The policy requires up to 15 minutes to take effect. 




## Use the `iam.allowedPolicyMemberDomains` constraint to implement domain-restricted sharing

The domain restriction constraint is a legacy managed constraint with the [list `constraint_type`](https://docs.cloud.google.com/organization-policy/create-organization-policies#list-constraint). You can specify an organization principal set or a Google Workspace customer ID in the `allowed_values` list of a domain restriction constraint. For more information, see [Organization principal set versus Google Workspace customer ID](https://docs.cloud.google.com/organization-policy/domain-restricted-sharing#org-id-vs-customer-id).

Your organization principal set and Google Workspace ID are not automatically allowed. To allow principals in your organization to access resources in your organization, either your organization principal set or Google Workspace ID must be included as an allowed principal set.

The domain restriction constraint doesn't support denying values, and an organization policy can't be saved with IDs in the `denied_values` list.

You can make an organization policy enforcing the domain restriction constraint conditional on any resource included in the [list of supported resources](https://docs.cloud.google.com/resource-manager/docs/tags/tags-supported-services#supported_service_resources). For example, Cloud Storage buckets, BigQuery datasets, or Compute Engine VMs.

###  Console 

To set an organization policy including a domain restriction constraint, do the following:

  1. In the Google Cloud console, go to the **Organization policies** page.

[Go to Organization policies](https://console.cloud.google.com/iam-admin/orgpolicies)

  2. From the project picker, select the organization resource on which you want to set the organization policy.

  3. On the **Organization policies** page, select **Domain Restricted Sharing** from the list of constraints.

  4. On the **Policy details** page, click **Manage policy**.

  5. Under **Applies to** , select **Override parent's policy**.

  6. Click **Add a rule**.

  7. Under **Policy values** , select custom.

**Note:** The domain restriction constraint does not support **Deny All**.
  8. Under **Policy type** , select **Allow**.

**Note:** The domain restriction constraint does not support **Deny** values.
  9. Under **Custom values** , enter an organization principal set or Google Workspace customer ID into the field.

  10. If you want to add multiple IDs, click **New policy value** to create an additional field.

  11. Click **Done**.

  12. Optionally, to make the domain restriction constraint conditional on a tag, click **Add condition**.

     1. In the **Title** field, enter a name for the condition.

     2. In the **Description** field, give your condition a description. The description provides context on the tags that are required and how they impact resources.

     3. You can use the **Condition builder** to create a condition that requires a particular tag for the constraint to take effect.

        1. In the **Condition type** menu in the **Condition builder** tab, select **Tag**.

        2. Select the **Operator** for your condition. To match an entire tag, use the **matches** operator. To match a tag key and a tag value, use the **matches ID** operator.

        3. If you selected the **matches** operator, enter the value namespaced name of the tag. If you selected the **matches ID** operator, enter the key and value IDs.

        4. You can create multiple conditions by clicking **Add**. If you add another condition, you can set the conditional logic to require all of them by toggling **And**. You can set the conditional logic to require only one of the conditions to be true by toggling **Or**.

        5. You can delete an expression by clicking the large **X** to the right of the condition fields.

        6. When you have finished editing your conditions, click **Save**.

  13. To enforce the policy, click **Set policy**.




###  gcloud 

Policies can be set through the Google Cloud CLI. To create a policy that includes the domain restriction constraint, run the following command:

To set an organization policy that includes the domain restriction constraint, run the following command:
    
    
    gcloud org-policies set-policy POLICY_PATH
    

Where `POLICY_PATH` is the full path to your organization policy YAML file, which should look like the following:
    
    
    name: organizations/ORGANIZATION_ID/policies/iam.allowedPolicyMemberDomains
    spec:
      rules:
      - condition: # This condition applies to the values block.
          expression: "resource.matchTag('ORGANIZATION_ID/environment', 'dev')"
        values:
          allowedValues:
          - PRINCIPAL_SET
      - values:
          allowedValues:
          - PRINCIPAL_SET
    

Replace the following:

  * ORGANIZATION_ID with the ID of the organization resource on which to set this policy.
  * PRINCIPAL_SET for the principal identifiers you want to allow. You can include either organization principal sets or Google Workspace customer IDs. For example, `is:principalSet://cloudresourcemanager.googleapis.com/organizations/01234567890123` or `is:C03g5e3bc`



Only identities specified in the list of `allowed_values` will be permitted in allow policies after this organization policy is enforced. To be allowed, principals must be in the specified organization principal set or part of a specified Google Workspace domain.

For example, if you created an organization policy that allowed only the customer ID of your company's Google Workspace domain, then only principals associated with that domain could be added to the allow policy from that point forward.

### Example error message

When the `iam.allowedPolicyMemberDomains` legacy managed constraint is violated by trying to add a principal that is not included in the `allowed_values` list, the operation will fail and then an error message will be displayed.

###  Console 

![Screenshot of Console](https://docs.cloud.google.com/static/organization-policy/images/drs_error_ui.png)

###  gcloud 
    
    
    ERROR: (gcloud.projects.set-iam-policy) FAILED_PRECONDITION:
    One or more users named in the policy do not belong to a permitted customer.
    

## Retrieving an organization principal set

You can get your organization resource ID using the Google Cloud console, the gcloud CLI, or the Cloud Resource Manager API.

###  console 

To get your organization resource ID using the Google Cloud console, do the following:

  1. Go to the Google Cloud console: 

[Go to the Google Cloud console](https://console.cloud.google.com/)

  2. From the project picker at the top of the page, select your organization resource.
  3. On the right side, click **More** , and then click **Settings**.   
![](https://docs.cloud.google.com/static/resource-manager/img/console-more-settings.png)



The **Settings** page displays your organization resource ID.

###  gcloud 

To find your organization resource ID, run the following command:
    
    
    gcloud organizations list
    

This command lists all the organization resources to which you belong to, and their corresponding organization resource IDs.

###  API 

To find your organization resource ID using the Cloud Resource Manager API, use the [`organizations.search()`](https://docs.cloud.google.com/resource-manager/reference/rest/v3/organizations/search) method, including a query for your domain. For example:
    
    
    GET https://cloudresourcemanager.googleapis.com/v3/organizations:search{query=domain:altostrat.com}
    

The response contains the metadata of the organization resource that belongs to `altostrat.com`, which includes the organization resource ID.

After you have your organization resource ID, you need to use the correct identifier for the set of principals belonging to it. For example:

`principalSet://iam.googleapis.com/organizations/01234567890123`

Entering the organization principal set allows the following principals to be granted roles in your organization:

  * All workforce identity pools in your organization
  * All service accounts and workload identity pools in any project in the organization
  * All [service agents](https://docs.cloud.google.com/iam/docs/service-account-types#service-agents) associated with resources in your organization.



For more information about IAM principal identifiers, see [Principal identifiers](https://docs.cloud.google.com/iam/docs/principal-identifiers).

## Retrieving a Google Workspace customer ID

Entering the Google Workspace customer ID allows the following principals to be granted roles in your organization:

  * All identities in all domains associated with your Google Workspace customer ID
  * All workforce identity pools in your organization
  * All service accounts and workload identity pools in any project in the organization
  * All [service agents](https://docs.cloud.google.com/iam/docs/service-account-types#service-agents) associated with resources in your organization.



The Google Workspace customer ID used by the domain restriction constraint can be obtained in two ways:

### gcloud

The [gcloud organizations list](https://docs.cloud.google.com/sdk/gcloud/reference/organizations/list) command can be used to see all organizations that you have the `resourcemanager.organizations.get` permission for:
    
    
    gcloud organizations list
    

This command will return the `DISPLAY_NAME`, `ID` (Organization ID), and `DIRECTORY_CUSTOMER_ID`. The Google Workspace customer ID is the `DIRECTORY_CUSTOMER_ID`.

### API

The [Google Workspace Directory API](https://developers.google.com/admin-sdk/directory/v1/guides/manage-customers#retrieve_a_customer) can be used to retrieve a Google Workspace customer ID.

While logged in as a Google Workspace admin, you can [visit the **Customers: get** API method documentation](https://developers.google.com/admin-sdk/directory/v1/reference/customers/get?apix_params=%7B%22customerKey%22%3A%22my_customer%22%2C%22fields%22%3A%22id%22%7D) and click **Execute**. After authorization, the response would show your customer ID.

Alternatively, you can use an API client:

  1. Obtain an OAuth access token for the `https://www.googleapis.com/auth/admin.directory.customer.readonly` scope.
  2. Run the following command to query the Google Workspace directory API:
         
         curl -# -X GET "https://www.googleapis.com/admin/directory/v1/customers/customerKey" \
         -H "Authorization: Bearer $access_token" -H "Content-Type: application/json"
         




This command will return a JSON response including the customer's information. The Google Workspace customer ID is the `id`.

## Configure exceptions for domain-restricted sharing

Some Google Cloud services use service accounts, service agents, and other accounts to perform actions on your behalf. Domain-restricted sharing can prevent these accounts from being automatically granted the IAM roles that they need, which can cause certain actions to fail.

The following table lists actions in Google Cloud that could be impacted by domain-restricted sharing. It also lists the accounts that need to be granted roles automatically for these actions to succeed.

If you use custom organization policies or the `iam.managed.allowedPolicyMembers` managed constraint to implement domain restricted sharing, then consider adding these accounts as exceptions to your domain restricted sharing constraint. To add an account as an exception, add the principal identifier for the account to the list of allowed members.

If you use the `iam.allowedPolicyMemberDomains` legacy managed constraint to implement domain restricted sharing, then you might need to force account access for these accounts to perform the listed actions.

Action | Principal identifier  
---|---  
Enable BigQuery log sink for a billing account | `serviceAccount:bUNIQUE_ID@gcp-sa-logging.iam.gserviceaccount.com`  
Enable storage access logging | `serviceAccount:cloud-storage-analytics@google.com`  
Use Pub/Sub as an endpoint for a Google Chat app | `serviceAccount:chat-api-push@system.gserviceaccount.com`  
Use Pub/Sub to receive real-time developer notifications from Google Play | `serviceAccount:google-play-developer-notifications@system.gserviceaccount.com`  
Use Pub/Sub to receive Cloud Billing budget alerts | `serviceAccount:billing-budget-alert@system.gserviceaccount.com`  
Use Pub/Sub to receive Cloud Billing cost anomaly alerts | `serviceAccount:cloud-billing-finops-alert@system.gserviceaccount.com`  
Use a signed URL with Cloud CDN | `serviceAccount:service-PROJECT_NUMBER@cloud-cdn-fill.iam.gserviceaccount.com`  
Private origin authentication with Cloud CDN | `serviceAccount:service-PROJECT_NUMBER@https-lb.iam.gserviceaccount.com`  
  
### Cloud Run public services

Cloud Run lets you [make services public](https://docs.cloud.google.com/run/docs/securing/managing-access#make-service-public). However, if you implement domain restricted sharing, then users outside of your organization won't be able to access public Cloud Run services.

To allow users to access public Cloud Run services, you must disable the Cloud Run Invoker IAM check for Cloud Run services. For more information, see [Disable the Cloud Run Invoker for services](https://docs.cloud.google.com/run/docs/securing/managing-access#invoker_check).

### Share other data publicly

If you use custom organization policies to implement domain restricted sharing, then you can add an exception to your organization policy to allow public data sharing.

Sharing data publicly involves the special principals `allUsers` and `allAuthenticatedUsers`. If you need to share data publicly while using domain restricted sharing, then you need to add an exception for these principals. Adding exceptions is only possible if you're using custom organization policies to implement domain restricted sharing.

To add an exception for `allUsers` and `allAuthenticatedUsers`, create a conditional custom organization policy based on [resource tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing).

  1. Create a tag key on your organization resource.
         
         gcloud resource-manager tags keys create allUsersIngress \
           --parent=organizations/ORGANIZATION_ID
         

Replace `ORGANIZATION_ID` with your [organization's ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id).

  2. Create a tag value for the tag key that you created.
         
         gcloud resource-manager tags values create True \
         --parent=ORGANIZATION_ID/allUsersIngress \
         --description="Allow allUsers to access internal Cloud Run services"
         

  3. [Attach the tag](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#attaching) to resources that you want to share publicly.

  4. Create a custom constraint using the `memberSubjectMatches` CEL function in your constraint's condition expression.

For example, the following condition expression restricts role grants to members in your organization, `allUsers`, and `allAuthenticatedUsers`:
         
         name: organizations/ORGANIZATION_ID/customConstraints/custom.allowInternalAndSpecialIdentitiesOnly
         resourceTypes: iam.googleapis.com/AllowPolicy
         methodTypes:
           - CREATE
           - UPDATE
         condition:
           "resource.bindings.all(
             binding,
             binding.members.all(member,
               (
                 MemberInPrincipalSet(member, ['//cloudresourcemanager.googleapis.com/organizations/ORG_ID'])
                 ||
                 MemberSubjectMatches(member, ['allUsers', 'allAuthenticatedUsers'])
               )
             )
           )"
         actionType: ALLOW
         displayName: Only allow organization members, allusers, and allAuthenticatedUsers to be granted roles
         

  5. Create an organization policy that enforces the custom constraint.
         
         name: organizations/ORGANIZATION_ID/policies/iam.allowedPolicyMemberDomains
         spec:
           rules:
           - allowAll: true
             condition:
               expression: resource.matchTag("ORGANIZATION_ID/allUsersIngress", "True")
               title: allowAllUsersIngress
         

  6. Enforce the organization policy.
         
         gcloud org-policies set-policy POLICY_PATH
         

Replace `POLICY_PATH` with the path and filename of your organization policy.




The conditional organization policy lets you grant permissions to the `allUsers` identity on resources tagged with `allUsersIngress: true`.

## Forcing account access

If you need to force account access for a project in violation of domain restrictions:

  1. Remove the organization policy containing the domain restriction constraint.

  2. Grant account access to the project.

  3. Implement the organization policy with the domain restriction constraint again.




Alternatively, you can grant access to a Google group that contains the relevant service accounts:

  1. Create a Google group within the allowed domain.

  2. Use the Google Workspace administrator panel to [turn off domain restriction for that group](https://support.google.com/a/answer/167097).

  3. Add the service account to the group.

  4. Grant access to the Google group in the allow policy.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
