---
url: https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-posture/
title: Manage a security posture \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:33:48.396488+00:00
---

# Manage a security posture  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-posture/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Manage a security posture Stay organized with collections  Save and categorize content based on your preferences. 

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) (requires [organization-level activation](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation)) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

This page describes how you can configure and use the [security posture service](https://docs.cloud.google.com/security-command-center/docs/security-posture-overview) after you activate Security Command Center. To start, you must create a posture that includes your policies, organized in policy sets, and then deploy the posture using a posture deployment. After a posture is deployed, you can monitor for drift and further refine your posture over time.

You can't use security posture management with project-level activations. For more information, see [Feature availability with project-level activations](https://docs.cloud.google.com/security-command-center/docs/activate-scc-project-level-limitations).

## Before you begin

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) (requires [organization-level activation](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation))

Complete these tasks before you complete the remaining tasks on this page.

### Activate Security Command Center

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) (requires [organization-level activation](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation))

Verify that you have [activated Security Command Center](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview) at the organization level.

If you want to use Security Health Analytics detectors as policies, select the Security Health Analytics service during the activation process.

### Set up permissions

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) (requires [organization-level activation](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation))

To get the permissions that you need to use posture, ask your administrator to grant you the [Security Posture Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/securityposture#securityposture.admin) (`roles/securityposture.admin`) IAM role. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For more information about security posture roles and security posture permissions, see [IAM for organization-level activations](https://docs.cloud.google.com/security-command-center/docs/access-control-org).

### Set up Google Cloud CLI

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) (requires [organization-level activation](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation))

In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

To set up the gcloud CLI to use service account impersonation to authenticate to Google APIs, rather than your user credentials, run the following command: 
    
    
    gcloud config set auth/impersonate_service_account SERVICE_ACCT_EMAIL

For more information, see [Service account impersonation](https://docs.cloud.google.com/security-command-center/docs/reference/authentication#sa-impersonation). 

### Enable APIs

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) (requires [organization-level activation](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation))

Enable the Organization Policy Service and the security posture service APIs:
    
    
    gcloud services enable orgpolicy.googleapis.com  securityposture.googleapis.com

### Configure connection to AWS

