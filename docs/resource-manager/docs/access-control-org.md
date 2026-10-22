---
url: https://docs.cloud.google.com/resource-manager/docs/access-control-org/
title: Access control for organization resources with IAM \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:58:18.886577+00:00
---

# Access control for organization resources with IAM  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/docs/access-control-org/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Resource Manager ](https://docs.cloud.google.com/resource-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/resource-manager/docs/resource-manager-overview)



Send feedback 

#  Access control for organization resources with IAM Stay organized with collections  Save and categorize content based on your preferences. 

Google Cloud offers [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs/overview), which lets you give more granular access to specific Google Cloud resources and prevents unwanted access to other resources. IAM lets you adopt the [security principle of least privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege), so you grant only the necessary access to your resources.

IAM lets you control **who (users)** has **what access (roles)** to **which resources** by setting allow policies. Allow policies grant specific roles to a user to give the user certain permissions.

This page explains the IAM roles that are available on the organization resource, and how to create and manage allow policies for organization resources using the Cloud Resource Manager API. For more information, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

**Note:** You can also use deny policies to prevent principals from using specific IAM permissions. For more information, see [Deny policies](https://docs.cloud.google.com/iam/docs/deny-overview). 

## Permissions and roles

To control access to resources, Google Cloud requires that accounts making API requests have appropriate IAM roles. IAM roles include permissions that let users perform specific actions on Google Cloud resources. For example, the `resourcemanager.organizations.get` permission allows a user to get details about their organization resource.

You don't directly give users permissions; instead, you grant them _roles_ , which have one or more permissions bundled within them.

You can grant one or more roles on the same resource.

### Use predefined roles

The following table lists the roles that you can grant to access an organization resource's properties, the description of what the role does, and the permissions bundled within that role.

**Note:** In addition to the roles listed in the following table, other Google Cloud services offer IAM roles that you can set at the organization resource level. For a list of all roles you can grant at the organization level, see [Understanding Roles](https://docs.cloud.google.com/iam/docs/understanding-roles).Role | Permissions  
---|---  
  
#### Organization Administrator 

(`roles/resourcemanager.organizationAdmin`) Access to manage IAM policies and view organization policies for organizations, folders, and projects.  Lowest-level resources where you can grant this role:

  * Project 

|  `essentialcontacts.*`

  * `essentialcontacts.contacts.create`
  * `essentialcontacts.contacts.delete`
  * `essentialcontacts.contacts.get`
  * `essentialcontacts.contacts.list`
  * `essentialcontacts.contacts.send`
  * `essentialcontacts.contacts.update`

`iam.policybindings.*`

  * `iam.policybindings.get`
  * `iam.policybindings.list`

`orgpolicy.constraints.list` `orgpolicy.policies.list` `orgpolicy.policy.get` `resourcemanager.capabilities.*`

  * `resourcemanager.capabilities.get`
  * `resourcemanager.capabilities.update`

`resourcemanager.folders.createPolicyBinding` `resourcemanager.folders.deletePolicyBinding` `resourcemanager.folders.get` `resourcemanager.folders.getIamPolicy` `resourcemanager.folders.list` `resourcemanager.folders.searchPolicyBindings` `resourcemanager.folders.setIamPolicy` `resourcemanager.folders.updatePolicyBinding` `resourcemanager.organizations.*`

  * `resourcemanager.organizations.createPolicyBinding`
  * `resourcemanager.organizations.deletePolicyBinding`
  * `resourcemanager.organizations.get`
  * `resourcemanager.organizations.getIamPolicy`
  * `resourcemanager.organizations.searchPolicyBindings`
  * `resourcemanager.organizations.setIamPolicy`
  * `resourcemanager.organizations.updatePolicyBinding`

`resourcemanager.projects.createPolicyBinding` `resourcemanager.projects.deletePolicyBinding` `resourcemanager.projects.get` `resourcemanager.projects.getIamPolicy` `resourcemanager.projects.list` `resourcemanager.projects.searchPolicyBindings` `resourcemanager.projects.setIamPolicy` `resourcemanager.projects.updatePolicyBinding`  
  
#### Organization Viewer 

(`roles/resourcemanager.organizationViewer`) Provides access to view an organization.  Lowest-level resources where you can grant this role:

  * Organization 

|  `resourcemanager.organizations.get`  
  
#### Organization Policy Administrator 

(`roles/orgpolicy.policyAdmin`) Provides access to define what restrictions an organization wants to place on the configuration of cloud resources by setting Organization Policies.  Lowest-level resources where you can grant this role:

  * Organization 

|  `cloudasset.assets.analyzeOrgPolicy` `cloudasset.assets.exportResource` `cloudasset.assets.listResource` `cloudasset.assets.searchAllResources` `orgpolicy.*`

  * `orgpolicy.constraints.list`
  * `orgpolicy.customConstraints.create`
  * `orgpolicy.customConstraints.delete`
  * `orgpolicy.customConstraints.get`
  * `orgpolicy.customConstraints.list`
  * `orgpolicy.customConstraints.update`
  * `orgpolicy.policies.create`
  * `orgpolicy.policies.delete`
  * `orgpolicy.policies.list`
  * `orgpolicy.policies.update`
  * `orgpolicy.policy.get`
  * `orgpolicy.policy.set`

`policysimulator.orgPolicyViolations.list` `policysimulator.orgPolicyViolationsPreviews.*`

  * `policysimulator.orgPolicyViolationsPreviews.create`
  * `policysimulator.orgPolicyViolationsPreviews.get`
  * `policysimulator.orgPolicyViolationsPreviews.list`

`recommender.orgPolicyInsights.*`

  * `recommender.orgPolicyInsights.get`
  * `recommender.orgPolicyInsights.list`
  * `recommender.orgPolicyInsights.update`

`recommender.orgPolicyRecommendations.*`

  * `recommender.orgPolicyRecommendations.get`
  * `recommender.orgPolicyRecommendations.list`
  * `recommender.orgPolicyRecommendations.update`

  
  
#### Browser 

(`roles/browser`) Read access to browse the hierarchy for a project, including the folder, organization, and allow policy. This role doesn't include permission to view resources in the project.  Lowest-level resources where you can grant this role:

  * Project 

|  `resourcemanager.folders.get` `resourcemanager.folders.list` `resourcemanager.organizations.get` `resourcemanager.projects.get` `resourcemanager.projects.getIamPolicy` `resourcemanager.projects.list`  
  
### Creating custom roles

In addition to the predefined roles described in this topic, you can also create [custom roles](https://docs.cloud.google.com/iam/docs/understanding-custom-roles) that are collections of permissions that you tailor to your needs. When creating a custom role for use with Resource Manager, be aware of the following points: 

  * List and get permissions, such as `resourcemanager.projects.get/list`, should always be granted as a pair.
  * When your custom role includes the `folders.list` and `folders.get` permissions, it should also include `projects.list` and `projects.get`. 
  * Be aware that the `setIamPolicy` permission for organization, folder, and project resources allows the user to grant all other permissions, and so should be assigned with care. 



## View existing access for an organization resource

You can view what roles a user is granted for an organization resource by getting that resource's allow policy. You can view the allow policy for an organization resource using the Google Cloud console, the Google Cloud CLI, or the [`getIamPolicy()`](https://docs.cloud.google.com/resource-manager/reference/rest/v3/organizations/getIamPolicy) method.

###  Console 

To view granted roles at the organization resource level using the Google Cloud console:

  1. Go to the **Manage resources** page in the Google Cloud console: 

[Open the Manage resources page](https://console.cloud.google.com/cloud-resource-manager)

  2. On the **Organization** drop-down menu, select your organization resource.

  3. Select the checkbox for the organization resource.

  4. In the **Info Panel** , under **Permissions** , click **Expand** a role and display all members who have that role.




###  gcloud 

Get the allow policy for the organization resource using the get-iam-policy command:
    
    
    gcloud organizations get-iam-policy \
    ORGANIZATION_ID --format json > \
    FILENAME.JSON
    

The command outputs the allow policy, which looks similar to the following:
    
    
    bindings:
    - members:
    - user:testuser1@gcp-test.com
    role: roles/editor
    - members:
    - user:admin@gcp-test.com
    role:roles/resourcemanager.organizationAdmin
    - members:
    - user:testuser2@gcp-test.com
    role: roles/resourcemanager.projectCreator
    etag": "BwU1aRxWk30="
    

###  API 

The following code snippet returns the allow policy for the organization resource `https://cloudresourcemanager.googleapis.com/v3/organizations/12345`.

Request:
    
    
    POST
    https://cloudresourcemanager.googleapis.com/v3/organizations/12345:getIamPolicy
    

Response:
    
    
    {
        "bindings": [
        {
            "role": "roles/resourcemanager.organizationAdmin",
            "members": [
            "user:email1@gmail.com"
        ]
        },
        {
            "role": "roles/resourcemanager.projectCreator",
            "members": [
                "user:email2@gmail.com",
                "user:email3@gmail.com",
                "serviceAccount:my-other-app@appspot.gserviceaccount.com"
            ]
        }
        ]
        "etag": "BwUjHYKHHiQ="
    }
    

###  Python 

The method [`getIamPolicy()`](https://docs.cloud.google.com/resource-manager/reference/rest/v3/organizations/getIamPolicy) lets you get an allow policy that was previously set.
    
    
    crm = discovery.build(
        'cloudresourcemanager', 'v3', http=creds.authorize(httplib2.Http()))
    policy = crm.organizations().getIamPolicy(
        resource=flags.organizationId, body={}).execute()
    print json.dumps(policy, indent=2)
    

## Grant access to an organization resource

Organization Administrators can grant IAM roles to team members so that they can access an organization's resources and APIs. You can grant roles to a user account email, a Google Group, a service account, or a G Suite domain. You can use the Google Cloud console, the gcloud CLI, or the [`setIamPolicy()`](https://docs.cloud.google.com/resource-manager/reference/rest/v3/organizations/setIamPolicy) method to grant roles.

**Note:** If you're getting started with Google Cloud, you can grant the appropriate IAM roles to your organization administrator groups as part of the [Google Cloud set up process](https://docs.cloud.google.com/docs/enterprise/setup-checklist).

###  Console 

To set access control at the organization resource level using the Google Cloud console:

  1. Go to the **Manage resources** page in the Google Cloud console: 

[Open the Manage resources page](https://console.cloud.google.com/cloud-resource-manager)

  2. On the **Organization** drop-down menu, select your organization resource.

  3. Select the checkbox for the organization resource. If you don't have a folder resource, the organization resource is not visible. To continue, see the instructions for granting roles through the [IAM](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#grant_access) page.

  4. If the **Info Panel** on the right is hidden, click **Show Info Panel** in the top right corner.

  5. In the **Info Panel** , in the **Permissions** tab, click **Add Member**.

  6. In the **New members** field, enter the team members you want to add. You can specify a user account email, a Google Group, a service account, or a G Suite domain.

  7. In the **Select a role** drop-down menu, select the role you want to grant to the team members.

  8. Click **Add**.




###  gcloud 

To set an organization resource's allow policy using the `gcloud` command:

  1. Get the allow policy for the organization resource using the `get-iam-policy` command and output the policy to a JSON file:
         
         gcloud organizations get-iam-policy \
         ORGANIZATION_ID \
         --format json > FILENAME.JSON
         

  2. The contents of the JSON file looks similar to the following:



    
    
    {
        "bindings": [
        {
            "members": [
                "user:testuser1@gcp-test.com"
            ],
            "role": "roles/editor"
        },
        {
            "members": [
                "user:admin@gcp-test.com",
            ],
            "role": "roles/resourcemanager.organizationAdmin"
        },
        {
            "members": [
                "user:testuser2@gcp-test.com"
            ],
            "role": "roles/resourcemanager.projectCreator"
        },
        ],
        "etag": "BwU1aRxWk30="
    }
    

  1. Open the JSON file in a text editor. Then, add a new entry to the `bindings` array to define an Organization Administrator. For example, to make `anotheradmin@gcp-test.com` an Organization Administrator, change the previous example as follows:


    
    
    {
        "bindings": [
        {
            "members": [
                "user:testuser1@gcp-test.com"
            ],
            "role": "roles/editor"
        },
        {
            "members": [
                "user:admin@gcp-test.com",
                "user:anotheradmin@gcp-test.com"
            ],
            "role": "roles/resourcemanager.organizationAdmin"
        },
        {
            "members": [
                "user:testuser20@gcp-test.com"
            ],
            "role": "roles/resourcemanager.projectCreator"
        },
        ],
        "etag": "BwU1aRxWk30="
    }
    

  1. Update the organization resource's allow policy by running the following command:


    
    
    gcloud organizations set-iam-policy \
    ORGANIZATION_ID policy.json
    

###  API 

Request:
    
    
    POST https://cloudresourcemanager.googleapis.com/v3/organizations/12345:setIamPolicy
    {
        "policy": {
        "version": "0",
        "bindings": [
        {
            "role": "roles/resourcemanager.organizationAdmin",
            "members": [
                "user:email1@gmail.com"
            ]
        },
        {
            "role": "roles/resourcemanager.projectCreator",
            "members": [
            "user:email2@gmail.com",
            "user:email3@gmail.com",
            "serviceAccount:my-other-app@appspot.gserviceaccount.com"
            ]
        }
        ]
        "etag": "BwUjHYKHHiQ="
        }
    }
    

Response:
    
    
    {
        "bindings": [
        {
            "role": "roles/resourcemanager.organizationAdmin",
            "members": [
                "user:email1@gmail.com"
            ]
        },
        {
            "role": "roles/resourcemanager.projectCreator",
            "members": [
                "user:email2@gmail.com",
                "user:email3@gmail.com",
                "serviceAccount:my-other-app@appspot.gserviceaccount.com"
            ]
        }
        ]
        "etag": "BwUjHYKJUiQ="
    }
    

The `setIamPolicy()` method lets you grant roles to users by attaching an allow policy to the organization resource. The allow policy is a collection of bindings that define .

**Read-Modify-Write** : A common pattern for updating a resource's metadata, such as the allow policy, involves reading its current state, updating the data locally, and then sending the modified data for writing. This pattern can result in a conflict if two or more independent processes attempt the sequence simultaneously. For example, if two project owners attempt to make conflicting changes to the allow policy simultaneously, one owner's changes might fail. IAM solves this problem by using an `etag` property in allow policies. This property verifies whether the allow policy has changed since the last request. When you make a request with an `etag` value, the system compares the `etag` value in the request with the existing `etag` value associated with the policy. It writes the allow policy only if the `etag` values match.

When you update an allow policy, first get the allow policy using `getIamPolicy()`, update the allow policy, and then write the updated allow policy using `setIamPolicy()`. When you set the allow policy, use the `etag` value only if the corresponding allow policy in `GetPolicyResponse` contains an `etag` value.

###  Python 

The [`setIamPolicy()`](https://docs.cloud.google.com/resource-manager/reference/rest/v3/organizations/setIamPolicy) method lets you attach an allow policy to a resource. The `setIamPolicy` method takes a `SetIamPolicyRequest`, which contains an allow policy to be set and the resource to which the allow policy is attached. It returns the resulting allow policy. We recommend following the [read-modify-write](https://docs.cloud.google.com/iam/docs/managing-policies#setting_a_policy) pattern when you update an allow policy using `setIamPolicy()`.

Here is some sample code to set an allow policy for an organization resource:
    
    
    crm = discovery.build(
        'cloudresourcemanager', 'v3', http=creds.authorize(httplib2.Http()))
    policy = crm.organizations().getIamPolicy(
        resource=flags.organizationId, body={}).execute()
    
    admin_binding = next(
        (binding
            for binding in policy['bindings']
            if binding['role'] == 'roles/resourcemanager.organizationAdmin'),
            None)
    
    # Add an empty Organization Administrator binding if not present.
    if not admin_binding:
        admin_binding = {
            'role': 'roles/resourcemanager.organizationAdmin',
            'members': []
        }
    policy['bindings'].append(admin_binding)
    
    # Add the new Admin (if necessary).
    new_admin = 'user:' + flags.adminEmail
    if new_admin not in admin_binding['members']:
        admin_binding['members'].append(new_admin)
    policy = crm.organizations().setIamPolicy(
        resource=flags.organizationId,
        body={
            'resource': flags.organizationId,
            'policy': policy
        }).execute()
    
    print json.dumps(policy, indent=2)
    

### Restrict project visibility for users

Users can see all projects they have access to in the Google Cloud console and in search queries, regardless of whether or not they are in the user's selected organization resource. You can use the Organization Policy Service to restrict the set of projects that are returned in queries and in the Google Cloud console. This lets you restrict users to see projects only within your domain.

The Organization Policy constraint `constraints/resourcemanager.accessBoundaries` is a [list constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview#list_constraints) that is enforced on your organization resource. The constraint accepts a list of organization resource IDs, which define the set of organization resources that make their resources visible to users in a query or the Google Cloud console.

Projects appear under `No organization` if the user does not have the `resourcemanager.organizations.get` permission on the parent organization resource of the project. This can make a project that is not part of your organization resource appear to be unassociated with any organization resource. If you use the `resourcemanager.accessBoundaries` constraint to disallow an organization resource, projects that belong to that organization resource don't appear in queries or in the Google Cloud console. Projects not yet migrated to an organization resource are not visible if you enforce this constraint.

We recommend migrating projects that are under `No organization` to your organization resource before enforcing this constraint. For information about moving projects into an organization resource, see [Moving a project](https://docs.cloud.google.com/resource-manager/docs/moving-projects-folders).

For information about setting an organization policy, see [Using constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/using-constraints).

### Grant conditional access

Certain IAM roles, such as Organization Policy Administrator (`roles/orgpolicy.policyAdmin`) can only be granted on an organization resource. Due to [policy inheritance](https://docs.cloud.google.com/iam/docs/resource-hierarchy-access-control), all resources in the organization normally inherit this role.

For more control over which resources the role is granted on, you can use [IAM Conditions](https://docs.cloud.google.com/iam/docs/conditions-overview). Using tags with conditions lets you grant access to resources only if they have the specified [tag](https://docs.cloud.google.com/iam/docs/tags-access-control). For example, the following allow policy grants the Organization Policy Administrator role only on resources that have the `environment: dev` tag, and doesn't grant it on any other resource:
    
    
    {
      "bindings": [
        {
          "members": [
            "{dynamic print variables.examples.principal_group_api}"
          ],
          "role": "roles/orgpolicy.policyAdmin",
          "condition": {
              "title": "Dev_environment_only",
              "description": "Only granted in the development environment",
              "expression":
                "resource.matchTag('123456789012/env', 'dev')"
          }
        }
      ],
      "etag": "BwWKmjvelug=",
      "version": 3
    }
    

## Test permissions

You can test IAM permissions on a user for an organization resource with the [`testIamPermissions()`](https://docs.cloud.google.com/resource-manager/reference/rest/v3/organizations/testIamPermissions) method. This method takes the resource URL and the set of permissions to test. It returns the subset of these permissions that the user can access.

You typically don't invoke `testIamPermissions()` if you're using the Google Cloud console directly to manage permissions. `testIamPermissions()` is intended for integration with your proprietary software such as a customized graphical user interface. For example, the Google Cloud console uses `testIamPermissions()` internally to determine which UI is available to the logged-in user.

###  API 

You can use the [`testIamPermissions()`](https://docs.cloud.google.com/resource-manager/reference/rest/v3/organizations/testIamPermissions) method to check which of the given permissions the caller has for the given resource. This method takes a resource name and a set of permissions as parameters, and returns the subset of permissions that the caller has.

Here is some sample code to test permissions for an organization resource:
    
    
    Request:
    
    POST https://cloudresourcemanager.googleapis.com/v3/organizations/12345:testIamPermissions
    
    {
        "permissions":  [
            "resourcemanager.organizations.get",
            "resourcemanager.organizations.setIamPolicy"
        ]
    }
    
    Response:
    
    {
        "permissions": [
            "resourcemanager.organizations.get"
        ]
    }
    

###  Python 
    
    
    crm = discovery.build(
        'cloudresourcemanager', 'v3', http=creds.authorize(httplib2.Http()))
    
    response = crm.organizations().testIamPermissions(
        resource=flags.organizationId,
        body={
            'resource': flags.organizationId,
            'permissions': [
                'resourcemanager.organizations.setIamPolicy',
                'resourcemanager.projects.patch'
            ]
        }).execute()
    
    print json.dumps(response, indent=2)
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
