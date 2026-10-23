---
url: https://docs.cloud.google.com/security-command-center/docs/custom-modules-sha-create/
title: Use custom modules for Security Health Analytics \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:33:08.948125+00:00
---

# Use custom modules for Security Health Analytics  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/custom-modules-sha-create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Use custom modules for Security Health Analytics Stay organized with collections  Save and categorize content based on your preferences. 

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

This page explains how to create, view, update, and delete custom modules for Security Health Analytics by using either the Google Cloud console or Google Cloud CLI.

For more introductory information, see [Overview of custom modules for Security Health Analytics](https://docs.cloud.google.com/security-command-center/docs/custom-modules-sha-overview).

## Before you begin

Before you can work with custom modules, you need the following prerequisites:

  * Security Health Analytics must be enabled. For information about enabling Security Health Analytics, see [Enable or disable a built-in service](https://docs.cloud.google.com/security-command-center/docs/how-to-configure-security-command-center#enable-service).
  * Your user account must be granted one or more Identity and Access Management (IAM) roles that contain the required permissions. For more information, see Required IAM permissions.
  * If you intend to write your own custom modules and upload them to Security Command Center by using `gcloud` commands, you need the Google Cloud CLI. For information about installing the gcloud CLI, see [Install the gcloud CLI](https://docs.cloud.google.com/sdk/docs/install).
  * If the Security Command Center API is not already enabled, you need to enable it before you can use custom modules for Security Health Analytics. You can enable the Security Command Center API on the [API Library page](https://console.cloud.google.com/projectselector2/apis/library) in the Google Cloud console.
  * To understand the usage limits for Security Health Analytics, see [Custom module quotas](https://docs.cloud.google.com/security-command-center/docs/custom-modules-sha-overview#custom_module_quotas).



### Required IAM permissions

To work with custom modules, you need the following Identity and Access Management (IAM) permissions:

Permission | Role  
---|---  
securitycenter.securityhealthanalyticscustommodules.create  
securitycenter.securityhealthanalyticscustommodules.update  
securitycenter.securityhealthanalyticscustommodules.delete | roles/securitycenter.settingsEditor  
roles/securitycenter.admin  
securitycenter.securityhealthanalyticscustommodules.get  
securitycenter.securityhealthanalyticscustommodules.list | roles/securitycenter.settingsViewer  
roles/securitycenter.adminViewer  
roles/securitycenter.admin  
securitycenter.securityhealthanalyticscustommodules.test | roles/securitycenter.securityHealthAnalyticsCustomModulesTester  
roles/securitycenter.adminViewer  
roles/securitycenter.adminEditor  
roles/securitycenter.admin  
  
For more information about IAM permissions and roles and how to grant them, see [Grant an IAM role by using the Google Cloud console](https://docs.cloud.google.com/iam/docs/grant-role-console).

## Create a custom module

This section explains how to create custom modules using the Google Cloud console, the gcloud CLI, or Terraform.

To test your custom module as a step in the creation process, you need to prepare test resource definitions in a YAML file. For instructions, see [Create test resources in a YAML file](https://docs.cloud.google.com/security-command-center/docs/custom-modules-sha-test#create-test-resources).

To create a custom module, select the method that you want to use from the following tabs:

###  Google Cloud console 

To create a custom module in the Google Cloud console, complete the following steps:

  1. Go to the Security Command Center **Settings** page in the Google Cloud console.

[Go to Settings](https://console.cloud.google.com/security/command-center/config/services)

  2. If prompted, select the organization, folder, or project in which you need to create the custom module.

  3. On the **Security Health Analytics** card, click **Manage Settings**.

  4. Click the **Modules** tab.

  5. Click add_box **Create module**. The **Create module for Security Health Analytics** page opens.

  6. On the **Configure module** panel, define the display name, resources to scan, and the detection logic:

     1. In the **Module name** field, specify a name for the module. The name must be between 1 and 128 characters, start with a lowercase letter, and contain alphanumeric characters or underscores only. This name becomes the finding category of the findings that this detector produces. You can't change the name after the module is created.

     2. Under **Add resource type** , specify one to five resource types to scan. You cannot specify a resource type more than once.

For a list of supported resource types, see [Supported resource types](https://docs.cloud.google.com/security-command-center/docs/custom-modules-sha-overview#supported-resource-type).

     3. In the **Expression editor** , write CEL expressions to run boolean checks on one or more properties of the resource that you specified in the last step. To trigger a finding, the expression must resolve to `TRUE`. For example, the following expression triggers a finding if a `CryptoKey` resource has a rotation period defined and the rotation period is longer than 2,592,000 seconds (30 days):
            
            has(resource.rotationPeriod) && (resource.rotationPeriod > duration('2592000s'))
            

For more information, see the following:

        * [Write CEL expressions](https://docs.cloud.google.com/security-command-center/docs/custom-modules-sha-code#cel_expressions)
        * [Referencing resource and policy properties in custom modules](https://docs.cloud.google.com/security-command-center/docs/custom-modules-sha-code#properties-referencing)
        * [List of Standard CEL Definitions](https://github.com/google/cel-spec/blob/master/doc/langdef.md#list-of-standard-definitions)
     4. Click **Next**. The **Define finding details** panel opens.

  7. On the **Define finding details** panel, describe the issue that the custom module detects, including its severity, what the issue is, how to fix the issue, and any data that you want to include in the findings as custom source properties:

     1. In the **Severity** field, specify the severity of the issue. You can specify `Low`, `Medium`, `High`, or `Critical`. `Medium` is the default.

For information about severity levels, see [Severity classifications for findings](https://docs.cloud.google.com/security-command-center/docs/finding-severity-classifications).

     2. In the **Finding description** field, explain the issue that the custom module detects. This explanation appears in each finding instance to help security teams understand and address the detected issue.

     3. In the **Finding next steps** field, explain the steps that your security team can take to fix or otherwise address the detected issue.

The steps display with each finding instance. Include specific steps that the security team can take to address the issue as quickly as possible.

     4. Optional: In the **Custom finding properties** field, specify up to 10 name-value pairs to define custom source properties to return with each finding instance. The information is returned as source properties in the finding JSON and is displayed on the **Source properties** tab in the finding details in the Google Cloud console. Specify the text or property values as key-value pairs:

        * In the **Property name** field, specify a name for the custom source property. The name must conform to the following rules: 
          * The name must begin with a lowercase letter.
          * The name must contain only alphanumeric characters or underscores.
          * The name must be between 1 and 128 characters in length.
          * Each name must be unique among the other source properties.
        * In the **Property value** field, specify one of the following values in 1024 characters or less: 
          * A text string enclosed in quotation marks. The quotation marks are included in the 1024 character limit. For example, `"This string provides additional useful information."`
          * Any property of the resource that is being scanned. For example, if you are checking the `CryptoKey` resource, you might specify `resource.rotationPeriod`. The value of the `rotationPeriod` property is returned.
     5. Click **Next**. The **Enable module** panel opens.

  8. Optional: Use the drop-down menu of the **Enable module** panel to specify whether the custom module is enabled or disabled upon creation. By default, custom modules are enabled upon creation. If you specify **Disable** , you can enable the module later on the **Modules** tab in the Security Health Analytics settings page.

  9. Click **Next**. The **Test module** panel opens.

  10. Optional: Before you create your custom module, we recommend that you test it.

To test a custom module, follow these steps:

     1. Create a YAML file that contains test resource definitions for the resources that your custom module checks.

For information about how to create a test data file, see [Create test resources in a YAML file](https://docs.cloud.google.com/security-command-center/docs/custom-modules-sha-test#create-test-resources).

     2. Under **Upload the YAML file** , click **Browse** to upload the YAML file that contains the test resource definitions. The test starts automatically when the file is uploaded.

     3. Under **Test results preview** , check the results.

        * If there are syntax or other errors in your YAML file, a floating error message displays near the bottom of the browser page.
        * If the test is a success, the test returns the following information:

          * The display name of the custom module.
          * The arbitrary name that you specified on the `resource` property in the test data file.
          * The organization, folder, or project in which the custom module was, or will be, created.

Test results are not stored or written to Security Command Center.

For more information, see [Testing custom modules](https://docs.cloud.google.com/security-command-center/docs/custom-modules-sha-test).

  11. Click **Create**. You are returned to the **Modules** page and should see the module that you created with a status of **Enabled**.




New custom modules are not immediately available for use by Security Health Analytics in scans. For more information, see Detection latency.

###  gcloud CLI 

To create a custom module by using `gcloud` commands, you first need to code the definition of the custom module in a YAML file that includes CEL expressions for the detection logic and output properties.

After the definition is complete, you upload the definition to Security Command Center by using gcloud CLI commands.

  1. Code a custom module definition in a YAML file according to the instructions in [Code a custom module for Security Health Analytics](https://docs.cloud.google.com/security-command-center/docs/custom-modules-sha-code).
  2. Save the YAML file to a location that is accessible to your instance of gcloud CLI.
  3. Upload the custom definition to Security Command Center:
         
         [gcloud scc custom-modules sha create](https://docs.cloud.google.com/sdk/gcloud/reference/scc/custom-modules/sha/create) \
             PARENT_FLAG=PARENT_ID \
             --display-name="MODULE_DISPLAY_NAME" \
             --enablement-state="ENABLEMENT_STATE" \
             --custom-config-from-file=MODULE_FILE_NAME.yaml
         

Replace the following:

     * `PARENT_FLAG`: the level at which you are creating the custom module, either `--organization`, `--folder`, or `--project`.
     * `PARENT_ID`: the ID of the organization, folder, or project in which you are creating the custom module.
     * `ENABLEMENT_STATE`: either `enabled` or `disabled`.
     * `MODULE_DISPLAY_NAME`: the finding category name that you want to display when the custom module returns a finding. The name must be between 1 and 128 characters, start with a lowercase letter, and contain alphanumeric characters or underscores only.
     * `MODULE_FILE_NAME`: the path and filename of the YAML file that contains the definition of the custom module.



###  Terraform 

Create a custom module for an organization:
    
    
    resource "google_scc_management_organization_security_health_analytics_custom_module" "example" {
      organization = "123456789"
      display_name = "basic_custom_module"
      location = "global"
      enablement_state = "ENABLED"
      custom_config {
        predicate {
          expression = "resource.rotationPeriod > duration(\"2592000s\")"
        }
        resource_selector {
          resource_types = [
            "cloudkms.googleapis.com/CryptoKey",
          ]
        }
        description = "The rotation period of the identified cryptokey resource exceeds 30 days."
        recommendation = "Set the rotation period to at most 30 days."
        severity = "MEDIUM"
      }
    }
    

Create a custom module for a folder:
    
    
    resource "google_folder" "folder" {
      parent       = "organizations/123456789"
      display_name = "folder-name"
      deletion_protection = false
    }
    
    resource "google_scc_management_folder_security_health_analytics_custom_module" "example" {
      folder = google_folder.folder.folder_id
      location = "global"
      display_name = "basic_custom_module"
      enablement_state = "ENABLED"
      custom_config {
        predicate {
          expression = "resource.rotationPeriod > duration(\"2592000s\")"
        }
        resource_selector {
          resource_types = [
            "cloudkms.googleapis.com/CryptoKey",
          ]
        }
        description = "The rotation period of the identified cryptokey resource exceeds 30 days."
        recommendation = "Set the rotation period to at most 30 days."
        severity = "MEDIUM"
      }
    }
    

Create a custom module for a project:
    
    
    resource "google_scc_management_project_security_health_analytics_custom_module" "example" {
      location = "global"
      display_name = "basic_custom_module"
      enablement_state = "ENABLED"
      custom_config {
        predicate {
          expression = "resource.rotationPeriod > duration(\"2592000s\")"
        }
        resource_selector {
          resource_types = [
            "cloudkms.googleapis.com/CryptoKey",
          ]
        }
        description = "The rotation period of the identified cryptokey resource exceeds 30 days."
        recommendation = "Set the rotation period to at most 30 days."
        severity = "MEDIUM"
      }
    }
    

## Detection latency

After you create or update the definition of a custom module, there can be a delay of up to several hours before the new or updated custom module is available for use in scans.

Creating or modifying a custom module doesn't trigger a scan. After a custom module is available for use, Security Health Analytics doesn't start using the custom modules until either the first batch scan or a change to the configuration of the target resource triggers a real-time scan.

For more information about Security Health Analytics scan types, see [Security Health Analytics scan types](https://docs.cloud.google.com/security-command-center/docs/concepts-security-health-analytics#sha-scan-types).

## Update a custom module

You can update most properties of Security Health Analytics custom modules.

The following properties of a custom module cannot be changed:

  * The display name.
  * The custom module ID.
  * The full resource name of the custom module.



When you update a custom module, any findings that the custom module generated previously are not updated at the same time. If the changes to the module result in changes to the generated findings, the findings will reflect the changes only after the next Security Health Analytics batch or real-time scan.

To modify a custom module, you can use either the Google Cloud console or the gcloud CLI. Click one of the following tabs for instructions.

###  Google Cloud console 

To update an existing custom module in the Google Cloud console, follow these steps:

  1. Go to the Security Command Center **Settings** page in the Google Cloud console.

[Go to Settings](https://console.cloud.google.com/security/command-center/config/services)

  2. In the project selector, select the organization, folder, or project in which the custom module was originally created. You can't edit a custom module anywhere else.

  3. On the **Security Health Analytics** card, click **Manage Settings**.

  4. Select the **Modules** tab. All of the Security Health Analytics detection modules are displayed.

  5. Use the filter field at the top of the list of modules or scroll to find the custom module that you need to modify.

  6. On the right side of the row of your custom module, click the **Action menu** icon, more_vert.

  7. From the **Action menu** , click the **Edit** icon (_edit_). The **View module** page opens and displays the **Configure module** tab.

  8. Edit the custom module fields of each tab on the **View module** page as needed.

  9. Optional: Before you save your updates, we recommend that you test them.

To test a custom module, follow these steps:

     1. Create a YAML file that contains test resource definitions for the resources that your custom module checks.

For information about how to create a test data file, see [Create test resources in a YAML file](https://docs.cloud.google.com/security-command-center/docs/custom-modules-sha-test#create-test-resources).

     2. Under **Upload the YAML file** , click **Browse** to upload the YAML file that contains the test resource definitions. The test starts automatically when the file is uploaded.

     3. Under **Test results preview** , check the results.

        * If there are syntax or other errors in your YAML file, a floating error message displays near the bottom of the browser page.
        * If the test is a success, the test returns the following information:

          * The display name of the custom module.
          * The arbitrary name that you specified on the `resource` property in the test data file.
          * The organization, folder, or project in which the custom module was, or will be, created.

Test results are not stored or written to Security Command Center.

For more information, see [Testing custom modules](https://docs.cloud.google.com/security-command-center/docs/custom-modules-sha-test).

  10. At the bottom of the page, click **Save**. Your changes are applied to the custom module.




###  gcloud CLI 

To update a custom module by using the gcloud CLI, you first edit the YAML definition of the custom module and then use `gcloud` commands to update the custom module in Security Health Analytics.

  1. Edit the custom module definition. For information about how to code a custom module definition, see [Coding a custom module for Security Health Analytics](https://docs.cloud.google.com/security-command-center/docs/custom-modules-sha-code).

  2. Save the edited YAML file to a location that is accessible to the gcloud CLI.

  3. Update the custom module in Security Health Analytics by issuing the following command:
         
         [gcloud scc custom-modules sha update](https://docs.cloud.google.com/sdk/gcloud/reference/scc/custom-modules/sha/update) MODULE_ID \
            PARENT_FLAG=PARENT_ID \
            --enablement-state="ENABLED" \
            --custom-config-from-file=MODULE_FILE_NAME.yaml
         

Replace the following:

     * `MODULE_ID`: the ID or full resource name of the custom module.
     * `PARENT_FLAG`: the level at which the custom module was created, either `--organization`, `--folder`, or `--project`.
     * `PARENT_ID`: the ID of the organization, folder, or project in which the custom module was created.
     * `MODULE_FILE_NAME`: the path and filename of the YAML file that contains the definition of the custom module.



## View a custom module

Select a tab to learn how to view a custom module definition.

###  Google Cloud console 

To view custom modules in the Google Cloud console, follow these steps:

  1. Go to the **Security Health Analytics** page in Security Command Center settings.

[Go to Settings](https://console.cloud.google.com/security/command-center/config/services/security-health-analytics)

  2. Click the **Modules** tab. The **Modules** panel opens.

  3. If necessary, use the filter field at the top of the list of modules to find the custom module that you need to modify.

  4. To view the details of the custom module definition, click the **Action menu** icon, more_vert, on the right side of the custom module row.

  5. From the **Action menu** , click the **Edit** icon, _edit_. The **View module** page opens and displays the **Configure module** tab.

  6. Click through the tabs on the **View module** page to see all of the fields of the custom module definition.




###  gcloud CLI 

To view the details of a custom module, enter the following command:
    
    
    [gcloud scc custom-modules sha get](https://docs.cloud.google.com/sdk/gcloud/reference/scc/custom-modules/sha/get) MODULE_ID \
          PARENT_FLAG=PARENT_ID
    

Replace the following:

  * `MODULE_ID`: the ID or full resource name of the custom module.
  * `PARENT_FLAG`: the level at which the custom module was created, either `--organization`, `--folder`, or `--project`.
  * `PARENT_ID`: the ID of the organization, folder, or project in which the custom module was created.



## List custom modules

Select a tab to learn how to display a list of custom modules.

###  Google Cloud console 

  1. Go to the **Security Health Analytics** page in Security Command Center settings.

[Go to Settings](https://console.cloud.google.com/security/command-center/config/services/security-health-analytics)

  2. Click the **Modules** tab. The **Modules** panel opens.

  3. Click in the filter field at the top of the list of modules to display the list of filter types.

  4. Select **Type** and enter `Custom`. The modules lists is updated to show only custom modules.




###  gcloud CLI 

To view a list of custom modules, enter the following command:
    
    
    [gcloud scc custom-modules sha list](https://docs.cloud.google.com/sdk/gcloud/reference/scc/custom-modules/sha/list) \
        PARENT_FLAG=PARENT_ID
    

Replace the following:

  * `PARENT_FLAG`: the level at which the custom module was created, either `--organization`, `--folder`, or `--project`.
  * `PARENT_ID`: the ID of the organization, folder, or project in which the custom module was created.



## Delete a custom module

You can delete a custom module from the organization, folder, or project in which it was created or a parent organization or folder. You cannot delete a custom module from a folder or project that inherits it.

**Note:** Deleted modules can't be recovered.

To learn how to delete a custom module, select one of the following tabs.

###  Google Cloud console 

  1. Go to the Security Command Center **Settings** page in the Google Cloud console.

[Go to Settings](https://console.cloud.google.com/security/command-center/config/services)

  2. If prompted, select your organization, folder, or project.

  3. On the **Security Health Analytics** card, click **Manage Settings**.

  4. Select the **Modules** tab. All of the Security Health Analytics detection modules are displayed.

  5. Use the filter field at the top of the list of modules or scroll to find the custom module that you need to modify.

  6. On the right side of the row of your custom module, click the **Action menu** icon, more_vert.

  7. From the **Action menu** , click **Delete**. The **Delete custom module** dialog opens.

  8. In the dialog, click **Delete**.




###  gcloud CLI 

To delete a custom module, enter the following command:
    
    
    [gcloud scc custom-modules sha delete](https://docs.cloud.google.com/sdk/gcloud/reference/scc/custom-modules/sha/delete) MODULE_ID \
        PARENT_FLAG=PARENT_ID
    

Replace the following:

  * `MODULE_ID`: the ID or full resource name of the custom module.
  * `PARENT_FLAG`: the level at which the custom module was created, either `--organization`, `--folder`, or `--project`.
  * `PARENT_ID`: the ID of the organization, folder, or project in which the custom module was created.



Findings for deleted custom modules are marked inactive by Security Health Analytics in the next batch scan.

## Reviewing findings

Findings generated by custom modules can be viewed in the Google Cloud console or the Security Command Center API.

###  Console 

  1. In the Google Cloud console, go to the **Findings** page of Security Command Center.

[Go to Findings](https://console.cloud.google.com/security/command-center/findingsv2)

  2. Select your Google Cloud project or organization.
  3. In the **Quick filters** section, in the **Source display name** subsection, select **Security Health Analytics Custom**. The findings query results are updated to show only the findings from this source. 
  4. To view the details of a specific finding, click the finding name in the **Category** column. The details panel for the finding opens and displays the **Summary** tab. 
  5. On the **Summary** tab, review the details of the finding, including information about what was detected, the affected resource, and—if available—steps that you can take to remediate the finding. 
  6. Optional: To view the full JSON definition of the finding, click the **JSON** tab.



###  gcloud CLI 

To view findings, do the following:

  1. Open a terminal window.
  2. To get the source ID for Security Health Analytics, running the following command:
         
         [gcloud scc sources describe](https://docs.cloud.google.com/sdk/gcloud/reference/scc/sources/describe) organizations/ORGANIZATION_ID \
         --source-display-name='Security Health Analytics Custom'
         

The display output should resemble the following. In the example, `SOURCE_ID` is a server-assigned ID for security sources.
         
         description: ...
         displayName: Security Health Analytics Custom
         name: organizations/ORGANIZATION_ID/sources/SOURCE_ID
         

  3. To list all findings generated by your custom modules, run the following command:
         
         [gcloud scc findings list](https://docs.cloud.google.com/sdk/gcloud/reference/scc/findings/list) ORGANIZATION_ID --source=SOURCE_ID
         

  4. To list findings for a specific custom module, run the following command:
         
         gcloud scc findings list ORGANIZATION_ID --source=SOURCE_ID --filter="category=\"MODULE_NAME\""
         




## What's next

You can manage findings generated by custom modules like all findings in Security Command Center. For instructions, see the following information:

  * [Work with findings in the Google Cloud console](https://docs.cloud.google.com/security-command-center/docs/how-to-work-with-findings-in-the-dashboard)
  * [Annotate findings with security marks](https://docs.cloud.google.com/security-command-center/docs/how-to-security-marks-findings)
  * [Setting up finding notifications](https://docs.cloud.google.com/security-command-center/docs/how-to-notifications)
  * [Exporting Security Command Center data](https://docs.cloud.google.com/security-command-center/docs/how-to-export-data)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