Enterprise (Deprecated) [service tier](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

To use built-in Security Health Analytics detectors that are specific to AWS, you must [connect to AWS for configuration and resource data collection](https://docs.cloud.google.com/security-command-center/docs/connect-scc-to-aws).

## Create and deploy a posture

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) (requires [organization-level activation](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation))

To start using a security posture, you must complete the following:

  * Create a posture YAML file that defines the policies that apply to your security posture.
  * Create a posture in Google Cloud that is based on the posture YAML file.
  * Deploy the posture.



The following sections provide detailed instructions.

### Create a posture YAML file

A posture consists of one or more policy sets that you deploy together. These policy sets include all the preventative and detective policies that you want to include in your posture.

To create your posture, do one of the following:

  * Copy a predefined posture template. If required, make any edits to the policies so that they apply to your environment and comply with your business's regulatory and security standards. For instructions, see Create a posture file from a predefined posture template.
  * Extract existing policies from your environment. If required, make any edits to the policies so that they comply with your business's regulatory and security standards. For instructions, see Create a posture file by extracting policies from an existing environment.
  * Create a Terraform resource that defines the posture. For instructions, see Create a Terraform resource with policy definitions.



For details about the fields that you can use in a posture, see the [`Posture` reference](https://docs.cloud.google.com/security-command-center/docs/reference/securityposture/rest/v1/Posture) and the [`PolicySet` reference](https://docs.cloud.google.com/security-command-center/docs/reference/securityposture/rest/v1/PolicySet).

#### Create a posture file from a predefined posture template

You can use a predefined posture template to create a posture file.

###  Console 

  1. In the Google Cloud console, go to the **Posture Management** page.

[Go to Posture Management](https://console.cloud.google.com/projectselector2/security/command-center/posture?supportedpurview=organizationId)

  2. Select an organization.

  3. In the **Templates** tab, click the template that you want to use.

  4. In the **Template details** page, click **Create Posture**.

**Note:** If you don't see **Create Posture** , create the posture using Google Cloud CLI instead.
  5. Provide a unique name for the posture and click **Create**. The **Posture details** page opens.

  6. Complete one of the following actions:

     * If you can use the posture without making any changes (for example, you used one of the `_essentials` templates), you can deploy the posture. For instructions, see Deploy a posture.
     * If you need to modify any of the policy sets or policies (for example, you used one of the __enhanced_ templates), complete Modify a posture YAML file and set the posture state to `ACTIVE`.



###  gcloud 

  1. Review the [predefined posture templates](https://docs.cloud.google.com/security-command-center/docs/security-posture-overview#predefined-policy) to determine which ones apply to your environment. You can apply some of them without making any changes, but others require you to customize the policies to match your environment.
  2. Use one of the following methods to copy the YAML files into your own text editor:

     * Copy the YAML file from the reference content in [predefined posture templates](https://docs.cloud.google.com/security-command-center/docs/security-posture-overview#predefined-policy).
     * Run the `gcloud scc posture-templates describe` command to copy the YAML file.
    
    gcloud scc posture-templates describe \
        organizations/ORGANIZATION_ID/locations/global/postureTemplates/POSTURE_TEMPLATE \
        --revision-id=REVISION_ID
    

Replace the following values:

     * `ORGANIZATION_ID` is the organization where you activated Security Command Center.
     * `POSTURE_TEMPLATE` is the template name of the predefined posture template, as described in [Predefined posture templates](https://docs.cloud.google.com/security-command-center/docs/security-posture-overview#predefined-policy).
     * `REVISION_ID` is the revision version for the predefined posture template. If you don't include the revision ID, the latest version of the predefined posture template is displayed.

For example, to view the secure AI, essentials predefined posture template under the `3589215982` organization, run the following:
    
    gcloud scc posture-templates describe \
        organizations/3589215982/locations/global/postureTemplates/secure_ai_essential \
        --revision-id=v.1.0
    

  3. Complete one of the following actions:

     * If you can use the posture without making any changes (for example, you used one of the `_essentials` templates), you can create the posture. For instructions, see Create a posture.
     * If you need to modify any of the policy sets or policies, complete Modify a posture YAML file.



#### Create a posture file by extracting policies from an existing environment

You can extract the policies (organization policies, including custom policies and all Security Health Analytics detectors, including custom detectors) that you configured in an existing project, folder, or organization to create a posture file. You can't extract policies from an organization, folder, or project that already has a posture applied to it.

This command only extracts the policies that you previously configured for the organization, folder, or project and doesn't extract policies from parent folders or organization.

If you connected to AWS, this command also extracts the detectors that are specific to AWS ([Preview](https://cloud.google.com/products/#product-launch-stages)).

  1. Run the `gcloud scc postures extract` command to extract the existing organization policies and Security Health Analytics detectors in your environment.
         
         gcloud scc postures extract POSTURE_NAME \
             --workload=WORKLOAD
         

Replace the following values:

     * `POSTURE_NAME` is the relative resource name of the posture. For example, `organizations/ORGANIZATION_ID/locations/global/postures/POSTURE_ID`.

       * `POSTURE_ID` is an alphanumeric name for your posture that is unique to your organization. `POSTURE_ID` is limited to 63 characters.
     * `WORKLOAD` is the project, folder, or organization that you are extracting the policies from. The workload is one of the following:

     * `projects/PROJECT_NUMBER`

     * `folder/FOLDER_ID`

     * `organizations/ORGANIZATION_ID`

For example, to extract policies from the `3589215982` folder under the `6589215984` organization, run the following:
    
    gcloud scc postures extract \
      organizations/6589215984/locations/global/postures/myStagingPosture \
      workload=folder/3589215982 > posture.yaml
    

  2. Open the resulting `posture.yaml` file for editing.

  3. Complete one of the following actions:

     * If you can use the posture without making any changes (for example, you used one of the `_essentials` templates), you can create the posture. For instructions, see Create a posture.
     * If you need to modify any of the policy sets or policies, complete Modify a posture YAML file.



#### Create a Terraform resource with policy definitions

You can create a Terraform configuration to create a posture resource.

For example, you can create a posture resource that includes built-in and custom organization policy constraints and built-in and custom Security Health Analytics detectors. Posture management support for built-in Security Health Analytics detectors that are specific to AWS is in [Preview](https://cloud.google.com/products#product-launch-stages).
    
    
    resource "google_securityposture_posture" "posture1"{
      posture_id  = "posture_example"
      parent      = "organizations/123456789"
      location    = "global"
      state       = "ACTIVE"
      description = "a new posture"
      policy_sets {
        policy_set_id = "list_constraint_policy_set"
        description   = "set of org policies with a list constraint"
        policies {
          policy_id = "resource_locations_policy"
          constraint {
            org_policy_constraint {
              canned_constraint_id = "gcp.resourceLocations"
              policy_rules {
                values {
                  allowed_values = ["in:us-locations"]
                }
              }
            }
          }
        }
      }
      policy_sets {
        policy_set_id = "org_policy_set"
        description   = "set of org policies"
        policies {
          policy_id = "canned_org_policy"
          constraint {
            org_policy_constraint {
              canned_constraint_id = "storage.uniformBucketLevelAccess"
              policy_rules {
                enforce = true
                condition {
                	description = "condition description"
                	expression  = "resource.matchTag('org_id/tag_key_short_name,'tag_value_short_name')"
                	title       = "a CEL condition"
                }
              }
            }
          }
        }
        policies {
          policy_id = "custom_org_policy"
          constraint {
            org_policy_constraint_custom {
              custom_constraint {
                name           = "organizations/123456789/customConstraints/custom.disableGkeAutoUpgrade"
                display_name   = "Disable GKE auto upgrade"
                description    = "Only allow GKE NodePool resource to be created or updated if AutoUpgrade is not enabled where this custom constraint is enforced."
                action_type    = "ALLOW"
                condition      = "resource.management.autoUpgrade == false"
                method_types   = ["CREATE", "UPDATE"]
                resource_types = ["container.googleapis.com/NodePool"]
              }
              policy_rules {
                enforce = true
                condition {
                	description = "condition description"
                	expression = "resource.matchTagId('tagKeys/key_id','tagValues/value_id')"
                	title = "a CEL condition"
                }
              }
            }
          }
        }
      }
      policy_sets {
        policy_set_id = "sha_policy_set"
        description   = "set of sha policies"
        policies {
          policy_id = "sha_builtin_module"
          constraint {
            security_health_analytics_module {
              module_name             = "BIGQUERY_TABLE_CMEK_DISABLED"
              module_enablement_state = "ENABLED"
            }
          }
          description = "enable BIGQUERY_TABLE_CMEK_DISABLED"
        }
        policies {
          policy_id = "sha_custom_module"
          constraint {
            security_health_analytics_custom_module {
              display_name = "custom_SHA_policy"
              config {
                predicate {
                  expression = "resource.rotationPeriod > duration('2592000s')"
                }
                custom_output {
                  properties {
                    name = "duration"
                    value_expression {
                      expression = "resource.rotationPeriod"
                    }
                  }
                }
                resource_selector {
                  resource_types = ["cloudkms.googleapis.com/CryptoKey"]
                }
                severity       = "LOW"
                description    = "Custom Module"
                recommendation = "Testing custom modules"
              }
              module_enablement_state = "ENABLED"
            }
          }
        }
      }
    
    }
    

For more information, see [google_securityposture_posture](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/securityposture_posture).

### Modify a posture YAML file

Complete the following steps to modify a posture YAML file:

  1. Open your posture YAML file in a text editor.
  2. Verify the `name`, `description`, and `state` at the beginning of the file.
         
         name: organizations/ORGANIZATION_ID/locations/global/posture/POSTURE_ID
         description: DESCRIPTION
         state: STATE
         

For details about these fields, see the [`Posture` reference](https://docs.cloud.google.com/security-command-center/docs/reference/securityposture/rest/v1/Posture).

For example:
         
         name: organizations/3589215982/locations/global/posture/stagingAIPosture
         description: This posture applies to staging environments for Vertex AI.
         state: ACTIVE
         

  3. Customize the policies within the file to meet your requirements.

For details about the fields that you can use, see the [`PolicySet` reference](https://docs.cloud.google.com/security-command-center/docs/reference/securityposture/rest/v1/PolicySet).

     1. Review the existing policies and their values. For policies that require information that is specific to your environment, set the values appropriately. For example, for the `ainotebooks.accessMode` policy in the secure AI, extended predefined posture, add the allowed modes of access under `policyRules`:
            
            - policyId: Define access mode for Vertex AI Workbench notebooks and instances
              complianceStandards:
              - standard: NIST SP 800-53
                control: AC-3(3)
              - standard: NIST SP 800-53
                control: AC-6(1)
              constraint:
                orgPolicyConstraint:
                  cannedConstraintId: ainotebooks.accessMode
                  policyRules:
                  - values:
                      allowedValues: service-account
              description: This list constraint defines the modes of access allowed to Vertex AI Workbench notebooks and instances where enforced. The allow or deny list can specify multiple users with the service-account mode or single-user access with the single-user mode. The access mode to be allowed or denied must be listed explicitly.
            

     2. Add additional organization policy constraints, as documented in [Organization policy constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints). If you are defining a custom organization policy, ensure that the YAML file includes the custom constraint definition. You can't use a custom constraint that you created using other methods (for example, using the Google Cloud console).

For example, you might want to set the `compute.trustedImageProjects` constraint to define projects that can be used for image storage and disk instantiation. If you copy this example, ensure that you replace `allowedValues` with a suitable list of projects:
            
            - policyId: Define projects with trusted images.
              complianceStandards:
              - standard:
                control:
              constraint:
                orgPolicyConstraint:
                  cannedConstraintId: compute.trustedImageProjects
                  policyRules:
                  - values:
                      allowedValues:
                      - project1
                      - project2
                      - projectN
              description: This is a complete list of projects from which images can be used.
            

     3. Add additional Security Health Analytics detectors, such as those documented in [Security Health Analytics findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#security-health-analytics-detectors). For example, add a Security Health Analytics detector to create a finding if a project is not using an API key for authentication:
            
            - policyId: API Key Exists
              constraint:
                securityHealthAnalyticsModule:
                  moduleEnablementState: ENABLED
                  moduleName: API_KEY_EXISTS
            

As another example, add a Security Health Analytics custom module to detect whether Gemini Enterprise Agent Platform datasets are encrypted:
            
            - policyId: CMEK key is used for Vertex AI DataSet
              complianceStandards:
              - standard: NIST SP 800-53
                control: SC-12
              - standard: NIST SP 800-53
                control: SC-13
              constraint:
                securityHealthAnalyticsCustomModule:
                  displayName: "vertexAIDatasetCMEKDisabled"
                  config:
                    customOutput: {}
                    predicate:
                      expression: "!has(resource.encryptionSpec)"
                    resourceSelector:
                      resourceTypes:
                      - aiplatform.googleapis.com/Dataset
                    severity: CRITICAL
                    description: "When enforced, this detector finds whether a dataset is not encrypted using CMEK."
                    recommendation: "Restore the SHA module. See https://cloud.google.com/security-command-center/docs/custom-modules-sha-overview."
                  moduleEnablementState: ENABLED
            

As another example, for the Enterprise (Deprecated) service tier, add a Security Health Analytics detector that's specific to AWS ([Preview](https://cloud.google.com/products/#product-launch-stages)):
            
            - policySetId: AWS policy set
              description:  Policy set containing AWS built-in SHA modules for securing S3 buckets.
              policies:
              - policyId: S3 bucket replication enabled
                complianceStandards:
                - standard: NIST 800-53 R5
                  control: SI-13(5)
                constraint:
                  securityHealthAnalyticsModule:
                    moduleEnablementState: ENABLED
                    moduleName: S3_BUCKET_REPLICATION_ENABLED
                description: This control checks whether an Amazon S3 bucket has Cross-Region Replication enabled. The control fails if the bucket does not have Cross-Region Replication enabled or if Same-Region Replication is also enabled.
            
              - policyId: S3 bucket logging enabled
                complianceStandards:
                - standard: NIST 800-53 R5
                  control: SI-7(8)
                - standard: PCI DSS 3.2.1
                  control: 10.3.1
                constraint:
                  securityHealthAnalyticsModule:
                    moduleEnablementState: ENABLED
                    moduleName: S3_BUCKET_LOGGING_ENABLED
                description: The AWS S3 Server Access Logging feature records access requests to storage buckets which is useful for security audits. By default, server access logging is not enabled for S3 buckets.
            

If you add a detector that's specific to AWS, you must deploy the posture at the organization level.

  4. Upload your posture file to a version-controlled source repository so that you can track the changes that you make to it over time.




### Create a posture

Complete this task to create a posture resource in Security Command Center that you can deploy. If you created a posture from a predefined posture template using the Google Cloud console, the posture resource is created automatically for you.

###  Console 

  1. In the Google Cloud console, go to the **Posture Management** page.

[Go to Posture Management](https://console.cloud.google.com/projectselector2/security/command-center/posture?supportedpurview=organizationId)

  2. Select an organization.

  3. Click **Create Posture**. You can create a posture by starting with an existing posture or template, or by using the policies applied to a resource. 

#### Create a posture using an existing posture or template

     1. Select **Start with an existing posture or template (browse postures)**.
     2. Specify posture details such as posture name and description.
     3. Click **Select Posture**. You can create a posture based on an existing posture or a template. 
        * Select **Posture** to create a posture using an existing posture. Select a posture from the list of postures displayed and then select one or more revisions from the list of available revisions for the selected posture. 
        * Select **Template** to create a posture using a template and then select one or more templates from the list of templates displayed. 
     4. Click **Save**. Under the **Policy Sets** section, you can view the list of policy sets associated with the selected posture. 
     5. Select the policies from the list of policy sets. You can also edit the policy and move the policy to a different policy set on this page. You cannot create a posture with two policies with the same name within the same policy set. 
     6. Click **Create**.

#### Create a posture using the policies applied on a resource

     1. Select **Start with a posture applied to a resource (browse resources)**.
     2. Specify posture details such as posture name and description.
     3. Click **Select resources**.
     4. Select a resource from the list of resources displayed and click **Create**.

You are redirected to the **Posture details** page showing information about the posture that you have created. You can see the policy sets associated with that posture.




###  gcloud 

  1. Run the `gcloud scc postures create` command to create a posture using the `posture.yaml` file.
         
         gcloud scc postures create POSTURE_NAME \
             --posture-from-file=POSTURE_FROM_FILE
         

Replace the following values:

     * `POSTURE_NAME` is the relative resource name of the posture. For example, `organizations/ORGANIZATION_ID/locations/global/postures/POSTURE_ID`.

       * `POSTURE_ID` is an alphanumeric name for your posture that is unique to your organization. `POSTURE_ID` is limited to 63 characters.

For example, to create a posture with the ID `posture-example-1` under the organization `organizations/3589215982`, run the following:
    
    gcloud scc postures create \
        organizations/3589215982/locations/global/postures/posture-example-1 \
        --posture-from-file=posture.yaml
    

If the posture creation process fails, delete the posture, troubleshoot the error, and try again.

  2. To verify that the posture created successfully, see View a posture.




To apply this posture to your environment, you must deploy the posture.

###  Terraform 

If you created a Terraform configuration for the posture resource, you must provision it using your infrastructure-as-code pipeline.

For more information, see [Terraform on Google Cloud](https://docs.cloud.google.com/docs/terraform).

### Deploy a posture

After you create a posture, you deploy it to a project, folder, or organization so that you can apply the policies and their definitions to specific resources in your organization and monitor for drift. You can only deploy one posture to a project, folder, or organization.

Verify that your posture state is `ACTIVE`.

When you deploy the posture, the following actions occur:

  * The definitions for organization policies and Security Health Analytics detectors are applied.
  * For each custom organization policy defined in the posture, a new custom constraint is created. This is true even if you created the posture from a template or from extracted policies and you kept those policies unchanged. The constraint ID includes the posture revision ID as a suffix. If all deployments of the posture are deleted, the suffix is replaced with a random UUID.
  * For each custom Security Health Analytics detector defined in the posture, a new custom constraint is created. This is true even if you created the posture from a template or from extracted policies and you kept those policies unchanged.
  * The default state for the custom modules is set to **Enabled**.




###  Console 

  1. In the Google Cloud console, go to the **Posture Management** page.

[Go to Posture Management](https://console.cloud.google.com/projectselector2/security/command-center/posture?supportedpurview=organizationId)

  2. Select an organization.

  3. On the **Postures** tab, click the posture that you want to deploy.

  4. On the **Posture details** page, select the revision of the posture. The posture revision you select must be in the active state.

  5. Click **Apply to resources**.

  6. Click **Select** to select the organization, folder, or project that you want to deploy the posture to.

  7. Click **Apply posture**.




###  gcloud 

Run the `gcloud scc posture-deployments create` command to deploy a posture to a project, folder, or organization.
    
    
    gcloud scc posture-deployments create POSTURE_DEPLOYMENT_NAME \
        --posture-name=POSTURE_NAME \
        --posture-revision-id=POSTURE_REVISION_ID \
        --target-resource=TARGET_RESOURCE
    

Replace the following values:

  * `POSTURE_DEPLOYMENT_NAME` is the relative resource name for the posture deployment. The format is `organizations/ORGANIZATION_ID/locations/global/postureDeployments/POSTURE_DEPLOYMENT_ID`.

  * `LOCATION` is `global`.

  * `POSTURE_ID` is an alphanumeric name for your posture that is unique to your organization.

  * `--posture-name=POSTURE_NAME` is the name for the posture that you're deploying. The format is `organizations/ORGANIZATION_ID/locations/global/postures/POSTURE_ID`.




If your posture includes a detector that's specific to AWS, you must deploy the posture at the organization level ([Preview](https://cloud.google.com/products/#product-launch-stages)).

For example, to deploy a posture, run the following command:
    
    
    gcloud scc posture-deployments create \
      organizations/3589215982/locations/global/postureDeployments/postureDeployment123 \
      --posture-name=organizations/3589215982/locations/global/postures/StagingAIPosture \
      --posture-revision-id=version1 \
      --target-resource=projects/4589215982
    

You can view status information as the command completes. If the posture deployment creation process fails, delete the deployment, troubleshoot the error, and try again.

###  Terraform 

You can create a Terraform resource to deploy a posture.
    
    
    resource "google_securityposture_posture_deployment" "posture_deployment_example" {
      posture_deployment_id          = "<POSTURE_DEPLOYMENT_ID>"
      parent = "organizations/<ORGANIZATION_ID>"
      location = "global"
      description = "a new posture deployment"
      target_resource = "<TARGET_RESOURCE>"
      posture_id = "<POSTURE_NAME>"
      posture_revision_id = "<POSTURE_REVISION_ID>"
    }
    

For more information, see [google_securityposture_posture_deployment](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/securityposture_posture_deployment).

## View posture and posture deployment information

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) (requires [organization-level activation](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation))

You can view posture and posture deployment information to see information such as the following:

  * What postures are deployed and where in the resource hierarchy (organizations, projects, and folders) they are applied
  * The revisions and state of postures
  * The operational details of a posture deployment



### View a posture

You can view information about a posture (such as its state and policy definitions).

###  Console 

  1. In the Google Cloud console, go to the **Posture Management** page.

[Go to Posture Management](https://console.cloud.google.com/projectselector2/security/command-center/posture?supportedpurview=organizationId)

  2. Select an organization.

  3. On the **Postures** tab, click the posture that you want to view. The posture details appear.




###  gcloud 

Run the `gcloud scc postures describe` command to see a posture that you created.
    
    
    gcloud scc postures describe POSTURE_NAME \
        --revision-id=REVISION_ID
    

Replace the following values:

  * `POSTURE_NAME` is the relative resource name of the posture. For example, `organizations/ORGANIZATION_ID/locations/global/postures/POSTURE_ID`.

  * `POSTURE_ID` is an alphanumeric name for your posture that is unique to your organization.

  * `revision-id=REVISION_ID` is an optional flag that specifies which version of the posture to view. If you don't include the flag, the latest version is returned.




For example, to view a posture with the name `organizations/3589215982/locations/global/postures/posture-example-1` and the revision ID `abcdefgh`, run the following:
    
    
    gcloud scc postures describe \
        organizations/3589215982/locations/global/postures/posture-example-1 \
        --revision-id=abcdefgh
    

### View information about a posture deployment operation

Run the `gcloud scc posture-operations describe` command to view the operation details for a posture deployment operation.
    
    
    gcloud scc posture-operations describe OPERATION_NAME
    

Where `OPERATION_NAME` is the relative resource name for the operation. The format is `organizations/ORGANIZATION_ID/locations/global/operations/OPERATION_ID`. You can obtain the `OPERATION_ID` by using the `--async` argument when you run the posture command.

For example, to view a scan operation with the name `organizations/3589215982/locations/global/operations/operation-1694515698847-605272e4bcd7c-f93dade6-067467ae`, run the following:
    
    
    gcloud scc posture-operations describe \
        organizations/3589215982/locations/global/operations/operation-1694515698847-605272e4bcd7c-f93dade6-067467ae
    

### View information about a posture deployment

You can view where a posture is deployed to, as well as the deployment state.

###  Console 

  1. In the Google Cloud console, go to the **Posture Management** page.

[Go to Posture Management](https://console.cloud.google.com/projectselector2/security/command-center/posture?supportedpurview=organizationId)

  2. Select an organization.

  3. On the **Postures** tab, click the posture that you deployed.

  4. Go to the **Resources** tab to view the projects, folders, and organization that the posture is deployed to, as well as the deployment state.




###  gcloud 

Run the `gcloud scc posture-deployments describe` command to view information about a deployed posture.
    
    
    gcloud scc posture-deployments describe POSTURE_DEPLOYMENT_NAME

Where `POSTURE_DEPLOYMENT_NAME` is the relative resource name for the posture deployment. The format is `organizations/ORGANIZATION_ID/locations/global/postureDeployments/POSTURE_DEPLOYMENT_ID`.

  * `LOCATION` is `global`.
  * `POSTURE_DEPLOYMENT_ID` is a unique name for the posture deployment.



For example, to view the details for a posture deployment that is named `organizations/3589215982/locations/global/postureDeployments/Posture-deployment-example-1`, run the following:
    
    
    gcloud scc posture-deployments describe \
        organizations/3589215982/locations/global/postureDeployments/Posture-deployment-example-1
    

## Update a posture and posture deployment

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) (requires [organization-level activation](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation))

You can update the following:

  * The state of the posture.
  * The policy definitions in a posture.
  * The organization, folders, or projects that a posture is deployed to.



### Update the policy definitions in a posture

You might need to update a posture when you enable more Google Cloud services, deploy additional resources, or require additional policies to meet new or changing compliance requirements. If you are updating a deployed posture revision, this task creates a new posture revision. Otherwise, the posture revision that you specify when you run the update command is updated.

  1. Open a YAML file in a text editor. Add the fields you want to update, along with their values. If you are updating policy sets, ensure that your file includes all the policy sets that you want to include in the posture, including the policy sets that already exist. For instructions, see Modify a posture YAML file.
  2. Run the `gcloud scc postures update` command to update the posture.
         
         gcloud scc postures update POSTURE_NAME \
             --posture-from-file=POSTURE_FROM_FILE \
             --revision-id=POSTURE_REVISION_ID \
             --update-mask=UPDATE_MASK
         

Replace the following values:

     * `POSTURE_NAME` is the relative resource name of the posture. For example, `organizations/ORGANIZATION_ID/locations/global/postures/POSTURE_ID`.

       * `POSTURE_ID` is an alphanumeric name for your posture that is unique to your organization.
     * `POSTURE_FROM_FILE` is the relative or absolute path to the `posture.yaml` file that includes your changes.

       * `POSTURE_ID` is an alphanumeric name for your posture that is unique to your organization.
     * `POSTURE_FROM_FILE` is the relative or absolute path to the `posture.yaml` file that includes your changes.

     * `--revision-id=REVISION_ID` is the posture revision that you want to deploy. If the posture is already deployed, the security posture service automatically creates a new version of the posture with a different revision ID and includes the revision ID in the output.

     * `--update-mask=UPDATE_MASK` is the list of fields that you want to update, in comma-separated format. This argument is optional. You can set `UPDATE_MASK` to one of the following values:

       * `*` or unspecified: Apply the changes that you made to the policy sets and posture description.
       * `policy_sets`: Apply the changes that you made to the policy sets only.
       * `description`: Apply the changes that you made to the posture description only.
       * `policy_sets, description`: Apply the changes that you made to the policy sets and posture description.
       * `state`: Apply the state change only.

For example, to update a posture with the name `posture-example-1` under the organization `organizations/3589215982/locations/global` and the revision ID set to `abcd1234`, run the following:
    
    gcloud scc postures update \
        organizations/3589215982/locations/global/posture-example-1 \
        --posture-from-file=posture.yaml --revision-id=abcd1234 --update-mask=policy_sets
    

If the posture update process fails, troubleshoot the error, and try again.

  3. To verify that the posture updated successfully, see View a posture.




### Change the state of a posture

The state of a posture determines whether it is available for deployment to a project, folder, or organization.

A posture can have the following states:

  * `DRAFT`: The posture revision is not ready for deployment. You cannot deploy a posture revision that is in the `DRAFT` state.
  * `ACTIVE`: The posture revision is available for deployment. You can change the state from `ACTIVE` to `DRAFT` or `DEPRECATED`.
  * `DEPRECATED`: A `DEPRECATED` posture revision cannot be deployed to a resource. You must delete all existing posture deployments of the posture before you can deprecate a posture revision. If you want to redeploy a posture revision that you deprecated, you must change its state to `ACTIVE`.




###  Console 

  1. In the Google Cloud console, go to the **Posture Management** page.

[Go to Posture Management](https://console.cloud.google.com/projectselector2/security/command-center/posture?supportedpurview=organizationId)

  2. Select an organization.

  3. On the **Postures** tab, click the posture you want to update.

  4. On the **Posture details** page, click **Edit**.

  5. Select the posture status and click **Save**.




###  gcloud 

To change the state of a posture, run the `gcloud scc postures update` command. You can't update the posture state at the same time that you update other fields. For instructions about running the `gcloud scc postures update` command, see Modify a posture YAML file.

### Update a posture deployment

Update a posture deployment on a project, folder, or organization to deploy a new posture or deploy a new revision of a posture.

If the posture revision that you're updating includes a custom organization constraint that was deleted using the Google Cloud console, you can't update the posture deployment using the same posture ID. The Organization Policy Service prevents the creation of custom organization constraints that have the same name. Instead, you must create a new version of the posture or use a different posture ID.

Also, findings for the policy deployments deleted as part of the update process will be deactivated.

###  Console 

  1. In the Google Cloud console, go to the **Posture Management** page.

[Go to Posture Management](https://console.cloud.google.com/projectselector2/security/command-center/posture?supportedpurview=organizationId)

  2. Select an organization.

  3. On the **Postures** tab, click the posture that you want to update.

  4. On the **Posture details** page, select the revision of the posture.

  5. Click **Apply to resources**.

  6. Click **Select** to select the organization, folder, or project that you want to deploy the posture to. If you see a message that the deployment already exists, delete the deployment before trying again.




###  gcloud 

Run the `gcloud scc posture-deployments update` command to deploy a posture.
    
    
    gcloud scc posture-deployments update POSTURE_DEPLOYMENT_NAME \
        --description=DESCRIPTION \
        --update-mask=UPDATE_MASK \
        --posture-id=POSTURE_ID \
        --posture-revision-id=POSTURE_REVISION_ID
    

Replace the following values:

  * `POSTURE_DEPLOYMENT_NAME` is the relative resource name for the posture deployment. The format is `organizations/ORGANIZATION_ID/locations/global/postureDeployments/POSTURE_DEPLOYMENT_ID`.

    * `POSTURE_DEPLOYMENT_ID` is a unique name for the posture deployment.
  * `--description=DESCRIPTION` is the optional description for the deployed posture.

  * `--posture-id=POSTURE_ID` is the name for your posture that is unique to your organization. The format is `organizations/ORGANIZATION_ID/locations/global/postures/POSTURE_NAME`

  * `--posture-revision-id=POSTURE_REVISION_ID` is the posture revision that you want to deploy. You can obtain it from the response that you receive when you create the posture or view the posture.

  * `--update-mask=UPDATE_MASK` is the list of fields that you want to update, in comma-separated format. This argument is optional.




For example, to update a posture deployment with the following criteria:

  * Organization: `organizations/3589215982/locations/global`
  * Posture deployment ID: `postureDeploymentexample`
  * Posture ID: `StagingAIPosture`
  * Revision: `version2`



Run the following command:
    
    
    gcloud scc posture-deployments update \
        organizations/3589215982/locations/global/postureDeployments/postureDeploymentexample \
        --posture-id=organizations/3589215982/locations/global/postures/StagingAIPosture \
        --posture-revision-id=version2
    

You can view status information as the command completes. If the posture deployment update process fails, delete the deployment, troubleshoot the error, and try again.

## Monitor posture drift

You can monitor a deployed posture for drift from your defined policies within security posture. Drift is a change to a policy that occurs outside of a posture. For example, drift occurs when an administrator changes a policy definition in the console instead of updating the posture deployment.

The security posture service creates findings that you can view in the Google Cloud console or gcloud CLI whenever drift occurs.

###  Console 

For all postures, you can monitor drift using the **Findings** page.

  1. In the Google Cloud console, go to the **Findings** page.

[Go to Posture Management](https://console.cloud.google.com/projectselector2/security/command-center/posture?supportedpurview=organizationId)

  2. Select an organization.

  3. Use the following filter options to investigate posture findings:

     * In the **Quick filters** pane, select the **Posture violation** finding. You can also enter the following filter in **Query preview** :
           
           state="ACTIVE" AND NOT mute="MUTED" AND finding_class="POSTURE_VIOLATION"
           

     * To view findings related to any Security Health Analytics custom modules that apply specifically to Gemini Enterprise Agent Platform workloads, run the following filter query:
           
           state="ACTIVE" AND NOT mute="MUTED" AND resource.type:"aiplatform"
           

     * To view findings related to drift from Gemini Enterprise Agent Platform organization policies that you applied in a posture, run the following filter query:
           
           state="ACTIVE" AND NOT mute="MUTED" AND
             (category="SECURITY_POSTURE_POLICY_DRIFT" OR
             category="SECURITY_POSTURE_POLICY_DELETE" OR
             category="SECURITY_POSTURE_DETECTOR_DRIFT" OR
             category="SECURITY_POSTURE_DETECTOR_DELETE")
             AND contains(risks, risk_category = "AI_WORKLOAD_AT_RISK")
           

  4. To view the details for a finding, click the finding.




###  gcloud 

In the gcloud CLI, to view drift findings, run the following:
    
    
    gcloud scc findings list ORGANIZATION_ID \
        --filter="category=\"SECURITY_POSTURE_DRIFT\""
    

Where `ORGANIZATION_ID` is the ID of the organization.

You can export these findings in the same way that you export any other findings from Security Command Center. For more information, see [Exporting Security Command Center data](https://docs.cloud.google.com/security-command-center/docs/how-to-export-data).

### Remediate posture findings

For information about addressing each finding, see [Security posture service findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#secposture-findings). You can also update the posture deployment with the same posture ID and posture revision.

### Generate a drift finding for testing purposes

After you deploy a posture, you can monitor for drift from your policies. To see drift findings in action in a testing environment, complete the following:

  1. In the console, go to the **Organization policy** page.

[Go to Organization policy](https://console.cloud.google.com/projectselector2/iam-admin/orgpolicies?supportedpurview=organizationId)

  2. Select an organization.

  3. Edit one of the policies that you defined in the deployed posture. For example, if you use a predefined secure AI posture, you could edit the **Restrict public IP access on new Vertex AI Workbench notebooks and instances** policy.

  4. After you change the policy, click **Set Policy**.

  5. Go to the **Findings** page.

[Go to Findings](https://console.cloud.google.com/projectselector2/security/command-center/findings?supportedpurview=organizationId)

  6. Select an organization.

  7. In the **Quick filters** pane, in the **Source display name** section, select **Security Posture**. A finding related to your change should appear within five minutes.

  8. To view the details for the finding, click the finding.




## Delete a posture deployment

You can delete a posture deployment if it didn't deploy properly, you no longer require a particular posture, or you no longer want a particular posture assigned to a project, folder, or organization. To delete a posture deployment, the posture deployment must be in one of the following states:

  * `ACTIVE`
  * `CREATE_FAILED`
  * `UPDATE_FAILED`
  * `DELETE_FAILED`



To verify the state of a posture deployment, see View information about a posture deployment.

When you delete a posture deployment, you remove the posture from the resource (your organization, folder, or project) that you assigned it to. Also, it deactivates the associated findings.

The output for different types of policies is as follows:

  * When you delete a posture deployment that includes custom organization policies, the custom organization policies are deleted. However, the custom constraint continues to exist.
  * When you delete a posture deployment that includes built-in Security Health Analytics detectors, the final state of the Security Health Analytics modules is dependent on the organization, folder, or project on which the deployment existed.

    * If you deployed a posture on a folder or project, built-in Security Health Analytics detectors inherit their state from the parent organization or folder.
    * If you deployed a posture at the organization level, built-in Security Health Analytics detectors revert to the default state. For a description of the default states, see [Enable and disable detectors](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-health-analytics#enable_and_disable_detectors).



###  Console 

  1. In the Google Cloud console, go to the **Posture Management** page.

[Go to Posture Management](https://console.cloud.google.com/projectselector2/security/command-center/posture?supportedpurview=organizationId)

  2. Select an organization.

  3. On the **Postures** tab, click the posture that you want to remove from the resource it is assigned to.

  4. On the **Posture details** page, select the revision of the posture and go to **Resources**.

  5. From the list of resources where the current active posture revision is deployed, click **Remove**.




###  gcloud 

Run the `gcloud scc posture-deployments delete` command to delete a posture deployment.
    
    
    gcloud scc posture-deployments delete POSTURE_DEPLOYMENT_NAME

`POSTURE_DEPLOYMENT_NAME` is the relative resource name for the posture deployment. The format is `organizations/ORGANIZATION_ID/locations/global/postureDeployments/POSTURE_DEPLOYMENT_ID`.

  * `POSTURE_DEPLOYMENT_ID` is the unique name for the posture deployment.



For example, to delete a posture deployment that is named `organizations/3589215982/locations/global/postureDeployments/posture-deployment-example-1`, run the following:
    
    
    gcloud scc posture-deployments delete \
        organizations/3589215982/locations/global/postureDeployments/posture-deployment-example-1
    

## Delete a posture

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) (requires [organization-level activation](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation))

When you delete a posture, you also delete all revisions. You can't delete a posture if any of its revisions are deployed. You must delete all posture deployments before you can complete this task.

###  Console 

  1. In the Google Cloud console, go to the **Posture Management** page.

[Go to Posture Management](https://console.cloud.google.com/projectselector2/security/command-center/posture?supportedpurview=organizationId)

  2. Select an organization.

  3. On the **Postures** tab, click the posture that you want to delete.

  4. On the **Posture details** page, click **Delete**.




###  gcloud 

Run the `gcloud scc postures delete` command to delete a posture.
    
    
     gcloud scc postures delete POSTURE_NAME
    

`POSTURE_NAME` is the relative resource name of the posture.

For example, `organizations/ORGANIZATION_ID/locations/global/postures/POSTURE_ID`. The posture ID is an alphanumeric name for your posture that is unique to your organization.

For example, to delete a posture that is named `organizations/3589215982/locations/global/postures/posture-example-1`, run the following:
    
    
     gcloud scc postures delete \
         organizations/3589215982/locations/global/postures/posture-example-1
    

## What's next

  * [Read the overview of security postures](https://docs.cloud.google.com/security-command-center/docs/security-posture-overview).
  * [Learn about custom modules for Security Health Analytics](https://docs.cloud.google.com/security-command-center/docs/custom-modules-sha-code).
  * [Learn about custom organization policy constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-custom-constraints#set_up_custom_constraint).
  * [Check the audit logs for posture-related operations](https://docs.cloud.google.com/security-command-center/docs/audit-logging-security-posture).
  * [Export security posture service data](https://docs.cloud.google.com/security-command-center/docs/how-to-export-data).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
