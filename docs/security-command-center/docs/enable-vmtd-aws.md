---
url: https://docs.cloud.google.com/security-command-center/docs/enable-vmtd-aws/
title: Enable VM Threat Detection for AWS \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:31:03.312383+00:00
---

# Enable VM Threat Detection for AWS  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/enable-vmtd-aws/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Enable VM Threat Detection for AWS Stay organized with collections  Save and categorize content based on your preferences. 

Enterprise (Deprecated) [service tier](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes how to set up and use [Virtual Machine Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-vm-threat-detection-overview) to [scan for malware](https://docs.cloud.google.com/security-command-center/docs/concepts-vm-threat-detection-overview#how-malware-detection-works) in the persistent disks of Amazon Elastic Compute Cloud (EC2) VMs.

To enable VM Threat Detection for AWS, you need to create an AWS IAM role on the AWS platform, enable the VM Threat Detection for AWS in Security Command Center, and then deploy a CloudFormation template on AWS.

## Before you begin

To enable the VM Threat Detection for use with AWS, you need certain IAM permissions and Security Command Center must be connected to AWS.

### Roles and permissions

To complete the setup of VM Threat Detection for AWS, you need to be granted roles with the necessary permissions in both Google Cloud and AWS.

#### Google Cloud roles

Make sure that you have the following role or roles on the organization: **Security Center Admin Editor** (`roles/securitycenter.adminEditor`) 

#### Check for the roles

  1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=organizationId)
  2. Select the organization. 
  3. In the **Principal** column, find all rows that identify you or a group that you're included in. To learn which groups you're included in, contact your administrator. 

  4. For all rows that specify or include you, check the **Role** column to see whether the list of roles includes the required roles. 



#### Grant the roles

  1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=organizationId)
  2. Select the organization. 
  3. Click person_add **Grant access**. 
  4. In the **New principals** field, enter your user identifier. This is typically the email address for a Google Account.

  5. Click **Select a role** , then search for the role. 
  6. To grant additional roles, click add **Add another role** and add each additional role. 
  7. Click **Save**. 



#### AWS roles

