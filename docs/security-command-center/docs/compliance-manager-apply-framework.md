---
url: https://docs.cloud.google.com/security-command-center/docs/compliance-manager-apply-framework/
title: Manage frameworks \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:13:52.477410+00:00
---

# Manage frameworks  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/compliance-manager-apply-framework/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Manage frameworks Stay organized with collections  Save and categorize content based on your preferences. 

Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

Compliance Manager frameworks consist of [cloud controls](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-overview#security-compliance-service-components) that help you meet the security and regulatory requirements for an organization or project in your cloud environments. Applying a framework is a two-step process. First, you must identify the cloud controls that align with your business's security and compliance obligations. Then, you deploy a framework that includes those cloud controls to the appropriate organization, folder, or project in Google Cloud. This page helps you complete the following steps:

  1. Assess which built-in framework best aligns with your regulatory and security requirements. You can create your own custom framework, but we recommend starting with a built-in framework.

  2. Determine which built-in cloud controls map to your business requirements. (Premium and Enterprise tiers only) You can [create custom cloud controls](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-manage-cloud-controls#create-custom-cloud-control), if required.

  3. Determine whether to deploy the framework to your Google Cloud organization, or to specific folders and projects. You can only deploy one framework to each organization, folder, or project. Compliance Manager supports [folders configured for application management](https://docs.cloud.google.com/resource-manager/docs/manage-applications).

  4. Copy an existing framework and modify it to match your requirements. If required, you can create a custom framework.

**Note:** The Standard tier supports only the Security Essentials framework. Other built-in frameworks require [Premium or Enterprise](https://docs.cloud.google.com/security-command-center/docs/service-tiers) tiers. For more information, see [Frameworks for Google Cloud](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-overview#frameworks-gcp).
  5. Deploy the framework on the appropriate organization, folder, or project.




## Before you begin

Complete these tasks before you complete the remaining tasks on this page.

### Set up permissions

  * To get the permissions that you need to apply frameworks, ask your administrator to grant you the following IAM roles on your organization or project: 

    * [Compliance Manager Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsecuritycompliance#cloudsecuritycompliance.admin) (`roles/cloudsecuritycompliance.admin`)
    * To view findings dashboards: [Compliance Manager Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsecuritycompliance#cloudsecuritycompliance.viewer) (`roles/cloudsecuritycompliance.viewer`) 
    * To deploy frameworks that include cloud controls that are based on organization policies, one of: 
      * [Organization Policy Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/orgpolicy#orgpolicy.policyAdmin) (`roles/orgpolicy.policyAdmin`)
      * [Assured Workloads Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredworkloads#assuredworkloads.admin) (`roles/assuredworkloads.admin`)
      * [Assured Workloads Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredworkloads#assuredworkloads.editor) (`roles/assuredworkloads.editor`)
    * (Organization-level only) To create a folder while deploying a framework, one of: 
      * [Folder Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.folderAdmin) (`roles/resourcemanager.folderAdmin`)
      * [Folder Creator ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.folderCreator) (`roles/resourcemanager.folderCreator`)
    * (Organization-level only) To create a project while deploying a framework, all of: 
      * [Project Billing Manager ](https://docs.cloud.google.com/iam/docs/roles-permissions/billing#billing.projectManager) (`roles/billing.projectManager`)
      * [Project Creator ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectCreator) (`roles/resourcemanager.projectCreator`)
      * [Project Deleter ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectDeleter) (`roles/resourcemanager.projectDeleter`)
    * To assign Data Security Posture Management (DSPM) frameworks to an [App Hub application](https://docs.cloud.google.com/app-hub/docs/overview), all of: [App Hub Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/apphub#apphub.viewer) (`roles/apphub.viewer`) 

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

The roles for deploying frameworks with organization policies contain the required `orgpolicy.policies.create`, `orgpolicy.policies.update`, and `orgpolicy.policies.get` permissions. 

For organization-level deployments, the roles for creating folders contain the required `resourcemanager.folders.get`, `resourcemanager.folders.create`, and `resourcemanager.folders.delete` permissions.

For organization-level deployments, the roles for creating projects contain the required `resourcemanager.projects.get`, `resourcemanager.projects.create`, `resourcemanager.projects.delete`, and `resourcemanager.projects.createBillingAssignment` permissions.

The roles for assigning DSPM frameworks to applications contain the required `apphub.locations.list`, `apphub.applications.list` and `apphub.applications.get` permissions. 

You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 




### Set up Google Cloud CLI

In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

To set up the gcloud CLI to use service account impersonation to authenticate to Google APIs, rather than your user credentials, run the following command: 
    
    
    gcloud config set auth/impersonate_service_account SERVICE_ACCT_EMAIL

For more information, see [Service account impersonation](https://docs.cloud.google.com/security-command-center/docs/reference/authentication#sa-impersonation). 

## View frameworks

Complete the following steps to view the configuration for built-in frameworks or other frameworks that you've already created.

###  Console 

  1. In the Google Cloud console, go to the **Compliance** page.

[Go to Compliance](https://console.cloud.google.com/security/command-center/compliance)

  2. Select your organization or project.

  3. To view all available frameworks, click the **Configure** tab.

The dashboard shows the available frameworks, a brief description, supported platforms and tiers, and the resources that the framework has been applied to.

**Note:** If you are in the Standard tier, you can view the Premium and Enterprise frameworks in your dashboard, but you can't deploy them.
  4. To view details about a specific framework, click the framework name.




###  CLI 

You can see information about a specific framework or list all the frameworks in your organization.

### See details about a framework

To see details about a specific framework, run the `gcloud compliance-manager frameworks describe` command:
    
    
    gcloud compliance-manager frameworks describe FRAMEWORK \
       --location=LOCATION \
       --organization=ORGANIZATION \
       [--major-revision-id=MAJOR_REVISION_ID]
    

Replace the following:

  * `FRAMEWORK`: the name of the framework

  * `ORGANIZATION`: your organization ID

  * `LOCATION`: the region that the framework is stored in

  * `MAJOR_REVISION_ID`: an optional flag that specifies which version of the framework to view. If you don't include the flag, the latest version is returned.




For example, to view a framework with the name `builtin-security-essentials` and the major revision number `12`, run the following:
    
    
    gcloud compliance-manager frameworks describe \
       builtin-security-essentials \
       --organization=3589215982 \
       --location=global \
       --major-revision-id=12
    

For more information, see [gcloud compliance-manager frameworks describe](https://docs.cloud.google.com/sdk/gcloud/reference/compliance-manager/frameworks/describe).

### Get list of frameworks

To get the list of frameworks in your organization, run the `gcloud compliance-manager frameworks list` command:
    
    
    gcloud compliance-manager frameworks list \
       --location=LOCATION \
       --organization=ORGANIZATION
    

Replace the following values:

  * `ORGANIZATION`: your organization ID

  * `LOCATION`: the region that the frameworks are stored in




For example, to view all frameworks within organization `3589215982` that are stored in the global location, run the following:
    
    
    gcloud compliance-manager frameworks list \
       --organization=3589215982 \
       --location=global
    

For information about optional flags, see [gcloud compliance-manager frameworks list](https://docs.cloud.google.com/sdk/gcloud/reference/compliance-manager/frameworks/list).

## Create a framework

After you determine which cloud controls apply to resources within your organization or a specific folder or project, you can create a framework. You can create a custom framework or copy an existing framework and modify it. When you copy a framework, it includes the latest releases of any built-in cloud controls.

###  Console 

  1. In the Google Cloud console, go to the **Compliance** page.

[Go to Compliance](https://console.cloud.google.com/security/command-center/compliance)

  2. Select your organization or project.

  3. In the **Configure** tab, click **Create custom framework**.

  4. Complete one of the following:

     * To use an existing framework, complete the following:

       1. Select **Start from an existing framework**.

       2. Select the framework that you want to copy.

       3. Click **Add**.

     * To create a custom framework, select **Start new**.

**Note:** On the Standard tier, you can only copy the [Security Essentials](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-frameworks#security-essentials) framework. On the Premium and Enterprise tiers, you can build custom frameworks or use any available built-in frameworks.
  5. Enter a name, unique identifier, and description for your framework. Click **Continue**.

If you're copying an existing framework, the list of cloud controls that were part of the existing framework displays.

  6. To add the cloud controls that you require, complete the following:

     * To add an existing cloud control, click **Add Cloud Controls**. Select all the cloud controls that you require and then click **Add**.

When you add a control, verify the control type (detective, preventive, or audit) of the control. Note that preventive and audit controls are available only in Premium and Enterprise tiers. Don't include audit-only controls in a framework that you want to use to monitor your environment and detect violations. You can't deploy frameworks that include audit-only controls.

     * (Premium and Enterprise tiers only) To create a custom cloud control, click **Create custom cloud control**. For instructions, see [Create a custom cloud control](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-manage-cloud-controls#create-custom-cloud-control).

  7. Click **Continue**.

  8. Add any additional parameters that the cloud controls require.

For example, if you want to enable a Data Security Posture Management (DSPM) cloud control such as the **Restrict Access to Sensitive Data to Permitted Users** cloud control, specify the locations that principals must use. For more information about Data Security Posture Management controls, see [Advanced data governance and security cloud controls](https://docs.cloud.google.com/security-command-center/docs/dspm-data-security#advanced-cloud-controls).

  9. Click **Create**.




###  CLI 

To create a custom framework, run the `gcloud compliance-manager frameworks create` command:
    
    
    gcloud compliance-manager frameworks create FRAMEWORK \
       --location=LOCATION \
       --organization=ORGANIZATION \
       --display-name=DISPLAY_NAME \
       [--description=DESCRIPTION] \
       [--category=[CATEGORY,...] \
       [--cloud-control-details=[majorRevisionId=MAJOR_REVISION_ID],[name=NAME],[parameters=PARAMETERS]]
    

Replace the following values:

  * `FRAMEWORK`: the unique alphanumeric identifier for framework

  * `ORGANIZATION`: your organization ID

  * `LOCATION`: the region that the framework is stored in

  * `DISPLAY_NAME`: a human-readable name for the framework

  * `DESCRIPTION`: an optional description of the purpose of the framework

  * `[CATEGORY,...]`: an optional parameter that defines the categories that the framework is part of. The recommended value for your customized framework is `custom-framework`.

  * --cloud-control-details=`[majorRevisionId=MAJOR_REVISION_ID],[name=NAME],[parameters=PARAMETERS]'

is the optional list of cloud controls to include in your framework, in the following format:

    * `MAJOR_REVISION_ID`: an optional flag that specifies which version of the cloud control to view. If you don't include the flag, the latest version is used.

    * `NAME`: the name of the cloud control, in the format `organizations/ORGANIZATION_ID/locations/LOCATION/cloudControls/NAME`. `NAME` is the unique ID of the cloud control. You can find the cloud control ID using the `gcloud compliance-manager cloud-controls list` command.

    * `PARAMETERS`: the optional parameters that certain cloud controls require—for example, if you want to enable a Data Security Posture Management cloud control such as the **Restrict Access to Sensitive Data to Permitted Users** cloud control, specify the locations that principals must use.

Alternatively, you can specify a JSON or YAML file that includes a list of all the cloud controls. For example, `--cloud-control-details=path_to_file.(yaml|json)`. Expand the following section to view example JSON and YAML files.

#### Example JSON file
    
    [
        {
          "name": "organizations/3589215982/locations/global/cloudControls/restrict-bucket-region",
          "majorRevisionId": 1,
          "parameters": [
            {
              "name": "location",
              "parameterValue": {
                "stringValue": "us-west"
              }
            }
          ]
        },
        {
          "name": "organizations/3589215982/locations/global/cloudControls/enable-binary-authorization",
          "majorRevisionId": 2
        }
      ]
          

#### Example YAML file
    
    - name: organizations/3589215982/locations/global/cloudControls/restrict-bucket-region
        majorRevisionId: 1
        parameters:
        - name: location
          parameterValue:
            stringValue: us-west
      - name: organizations/3589215982/locations/global/cloudControls/enable-binary-authorization
        majorRevisionId: 2
          

If you don't specify cloud controls when you create a framework, you can add them later using the Console.




For example, to create a framework with the name `my-custom-framework`, run the following:
    
    
    gcloud compliance-manager frameworks create \
       my-custom-framework \
       --organization=3589215982 \
       --location=global \
       --description="This framework is my custom framework" \
       --display-name="My framework name" \
       --cloud-control-details='[{"name":"organizations/3589215982/locations/global/cloudControls/restrict-bucket-region","majorRevisionId":1,"parameters":[{"name":"location","parameterValue":{"stringValue":"us-west"}}]},{"name":"organizations/3589215982/locations/global/cloudControls/enable-binary-authorization","majorRevisionId":2}]'
    

For more information, see [gcloud compliance-manager frameworks create](https://docs.cloud.google.com/sdk/gcloud/reference/compliance-manager/frameworks/create).

###  Terraform 

The following sample shows how you can create a framework using Terraform.
    
    
    resource "google_cloud_security_compliance_framework" "example" {
      parent       = "organizations/123456789"
      location     = "global"
      framework_id = "example-framework"
    
      display_name = "Terraform Framework Name"
      description  = "An Terraform description for the framework"
    
      cloud_control_details {
    		name              = "organizations/123456789/locations/global/cloudControls/builtin-assess-resource-availability"
    		major_revision_id = "2"
    
        parameters {
          name = "location"
          parameter_value {
            string_value = "us-central1"
          }
        }
      }
    
        cloud_control_details {
    		name              = "organizations/123456789/locations/global/cloudControls/builtin-cmek-key-in-use-for-bigquery-table"
    		major_revision_id = "1"
    
        parameters {
          name = "location"
          parameter_value {
            string_list_value {
              values = ["us-central1", "us-west1"]
            }
          }
        }
      }
    
      cloud_control_details {
    		name              = "organizations/123456789/locations/global/cloudControls/builtin-enable-automatic-backups-cloud-sql"
    		major_revision_id = "3"
    
        parameters {
          name = "location"
          parameter_value {
            bool_value = true
          }
        }
      }
    
      cloud_control_details {
    		name              = "organizations/123456789/locations/global/cloudControls/builtin-require-cmek-on-bigquery-datasets"
    		major_revision_id = "2"
    
        parameters {
          name = "location"
          parameter_value {
            number_value = 1
          }
        }
      }
    
    
    }
    

## Deploy a framework

Deploy a framework to an organization, folder, or project so that you can control and monitor those resources using the framework's cloud controls. You can deploy multiple frameworks to each organization, folder, or project. If you are deploying a framework that includes only the [advanced data security cloud controls](https://docs.cloud.google.com/security-command-center/docs/dspm-data-security#advanced-cloud-controls), you can deploy the framework to App Hub applications in folders configured for application management.

Folders and projects inherit frameworks through the Google Cloud [resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy). Therefore, if you deploy frameworks at the organization level and at a project level, all the cloud controls within both frameworks apply to the resources in the project. If there are any differences in cloud control definitions, the lower-level cloud control is used by the resources in the project. For example, if a cloud control rule is set to Allow at the organization level and to Deny at the project level, the project-level setting of Deny is applied to the resources in the project.

As a best practice, we recommend that you deploy a framework at the organization level that includes the cloud controls that can apply to your entire business. You can then deploy more stringent frameworks to folders and projects that require them.

**Note:**

  * If you deploy a framework to a folder or project that has Security Health Analytics enabled, you might receive duplicate findings. Compliance Manager uses a different evaluation engine then Security Health Analytics.



###  Console 

  1. In the Google Cloud console, go to the **Compliance** page.

[Go to Compliance](https://console.cloud.google.com/security/command-center/compliance)

  2. Select your organization or project.

  3. In the **Configure** tab, for the framework that you want to deploy, click more_vert **More Actions > Apply to resources**.

  4. Choose **Monitor** or **Monitor and prevent** to monitor for drift only.

  5. Select the resource that you want to deploy the framework to. You can choose an existing organization, folder, or project. For DSPM only, you can select an application to deploy a framework that includes only DSPM advanced cloud controls to an application. Optionally, you can create a new folder or project and deploy the framework to it.

  6. Complete one of the following:

     * If you selected **Monitor** , complete the following:

       1. Verify the information.
       2. If you selected a folder configured for application management and your framework includes only [advanced DSPM cloud controls](https://docs.cloud.google.com/security-command-center/docs/dspm-data-security#advanced-cloud-controls), select the application that you want to monitor.
       3. Click **Monitor**.
     * If you selected **Monitor and prevent** , complete the following:

       1. Click **Next**. Review the cloud controls and modes.
       2. Click **Continue**.
       3. If displayed, verify the additional information that's required for some cloud controls.
       4. Click **Next**.
       5. Review your selections and then click **Enforce**.



###  CLI 

To deploy a framework in your organization, run the `gcloud compliance-manager framework-deployments create` command. Consider the following best practices:

  * Create a separate YAML or JSON file for your cloud control metadata.

  * Use the appropriate target flags to indicate whether you're going to deploy to an existing organization, folder, or project; or whether you're going to create a new project or folder at the same time as deploying the framework.

  * Use resource identifiers only, instead of fully qualified resource names, if possible.



    
    
    gcloud compliance-manager framework-deployments create \
       (FRAMEWORK_DEPLOYMENT : \
       --location=LOCATION \
       --organization=ORGANIZATION) \
       --cloud-control-metadata=[cloudControlDetails=CLOUD_CONTROL_DETAILS],[enforcementMode=ENFORCEMENT_MODE] \
       (--framework=FRAMEWORK : \
       --framework-major-revision-id=FRAMEWORK_MAJOR_REVISION_ID) \
       (--target-resource-config-existing=TARGET_RESOURCE_CONFIG_EXISTING     | \
       --target-resource-creation-config-folder-display-name=TARGET_RESOURCE_CREATION_CONFIG_FOLDER_DISPLAY_NAME \
       --target-resource-creation-config-folder-parent=TARGET_RESOURCE_CREATION_CONFIG_FOLDER_PARENT     | \
       --target-resource-creation-config-project-billing-account-id=TARGET_RESOURCE_CREATION_CONFIG_PROJECT_BILLING_ACCOUNT_ID \
       --target-resource-creation-config-project-display-name=TARGET_RESOURCE_CREATION_CONFIG_PROJECT_DISPLAY_NAME \
       --target-resource-creation-config-project-parent=TARGET_RESOURCE_CREATION_CONFIG_PROJECT_PARENT) \
       [--description=DESCRIPTION]
    

Replace the following values:

  * `FRAMEWORK_DEPLOYMENT`: the ID of the framework deployment

  * `ORGANIZATION`: your organization ID

  * `LOCATION`: the region that the framework deployment is stored in

  * `cloud-control-metadata=[cloudControlDetails=CLOUD_CONTROL_DETAILS],[enforcementMode=ENFORCEMENT_MODE]`: the list of cloud controls in the framework, with their names, parameters, revision ID, and enforcement mode, in the following format:

    * `CLOUD_CONTROL_DETAILS`: an object that includes the list of cloud control names, parameters, and revision IDs. It uses the following format:

      * `name=NAME`: the full resource name of the cloud control, in the format `organizations/ORGANIZATION_ID/locations/LOCATION/cloudControls/CLOUD_CONTROL_NAME`

      * `majorRevisionId=MAJOR_REVISION_ID`: the major version of the cloud control

      * `parameters=PARAMETERS`: the optional parameters that certain cloud controls require—for example, if you want to enable a Data Security Posture Management cloud control such as the **Restrict Access to Sensitive Data to Permitted Users** cloud control, specify the locations that principals must use.

    * `ENFORCEMENT_MODE`: whether the control is an `AUDIT`, `DETECTIVE`, or `PREVENTIVE` control

Alternatively, you can specify a JSON or YAML file that includes the cloud control details and enforcement modes. For example, `--cloud-control-metadata=path_to_file.(yaml|json)`. Expand the following sections to view example JSON and YAML files.

#### Example JSON file
          
          [
              {
                "cloudControlDetails": {
                  "name": "organizations/3589215982/locations/global/cloudControls/restrict-bucket-region",
                  "majorRevisionId": 1,
                  "parameters": [
                    {
                      "name": "location",
                      "parameterValue": {
                        "stringValue": "us-west"
                      }
                    }
                  ]
                },
                "enforcementMode": "DETECTIVE"
              },
              {
                "cloudControlDetails": {
                  "name": "organizations/3589215982/locations/global/cloudControls/enable-binary-authorization",
                  "majorRevisionId": 2
                },
                "enforcementMode": "DETECTIVE"
              }
            ]
                

#### Example YAML file
          
          - cloudControlDetails:
                name: organizations/3589215982/locations/global/cloudControls/restrict-bucket-region
                majorRevisionId: 1
                parameters:
                - name: location
                  parameterValue:
                    stringValue: us-west
              enforcementMode: DETECTIVE
            - cloudControlDetails:
                name: organizations/3589215982/locations/global/cloudControls/enable-binary-authorization
                majorRevisionId: 2
              enforcementMode: DETECTIVE
                

    * `FRAMEWORK`: the name of an existing framework that you want to deploy, in the format `organizations/ORGANIZATION_ID/locations/LOCATION/frameworks/FRAMEWORK_NAME`

    * `FRAMEWORK_MAJOR_REVISION_ID`: the version number of the framework that you want to deploy

    * `TARGET_RESOURCE_CONFIG_EXISTING `: the name of an existing organization, folder, or project that you want to deploy the new framework to, in one of the following formats:

      * `organizations/ORGANIZATION_ID`
      * `folders/FOLDER_ID`
      * `projects/PROJECT_ID`
    * `TARGET_RESOURCE_CREATION_CONFIG_FOLDER_DISPLAY_NAME`: the name of the folder that you want to create and then deploy the framework to

    * `TARGET_RESOURCE_CREATION_CONFIG_FOLDER_PARENT`: the name of the existing organization or folder that you want to create the new folder in. Supported formats are `organizations/ORGANIZATION_ID` and `folders/FOLDER_ID`.

    * `TARGET_RESOURCE_CREATION_CONFIG_PROJECT_BILLING_ACCOUNT_ID`: the billing account ID to assign to the new project, if you're creating a new project that you want to deploy the framework to

    * `TARGET_RESOURCE_CREATION_CONFIG_PROJECT_DISPLAY_NAME`: the name of the project that you want to create and then deploy the framework to

    * `TARGET_RESOURCE_CREATION_CONFIG_PROJECT_PARENT`: the name of the existing organization or folder that you want to create the new project in. Supported formats are `organizations/ORGANIZATION_ID` and `folders/FOLDER_ID`.

    * `DESCRIPTION`: an optional description for the framework deployment




For example, to deploy a framework that's named `organizations/3589215982/locations/global/frameworks/builtin-aipp` to an existing folder with the folder ID `example-folder` run the following:
    
    
    gcloud compliance-manager framework-deployments create \
       example-framework-deployment \
       --organization=3589215982 \
       --location=global \
       --cloud-control-metadata='[{"cloudControlDetails": {"name": "organizations/3589215982/locations/global/cloudControls/restrict-bucket-region", "majorRevisionId": "1", "parameters": []}, "enforcementMode": "DETECTIVE"}, {"cloudControlDetails": {"name": "organizations/3589215982/locations/global/cloudControls/enable-binary-authorization", "majorRevisionId": 2}, "enforcementMode": "DETECTIVE"}]' \
       --framework="organizations/3589215982/locations/global/frameworks/builtin-aipp" \
       --framework-major-revision-id=6 \
       --target-resource-config-existing="folders/example-folder" \
       --description="Deployment for AI Platform into example-folder"
    

For example, to deploy a framework that's named `organizations/3589215982/locations/global/frameworks/builtin-aipp`, and create a new project named `example-new-project` in an existing folder with the folder ID `example-folder` run the following:
    
    
    gcloud compliance-manager framework-deployments create \
      example-framework-deployment \
       --organization=3589215982 \
       --location=global \
       --cloud-control-metadata=deploy-controls.yaml \
       --framework="organizations/3589215982/locations/global/frameworks/builtin-aipp" \
       --framework-major-revision-id=6 \
       --target-resource-creation-config-project-billing-account-id=012345-567890-ABCDEF \
       --target-resource-creation-config-project-display-name=example-new-project \
       --target-resource-creation-config-project-parent=folders/example-folder \
       --description="Deployment for AI Platform into a new example-new-project in example-folder"
    

For information, see [gcloud compliance-manager framework-deployments create](https://docs.cloud.google.com/sdk/gcloud/reference/compliance-manager/framework-deployments/create).

###  Terraform 

The following sample shows how you can deploy a framework using Terraform.
    
    
    resource "google_cloud_security_compliance_cloud_control" "example" {
      parent           = "organizations/123456789"
      location         = "global"
      cloud_control_id = "example-cloudcontrol"
    
      display_name              = "TF test CloudControl Name"
      description               = "A test cloud control for security compliance"
      categories                = ["CC_CATEGORY_INFRASTRUCTURE"]
      severity                  = "HIGH"
      finding_category          = "SECURITY_POLICY"
      remediation_steps         = "Review and update the security configuration according to best practices."
      supported_cloud_providers = ["GCP"]
    
      rules {
        description       = "Ensure compute instances have secure boot enabled"
        rule_action_types = ["RULE_ACTION_TYPE_DETECTIVE"]
    
        cel_expression {
          expression = "resource.data.shieldedInstanceConfig.enableSecureBoot == true"
          resource_types_values {
            values = ["compute.googleapis.com/Instance"]
          }
        }
      }
    
      parameter_spec {
        name        = "enabled"
        value_type  = "BOOLEAN"
        is_required = true
      }
    
      parameter_spec {
        name        = "regions"
        value_type  = "STRINGLIST"
        is_required = true
      }
    
      parameter_spec {
        name        = "location"
        value_type  = "STRING"
        is_required = true
      }
    
      parameter_spec {
        name        = "oneof-parameter"
        value_type  = "ONEOF"
        is_required = true
    
        sub_parameters {
          name        = "test-oneof"
          value_type  = "STRING"
          is_required = true
        }
    
        sub_parameters {
          name        = "updated-test-oneof"
          value_type  = "STRING"
          is_required = true
        }
      }
    
      parameter_spec {
        name        = "bool-parameter"
        value_type  = "ONEOF"
        is_required = true
    
        sub_parameters {
          name        = "bool-oneof"
          value_type  = "BOOLEAN"
          is_required = true
        }
    
        sub_parameters {
          name        = "updated-bool-oneof"
          value_type  = "BOOLEAN"
          is_required = true
        }
      }
    
      parameter_spec {
        name        = "number-parameter"
        value_type  = "ONEOF"
        is_required = true
    
        sub_parameters {
          name        = "number-oneof"
          value_type  = "NUMBER"
          is_required = true
        }
    
        sub_parameters {
          name        = "updated-number-oneof"
          value_type  = "NUMBER"
          is_required = true
        }
      }
    
      parameter_spec {
        name        = "string-list-parameter"
        value_type  = "ONEOF"
        is_required = true
    
        sub_parameters {
          name        = "string-list-oneof"
          value_type  = "STRINGLIST"
          is_required = true
        }
    
        sub_parameters {
          name        = "updated-string-list-oneof"
          value_type  = "STRINGLIST"
          is_required = true
        }
      }
    }
    
    resource "google_cloud_security_compliance_framework" "example" {
      parent       = "organizations/123456789"
      location     = "global"
      framework_id = "example-framework"
    
      display_name = "Terraform Framework Name"
      description  = "An Terraform description for the framework"
    
      cloud_control_details {
        name              = google_cloud_security_compliance_cloud_control.example.name
        major_revision_id = "1"
    
        parameters {
          name = "enabled"
          parameter_value {
            bool_value = true
          }
        }
      }
    }
    
    resource "google_cloud_security_compliance_framework_deployment" "example" {
      parent                  = "organizations/123456789"
      location                = "global"
      framework_deployment_id = "example-deployment"
      description             = "A framework deployment for cloud security compliance"
    
      framework {
        framework         = google_cloud_security_compliance_framework.example.name
        major_revision_id = "1"
      }
    
      target_resource_config {
        existing_target_resource = "organizations/123456789"
      }
    
      cloud_control_metadata {
        enforcement_mode = "DETECTIVE"
    
        cloud_control_details {
          name              = google_cloud_security_compliance_cloud_control.example.name
          major_revision_id = "1"
    
          parameters {
            name = "enabled"
            parameter_value {
              bool_value = true
            }
          }
    
          parameters {
            name = "regions"
            parameter_value {
              string_list_value {
                values = ["us-central1", "us-west1", "us-east1"]
              }
            }
          }
    
          parameters {
            name = "location"
            parameter_value {
              string_value = "us-central1"
            }
          }
    
          parameters {
            name = "oneof-parameter"
            parameter_value {
              oneof_value {
                name = "test-oneof"
                parameter_value {
                  string_value = "test-value"
                }
              }
            }
          }
    
          parameters {
            name = "bool-parameter"
            parameter_value {
              oneof_value {
                name = "bool-oneof"
                parameter_value {
                  bool_value = true
                }
              }
            }
          }
    
          parameters {
            name = "number-parameter"
            parameter_value {
              oneof_value {
                name = "number-oneof"
                parameter_value {
                  number_value = 123.45
                }
              }
            }
          }
    
          parameters {
            name = "string-list-parameter"
            parameter_value {
              oneof_value {
                name = "string-list-oneof"
                parameter_value {
                  string_list_value {
                    values = ["value1", "value2"]
                  }
                }
              }
            }
          }
        }
      }
    }
    

After you deploy the framework, you can monitor your environment for any drift from your defined cloud controls. Security Command Center reports instances of drift as _findings_ that you can review, filter, and resolve. It can take approximately six hours after you deploy a framework for findings related to cloud controls to appear.

## Edit a custom framework

After you create a framework, you can change its name and description, add or remove cloud controls, and update any parameters. You can only edit frameworks that you create; you can't edit built-in frameworks. Also, you can only edit frameworks that aren't deployed.

  1. In the Google Cloud console, go to the **Compliance** page.

[Go to Compliance](https://console.cloud.google.com/projectselector2/security/command-center/compliance?supportedpurview=organizationId)

  2. Select your organization or project.

  3. On the **Configure** tab, click the framework that you want to edit.

  4. On the **Framework details** page, verify that the framework isn't assigned to a resource. If required, remove the assignments.

  5. Click **Actions > Edit**.

  6. In the **Update framework details** page, change the name and description as required. Click **Continue**.

  7. To change the cloud controls that are included in the framework, complete the following:

     * To add an existing cloud control, click **Add Cloud Controls**. Select all the cloud controls that you require and then click **Add**.

     * To create a custom cloud control, click **Create custom cloud control**. For instructions, see [Create a custom cloud control](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-manage-cloud-controls#create-custom-cloud-control).

     * To remove a cloud control, select the cloud control and click **Remove**.

  8. Click **Continue**.

  9. Add any additional parameters that the cloud controls require.

  10. Click **Save**.




## Remove a deployed framework from a resource

You can remove a framework from the organization, folders, or projects that you assigned the framework to. Removing the framework means that Compliance Manager no longer generates findings for that node of your resource hierarchy.

When you remove a framework, the state of most of the related findings changes to `Inactive` after seven days. If your framework includes the _Restrict Flow of Sensitive Data Across Geographic Jurisdictions_ cloud control, the findings change to `Inactive` after 90 days. The states for findings that are related to the _Restrict Flow of Sensitive Data Across Geographic Jurisdictions_ cloud control and the _Restrict Access to Sensitive Data to Permitted Users_ cloud control aren't automatically changed.

###  Console 

  1. In the Google Cloud console, go to the **Compliance** page.

[Go to Compliance](https://console.cloud.google.com/projectselector2/security/command-center/compliance?supportedpurview=organizationId)

  2. Select your organization or project.

  3. On the **Configure** tab, click the framework that you want to remove.

  4. On the **Framework details** page, click **Actions > Manage resource assignments**.

  5. In the **Assigned resources** table, find the resource that you want to remove and click delete **Delete**.

  6. Review the confirmation message and click **Unassign**.

  7. Optional: Change the state of associated findings to `Inactive`. For instructions, see [Change the state of a finding](https://docs.cloud.google.com/security-command-center/docs/review-manage-findings#change-state).




###  CLI 

To remove a particular framework deployment in your organization, run the `gcloud compliance-manager framework-deployments delete` command:
    
    
    gcloud compliance-manager framework-deployments delete \
       FRAMEWORK_DEPLOYMENT \
       --location=LOCATION \
       --organization=ORGANIZATION \
       --etag=ETAG_ID
    

Replace the following values:

  * `FRAMEWORK_DEPLOYMENT`: the ID of the framework deployment

  * `ORGANIZATION`: your organization ID

  * `LOCATION`: the region that the framework deployment is stored in

  * `ETAG_ID`: the identifier for the current version of the framework deployment, that helps ensure that you're deleting the intended version of the framework deployment. If the identifier doesn't match the current version, then the request fails. If you omit this value, then Compliance Manager deletes the framework deployment unconditionally.




For example, to remove `example-deployment` from organization `3589215982` and stored in the global location, run the following:
    
    
    gcloud compliance-manager framework-deployments delete \
       example-deployment \
       --organization=3589215982 \
       --location=global \
       --etag=MTc3NDU4MjM4OTY0MzU5MjQ5OTI=
    

For information about optional flags, see [gcloud compliance-manager framework-deployments delete](https://docs.cloud.google.com/sdk/gcloud/reference/compliance-manager/framework-deployments/delete).

## Update a framework to a newer release

Google publishes regular updates to its built-in frameworks as services deploy new features or as new best practices emerge.

You can view the releases of built-in frameworks in the frameworks dashboard in the **Configure** tab or in the framework details page.

Google notifies you in the console and release notes when the following updates occur:

  * Built-in cloud controls are added or removed from a framework.
  * [Built-in cloud controls are updated](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-manage-cloud-controls#update-cloud-control-version).



To update a framework, complete the following:

  1. In the Google Cloud console, go to the **Compliance** page.

[Go to Compliance](https://console.cloud.google.com/projectselector2/security/command-center/compliance?supportedpurview=organizationId)

  2. Select your organization or project.

  3. On the **Configure** tab, click the framework that you want to update.

  4. On the **Framework details** page, in the **Assigned resources** table, review the **Update status** for any assignments that are identified as **Update available**.

  5. To apply the changes, complete the following:

     1. Remove the resource assignment.

**Note:** When you remove a resource assignment, Compliance Manager no longer evaluates that resource using that framework. Findings are no longer created.
     2. Redeploy the framework to your resource so that Compliance Manager can resume evaluating the resource and creating findings.




## Delete a custom framework

Delete a framework when it's no longer required. You can only delete frameworks that you create; you can't delete built-in frameworks.

**Note:** You can't recover a framework after you delete it.

###  Console 

  1. In the Google Cloud console, go to the **Compliance** page.

[Go to Compliance](https://console.cloud.google.com/projectselector2/security/command-center/compliance?supportedpurview=organizationId)

  2. Select your organization or project.

  3. On the **Configure** tab, click the framework that you want to unassign resources from.

  4. On the **Framework details** page, verify that the framework isn't assigned to a resource. If required, remove the assignments.

  5. Click **Actions > Delete**.

  6. In the **Delete** window, review the message. Type `Delete` and click **Confirm**.




###  CLI 

To delete a particular framework in your organization, run the `gcloud compliance-manager frameworks delete` command:
    
    
    gcloud compliance-manager frameworks delete \
       FRAMEWORK \
       --location=LOCATION \
       --organization=ORGANIZATION
    

Replace the following values:

  * `FRAMEWORK`: the name of the framework

  * `ORGANIZATION`: your organization ID

  * `LOCATION`: the region that the framework is stored in




For example, to remove `example-framework` from organization `3589215982` and stored in the global location, run the following:
    
    
    gcloud compliance-manager frameworks delete \
       example-framework \
       --organization=3589215982 \
       --location=global
    

For information about optional flags, see [gcloud compliance-manager frameworks delete](https://docs.cloud.google.com/sdk/gcloud/reference/compliance-manager/frameworks/delete).

## What's next

  * [Monitor your frameworks for compliance](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-monitor-framework).
  * [Audit your environment with Compliance Manager](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-audit).
  * [Review and manage findings in the console](https://docs.cloud.google.com/security-command-center/docs/review-manage-findings).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
