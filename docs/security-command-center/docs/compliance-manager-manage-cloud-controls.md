---
url: https://docs.cloud.google.com/security-command-center/docs/compliance-manager-manage-cloud-controls/
title: Manage cloud controls \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:50:43.106506+00:00
---

# Manage cloud controls  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/compliance-manager-manage-cloud-controls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Manage cloud controls Stay organized with collections  Save and categorize content based on your preferences. 

Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

Compliance Manager includes many built-in cloud controls that you can add to frameworks and deploy in your environment. If required, you can create and manage your own custom cloud controls and update built-in cloud controls.

**Note:** Custom cloud controls are exclusive to Premium and Enterprise [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers). 

## Before you begin

Complete these tasks before you complete the remaining tasks on this page.

### Set up permissions

  * To get the permissions that you need to manage cloud controls frameworks, ask your administrator to grant you the following IAM roles on your organization or project: 

    * [Compliance Manager Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsecuritycompliance#cloudsecuritycompliance.admin) (`roles/cloudsecuritycompliance.admin`)
    * To create or modify cloud controls that are based on organization policies, one of: 
      * [Organization Policy Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/orgpolicy#orgpolicy.policyAdmin) (`roles/orgpolicy.policyAdmin`)
      * [Assured Workloads Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredworkloads#assuredworkloads.admin) (`roles/assuredworkloads.admin`)
      * [Assured Workloads Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredworkloads#assuredworkloads.editor) (`roles/assuredworkloads.editor`)
    * To create or modify cloud controls that are based on project policies: [Project IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`) 

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 




### Set up Google Cloud CLI

In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

To set up the gcloud CLI to use service account impersonation to authenticate to Google APIs, rather than your user credentials, run the following command: 
    
    
    gcloud config set auth/impersonate_service_account SERVICE_ACCT_EMAIL

For more information, see [Service account impersonation](https://docs.cloud.google.com/security-command-center/docs/reference/authentication#sa-impersonation). 

## View cloud controls

Complete the following steps to view built-in cloud controls and any custom cloud controls that you already created.

###  Console 

  1. In the Google Cloud console, go to the **Compliance** page.

[Go to Compliance](https://console.cloud.google.com/security/command-center/compliance)

  2. Select your organization or project.

  3. In the **Configure** tab, click **Cloud Controls**. The available cloud controls display.

The dashboard includes information about which frameworks include the cloud control and the number of resources (organization, folders, and projects) that the cloud control is applied to.

  4. To view details about a cloud control, click the control name.




###  CLI 

You can see information about a specific cloud control or list all the cloud controls in your organization.

### See details about a cloud control

To see details about a specific cloud control, run the `gcloud compliance-manager cloud-controls describe` command:
    
    
    gcloud compliance-manager cloud-controls describe CLOUD_CONTROL \
       --location=LOCATION \
       --organization=ORGANIZATION \
       [--major-revision-id=MAJOR_REVISION_ID]
    

Replace the following values:

  * `CLOUD_CONTROL`: the name of the cloud control

  * `ORGANIZATION`: your organization ID

  * `LOCATION`: the region that the cloud control is stored in

  * `MAJOR_REVISION_ID` is an optional flag that specifies which version of the cloud control to view. If you don't include the flag, the latest version is returned.




For example, to view a cloud control with the name `builtin-block-external-ip-addresses-for-vm-access` and the major revision number `1`, run the following:
    
    
    gcloud compliance-manager cloud-controls describe \
       builtin-block-external-ip-addresses-for-vm-access \
       --organization=3589215982 \
       --location=global \
       --major-revision-id=1
    

For more information, see [gcloud compliance-manager cloud-controls describe](https://docs.cloud.google.com/sdk/gcloud/reference/compliance-manager/cloud-controls/describe).

### Get list of cloud controls

To get the list of cloud controls in your organization, run the `gcloud compliance-manager cloud-controls list` command:
    
    
    gcloud compliance-manager cloud-controls list \
       --location=LOCATION \
       --organization=ORGANIZATION
    

Replace the following values:

  * `ORGANIZATION`: your organization ID

  * `LOCATION`: the region that the cloud controls are stored in




For example, to view all cloud controls within organization `3589215982` and stored in the global location, run the following:
    
    
    gcloud compliance-manager cloud-controls list \
       --organization=3589215982 \
       --location=global
    

For information about optional flags, see [gcloud compliance-manager cloud-controls list](https://docs.cloud.google.com/sdk/gcloud/reference/compliance-manager/cloud-controls/list).

## Create a custom cloud control

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

When you create a custom cloud control, you apply a rule to any Cloud Asset Inventory [resource type](https://docs.cloud.google.com/asset-inventory/docs/asset-types#resource-types).

###  Console 

When using the console, you can create custom cloud controls with one rule that applies to one Cloud Asset Inventory resource type.

  1. In the Google Cloud console, go to the **Compliance** page.

[Go to Compliance](https://console.cloud.google.com/security/command-center/compliance)

  2. Select your organization or project.

  3. In the **Configure** tab, click **Cloud Controls**. The list of available cloud controls are displayed.

  4. Create a cloud control, either with Gemini or manually:




###  Use Gemini 

  1. Ask Gemini to generate a cloud control for you. Based on your prompt, Gemini provides a unique identifier, a name, associated detection logic, and possible remediation steps.

  2. Review the recommendations and make any required changes.

  3. Save your custom cloud control.




###  Create manually 

  1. In **Cloud control ID** , provide a unique identifier for your control.

  2. Enter a name and description to help users in your organization understand the purpose of the custom cloud control.

  3. Optional: Select the categories for the control. Click **Continue**.

  4. Select an available resource type for your custom cloud control. Compliance Manager supports all resource types. To find the name for a resource, see [Asset types](https://docs.cloud.google.com/asset-inventory/docs/asset-types).

  5. Provide the detection logic for your cloud control, in Common Expression Language (CEL) format.

CEL expressions let you define how you want to evaluate the properties of a resource. For more information and examples, see [Write rules for custom cloud controls](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-write-cel-expressions). Click **Continue**.

If your evaluation rule isn't valid, an error is displayed.

  6. Select an appropriate findings severity.

  7. Write your remediation instructions so that incident responders and administrators in your organization can resolve any findings for the cloud control. Click **Continue**.

  8. Review your entries, and then click **Create**.




###  CLI 

When using the gcloud CLI, you can create a custom cloud control with a maximum of three rules. Each rule can apply to only one resource type.

To create a custom cloud control, run the `gcloud compliance-manager cloud-controls create` command:
    
    
    gcloud compliance-manager cloud-controls create CLOUD_CONTROL \
       --location=LOCATION \
       --organization=ORGANIZATION \
       [--display-name=DISPLAY_NAME] \
       [--description=DESCRIPTION] \
       [--categories=[CATEGORIES,...]] \
       [--finding-category=FINDING_CATEGORY] \
       [--parameter-spec=[defaultValue=DEFAULTVALUE],[description=DESCRIPTION],[displayName=DISPLAYNAME],[isRequired=ISREQUIRED],[name=NAME],[substitutionRules=SUBSTITUTIONRULES],[validation=VALIDATION],[valueType=VALUETYPE]] \
       [--remediation-steps=REMEDIATION_STEPS] \
       [--rules=[celExpression=CELEXPRESSION],[description=DESCRIPTION],[ruleActionTypes=RULEACTIONTYPES]] \
       [--severity=SEVERITY] \
       [--supported-cloud-providers=[SUPPORTED_CLOUD_PROVIDERS,…]] \
       [--supported-target-resource-types=[SUPPORTED_TARGET_RESOURCE_TYPES,…]]
    

Replace the following values:

  * `CLOUD_CONTROL`: a unique alphanumeric name for the cloud control

  * `ORGANIZATION`: your organization ID

  * `LOCATION`: the region that the cloud control is stored in

  * `DISPLAY_NAME`: a human-readable name for the cloud control

  * `DESCRIPTION`: an optional description of the purpose of the cloud control

  * `CATEGORIES,…`: an optional parameter that defines the categories that the cloud control is part of. For a list of permitted categories, see [gcloud compliance-manager cloud-controls create](https://docs.cloud.google.com/sdk/gcloud/reference/compliance-manager/cloud-controls/create).

  * `FINDING_CATEGORY`: the value that shows in the Security Command Center findings dashboard when the cloud control generates a finding

  * --parameter-spec=[defaultValue=DEFAULTVALUE], \
         [description=DESCRIPTION], \
         [displayName= DISPLAYNAME], \
         [isRequired=ISREQUIRED], \
         [name=NAME], \
         [substitutionRules=SUBSTITUTIONRULES], \
         [validation=VALIDATION], \
         [valueType=VALUETYPE]...]
        

is the optional parameter information for the cloud control, in the following format:

    * `DEFAULTVALUE`: the data that is applied if a user doesn't customize the parameter when deploying a framework. Supported value types are `boolValue`, `numberValue`, `stringListValue`, or `stringValue`.

    * `DESCRIPTION`: an optional description of the control

    * `ISREQUIRED`: `true` if the control requires a parameter to be set

    * `NAME`: the name of the parameter

    * `SUBSTITUTIONRULES`: how and where Compliance Manager injects the custom value for the parameter. Specify the targeted path inside the rule using a proto dot notation (for example, `rules[0].org_policy_constraint...`) Choose one of the following options:

      * `attributeSubstitutionRule` when you want to inject the parameter value directly into a structural field of your rule (for example, filling a list of restricted values inside an organization policy constraint rule template).

      * `placeholderSubstitutionRule` when your rule uses a text string (or CEL expression). The string must contain a placeholder variable that's prefixed with `$` (for example, `$deniedServices`), and this rule tells the compiler to map the parameter to that placeholder.

The following example creates a list parameter named `deniedServices` with the `STRINGLIST` type. It uses `attributeSubstitutionRule` to add user-provided service names (such as `compute.googleapis.com`) directly into a structural custom organization policy rule (`denied_values`) when deployed:
    
    --parameter-spec='name=deniedServices,isRequired=true,valueType=STRINGLIST,substitutionRules=[{attributeSubstitutionRule={attribute="rules[0].org_policy_constraint.policy_rules[0].values.denied_values"}}]'

    * `VALIDATION` is the permitted set of values. Choose one of the following options:

      * Use `allowedValues` to enforce a static allowlist—for example, limit location parameters to specific string fields: `validation={allowedValues={values=[{stringValue=us-central1},{stringValue=us-west1}]}}`

      * Use `intRange` to enforce numeric bounds on integers—for example, set a retention period between 1 and 365: `validation={intRange={min=1,max=365}}`

      * Use `regexpPattern` to enforce regular expression matching on string text—for example, require strict alphanumeric naming: `validation={regexpPattern={pattern="^[a-z][-a-z0-9]*$"}}`

    * `VALUETYPE`: the data type or format of the value that a user provides for this parameter. Supported value types are `STRING`, `BOOLEAN`, `STRINGLIST`, `NUMBER`, and `ONEOF`.

Alternatively, you can specify a JSON or YAML file that defines the parameters. For example, `--parameter-spec=path_to_file.(yaml|json)`. Expand the following section to view example JSON and YAML files.

#### Example JSON file
    
    [
        {
          "name": "deniedServices",
          "displayName": "Services Requiring CMEK",
          "description": "List of service names that must use Customer-Managed Encryption Keys.",
          "isRequired": true,
          "valueType": "STRINGLIST",
          "substitutionRules": [
            {
              "attributeSubstitutionRule": {
                "attribute": "rules[0].org_policy_constraint.policy_rules[0].values.denied_values"
              }
            }
          ]
        }
      ]
          

#### Example YAML file
    
    - name: deniedServices
        displayName: "Services Requiring CMEK"
        description: "List of service names that must use Customer-Managed Encryption Keys."
        isRequired: true
        valueType: STRINGLIST
        substitutionRules:
        - attributeSubstitutionRule:
            attribute: "rules[0].org_policy_constraint.policy_rules[0].values.denied_values"
          

  * REMEDIATION_STEPS: the steps required to resolve any findings. This string is limited to 400 characters.

  * `--rules=[celExpression=CELEXPRESSION],[description=DESCRIPTION],[ruleActionTypes=RULEACTIONTYPES]` is the rule that you want to enforce, in the following format:

    * `CELEXPRESSION`: the common expression language (CEL) expression of the rule. For information about writing CEL expressions, see [Write rules for custom cloud controls](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-write-cel-expressions). Include the following:

      * `expression`: the CEL expression, with a maximum of 1000 characters

      * `resourceTypesValues`: the name of the resources, in the format `SERVICE_NAME/type`. Use a `values` array to list all your resource types that you want to apply the rule to—for example, `values=[compute.googleapis.com/Instance]`.

    * `DESCRIPTION`: a description of the rule

    * `RULEACTIONTYPES`: the action that the rule performs. Supported values are `rule-action-type-detective`, `rule-action-type-preventive`, and `rule-action-type-audit`.

For example, to check the Cloud Key Management Service key rotation period, enter the following:
    
    --rules="[
      {
        \"celExpression\": {
          \"expression\": \"has(resource.data.rotationPeriod) && resource.data.rotationPeriod < duration('60h')\",
          \"resourceTypesValues\": {
            \"values\": [
              \"cloudkms.googleapis.com/CryptoKey\"
            ]
          }
        },
        \"description\": \"Check KMS key rotation period\",
        \"ruleActionTypes\": [
          \"rule-action-type-detective\"
        ]
      }
    ]"
    

Alternatively, you can specify a JSON or YAML file that defines the rule. For example, `--rules=path_to_file.(yaml|json)`. Expand the following section to view example JSON and YAML files.

#### Example JSON file
    
    [
        {
          "celExpression": {
            "expression": "has(resource.data.rotationPeriod) && resource.data.rotationPeriod < duration('60h')",
            "resourceTypesValues": {
              "values": [
                "cloudkms.googleapis.com/CryptoKey"
              ]
            }
          },
          "description": "Check KMS key rotation period to ensure it is under 60 hours.",
          "ruleActionTypes": [
            "rule-action-type-detective"
          ]
        }
      ]
          

#### Example YAML file
    
    - celExpression:
          expression: "has(resource.data.rotationPeriod) && resource.data.rotationPeriod < duration('60h')"
          resourceTypesValues:
            values:
            - cloudkms.googleapis.com/CryptoKey
        description: "Check KMS key rotation period to ensure it is under 60 hours."
        ruleActionTypes:
        - rule-action-type-detective
          

  * `SEVERITY`: the criticality level for the cloud control. Supported values are `critical`, `high`, `medium`, and `low`.

  * `SUPPORTED_CLOUD_PROVIDERS,…`: the cloud providers that this cloud control applies to. The only supported value is `gcp`.

  * `SUPPORTED_TARGET_RESOURCE_TYPES,…`: the resource types (organization, folder, project, or app-enabled folder in App Hub) that the cloud control supports. Supported values are `target-resource-crm-type-folder`, `target-resource-crm-type-org`, `target-resource-crm-type-project`, and `target-resource-type-application`.




For example, to create a cloud control that enforces resource locations, run the following command:
    
    
      gcloud compliance-manager cloud-controls create \
         restrict-resource-locations \
         --organization=3589215982 \
         --location=global \
         --display-name="Restrict Resource Locations" \
         --description="Enforces checks to ensure resources are only deployed in approved cloud regions." \
         --severity=high \
         --finding-category="LOCATION_VIOLATION" \
         --supported-cloud-providers="gcp" \
         --supported-target-resource-types="target-resource-crm-type-project" \
         --parameter-spec='name=allowedLocations,isRequired=true,valueType=STRINGLIST,substitutionRules=[{placeholderSubstitutionRule={attribute="rules[0].cel_expression.expression"}}]' \
         --rules="[{\"celExpression\": {\"expression\": \"resource.location in \$allowedLocations\", \"resourceTypesValues\": {\"values\": [\"compute.googleapis.com/Instance\"]}}, \"description\": \"Check Compute Engine instance locations\", \"ruleActionTypes\": [\"rule-action-type-detective\"]}]"
    

To create the same control but use YAML files to define the parameters and rules, run:
    
    
         gcloud compliance-manager cloud-controls create \
         restrict-resource-locations \
         --organization=3589215982 \
         --location=global \
         --display-name="Restrict Resource Locations" \
         --description="Enforces checks to ensure resources are only deployed in approved cloud regions." \
         --severity=high \
         --finding-category="LOCATION_VIOLATION" \
         --supported-cloud-providers="gcp" \
         --supported-target-resource-types="target-resource-crm-type-project" \
         --parameter-spec=parameters.yaml \
         --rules=rules.yaml
    

For more information, see [gcloud compliance-manager cloud-controls create](https://docs.cloud.google.com/sdk/gcloud/reference/compliance-manager/cloud-controls/create).

###  Terraform 

When using Terraform, you can create a custom cloud control with a maximum of three rules. Each rule can apply to only one resource type.

The following sample shows how you can create a custom cloud control using Terraform.
    
    
    resource "google_cloud_security_compliance_cloud_control" "example" {
      parent              = "organizations/123456789"
      location            = "global"
      cloud_control_id    = "example-cloudcontrol"
    
      display_name      = "TF test CloudControl Name"
      description       = "A test cloud control for security compliance"
      categories        = ["CC_CATEGORY_INFRASTRUCTURE"]
      severity          = "HIGH"
      finding_category  = "SECURITY_POLICY"
      remediation_steps = "Review and update the security configuration according to best practices."
    
      supported_cloud_providers        = ["GCP"]
    
      rules {
        description         = "Ensure compute instances have secure boot enabled"
        rule_action_types   = ["RULE_ACTION_TYPE_DETECTIVE"]
    
        cel_expression {
          expression = "resource.data.shieldedInstanceConfig.enableSecureBoot == true"
          resource_types_values {
            values = ["compute.googleapis.com/Instance"]
          }
        }
      }
    
      parameter_spec {
        name         = "location"
        display_name = "Resource Location"
        description  = "The location where the resource should be deployed"
        value_type   = "STRING"
        is_required  = true
    
        default_value {
          string_value = "us-central1"
        }
    
        validation {
          regexp_pattern {
            pattern = "^[a-z]+-[a-z]+[0-9]$"
          }
        }
      }
    
      parameter_spec {
        name         = "enable_secure_boot"
        display_name = "Enable Secure Boot"
        description  = "Whether to enable secure boot for instances"
        value_type   = "BOOLEAN"
        is_required  = true
    
        default_value {
          bool_value = true
        }
    
        substitution_rules {
          attribute_substitution_rule {
            attribute = "rules[0].cel_expression.expression"
          }
        }
    
        validation {
          allowed_values {
            values {
              bool_value = true
            }
          }
        }
      }
    
      parameter_spec {
        name         = "max_instances"
        display_name = "Maximum Instances"
        description  = "Maximum number of instances allowed"
        value_type   = "NUMBER"
        is_required  = false
    
        default_value {
          number_value = 10
        }
    
        substitution_rules {
          placeholder_substitution_rule {
            attribute = "rules[0].description"
          }
        }
    
        validation {
          int_range {
            min = "1"
            max = "100"
          }
        }
      }
    
      parameter_spec {
        name         = "allowed_regions"
        display_name = "Allowed Regions"
        description  = "List of regions where resources can be deployed"
        value_type   = "STRINGLIST"
        is_required  = true
    
        default_value {
          string_list_value {
            values = ["us-central1", "us-east1", "us-west1"]
          }
        }
    
        validation {
          allowed_values {
            values {
              string_list_value {
                values = ["us-central1", "us-east1"]
              }
            }
            values {
              string_list_value {
                values = ["us-west1", "us-west2"]
              }
            }
          }
        }
      }
    
      parameter_spec {
        name         = "environment_type"
        display_name = "Environment Type"
        description  = "The type of environment"
        value_type   = "STRING"
        is_required  = true
    
        default_value {
          string_value = "production"
        }
    
        validation {
          allowed_values {
            values {
              string_value = "production"
            }
            values {
              string_value = "staging"
            }
            values {
              number_value = 1
            }
          }
        }
      }
    }
    

## Edit a custom cloud control

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

After you create a cloud control, you can change its name, description, rules, remediation steps, and severity level. You can't change the cloud control category.

  1. In the Google Cloud console, go to the **Compliance** page.

[Go to Compliance](https://console.cloud.google.com/security/command-center/compliance)

  2. Select your organization or project.

  3. In the **Configure** tab, click **Cloud Controls**. The list of available cloud controls display.

  4. Click the cloud control that you want to edit.

  5. In the **Cloud controls details** page, verify that the cloud control isn't included in a framework. If required, [edit the framework to remove the cloud control](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-apply-framework#update-custom-framework).

  6. Click **Edit**.

  7. In the **Edit custom cloud control** page, change the name and description as required. Click **Continue**.

  8. Update the rules, finding severity, and remediation steps. Click **Continue**.

  9. Review your changes and click **Save**.




## Update a built-in cloud control to a newer release

Google publishes regular updates to its built-in cloud controls as services deploy new features or as new best practices emerge. Updates can include new controls or changes to existing controls.

You can view the releases of built-in cloud controls in the cloud controls dashboard in the **Configure** tab or in the cloud control details page.

Google notifies you in the release notes when the following items are updated:

  * Cloud control name
  * Finding category
  * Change in the detective or preventive logic in a rule
  * Underlying logic of a rule



To update a cloud control after you receive a notification, you must unassign and redeploy the frameworks that include the cloud control. For instructions, see [Update a framework to a newer release](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-apply-framework#update-framework-version).

## Delete a custom cloud control

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

Delete a cloud control when it's no longer required. You can only delete cloud controls that you create. You can't delete built-in cloud controls.

###  Console 

  1. In the Google Cloud console, go to the **Compliance** page.

[Go to Compliance](https://console.cloud.google.com/security/command-center/compliance)

  2. Select your organization or project.

  3. In the **Configure** tab, click **Cloud Controls**. The list of available cloud controls display.

  4. Click the cloud control that you want to delete.

  5. In the **Cloud controls details** page, verify that the cloud control isn't included in a framework. If required, [edit the framework to remove the cloud control](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-apply-framework#update-custom-framework).

  6. Click **Delete**.

  7. In the **Delete** window, review the message. Type `Delete` and click **Confirm**.




###  CLI 

To delete a custom cloud control, run the `gcloud compliance-manager cloud-controls delete` command:
    
    
    gcloud compliance-manager cloud-controls delete CLOUD_CONTROL \
       --location=LOCATION \
       --organization=ORGANIZATION
    

Replace the following values:

  * `CLOUD_CONTROL`: the name of the cloud control

  * `ORGANIZATION`: your organization ID

  * `LOCATION`: the region that the cloud control is stored in




For example, to delete a cloud control with the name `restrict-resource-locations`, run the following:
    
    
    gcloud compliance-manager cloud-controls delete \
       restrict-resource-locations \
       --organization=3589215982 \
       --location=global
    

For more information, see [gcloud compliance-manager cloud-controls delete](https://docs.cloud.google.com/sdk/gcloud/reference/compliance-manager/cloud-controls/delete).

## Mapping of Security Health Analytics detectors to cloud controls

The following table shows how Compliance Manager cloud controls map to Security Health Analytics detectors.

Finding category in Security Health Analytics | Cloud control name in Compliance Manager  
---|---  
`ACCESS_TRANSPARENCY_DISABLED` | Enable Access Transparency  
`ADMIN_SERVICE_ACCOUNT` | Block Administrator Roles from Service Accounts  
`ALLOWED_INGRESS_ORG_POLICY` | Configure the Allowed Ingress Settings for Cloud Run Organization Policy Constraint  
`ALLOWED_VPC_EGRESS_ORG_POLICY` | Configure the Allowed VPC Egress Settings for Cloud Run Organization Policy Constraint  
`ALLOYDB_AUTO_BACKUP_DISABLED` | Enable AlloyDB Automated Backups on Cluster  
`ALLOYDB_BACKUPS_DISABLED` | Enable AlloyDB Backups on Cluster  
`ALLOYDB_CMEK_DISABLED` | Enable CMEK for AlloyDB Clusters  
`ALLOYDB_LOG_ERROR_VERBOSITY` | Set Log Error Verbosity Flag for AlloyDB Instances  
`ALLOYDB_LOG_MIN_ERROR_STATEMENT_SEVERITY` | Set Log Min Error Statement Flag for AlloyDB Instances  
`ALLOYDB_LOG_MIN_MESSAGES` | Set Log Min Messages Flag for AlloyDB Instances  
`ALLOYDB_PUBLIC_IP` | Block Public IP Addresses for AlloyDB Cluster Instances  
`ALPHA_CLUSTER_ENABLED` | Disable Alpha Features on GKE Clusters  
`API_KEY_APPS_UNRESTRICTED` | Restrict API Keys for Required APIs Only  
`API_KEY_EXISTS` | Not available  
`API_KEY_NOT_ROTATED` | Require Rotation of API Key  
`AUDIT_CONFIG_NOT_MONITORED` | Configure Log Metrics and Alerts for Audit Logging Changes  
`AUDIT_LOGGING_DISABLED` | Implement Event Logging for Google Cloud Services  
`AUTO_BACKUP_DISABLED` | Enable Automatic Backups for Cloud SQL Databases  
`AUTO_REPAIR_DISABLED` | Enable Auto Repair for GKE Clusters  
`AUTO_UPGRADE_DISABLED` | Enable Auto Upgrade on GKE Clusters  
`BIGQUERY_TABLE_CMEK_DISABLED` | Enable CMEK for BigQuery Tables  
`BINARY_AUTHORIZATION_DISABLED` | Require Binary Authorization on a Cluster  
`BUCKET_CMEK_DISABLED` | Enable CMEK for Cloud Storage Buckets  
`BUCKET_IAM_NOT_MONITORED` | Configure Log Metrics and Alerts for Cloud Storage IAM Policy Changes  
`BUCKET_LOGGING_DISABLED` | Require Cloud Storage Bucket Logging  
`BUCKET_POLICY_ONLY_DISABLED` | Enable Uniform Bucket-Level Access on Cloud Storage Buckets  
`CLOUD_ASSET_API_DISABLED` | Enable Cloud Asset Inventory Service  
`CLUSTER_LOGGING_DISABLED` | Enable Cloud Logging on GKE Clusters  
`CLUSTER_MONITORING_DISABLED` | Enable Cloud Monitoring on GKE Clusters  
`CLUSTER_PRIVATE_GOOGLE_ACCESS_DISABLED` | Enable Private Google Access on an instance  
`CLUSTER_SECRETS_ENCRYPTION_DISABLED` | Enable Encryption on GKE Clusters  
`CLUSTER_SHIELDED_NODES_DISABLED` | Enable Shielded GKE Nodes on a Cluster  
`COMPUTE_PROJECT_WIDE_SSH_KEYS_ALLOWED` | Block Project-Wide SSH Keys on Compute Engine Instances  
`COMPUTE_SECURE_BOOT_DISABLED` | Enable Secure Boot on Compute Engine Instances  
`COMPUTE_SERIAL_PORTS_ENABLED` | Block Serial Ports for Compute Engine Instances  
`CONFIDENTIAL_COMPUTING_DISABLED` | Enable Confidential Computing for Compute Engine Instances  
`COS_NOT_USED` | Require Container-Optimized OS for a GKE Cluster  
`CUSTOM_ORG_POLICY_VIOLATION` | Not available  
`CUSTOM_ROLE_NOT_MONITORED` | Configure Log Metrics and Alerts for Custom Role Changes  
`DATAPROC_CMEK_DISABLED` | Require CMEK on Dataproc Clusters  
`DATAPROC_IMAGE_OUTDATED` | Use Latest Image Versions on Dataproc Clusters  
`DATASET_CMEK_DISABLED` | Enable CMEK for BigQuery Datasets  
`DEFAULT_NETWORK` | Use Networks with Custom Firewall Rules  
`DEFAULT_SERVICE_ACCOUNT_USED` | Use Custom Service Accounts for Compute Engine Instances  
`DISABLE_VPC_EXTERNAL_IP_V6_ORG_POLICY` | Configure the Disable VPC External IPv6 Usage Organization Policy  
`DISABLE_VPC_INTERNAL_IP_V6_ORG_POLICY` | Configure the Disable VPC External IPv6 Usage Organization Policy  
`DISABLED_SERIAL_PORT_ACCESS_ORG_POLICY` | Configure the Disable VM Serial Port Logging to Stackdriver Organization Policy  
`DISK_CMEK_DISABLED` | Enable CMEK on Compute Engine Persistent Disks  
`DISK_CSEK_DISABLED` | Enable CSEK On Compute Engine Persistent Disks  
`DNS_LOGGING_DISABLED` | Enable Cloud DNS Logs Monitoring  
`DNSSEC_DISABLED` | Enable DNSSEC for Cloud DNS  
`EGRESS_DENY_RULE_NOT_SET` | Enforce Deny All Egress Firewall Rule  
`ESSENTIAL_CONTACTS_NOT_CONFIGURED` | Define Essential Contacts  
`FIREWALL_NOT_MONITORED` | Configure Log Metrics and Alerts for VPC Network Firewall Changes  
`FIREWALL_RULE_LOGGING_DISABLED` | Enable Firewall Rule Logging  
`FLOW_LOGS_DISABLED` | Enable Flow Logs for VPC Subnet  
`FULL_API_ACCESS` | Restrict API Access to Google Cloud APIs for Compute Engine Instances  
`HTTP_LOAD_BALANCER` | Enforce HTTPS Traffic Only  
`INCORRECT_BQ4G_SERVICE_PERIMETER` | Define Service Perimeters in VPC Service Controls  
`INSTANCE_OS_LOGIN_DISABLED` | Enable OS Login  
`INTEGRITY_MONITORING_DISABLED` | Enable Integrity Monitoring on GKE Clusters  
`INTRANODE_VISIBILITY_DISABLED` | Enable Intranode Visibility for GKE Clusters  
`IP_ALIAS_DISABLED` | Enable IP Alias Range for GKE Clusters  
`IP_FORWARDING_ENABLED` | Prevent IP Forwarding on Compute Engine Instances  
`KMS_KEY_NOT_ROTATED` | Define Rotation Period for Cloud KMS Keys  
`KMS_PROJECT_HAS_OWNER` | Not available  
`KMS_PUBLIC_KEY` | Not available  
`KMS_ROLE_SEPARATION` | Enforce Separation of Duties  
`LEGACY_AUTHORIZATION_ENABLED` | Block Legacy Authorization on GKE Clusters  
`LEGACY_METADATA_ENABLED` | Disable Legacy Metadata Server Endpoints on Compute Engine  
`LEGACY_NETWORK` | Don't Use Legacy Networks  
`LOAD_BALANCER_LOGGING_DISABLED` | Enable Load Balancer Logging  
`LOCKED_RETENTION_POLICY_NOT_SET` | Lock Storage Bucket Retention Policies  
`LOG_NOT_EXPORTED` | Configure Log Sinks  
`MASTER_AUTHORIZED_NETWORKS_DISABLED` | Enable Control Plane Authorized Networks on GKE Clusters  
`MFA_NOT_ENFORCED` | Not available  
`NETWORK_NOT_MONITORED` | Configure Log Metrics and Alerts for VPC Network Changes  
`NETWORK_POLICY_DISABLED` | Enable Network Policy on GKE Clusters  
`NODEPOOL_BOOT_CMEK_DISABLED` | Enable CMEK on GKE Node Pool Boot Disks  
`NODEPOOL_SECURE_BOOT_DISABLED` | Enable Secure Boot for Shielded GKE Nodes  
`NON_ORG_IAM_MEMBER` | Not available  
`OBJECT_VERSIONING_DISABLED` | Enable Object Versioning on Buckets  
`OPEN_CASSANDRA_PORT` | Block Connections to Cassandra Ports from All IP Addresses  
`OPEN_CISCOSECURE_WEBSM_PORT` | Block Connections to CiscoSecure/WebSM Ports from All IP Addresses  
`OPEN_DIRECTORY_SERVICES_PORT` | Block Connections to Directory Services Ports from All IP Addresses  
`OPEN_DNS_PORT` | Block Connections to DNS Ports from All IP Addresses  
`OPEN_ELASTICSEARCH_PORT` | Block Connections to Elasticsearch Ports from All IP Addresses  
`OPEN_FIREWALL` | Not available  
`OPEN_FTP_PORT` | Block Connections to FTP Ports from All IP Addresses  
`OPEN_GROUP_IAM_MEMBER` | Not available  
`OPEN_HTTP_PORT` | Block Connections to HTTP Ports from All IP Addresses  
`OPEN_LDAP_PORT` | Block Connections to LDAP Ports from All IP Addresses  
`OPEN_MEMCACHED_PORT` | Block Connections to Memcached Ports from All IP Addresses  
`OPEN_MONGODB_PORT` | Block Connections to MongoDB Ports from All IP Addresses  
`OPEN_MYSQL_PORT` | Block Connections to MySQL Ports from All IP Addresses  
`OPEN_NETBIOS_PORT` | Block Connections to NetBIOS Ports from All IP Addresses  
`OPEN_ORACLEDB_PORT` | Block Connections to Oracle Database Ports from All IP Addresses  
`OPEN_POP3_PORT` | Block Connections to POP3 Server Ports from All IP Addresses  
`OPEN_POSTGRESQL_PORT` | Block Connections to PostgreSQL Server Ports from All IP Addresses  
`OPEN_RDP_PORT` | Block Access to RDP Port  
`OPEN_REDIS_PORT` | Block Connections to Redis Server Ports from All IP Addresses  
`OPEN_SMTP_PORT` | Block Connections to SMTP Server Ports from All IP Addresses  
`OPEN_SSH_PORT` | Block Access to SSH Port  
`OPEN_TELNET_PORT` | Block Connections to Telnet Server Ports from All IP Addresses  
`ORG_POLICY_CONFIDENTIAL_VM_POLICY` | Enable the Confidential VM Organization Policy Constraint  
`OS_LOGIN_DISABLED` | Enable OS Login for All Instances at Project Level  
`OVER_PRIVILEGED_ACCOUNT` | Use Least Privilege Service Accounts for GKE Clusters  
`OVER_PRIVILEGED_SCOPES` | Create GKE Clusters with Limited Service Account Access Scopes  
`OVER_PRIVILEGED_SERVICE_ACCOUNT_USER` | Block Administrator Roles from Service Accounts  
`OWNER_NOT_MONITORED` | Not available  
`POD_SECURITY_POLICY_DISABLED` | Not available  
`PRIMITIVE_ROLES_USED` | Restrict Legacy IAM Roles  
`PRIVATE_CLUSTER_DISABLED` | Enable Private Clusters for GKE  
`PRIVATE_GOOGLE_ACCESS_DISABLED` | Enable Private Google Access for VPC Subnets  
`PUBLIC_BUCKET_ACL` | Restrict Public Access to Cloud Storage Buckets  
`PUBLIC_COMPUTE_IMAGE` | Restrict Public Access to Compute Images  
`PUBLIC_DATASET` | Restrict Public Access to BigQuery Datasets  
`PUBLIC_IP_ADDRESS` | Restrict Public IP Addresses to Compute Engine Instances  
`PUBLIC_LOG_BUCKET` | Restrict Public Access to Cloud Storage Buckets  
`PUBLIC_SQL_INSTANCE` | Restrict Public Access to Cloud SQL Database Instances  
`PUBSUB_CMEK_DISABLED` | Encrypt Pub/Sub topic with CMEK  
`QL_LOG_STATEMENT_STATS_ENABLED` | Enable Log Statement Flag for PostgreSQL  
`REDIS_ROLE_USED_ON_ORG` | Not available  
`RELEASE_CHANNEL_DISABLED` | Subscribe a GKE Cluster to a Release Channel  
`REQUIRE_OS_LOGIN_ORG_POLICY` | Enable OS Login  
`REQUIRE_VPC_CONNECTOR_ORG_POLICY` | Define VPC Connector Egress For Cloud Run Functions  
`RESTRICT_AUTHORIZED_NETWORKS_ORG_POLICY` | Enable the Restrict Authorized Networks on Cloud SQL Instances Organization Policy Constraint  
`ROUTE_NOT_MONITORED` | Configure Log Metrics and Alerts for VPC Route Changes  
`RSASHA1_FOR_SIGNING` | Avoid RSASHA1 for DNSSEC Signing  
`S3_BUCKET_ACCESS_LOGGING_ENABLED_CLOUDTRAIL_S3_BUCKET` | Not available  
`S3_BUCKETS_CONFIGURED_BLOCK_PUBLIC_ACCESS_BUCKET_AND_ACCOUNT_SETTINGS` | Not available  
`SERVICE_ACCOUNT_KEY_NOT_ROTATED` | Require Service Account Key Rotation  
`SERVICE_ACCOUNT_ROLE_SEPARATION` | Enforce Separation of Duties  
`SHIELDED_VM_DISABLED` | Enable Shielded VM for Compute Engine Instances  
`SKIP_DEFAULT_NETWORK_CREATION_ORG_POLICY` | Restrict Default Network Creation for Compute Engine Instances  
`SQL_CMEK_DISABLED` | Enable CMEK for Cloud SQL Databases  
`SQL_CONTAINED_DATABASE_AUTHENTICATION` | Turn Off Contained Database Authentication Flag for SQL Server  
`SQL_CROSS_DB_OWNERSHIP_CHAINING` | Turn Off Cross Database Ownership Chaining Flag for SQL Server  
`SQL_EXTERNAL_SCRIPTS_ENABLED` | Turn Off External Scripts Flag for SQL Server  
`SQL_INSTANCE_NOT_MONITORED` | Configure Log Metrics and Alerts for Cloud SQL Configuration Changes  
`SQL_LOCAL_INFILE` | Turn Off Local Infile Flag for MySQL  
`SQL_LOG_CHECKPOINTS_DISABLED` | Enable Log Checkpoints Flag for PostgreSQL  
`SQL_LOG_CONNECTIONS_DISABLED` | Enable Log Connections Flag for PostgreSQL  
`SQL_LOG_DISCONNECTIONS_DISABLED` | Enable Log Disconnections Flag for PostgreSQL  
`SQL_LOG_DURATION_DISABLED` | Enable Log Duration Flag for PostgreSQL instance  
`SQL_LOG_ERROR_VERBOSITY` | Enable Log Error Verbosity Flag for PostgreSQL  
`SQL_LOG_EXECUTOR_STATS_ENABLED` | Turn Off Log Executor Stats Flag for PostgreSQL  
`SQL_LOG_HOSTNAME_ENABLED` | Turn off Log Hostname Flag for PostgreSQL  
`SQL_LOG_LOCK_WAITS_DISABLED` | Enable Log Locks Wait Flag for PostgreSQL instance  
`SQL_LOG_MIN_DURATION_STATEMENT_ENABLED` | Turn Off Log Min Duration Statement Flag for PostgreSQL  
`SQL_LOG_MIN_ERROR_STATEMENT_SEVERITY` | Enable Log Min Error Statement Flag for PostgreSQL  
`SQL_LOG_MIN_ERROR_STATEMENT_SEVERITY` | Not available  
`SQL_LOG_MIN_MESSAGE` | Enable Log Min Messages Flag for PostgreSQL  
`SQL_LOG_PARSER_STATS_ENABLED` | Turn off Log Parser Stats Flag for PostgreSQL  
`SQL_LOG_PLANNER_STATS_ENABLED` | Turn off Log Planner Stats Flag for PostgreSQL  
`SQL_LOG_STATEMENT` | Enable Log Statement Flag for PostgreSQL  
`SQL_LOG_TEMP_FILES` | Enable Log Temp Files Flag for PostgreSQL instance  
`SQL_NO_ROOT_PASSWORD` | Not available  
`SQL_PUBLIC_IP` | Block Public IP Addresses for Cloud SQL Instances  
`SQL_REMOTE_ACCESS_ENABLED` | Turn Off Remote Access Flag for SQL Server  
`SQL_SCANNER` | Enable SSL Encryption On AlloyDB Instances  
`SQL_SKIP_SHOW_DATABASE_DISABLED` | Enable Skip Show Database Flag for MySQL  
`SQL_TRACE_FLAG_3625` | Enable 3625 Trace Database Flag for SQL Server  
`SQL_USER_CONNECTIONS_CONFIGURED` | Don't Use User Connections Flag for SQL Server  
`SQL_USER_OPTIONS_CONFIGURED` | Don't Use User Options Flag for SQL Server  
`SQL_WEAK_ROOT_PASSWORD` | Not available  
`SSL_NOT_ENFORCED` | Enforce SSL for all Incoming Database Connections  
`TOO_MANY_KMS_USERS` | Limit KMS Crypto Keys Users to Three  
`UNIFORM_BUCKET_LEVEL_ACCESS_ORG_POLICY` | Enable Uniform Bucket-Level Access on Cloud Storage Buckets  
`USER_MANAGED_SERVICE_ACCOUNT_KEY` | Restrict User Managed Service Account Keys  
`VPC_FLOW_LOGS_SETTINGS_NOT_RECOMMENDED` | Not available  
`WEAK_SSL_POLICY` | Restrict Insecure SSL Policies for Compute Engine Instances  
`WEB_UI_ENABLED` | Don't Use Kubernetes Web UI  
`WORKLOAD_IDENTITY_DISABLED` | Enable Workload Identity Federation for GKE on clusters  
  
## What's next

  * [Write rules for custom cloud controls](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-write-cel-expressions).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
