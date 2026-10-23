---
url: https://docs.cloud.google.com/monitoring/docs/access-control-with-tags/
title: Use Tags to control access to resources \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:54:49.615386+00:00
---

# Use Tags to control access to resources  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/docs/access-control-with-tags/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  Use Tags to control access to resources Stay organized with collections  Save and categorize content based on your preferences. 

[Tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview) lets you restrict who can edit or delete specific Cloud Monitoring dashboards and alerting policies. Tags are key-value pairs that you create and attach to resources, which you can pair with Identity and Access Management (IAM) conditions or deny policies to enforce team-scoped access or protect Terraform-managed resources.

When you use tags to control access to dashboards and alerting policies, you can configure a maximum of 250 teams per project. For additional limitations on tags, see [Tag limits](https://docs.cloud.google.com/resource-manager/docs/limits#tag-limits).

## Access control patterns

You can implement access control for dashboards and alerting policies by using one of the following patterns:

  * Control access to Terraform-managed resources: Use tags and IAM deny policies so that tagged resources can only be edited by Terraform. Terraform-managed resources are protected from manual, unapproved changes in the Google Cloud console or through other clients.

  * Control access to team-managed resources: Use per-team tags and conditional IAM role grants to ensure that only members of a specific team can edit or delete team-managed dashboards and alerting policies.




## Protect Terraform-managed resources

This section describes how to use tags and IAM deny policies so that tagged dashboards and alerting policies can only be edited or deleted using a [service account configured to use Terraform](https://docs.cloud.google.com/docs/terraform/authentication).

### Before you begin

To get the permissions that you need to configure tags and IAM deny policies for your project, ask your administrator to grant you the following IAM roles on your project or organization: 

  * Create tags: [Tag Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagAdmin) (`roles/resourcemanager.tagAdmin`) 
  * Manage IAM deny policies: [Deny Policy Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.denyAdmin) (`roles/iam.denyAdmin`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Protect resources using a deny policy

###  Google Cloud console 

  1. [Create a tag](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#creating) that indicates the resource is managed by Terraform. For example, create a tag key `edit_restriction` with a tag value `terraform_only`.
  2. [Create an IAM deny policy](https://docs.cloud.google.com/iam/docs/deny-access#create-deny-rule) that denies update and delete permissions to all principals, except for your Terraform service account, when the resource has the `edit_restriction:terraform_only` tag.

The deny policy must contain the following configurations:

     * **Permissions to deny** : 
       * `monitoring.dashboards.update`
       * `monitoring.dashboards.delete`
       * `monitoring.alertPolicies.update`
       * `monitoring.alertPolicies.delete`
     * **Condition** : The resource must have the tag `edit_restriction:terraform_only`.
     * **Exemption** : Add the principal identifier for the Terraform service account to the exception list of the deny rule.
  3. Create the dashboard or alerting policy you want to protect, and then attach the tag to the resource.




###  Terraform 

To configure restrictions by using Terraform, do the following:

  1. [Install and configure Terraform](https://docs.cloud.google.com/docs/terraform/install-configure-terraform) for your project.
  2. [Create the tag key and tag value](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#creating).
  3. [Create the IAM deny policy](https://docs.cloud.google.com/iam/docs/deny-access#create-deny-rule).
  4. Create the alerting policy or dashboard that you want to protect. For details, see [Create alerting policies using Terraform](https://docs.cloud.google.com/monitoring/alerts/terraform) and [Create dashboards using Terraform](https://docs.cloud.google.com/monitoring/dashboards/api-dashboard#terraform_1).
  5. Bind the tag to the resource. To attach a tag to a dashboard or alerting policy by using Terraform, create a tag binding resource by using `google_tags_tag_binding`.



For example, the following Terraform configuration does the following:

  * Creates a tag key and value.
  * Creates a deny policy.
  * Creates an alerting policy.
  * Binds a tag to the alerting policy.



Note that you can't create a resource and bind a tag to it in the same command; you must create the resource and the tag binding separately.
    
    
    # Create the tag key.
    resource "google_tags_tag_key" "lock_key" {
      parent     = "projects/PROJECT_ID"
      short_name = "edit_restriction"
    }
    
    # Create the tag value.
    resource "google_tags_tag_value" "restricted_value" {
      parent     = "tagKeys/${google_tags_tag_key.lock_key.name}"
      short_name = "terraform_only"
    }
    
    # Define the IAM deny policy.
    resource "google_iam_deny_policy" "terraform_lock" {
      parent       = urlencode(
        "cloudresourcemanager.googleapis.com/projects/PROJECT_ID"
      )
      name         = "terraform-exclusive-lock"
      display_name = "Deny modifications except for Terraform service account"
    
      rules {
        deny_rule {
          denied_principals = ["principalSet://goog/public:all"]
    
          # Exempt the Terraform service account.
          exception_principals = [
            join("", [
              "principal://iam.googleapis.com/projects/-/",
              "serviceAccounts/TERRAFORM_SERVICE_ACCOUNT_EMAIL"
            ])
          ]
    
          denied_permissions = [
            "monitoring.googleapis.com/alertPolicies.update",
            "monitoring.googleapis.com/alertPolicies.delete",
            "monitoring.googleapis.com/dashboards.update",
            "monitoring.googleapis.com/dashboards.delete"
          ]
    
          denial_condition {
            title      = "is_restricted_resource"
            expression = join("", [
              "resource.matchTag(",
              "'PROJECT_ID/edit_restriction', ",
              "'terraform_only')"
            ])
          }
        }
      }
    }
    
    # Create the alerting policy.
    resource "google_monitoring_alert_policy" "protected_policy" {
      display_name = "Restricted Alert Policy"
      combiner     = "OR"
      conditions {
        display_name = "High CPU"
        condition_threshold {
          filter     = join(" AND ", [
            "metric.type=\"compute.googleapis.com/instance/cpu/utilization\"",
            "resource.type=\"gce_instance\""
          ])
          duration   = "60s"
          comparison = "COMPARISON_GT"
          threshold_value = 0.9
        }
      }
    }
    
    # Bind the tag to the alerting policy.
    resource "google_tags_tag_binding" "policy_binding" {
      parent    = join("", [
        "//monitoring.googleapis.com/",
        google_monitoring_alert_policy.protected_policy.name
      ])
      tag_value = google_tags_tag_value.restricted_value.id
    }
    

## Configure team-scoped access

Suppose you are an administrator for a project that monitors applications for multiple teams. You want team members to be able to create dashboards and alerting policies, but edit only their own team's resources. You don't want to grant team members the broad Monitoring Editor role (`roles/monitoring.editor`) because that role grants permission to edit all monitoring resources in the project.

This section illustrates how you can use tags to give a team member the permissions needed to edit only team-owned dashboards and alerting policies.

### Before you begin

To get the permissions that you need to configure tags and IAM roles for your project, ask your administrator to grant you the following IAM roles on your project or organization: 

  * Create tags: [Tag Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagAdmin) (`roles/resourcemanager.tagAdmin`) 
  * Create a custom role: [Role Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.roleAdmin) (`roles/iam.roleAdmin`) 
  * Manage project roles: [Project IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Apply team-specific tags

###  Google Cloud console 

  1. [Create a tag](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#creating) for each team. Create a new tag key, and then create tag values for that key. For example, if you create a tag key named `owner` with values `team_a` and `team_b`, you get two tags: `owner:team_a` and `owner:team_b`. Record the tag key ID and value ID for each tag.
  2. [Create a custom role](https://docs.cloud.google.com/iam/docs/creating-custom-roles) named "Dashboard and Alerting Policy Creator" and add the following permissions:

     * `monitoring.alertPolicies.create`
     * `monitoring.alertPolicies.createTagBinding`
     * `monitoring.dashboards.create`
     * `monitoring.dashboards.createTagBinding`
     * `resourcemanager.tagValueBindings.create`

This role lets you create dashboards and alerting policies and apply tags.

  3. [Grant the following roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#single-role) to all team members:

     * Dashboard and Alerting Policy Creator (the custom role you created)
     * Monitoring Viewer (`roles/monitoring.viewer`)
     * Tag Viewer (`roles/resourcemanager.tagViewer`)
  4. For each team, grant team members the following roles with an [IAM condition](https://docs.cloud.google.com/iam/docs/conditions-overview) attached:

     * Tag User (`roles/resourcemanager.tagUser`), which lets you apply your team's tag to resources.
     * Monitoring Editor (`roles/monitoring.editor`), which lets you edit dashboards and alerting policies that have your team's tag.

Add the IAM condition to the role grants as follows:

     * **Condition Type** : `Tag`
     * **Operator** : `has value ID`
     * **keyID** : KEY_ID
     * **valueID** : TEAM_VALUE_ID

Find the tag key ID and value ID in the Resource Manager. For more information, see [Access to tagged resources](https://docs.cloud.google.com/iam/docs/tags-access-control#control-access).

  5. Create the dashboard or alerting policy you want to restrict access to, and then attach the tag to the resource.




###  Terraform 

To configure team-scoped access by using Terraform, do the following:

  1. [Install and configure Terraform](https://docs.cloud.google.com/docs/terraform/install-configure-terraform) for your project.
  2. [Create the tag key and tag value](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#creating) for each team.
  3. [Create a custom role](https://docs.cloud.google.com/iam/docs/creating-custom-roles) and add the following permissions: 
     * `monitoring.alertPolicies.create`
     * `monitoring.alertPolicies.createTagBinding`
     * `monitoring.dashboards.create`
     * `monitoring.dashboards.createTagBinding`
     * `resourcemanager.tagValueBindings.create`
  4. Grant the custom role, the Monitoring Viewer role (`roles/monitoring.viewer`), and the Tag Viewer role (`roles/resourcemanager.tagViewer`) to all members.
  5. For each team, grant the Tag User role (`roles/resourcemanager.tagUser`) and the Monitoring Editor role (`roles/monitoring.editor`) with a conditional binding based on the team's tag value.
  6. Create the alerting policy or dashboard that you want to restrict access to. For details, see [Create dashboards using Terraform](https://docs.cloud.google.com/monitoring/dashboards/api-dashboard#terraform_1) and [Create alerting policies using Terraform](https://docs.cloud.google.com/monitoring/alerts/terraform).
  7. Bind the tag to the resource. To attach a tag to a dashboard or alerting policy by using Terraform, create a tag binding resource by using `google_tags_tag_binding`.



For example, the following Terraform configuration does the following:

  * Creates a tag key and value.
  * Creates a custom role.
  * Applies IAM bindings that grant required roles and conditional permissions.
  * Creates a dashboard.
  * Binds a tag to the dashboard to establish team ownership.



Note that you can't create a resource and bind a tag to it in the same command; you must create the resource and the tag binding separately.
    
    
    # Create the tag key.
    resource "google_tags_tag_key" "res_tag_key" {
      parent      = "projects/PROJECT_ID"
      short_name  = "owner"
      description = "Identifies the team that owns the resource"
    }
    
    # Create the tag value.
    # Note: You must create a tag value resource for each team.
    resource "google_tags_tag_value" "team_a_value" {
      parent      = "tagKeys/${google_tags_tag_key.res_tag_key.name}"
      short_name  = "team_a"
      description = "Team A ownership tag value"
    }
    
    # Create the custom Creator role.
    resource "google_project_iam_custom_role" "creator_role" {
      role_id     = "dashboardAndPolicyCreator"
      title       = "Dashboard and Alerting Policy Creator"
      permissions = [
        "monitoring.alertPolicies.create",
        "monitoring.alertPolicies.createTagBinding",
        "monitoring.dashboards.create",
        "monitoring.dashboards.createTagBinding",
        "resourcemanager.tagValueBindings.create"
      ]
    }
    
    # Grant the Custom Creator role to all members.
    resource "google_project_iam_binding" "creator_grant" {
      project = "PROJECT_ID"
      role    = join("/", [
        "projects",
        "PROJECT_ID",
        "roles",
        google_project_iam_custom_role.creator_role.role_id
      ])
      members = ["group:ALL_MEMBERS_GROUP_EMAIL"]
    }
    
    # Grant the Monitoring Viewer role to all members.
    resource "google_project_iam_binding" "viewer_grant" {
      project = "PROJECT_ID"
      role    = "roles/monitoring.viewer"
      members = ["group:ALL_MEMBERS_GROUP_EMAIL"]
    }
    
    # Grant the Tag Viewer role to all members.
    resource "google_project_iam_binding" "tag_viewer_grant" {
      project = "PROJECT_ID"
      role    = "roles/resourcemanager.tagViewer"
      members = ["group:ALL_MEMBERS_GROUP_EMAIL"]
    }
    
    # Grant the Tag User role with a condition.
    # Note: You have to configure this team-specific binding for each team.
    resource "google_project_iam_binding" "tag_user_grant" {
      project = "PROJECT_ID"
      role    = "roles/resourcemanager.tagUser"
      members = ["group:TEAM_A_GROUP_EMAIL"]
    
      condition {
        title       = "restrict_to_team_a"
        description = "Allow Tag User only for team_a tag"
        expression  = join("", [
          "resource.matchTagId('",
          google_tags_tag_key.res_tag_key.name,
          "', '",
          google_tags_tag_value.team_a_value.id,
          "')"
        ])
      }
    }
    
    # Grant the Monitoring Editor role with a condition.
    # Note: You have to configure this team-specific binding for each team.
    resource "google_project_iam_binding" "editor_grant" {
      project = "PROJECT_ID"
      role    = "roles/monitoring.editor"
      members = ["group:TEAM_A_GROUP_EMAIL"]
    
      condition {
        title       = "restrict_to_team_a"
        description = "Allow Monitoring Editor only for team_a tag"
        expression  = join("", [
          "resource.matchTagId('",
          google_tags_tag_key.res_tag_key.name,
          "', '",
          google_tags_tag_value.team_a_value.id,
          "')"
        ])
      }
    }
    
    # Create the dashboard.
    resource "google_monitoring_dashboard" "example_dashboard" {
      dashboard_json = jsonencode({
        "displayName": "System Health Overview",
        "gridLayout": { "columns": "2", "widgets": [] }
      })
    }
    
    # Apply the tag binding to the dashboard to give team A ownership.
    resource "google_tags_tag_binding" "dashboard_tag" {
      parent    = join("", [
        "//monitoring.googleapis.com/",
        google_monitoring_dashboard.example_dashboard.id
      ])
      tag_value = google_tags_tag_value.team_a_value.id
    }
    

## Manage tags on dashboards and alerting policies

You can attach, list, and remove tags on dashboards and alerting policies by using the Google Cloud console or the `gcloud` CLI.

### Before you begin

To get the permissions that you need to manage tags on Cloud Monitoring resources, ask your administrator to grant you the following IAM roles on your project or organization: 

  * [Monitoring Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.viewer) (`roles/monitoring.viewer`)
  * [Tag Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)
  * A custom role with the minimum permissions necessary for the tag operations you need and the resource type you need them on. For more information, expand the **Required permissions** section. 



To see the permissions required for each tag operation when you set up your custom role, expand the **Required permissions** section: 

#### Required permissions

For each listed tag operation, the following permissions are required:

  * Attach tags to dashboards: 
    * `resourcemanager.tagValueBindings.create`
    * `monitoring.dashboards.createTagBinding`
  * Attach tags to alerting policies: 
    * `resourcemanager.tagValueBindings.create`
    * `monitoring.alertPolicies.createTagBinding`
  * Remove tags from dashboards: 
    * `resourcemanager.tagValueBindings.delete`
    * `monitoring.dashboards.deleteTagBinding`
  * Remove tags from alerting policies: 
    * `resourcemanager.tagValueBindings.delete`
    * `monitoring.alertPolicies.deleteTagBinding`



### Attach tags

To attach a tag to a dashboard or alerting policy, do the following:

###  Google Cloud console 

Select the resource type you want to attach tags to:

###  Dashboards 

  1. In the Google Cloud console, go to the dashboard **Dashboards** page: 

[Go to **Dashboards**](https://console.cloud.google.com/monitoring/dashboards)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Select the dashboard you want to attach a tag to.
  3. Click **Tags**.
  4. In the dialog, in the **Direct tags** section, locate the tag by selecting the organization or project in which the tag was created. For example, to use a tag that was created at the project level, choose **Select current project** as the scope. 

You can also manually search for the project, organization, or tag ID by selecting the **Manual Entry** option.

  5. Select the appropriate key-value pair, and then click **Save**.
  6. A dialog confirming your changes appears. Click **Confirm** to finalize your changes.



###  Alerting policies 

  1. In the Google Cloud console, go to the _notifications_ **Policies** page: 

[Go to **Alerting Policies**](https://console.cloud.google.com/monitoring/alerting/policies)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Select the alerting policy you want to attach a tag to.
  3. Click **Tags**.
  4. In the dialog, in the **Direct tags** section, locate the tag by selecting the organization or project in which the tag was created. For example, to use a tag that was created at the project level, choose **Select current project** as the scope. 

You can also manually search for the project, organization, or tag ID by selecting the **Manual Entry** option.

  5. Select the appropriate key-value pair, and then click **Save**.
  6. A dialog confirming your changes appears. Click **Confirm** to finalize your changes.



###  gcloud 

Before using any of the command data below, make the following replacements: 

  * TAG_VALUE_ID: The permanent ID or the namespaced name of the tag value. For example, `tagValues/4567890123`. For more information about tag identifiers, see [Tag definitions and identifiers](https://docs.cloud.google.com/iam/docs/tags-access-control#definitions).
  * PARENT: The fully qualified name of the parent resource. For example, `//monitoring.googleapis.com/projects/PROJECT_ID_OR_NUMBER/dashboards/DASHBOARD_ID` or `//monitoring.googleapis.com/projects/PROJECT_ID_OR_NUMBER/alertPolicies/POLICY_ID`.



Execute the [`resource-manager tags bindings create`](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/tags/bindings/create) command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud resource-manager tags bindings create \
        --tag-value=TAG_VALUE_ID \
        --parent=PARENT

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud resource-manager tags bindings create `
        --tag-value=TAG_VALUE_ID `
        --parent=PARENT

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud resource-manager tags bindings create ^
        --tag-value=TAG_VALUE_ID ^
        --parent=PARENT

You should receive a response similar to the following:
    
    
    '@type': type.googleapis.com/google.cloud.resourcemanager.v3.TagBinding
    name: tagBindings/%2F%2Fmonitoring.googleapis.com%2Fprojects%2F1234567890%2FalertPolicies%2F0987654321/tagValues/1029384756
    parent: //monitoring.googleapis.com/projects/1234567890/alertPolicies/0987654321
    tagValue: tagValues/1029384756
    tagValueNamespacedName: my-project/owner/team_a
    

### View tags

To view the tags attached to a dashboard or alerting policy, do the following:

###  Google Cloud console 

Select the resource type you want to view tags for:

###  Dashboards 

  1. In the Google Cloud console, go to the dashboard **Dashboards** page: 

[Go to **Dashboards**](https://console.cloud.google.com/monitoring/dashboards)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Select the dashboard you want to view tags for.
  3. Click **Tags**. A dialog opens, listing all attached tags.



###  Alerting policies 

  1. In the Google Cloud console, go to the _notifications_ **Policies** page: 

[Go to **Alerting Policies**](https://console.cloud.google.com/monitoring/alerting/policies)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Select the alerting policy you want to view tags for.
  3. Click **Tags**. A dialog opens, listing all attached tags.



###  gcloud 

Before using any of the command data below, make the following replacements: 

  * PARENT: The fully qualified name of the parent resource. For example, `//monitoring.googleapis.com/projects/PROJECT_ID_OR_NUMBER/dashboards/DASHBOARD_ID` or `//monitoring.googleapis.com/projects/PROJECT_ID_OR_NUMBER/alertPolicies/POLICY_ID`.



Execute the [`resource-manager tags bindings list`](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/tags/bindings/list) command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud resource-manager tags bindings list \
        --parent=PARENT

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud resource-manager tags bindings list `
        --parent=PARENT

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud resource-manager tags bindings list ^
        --parent=PARENT

To view tags inherited by the resource, add the `--effective` flag. Adding this flag returns a response similar to the following:
    
    
      namespacedTagKey: my-project/owner
      namespacedTagValue: my-project/owner/team_a
      tagKey: tagKeys/5647382910
      tagValue: tagValues/1029384756
      inherited: true
      

If all tags are explicitly attached to the resource and no tags are inherited, then the `inherited` field is omitted.

### Remove tags from a resource

To remove a tag attached to a dashboard or alerting policy, you must delete the tag binding. Removing a tag from a resource doesn't delete the tag. For instructions on how to delete a tag, see [Deleting tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#deleting).

###  Google Cloud console 

Select the resource type you want to remove tags from:

###  Dashboards 

  1. In the Google Cloud console, go to the dashboard **Dashboards** page: 

[Go to **Dashboards**](https://console.cloud.google.com/monitoring/dashboards)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Select the dashboard you want to remove a tag from.
  3. Click **Tags**.
  4. In the dialog, hold the pointer over the tag to remove, and click delete **Delete item**. Click **Save** to save your changes.
  5. A dialog confirming your changes appears. Click **Confirm** to finalize your changes.



###  Alerting policies 

  1. In the Google Cloud console, go to the _notifications_ **Policies** page: 

[Go to **Alerting Policies**](https://console.cloud.google.com/monitoring/alerting/policies)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Select the alerting policy you want to remove a tag from.
  3. Click **Tags**.
  4. In the dialog, hold the pointer over the tag to remove, and click delete **Delete item**. Click **Save** to save your changes.
  5. A dialog confirming your changes appears. Click **Confirm** to finalize your changes.



###  gcloud 

Before using any of the command data below, make the following replacements: 

  * TAG_VALUE_ID: The permanent ID or the namespaced name of the tag value. For example, `tagValues/4567890123`. For more information about tag identifiers, see [Tag definitions and identifiers](https://docs.cloud.google.com/iam/docs/tags-access-control#definitions).
  * PARENT: The fully qualified name of the parent resource. For example, `//monitoring.googleapis.com/projects/PROJECT_ID_OR_NUMBER/dashboards/DASHBOARD_ID` or `//monitoring.googleapis.com/projects/PROJECT_ID_OR_NUMBER/alertPolicies/POLICY_ID`.



Execute the [`resource-manager tags bindings delete`](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/tags/bindings/delete) command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud resource-manager tags bindings delete \
        --tag-value=TAG_VALUE_ID \
        --parent=PARENT

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud resource-manager tags bindings delete `
        --tag-value=TAG_VALUE_ID `
        --parent=PARENT

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud resource-manager tags bindings delete ^
        --tag-value=TAG_VALUE_ID ^
        --parent=PARENT

The response is empty. 

## Limitations

You can't filter dashboards or alerting policies by attached tags. If you want to list resources that have a specific tag attached, then we recommend that you attach a label along with the tag and filter by the label. For information on adding labels, see [Annotate alerts with labels](https://docs.cloud.google.com/monitoring/alerts/labels) and [Add or remove labels to dashboards](https://docs.cloud.google.com/monitoring/charts/dashboards#add-remove-labels).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