In Amazon Web Services (AWS), an AWS administrative user must create the AWS account that you need for enabling scans. You assign this role later when you install the CloudFormation template on AWS.

  * To create a role for VM Threat Detection in AWS, follow the steps in [Create a role for an AWS service (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html#roles-creatingrole-service-console).

Note the following:

    * For **service or use case** , select **lambda**.
    * Add the following permission policies: 
      * `AmazonSSMManagedInstanceCore`
      * `AWSLambdaBasicExecutionRole`
      * `AWSLambdaVPCAccessExecutionRole`
    * Save the policy and then re-open it. Click Add Permission > **Create Inline policy**.
    * Create a permission policy for the AWS role: 
      1. Follow the instructions to modify and copy the permissions policy: [Role policy for Vulnerability Assessment for AWS and VM Threat Detection](https://docs.cloud.google.com/security-command-center/docs/vulnerability-assessment-aws-role-policy).
      2. Enter the policy into the JSON editor in AWS.
    * For trust relationships, add the following JSON entry to any existing statement array:
          
          {
            "Version": "2012-10-17",
            "Statement": [
              {
                "Sid": "Statement1 or replace with a unique statementId",
                "Effect": "Allow",
                "Principal": {
                  "Service": "cloudformation.amazonaws.com"
                },
                "Action": "sts:AssumeRole"
              }
            ]
          }
          




### Confirm Security Command Center is connected to AWS

VM Threat Detection requires access to the inventory of AWS resources that Cloud Asset Inventory maintains when you create an AWS connector.

If a connection is not already established, you are required to set one up when you enable VM Threat Detection for AWS.

To set up a connection, [create an AWS connector](https://docs.cloud.google.com/security-command-center/docs/connect-scc-to-aws).

## Enable VM Threat Detection for AWS in Security Command Center

VM Threat Detection for AWS must be enabled on Google Cloud at the organization level.

### Console

  1. In the Google Cloud console, go to the **Virtual Machine Threat Detection Service Enablement** page.

[Go to Service Enablement](https://console.cloud.google.com/projectselector2/security/command-center/config/services/vm-threat-detection/enablement?supportedpurview=project,folder,organizationId)

  2. Select your organization.

  3. Click the **Amazon Web Services** tab.

  4. In the **Service Enablement** section, in the **Status** field, select **Enable**.

  5. In the **AWS connector** section, verify that the status displays **AWS Connector added**.

If the status displays **No AWS connector added** , click **Add AWS connector**. Complete the steps in [Connect to AWS for configuration and resource data collection](https://docs.cloud.google.com/security-command-center/docs/connect-scc-to-aws) before you go to the next step. 




### gcloud

The [`gcloud scc manage services update`](https://docs.cloud.google.com/sdk/gcloud/reference/scc/manage/services/update) command updates the state of a Security Command Center service or module. 

Before using any of the command data below, make the following replacements: 

  * `ORGANIZATION_ID`: the numeric identifier of the organization 
  * `NEW_STATE`: `ENABLED` to enable VM Threat Detection for AWS; `DISABLED` to disable VM Threat Detection for AWS 



Execute the [`gcloud scc manage services update`](https://docs.cloud.google.com/sdk/gcloud/reference/scc/manage/services/update) command: 

#### Linux, macOS, or Cloud Shell
    
    
    gcloud scc manage services update vm-threat-detection-aws \
        --organization=ORGANIZATION_ID \
        --enablement-state=NEW_STATE

#### Windows (PowerShell)
    
    
    gcloud scc manage services update vm-threat-detection-aws `
        --organization=ORGANIZATION_ID `
        --enablement-state=NEW_STATE

#### Windows (cmd.exe)
    
    
    gcloud scc manage services update vm-threat-detection-aws ^
        --organization=ORGANIZATION_ID ^
        --enablement-state=NEW_STATE

You should receive a response similar to the following:
    
    
    effectiveEnablementState: ENABLED
    intendedEnablementState: ENABLED
    modules:
      MALWARE_DISK_SCAN_YARA_AWS:
        effectiveEnablementState: ENABLED
        intendedEnablementState: ENABLED
    name: organizations/1234567890/locations/global/securityCenterServices/vm-threat-detection-aws
    updateTime: '2025-03-21T18:45:52.033110465Z'
    

### REST

The Security Command Center Management API's `[organizations.locations.securityCenterServices.patch](https://docs.cloud.google.com/security-command-center/docs/reference/security-center-management/rest/v1/organizations.locations.securityCenterServices/patch)` method updates the state of a Security Command Center service or module. 

Before using any of the request data, make the following replacements: 

  * `QUOTA_PROJECT`: the project ID to use for billing and quota tracking. 
  * `ORGANIZATION_ID`: the numeric identifier of the organization 
  * `NEW_STATE`: `ENABLED` to enable VM Threat Detection for AWS; `DISABLED` to disable VM Threat Detection for AWS 



HTTP method and URL: 
    
    
    PATCH https://securitycentermanagement.googleapis.com/v1/organizations/ORGANIZATION_ID/locations/global/securityCenterServices/vm-threat-detection-aws?updateMask=intendedEnablementState

Request JSON body: 
    
    
    {
      "intendedEnablementState": "NEW_STATE"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: QUOTA_PROJECT" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://securitycentermanagement.googleapis.com/v1/organizations/ORGANIZATION_ID/locations/global/securityCenterServices/vm-threat-detection-aws?updateMask=intendedEnablementState"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "QUOTA_PROJECT" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://securitycentermanagement.googleapis.com/v1/organizations/ORGANIZATION_ID/locations/global/securityCenterServices/vm-threat-detection-aws?updateMask=intendedEnablementState" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "organizations/1234567890/locations/global/securityCenterServices/vm-threat-detection-aws",
      "intendedEnablementState": "ENABLED",
      "effectiveEnablementState": "ENABLED",
      "modules": {
        "MALWARE_DISK_SCAN_YARA_AWS": {
          "intendedEnablementState": "ENABLED",
          "effectiveEnablementState": "ENABLED"
        }
      },
      "updateTime": "2025-03-21T18:45:52.033110465Z"
    }
    

If you have already enabled the Vulnerability Assessment for AWS service and have deployed the CloudFormation template as part of that feature, then you are done setting up VM Threat Detection for AWS.

Otherwise, wait six hours and then perform the next task: download the CloudFormation template.

## Download the CloudFormation template

Perform this task at least six hours after enabling VM Threat Detection for AWS.

**Note:** If you have already enabled the Vulnerability Assessment for AWS service and have deployed the CloudFormation template as part of that feature, then skip this task. No further actions are needed to set up VM Threat Detection for AWS.

  1. In the Google Cloud console, go to the **Virtual Machine Threat Detection Service Enablement** page.

[Go to Service Enablement](https://console.cloud.google.com/projectselector2/security/command-center/config/services/vm-threat-detection/enablement?supportedpurview=project,folder,organizationId)

  2. Select your organization.

  3. Click the **Amazon Web Services** tab.

  4. In the **Deploy CloudFormation template** section, click **Download CloudFormation template**. A JSON template is downloaded to your workstation. You need to deploy the template in each AWS account that you need to scan.




## Deploy the AWS CloudFormation template

Deploy the CloudFormation template at least six hours after [creating an AWS connector](https://docs.cloud.google.com/security-command-center/docs/connect-scc-to-aws).

For detailed information about how to deploy a CloudFormation template, see [Create a stack from the CloudFormation console](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.html) in the AWS documentation.

Keep the following in mind: * After the CloudFormation template is uploaded, enter a unique stack name. Don't modify any other parameters in the template. * For **Permissions** in the stack options, select the AWS role that you created previously. * After you deploy the CloudFormation template, the stack takes a few minutes to start running.

The status of the deployment is displayed in the AWS console. If the CloudFormation template fails to deploy, see Troubleshooting.

**Note:** If you disable VM Threat Detection and enable it again later, you might need to perform these steps again.

After scans start running, if any threats are detected, the corresponding findings are generated and displayed on the Security Command Center **Findings** page in the Google Cloud console. For more information, see [Review findings in the Google Cloud console](https://docs.cloud.google.com/security-command-center/docs/how-to-use-vm-threat-detection#findings-vmtd).

## Manage modules

This section describes how to enable or disable modules and view their settings.

### Enable or disable a module

After you enable or disable a module, it can take up to an hour for your changes to take effect.

For information about all VM Threat Detection threat findings and the modules that generate them, see [Threat findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vm-threat-detection-overview#threat_detection).

**Note:** If you disable Virtual Machine Threat Detection for AWS, Security Command Center also disables the individual Virtual Machine Threat Detection for AWS modules and stores their previous enablement states. If you re-enable Virtual Machine Threat Detection for AWS, Security Command Center restores the modules to their previous enablement states. 

### Console

If Virtual Machine Threat Detection for AWS is enabled, you can set the enablement state of its individual modules at the organization level.

  1. In the Google Cloud console, go to the **Modules** page.

[Go to Modules](https://console.cloud.google.com/projectselector2/security/command-center/config/services/vm-threat-detection/aws/modules?supportedpurview=organizationId)

  2. Select your organization.

  3. On the **Modules** tab, in the **Status** column, select the current status of the module that you want to enable or disable, and then select one of the following:

     * **Enable** : Enable the module.
     * **Disable** : Disable the module.



### gcloud

The [`gcloud scc manage services update`](https://docs.cloud.google.com/sdk/gcloud/reference/scc/manage/services/update) command updates the state of a Security Command Center service or module. 

Before using any of the command data below, make the following replacements: 

  * `RESOURCE_TYPE`: the type of resource to update (`organization`, `folder`, or `project`). 
  * `RESOURCE_ID`: the numeric identifier for the organization, folder, or project to update. For projects, you can also use the alphanumeric project ID. 
  * `MODULE_NAME`: the name of the module to enable or disable. For valid values, see [Threat findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vm-threat-detection-overview#threat_detection) that support AWS. 
  * `NEW_STATE`: `ENABLED` to enable the module; `DISABLED` to disable the module; or `INHERITED` to inherit the enablement status of the parent resource (valid only for projects and folders). 



Save the following content in a file called `request.json`: 
    
    
    {
      "MODULE_NAME": {
        "intendedEnablementState": "NEW_STATE"
      }
    }

Execute the [`gcloud scc manage services update`](https://docs.cloud.google.com/sdk/gcloud/reference/scc/manage/services/update) command: 

#### Linux, macOS, or Cloud Shell
    
    
    gcloud scc manage services update vm-threat-detection-aws \
        --RESOURCE_TYPE=RESOURCE_ID \
        --module-config-file=request.json

#### Windows (PowerShell)
    
    
    gcloud scc manage services update vm-threat-detection-aws `
        --RESOURCE_TYPE=RESOURCE_ID `
        --module-config-file=request.json

#### Windows (cmd.exe)
    
    
    gcloud scc manage services update vm-threat-detection-aws ^
        --RESOURCE_TYPE=RESOURCE_ID ^
        --module-config-file=request.json

You should receive a response similar to the following:
    
    
    effectiveEnablementState: ENABLED
    intendedEnablementState: ENABLED
    modules:
      MALWARE_DISK_SCAN_YARA_AWS:
        effectiveEnablementState: ENABLED
        intendedEnablementState: ENABLED
    name: organizations/1234567890/locations/global/securityCenterServices/vm-threat-detection-aws
    updateTime: '2025-03-21T18:45:52.033110465Z'
    

### REST

The Security Command Center Management API's `[RESOURCE_TYPE.locations.securityCenterServices.patch](https://docs.cloud.google.com/security-command-center/docs/reference/security-center-management/rest/v1/organizations.locations.securityCenterServices/patch)` method updates the state of a Security Command Center service or module. 

Before using any of the request data, make the following replacements: 

  * `RESOURCE_TYPE`: the type of resource to update (`organizations`, `folders`, or `projects`). 
  * `QUOTA_PROJECT`: the project ID to use for billing and quota tracking. 
  * `RESOURCE_ID`: the numeric identifier for the organization, folder, or project to update. For projects, you can also use the alphanumeric project ID. 
  * `MODULE_NAME`: the name of the module to enable or disable. For valid values, see [Threat findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vm-threat-detection-overview#threat_detection) that support AWS. 
  * `NEW_STATE`: `ENABLED` to enable the module; `DISABLED` to disable the module; or `INHERITED` to inherit the enablement status of the parent resource (valid only for projects and folders). 



HTTP method and URL: 
    
    
    PATCH https://securitycentermanagement.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/securityCenterServices/vm-threat-detection-aws?updateMask=modules

Request JSON body: 
    
    
    {
      "modules": {
        "MODULE_NAME": {
          "intendedEnablementState": "NEW_STATE"
        }
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: QUOTA_PROJECT" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://securitycentermanagement.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/securityCenterServices/vm-threat-detection-aws?updateMask=modules"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "QUOTA_PROJECT" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://securitycentermanagement.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/securityCenterServices/vm-threat-detection-aws?updateMask=modules" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "organizations/1234567890/locations/global/securityCenterServices/vm-threat-detection-aws",
      "intendedEnablementState": "ENABLED",
      "effectiveEnablementState": "ENABLED",
      "modules": {
        "MALWARE_DISK_SCAN_YARA_AWS": {
          "intendedEnablementState": "ENABLED",
          "effectiveEnablementState": "ENABLED"
        }
      },
      "updateTime": "2025-03-21T18:45:52.033110465Z"
    }
    

### View the settings of VM Threat Detection for AWS modules

For information about all VM Threat Detection threat findings and the modules that generate them, see [Threat findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vm-threat-detection-overview#threat_detection).

### Console

The Google Cloud console lets you view settings for VM Threat Detection modules at the organization level.

  1. In the Google Cloud console, go to the **Modules** page.

[Go to Modules](https://console.cloud.google.com/projectselector2/security/command-center/config/services/vm-threat-detection/aws/modules?supportedpurview=organizationId)

  2. Select your organization. 




### gcloud

The [`gcloud scc manage services describe`](https://docs.cloud.google.com/sdk/gcloud/reference/scc/manage/services/describe) command gets the state of a Security Command Center service or module. 

Before using any of the command data below, make the following replacements: 

  * `RESOURCE_TYPE`: the type of resource to get (`organization`, `folder`, or `project`) 
  * `RESOURCE_ID`: the numeric identifier for the organization, folder, or project to get. For projects, you can also use the alphanumeric project ID. 



Execute the [`gcloud scc manage services describe`](https://docs.cloud.google.com/sdk/gcloud/reference/scc/manage/services/describe) command: 

#### Linux, macOS, or Cloud Shell
    
    
    gcloud scc manage services describe vm-threat-detection-aws \
        --RESOURCE_TYPE=RESOURCE_ID

#### Windows (PowerShell)
    
    
    gcloud scc manage services describe vm-threat-detection-aws `
        --RESOURCE_TYPE=RESOURCE_ID

#### Windows (cmd.exe)
    
    
    gcloud scc manage services describe vm-threat-detection-aws ^
        --RESOURCE_TYPE=RESOURCE_ID

You should receive a response similar to the following:
    
    
    effectiveEnablementState: ENABLED
    intendedEnablementState: ENABLED
    modules:
      MALWARE_DISK_SCAN_YARA_AWS:
        effectiveEnablementState: ENABLED
        intendedEnablementState: ENABLED
    name: organizations/1234567890/locations/global/securityCenterServices/vm-threat-detection-aws
    updateTime: '2025-03-21T18:45:52.033110465Z'
    

### REST

The Security Command Center Management API's `[RESOURCE_TYPE.locations.securityCenterServices.get](https://docs.cloud.google.com/security-command-center/docs/reference/security-center-management/rest/v1/organizations.locations.securityCenterServices/patch)` method gets the state of a Security Command Center service or module. 

Before using any of the request data, make the following replacements: 

  * `RESOURCE_TYPE`: the type of resource to get (`organizations`, `folders`, or `projects`). 
  * `QUOTA_PROJECT`: the project ID to use for billing and quota tracking. 
  * `RESOURCE_ID`: the numeric identifier for the organization, folder, or project to get. For projects, you can also use the alphanumeric project ID. 



HTTP method and URL: 
    
    
    GET https://securitycentermanagement.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/securityCenterServices/vm-threat-detection-aws

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: QUOTA_PROJECT" \  
         "https://securitycentermanagement.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/securityCenterServices/vm-threat-detection-aws"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "QUOTA_PROJECT" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://securitycentermanagement.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/securityCenterServices/vm-threat-detection-aws" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "organizations/1234567890/locations/global/securityCenterServices/vm-threat-detection-aws",
      "intendedEnablementState": "ENABLED",
      "effectiveEnablementState": "ENABLED",
      "modules": {
        "MALWARE_DISK_SCAN_YARA_AWS": {
          "intendedEnablementState": "ENABLED",
          "effectiveEnablementState": "ENABLED"
        }
      },
      "updateTime": "2025-03-21T18:45:52.033110465Z"
    }
    

## Troubleshooting

If you enabled the VM Threat Detection service, but scans are not running, check the following:

  * Check that the AWS connector is properly set up.
  * Confirm that the CloudFormation template stack deployed completely. Its status in the AWS account should be `CREATION_COMPLETE`.



## What's next

  * Learn how to [use VM Threat Detection](https://docs.cloud.google.com/security-command-center/docs/how-to-use-vm-threat-detection).
  * Learn how to [respond to Compute Engine threat findings](https://docs.cloud.google.com/security-command-center/docs/respond-compute-engine-threats).
  * Refer to the [Threat findings index](https://docs.cloud.google.com/security-command-center/docs/threat-findings-index).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
