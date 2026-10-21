---
url: https://docs.cloud.google.com/assured-workloads/docs/create-new-project-fedramp-us-regions/
title: Create a new Assured Workloads folder \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:49:58.536135+00:00
---

# Create a new Assured Workloads folder  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/assured-workloads/docs/create-new-project-fedramp-us-regions/

The names for some Assured Workloads control packages have changed. For information about the name change, see [Control package renaming notice](https://docs.cloud.google.com/assured-workloads/docs/overview#name-change). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Assured Workloads ](https://docs.cloud.google.com/assured-workloads/docs)
  * [ Guides ](https://docs.cloud.google.com/assured-workloads/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create a new Assured Workloads folder

This page describes how to create a new Assured Workloads folder for each [control package](https://docs.cloud.google.com/assured-workloads/docs/control-packages).

For more information about Assured Workloads, see the [Assured Workloads overview](https://docs.cloud.google.com/assured-workloads/docs/overview).

## Select a control package

Select a control package to learn how to create an Assured Workloads folder:

Select a control packageData Boundary for CJISData Boundary for FedRAMP ModerateData Boundary for FedRAMP HighUS Data Boundary for Healthcare and Life SciencesUS Data Boundary for Healthcare and Life Sciences with SupportData Boundary for IL2Data Boundary for IL4Data Boundary for IL5Data Boundary for ITARData Boundary for IRS 1075Australia Data BoundaryAustralia Data Boundary and SupportBrazil Data BoundaryData Boundary for Canada Controlled GoodsData Boundary for Canada Protected BCanada Data BoundaryCanada Data Boundary and SupportChile Data BoundaryEU Data BoundaryEU Data Boundary and SupportEU Data Boundary with Access JustificationsHong Kong Data BoundaryIndia Data BoundaryIndonesia Data BoundaryIsrael Data BoundaryIsrael Data Boundary and SupportJapan Data BoundaryQatar Data BoundarySingapore Data BoundarySouth Africa Data BoundarySouth Korea Data BoundaryKingdom of Saudi Arabia Data Boundary with Access JustificationsSwitzerland Data BoundarySwitzerland Data Boundary with Access JustificationsTaiwan Data BoundaryUK Data BoundaryUS Data BoundaryUS Data Boundary and Support

  *   * ## Before you begin

If you haven't already, you must complete the following below to create an Assured Workloads folder for the [ Data Boundary for CJIS control package](https://docs.cloud.google.com/assured-workloads/docs/control-packages#cjis):

    1. Ensure that you understand [Assured Workloads concepts](https://docs.cloud.google.com/assured-workloads/docs/overview). 
    2. If [Access Transparency](https://docs.cloud.google.com/assured-workloads/docs/access-transparency) is not enabled on your organization, it will automatically be enabled when you create an Assured Workloads folder. Any projects you create or move into the folder will be configured to use Access Transparency. 
    3. Ensure that you understand [how to get support](https://docs.cloud.google.com/assured-workloads/docs/getting-support) for Assured Workloads. 
    4. Ensure that you understand the [additional cost](https://docs.cloud.google.com/assured-workloads/pricing) when using Data Boundary for CJIS in Assured Workloads. 
    5. [Set up Cloud Identity](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin) and [verify your domain](https://docs.cloud.google.com/identity/docs/verify-domain). 
    6. After Cloud Identity has been configured, [create an organization](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization). 

### Required IAM roles

To create an Assured Workloads folder, you must be granted the **Assured Workloads Administrator** (`roles/assuredworkloads.admin`) role, which contains the minimum IAM permissions to create and manage Assured Workloads folders.

## Create an Assured Workloads folder for Data Boundary for CJIS

    1. In the Google Cloud console, go to the **Assured Workloads** page. 

[ Go to Assured Workloads](https://console.cloud.google.com/compliance/assuredworkloads)

    2. If prompted, select your organization.
    3. Click add_box**CREATE** to go to the **Create an Assured Workloads folder** page.
    4. In the step to **Add folder details** : 
       * In **Folder name** , enter a unique name for the folder, such as `aw-my-folder-name`. The folder name must be a minimum of 4 characters in length and a maximum of 30, and can only contain letters, numbers, spaces, and hyphens. **Tip:** When you name your Assured Workloads folders, consider the following: 
         * To identify the folder as an Assured Workloads folder, include a prefix in its name (such as `aw-`). This identifier can help you locate the folder from a list of other resources. 
         * Do not include sensitive data or personally identifiable information (PII) in the folder name. 
       * In **Organization** , select the organization in which to create your folder. This location can't be changed later.
       * In **Folder location** , select the location in the resource hierarchy where the folder will be created. An Assured Workloads folder can be created as a child of an organization or of another folder.
       * Click **Next**.
    5. In the step to **Choose a control package option** , select **Regulatory Controls** from the drop-down menu.
    6. Select **Data Boundary for CJIS** from the drop-down menu. See [Control packages](https://docs.cloud.google.com/assured-workloads/docs/control-packages) to learn about other options.
    7. In **Select resource location** , choose the [location](https://docs.cloud.google.com/assured-workloads/docs/locations) where resource creation and usage will be enforced by the folder's [organization policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations). See [Resource locations supported services](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations-supported-services) for a list of all resources that can be restricted by the Resource Locations organization policy constraint, as some resources may be out of scope and unrestrictable. 
    8. Review the details about the control option you've selected, and click **Next**.
    9. (Optional) In the step to **Configure additional settings** , you can create a new project and a key ring for your [Customer Managed Encryption Keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek). No keys are created during this step, as Assured Workloads does not automatically create any cryptographic keys for you. See [Supporting compliance with key management](https://docs.cloud.google.com/assured-workloads/docs/key-management) for more information. **Note** : Data Boundary for CJIS does not require using CMEK; you can click **Next** to skip this step.
    10. In the step to **Review and create folder** , review the details about your new Assured Workloads folder and ensure that they are correct. Then, click **Create Folder**. 

After completing the steps above, Assured Workloads creates the following resources:

    * An Assured Workloads folder, which enforces security controls on [supported Google Cloud products](https://docs.cloud.google.com/assured-workloads/docs/supported-products) to adhere with the Data Boundary for CJIS control package. These controls include setting an organization policy that [restricts resource usage](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources) to only those supported products, and allows creating or using resources only in [allowed locations](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations). 
    * If you chose to create one, a CMEK project that contains the configured CMEK key ring. **Note** : Folder creation does not automatically create keys for you. After creating the folder, you must create an encryption key before adding any resources. See [Create and obtain a CMEK key](https://docs.cloud.google.com/assured-workloads/docs/create-and-obtain-cmek) to learn more. 

## Use your new Assured Workloads folder

To start using your Assured Workloads folder, it's important that you put the resources that you want to be compliant with Data Boundary for CJIS in the new folder. You can create projects inside of the folder along with [resources for supported products](https://docs.cloud.google.com/assured-workloads/docs/supported-products), or [migrate existing projects](https://docs.cloud.google.com/assured-workloads/docs/migrate-workload). Some possible next steps include the following:

    * Create a new project in the newly-created Assured Workloads folder, and then create a Compute Engine VM inside the project. The VM instance will be configured to meet the compliance requirements for Data Boundary for CJIS. 
    * [Analyze an existing project](https://docs.cloud.google.com/assured-workloads/docs/migrate-workload) that you want to make compliant with Data Boundary for CJIS, and make any of the required changes. Then, move the project to the newly-created Assured Workloads folder. 

### Enabling BigQuery in your folder

If your selected control package lists BigQuery as a supported service, BigQuery is supported, but it isn't automatically enabled when you create a new Assured Workloads folder due to an internal configuration process. This process normally finishes in ten minutes, but can take much longer in some circumstances. To check whether the process is finished and to enable BigQuery, complete the following steps:  

    1. In the Google Cloud console, go to the **Assured Workloads** page. 

[ Go to Assured Workloads](https://console.cloud.google.com/compliance/assuredworkloads)

    2. Select your new Assured Workloads folder from the list.
    3. On the **Folder Details** page in the **Allowed services** section, click **Review Available Updates**.
    4. In the **Allowed services** pane, review the services to be added to the [Resource Usage Restriction](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources) organization policy for the folder. If BigQuery services are listed, click **Allow Services** to add them.  
  
If BigQuery services are not listed, wait for the internal process to complete. If the services are not listed within 12 hours of folder creation, contact [Cloud Customer Care](https://docs.cloud.google.com/support). 

After the enablement process is completed, you can use BigQuery in your Assured Workloads folder.

Gemini in BigQuery is not supported by Assured Workloads.

  * ## Before you begin

If you haven't already, you must complete the following below to create an Assured Workloads folder for the [ Data Boundary for FedRAMP Moderate control package](https://docs.cloud.google.com/assured-workloads/docs/control-packages#fedramp-moderate):

    1. Ensure that you understand [Assured Workloads concepts](https://docs.cloud.google.com/assured-workloads/docs/overview). 
    2. If [Access Transparency](https://docs.cloud.google.com/assured-workloads/docs/access-transparency) is not enabled on your organization, it will automatically be enabled when you create an Assured Workloads folder. Any projects you create or move into the folder will be configured to use Access Transparency. 
    3. Ensure that you understand [how to get support](https://docs.cloud.google.com/assured-workloads/docs/getting-support) for Assured Workloads. 
    4. [Set up Cloud Identity](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin) and [verify your domain](https://docs.cloud.google.com/identity/docs/verify-domain). 
    5. After Cloud Identity has been configured, [create an organization](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization). 

### Required IAM roles

To create an Assured Workloads folder, you must be granted the **Assured Workloads Administrator** (`roles/assuredworkloads.admin`) role, which contains the minimum IAM permissions to create and manage Assured Workloads folders.

## Create an Assured Workloads folder for Data Boundary for FedRAMP Moderate

    1. In the Google Cloud console, go to the **Assured Workloads** page. 

[ Go to Assured Workloads](https://console.cloud.google.com/compliance/assuredworkloads)

    2. If prompted, select your organization.
    3. Click add_box**CREATE** to go to the **Create an Assured Workloads folder** page.
    4. In the step to **Add folder details** : 
       * In **Folder name** , enter a unique name for the folder, such as `aw-my-folder-name`. The folder name must be a minimum of 4 characters in length and a maximum of 30, and can only contain letters, numbers, spaces, and hyphens. **Tip:** When you name your Assured Workloads folders, consider the following: 
         * To identify the folder as an Assured Workloads folder, include a prefix in its name (such as `aw-`). This identifier can help you locate the folder from a list of other resources. 
         * Do not include sensitive data or personally identifiable information (PII) in the folder name. 
       * In **Organization** , select the organization in which to create your folder. This location can't be changed later.
       * In **Folder location** , select the location in the resource hierarchy where the folder will be created. An Assured Workloads folder can be created as a child of an organization or of another folder.
       * Click **Next**.
    5. In the step to **Choose a control package option** , select **Regulatory Controls** from the drop-down menu.
    6. Select **Data Boundary for FedRAMP Moderate** from the drop-down menu. See [Control packages](https://docs.cloud.google.com/assured-workloads/docs/control-packages) to learn about other options.
    7. In **Select resource location** , choose the [location](https://docs.cloud.google.com/assured-workloads/docs/locations) where resource creation and usage will be enforced by the folder's [organization policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations). See [Resource locations supported services](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations-supported-services) for a list of all resources that can be restricted by the Resource Locations organization policy constraint, as some resources may be out of scope and unrestrictable. 
    8. Review the details about the control option you've selected, and click **Next**.
    9. (Optional) In the step to **Configure additional settings** , you can create a new project and a key ring for your [Customer Managed Encryption Keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek). No keys are created during this step, as Assured Workloads does not automatically create any cryptographic keys for you. See [Supporting compliance with key management](https://docs.cloud.google.com/assured-workloads/docs/key-management) for more information. **Note** : Data Boundary for FedRAMP Moderate does not require using CMEK; you can click **Next** to skip this step.
    10. In the step to **Review and create folder** , review the details about your new Assured Workloads folder and ensure that they are correct. Then, click **Create Folder**. 

After completing the steps above, Assured Workloads creates the following resources:

    * An Assured Workloads folder, which enforces security controls on [supported Google Cloud products](https://docs.cloud.google.com/assured-workloads/docs/supported-products) to adhere with the Data Boundary for FedRAMP Moderate control package. These controls include setting an organization policy that [restricts resource usage](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources) to only those supported products, and allows creating or using resources only in [allowed locations](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations). 
    * If you chose to create one, a CMEK project that contains the configured CMEK key ring. **Note** : Folder creation does not automatically create keys for you. After creating the folder, you must create an encryption key before adding any resources. See [Create and obtain a CMEK key](https://docs.cloud.google.com/assured-workloads/docs/create-and-obtain-cmek) to learn more. 

## Use your new Assured Workloads folder

To start using your Assured Workloads folder, it's important that you put the resources that you want to be compliant with Data Boundary for FedRAMP Moderate in the new folder. You can create projects inside of the folder along with [resources for supported products](https://docs.cloud.google.com/assured-workloads/docs/supported-products), or [migrate existing projects](https://docs.cloud.google.com/assured-workloads/docs/migrate-workload). Some possible next steps include the following:

    * Create a new project in the newly-created Assured Workloads folder, and then create a Compute Engine VM inside the project. The VM instance will be configured to meet the compliance requirements for Data Boundary for FedRAMP Moderate. 
    * [Analyze an existing project](https://docs.cloud.google.com/assured-workloads/docs/migrate-workload) that you want to make compliant with Data Boundary for FedRAMP Moderate, and make any of the required changes. Then, move the project to the newly-created Assured Workloads folder. 

### Enabling BigQuery in your folder

If your selected control package lists BigQuery as a supported service, BigQuery is supported, but it isn't automatically enabled when you create a new Assured Workloads folder due to an internal configuration process. This process normally finishes in ten minutes, but can take much longer in some circumstances. To check whether the process is finished and to enable BigQuery, complete the following steps:  

    1. In the Google Cloud console, go to the **Assured Workloads** page. 

[ Go to Assured Workloads](https://console.cloud.google.com/compliance/assuredworkloads)

    2. Select your new Assured Workloads folder from the list.
    3. On the **Folder Details** page in the **Allowed services** section, click **Review Available Updates**.
    4. In the **Allowed services** pane, review the services to be added to the [Resource Usage Restriction](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources) organization policy for the folder. If BigQuery services are listed, click **Allow Services** to add them.  
  
If BigQuery services are not listed, wait for the internal process to complete. If the services are not listed within 12 hours of folder creation, contact [Cloud Customer Care](https://docs.cloud.google.com/support). 

After the enablement process is completed, you can use BigQuery in your Assured Workloads folder.

Gemini in BigQuery is not supported by Assured Workloads.

  * ## Before you begin

If you haven't already, you must complete the following below to create an Assured Workloads folder for the [ Data Boundary for FedRAMP High control package](https://docs.cloud.google.com/assured-workloads/docs/control-packages#fedramp-high):

    1. Ensure that you understand [Assured Workloads concepts](https://docs.cloud.google.com/assured-workloads/docs/overview). 
    2. If [Access Transparency](https://docs.cloud.google.com/assured-workloads/docs/access-transparency) is not enabled on your organization, it will automatically be enabled when you create an Assured Workloads folder. Any projects you create or move into the folder will be configured to use Access Transparency. 
    3. Ensure that you understand [how to get support](https://docs.cloud.google.com/assured-workloads/docs/getting-support) for Assured Workloads. 
    4. Ensure that you understand the [additional cost](https://docs.cloud.google.com/assured-workloads/pricing) when using Data Boundary for FedRAMP High in Assured Workloads. 
    5. [Set up Cloud Identity](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin) and [verify your domain](https://docs.cloud.google.com/identity/docs/verify-domain). 
    6. After Cloud Identity has been configured, [create an organization](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization). 

### Required IAM roles

To create an Assured Workloads folder, you must be granted the **Assured Workloads Administrator** (`roles/assuredworkloads.admin`) role, which contains the minimum IAM permissions to create and manage Assured Workloads folders.

## Create an Assured Workloads folder for Data Boundary for FedRAMP High

    1. In the Google Cloud console, go to the **Assured Workloads** page. 

[ Go to Assured Workloads](https://console.cloud.google.com/compliance/assuredworkloads)

    2. If prompted, select your organization.
    3. Click add_box**CREATE** to go to the **Create an Assured Workloads folder** page.
    4. In the step to **Add folder details** : 
       * In **Folder name** , enter a unique name for the folder, such as `aw-my-folder-name`. The folder name must be a minimum of 4 characters in length and a maximum of 30, and can only contain letters, numbers, spaces, and hyphens. **Tip:** When you name your Assured Workloads folders, consider the following: 
         * To identify the folder as an Assured Workloads folder, include a prefix in its name (such as `aw-`). This identifier can help you locate the folder from a list of other resources. 
         * Do not include sensitive data or personally identifiable information (PII) in the folder name. 
       * In **Organization** , select the organization in which to create your folder. This location can't be changed later.
       * In **Folder location** , select the location in the resource hierarchy where the folder will be created. An Assured Workloads folder can be created as a child of an organization or of another folder.
       * Click **Next**.
    5. In the step to **Choose a control package option** , select **Regulatory Controls** from the drop-down menu.
    6. Select **Data Boundary for FedRAMP High** from the drop-down menu. See [Control packages](https://docs.cloud.google.com/assured-workloads/docs/control-packages) to learn about other options.
    7. In **Select resource location** , choose the [location](https://docs.cloud.google.com/assured-workloads/docs/locations) where resource creation and usage will be enforced by the folder's [organization policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations). See [Resource locations supported services](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations-supported-services) for a list of all resources that can be restricted by the Resource Locations organization policy constraint, as some resources may be out of scope and unrestrictable. 
    8. Review the details about the control option you've selected, and click **Next**.
    9. (Optional) In the step to **Configure additional settings** , you can create a new project and a key ring for your [Customer Managed Encryption Keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek). No keys are created during this step, as Assured Workloads does not automatically create any cryptographic keys for you. See [Supporting compliance with key management](https://docs.cloud.google.com/assured-workloads/docs/key-management) for more information. **Note** : Data Boundary for FedRAMP High does not require using CMEK; you can click **Next** to skip this step.
    10. In the step to **Review and create folder** , review the details about your new Assured Workloads folder and ensure that they are correct. Then, click **Create Folder**. 

After completing the steps above, Assured Workloads creates the following resources:

    * An Assured Workloads folder, which enforces security controls on [supported Google Cloud products](https://docs.cloud.google.com/assured-workloads/docs/supported-products) to adhere with the Data Boundary for FedRAMP High control package. These controls include setting an organization policy that [restricts resource usage](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources) to only those supported products, and allows creating or using resources only in [allowed locations](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations). 
    * If you chose to create one, a CMEK project that contains the configured CMEK key ring. **Note** : Folder creation does not automatically create keys for you. After creating the folder, you must create an encryption key before adding any resources. See [Create and obtain a CMEK key](https://docs.cloud.google.com/assured-workloads/docs/create-and-obtain-cmek) to learn more. 

## Use your new Assured Workloads folder

To start using your Assured Workloads folder, it's important that you put the resources that you want to be compliant with Data Boundary for FedRAMP High in the new folder. You can create projects inside of the folder along with [resources for supported products](https://docs.cloud.google.com/assured-workloads/docs/supported-products), or [migrate existing projects](https://docs.cloud.google.com/assured-workloads/docs/migrate-workload). Some possible next steps include the following:

    * Create a new project in the newly-created Assured Workloads folder, and then create a Compute Engine VM inside the project. The VM instance will be configured to meet the compliance requirements for Data Boundary for FedRAMP High. 
    * [Analyze an existing project](https://docs.cloud.google.com/assured-workloads/docs/migrate-workload) that you want to make compliant with Data Boundary for FedRAMP High, and make any of the required changes. Then, move the project to the newly-created Assured Workloads folder. 

### Enabling BigQuery in your folder

If your selected control package lists BigQuery as a supported service, BigQuery is supported, but it isn't automatically enabled when you create a new Assured Workloads folder due to an internal configuration process. This process normally finishes in ten minutes, but can take much longer in some circumstances. To check whether the process is finished and to enable BigQuery, complete the following steps:  

    1. In the Google Cloud console, go to the **Assured Workloads** page. 

[ Go to Assured Workloads](https://console.cloud.google.com/compliance/assuredworkloads)

    2. Select your new Assured Workloads folder from the list.
    3. On the **Folder Details** page in the **Allowed services** section, click **Review Available Updates**.
    4. In the **Allowed services** pane, review the services to be added to the [Resource Usage Restriction](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources) organization policy for the folder. If BigQuery services are listed, click **Allow Services** to add them.  
  
If BigQuery services are not listed, wait for the internal process to complete. If the services are not listed within 12 hours of folder creation, contact [Cloud Customer Care](https://docs.cloud.google.com/support). 

After the enablement process is completed, you can use BigQuery in your Assured Workloads folder.

Gemini in BigQuery is not supported by Assured Workloads.

  * ## Before you begin

If you haven't already, you must complete the following below to create an Assured Workloads folder for the [ US Data Boundary for Healthcare and Life Sciences control package](https://docs.cloud.google.com/assured-workloads/docs/control-packages#hcls):

    1. Ensure that you understand [Assured Workloads concepts](https://docs.cloud.google.com/assured-workloads/docs/overview). 
    2. If [Access Transparency](https://docs.cloud.google.com/assured-workloads/docs/access-transparency) is not enabled on your organization, it will automatically be enabled when you create an Assured Workloads folder. Any projects you create or move into the folder will be configured to use Access Transparency. 
    3. Ensure that you understand [how to get support](https://docs.cloud.google.com/assured-workloads/docs/getting-support) for Assured Workloads. 
    4. [Set up Cloud Identity](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin) and [verify your domain](https://docs.cloud.google.com/identity/docs/verify-domain). 
    5. After Cloud Identity has been configured, [create an organization](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization). 

### Required IAM roles

To create an Assured Workloads folder, you must be granted the **Assured Workloads Administrator** (`roles/assuredworkloads.admin`) role, which contains the minimum IAM permissions to create and manage Assured Workloads folders.

## Create an Assured Workloads folder for US Data Boundary for Healthcare and Life Sciences

    1. In the Google Cloud console, go to the **Assured Workloads** page. 

[ Go to Assured Workloads](https://console.cloud.google.com/compliance/assuredworkloads)

    2. If prompted, select your organization.
    3. Click add_box**CREATE** to go to the **Create an Assured Workloads folder** page.
    4. In the step to **Add folder details** : 
       * In **Folder name** , enter a unique name for the folder, such as `aw-my-folder-name`. The folder name must be a minimum of 4 characters in length and a maximum of 30, and can only contain letters, numbers, spaces, and hyphens. **Tip:** When you name your Assured Workloads folders, consider the following: 
         * To identify the folder as an Assured Workloads folder, include a prefix in its name (such as `aw-`). This identifier can help you locate the folder from a list of other resources. 
         * Do not include sensitive data or personally identifiable information (PII) in the folder name. 
       * In **Organization** , select the organization in which to create your folder. This location can't be changed later.
       * In **Folder location** , select the location in the resource hierarchy where the folder will be created. An Assured Workloads folder can be created as a child of an organization or of another folder.
       * Click **Next**.
    5. In the step to **Choose a control package option** , select **Regulatory Controls** from the drop-down menu.
    6. Select **US Data Boundary for Healthcare and Life Sciences** from the drop-down menu. See [Control packages](https://docs.cloud.google.com/assured-workloads/docs/control-packages) to learn about other options.
    7. In **Select resource location** , choose the [location](https://docs.cloud.google.com/assured-workloads/docs/locations) where resource creation and usage will be enforced by the folder's [organization policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations). See [Resource locations supported services](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations-supported-services) for a list of all resources that can be restricted by the Resource Locations organization policy constraint, as some resources may be out of scope and unrestrictable. 
    8. Review the details about the control option you've selected, and click **Next**.
    9. (Optional) In the step to **Configure additional settings** , you can create a new project and a key ring for your [Customer Managed Encryption Keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek). No keys are created during this step, as Assured Workloads does not automatically create any cryptographic keys for you. See [Supporting compliance with key management](https://docs.cloud.google.com/assured-workloads/docs/key-management) for more information. **Note** : US Data Boundary for Healthcare and Life Sciences does not require using CMEK; you can click **Next** to skip this step.
    10. In the step to **Review and create folder** , review the details about your new Assured Workloads folder and ensure that they are correct. Then, click **Create Folder**. 

After completing the steps above, Assured Workloads creates the following resources:

    * An Assured Workloads folder, which enforces security controls on [supported Google Cloud products](https://docs.cloud.google.com/assured-workloads/docs/supported-products) to adhere with the US Data Boundary for Healthcare and Life Sciences control package. These controls include setting an organization policy that [restricts resource usage](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources) to only those supported products, and allows creating or using resources only in [allowed locations](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations). 
    * If you chose to create one, a CMEK project that contains the configured CMEK key ring. **Note** : Folder creation does not automatically create keys for you. After creating the folder, you must create an encryption key before adding any resources. See [Create and obtain a CMEK key](https://docs.cloud.google.com/assured-workloads/docs/create-and-obtain-cmek) to learn more. 

## Use your new Assured Workloads folder

To start using your Assured Workloads folder, it's important that you put the resources that you want to be compliant with US Data Boundary for Healthcare and Life Sciences in the new folder. You can create projects inside of the folder along with [resources for supported products](https://docs.cloud.google.com/assured-workloads/docs/supported-products), or [migrate existing projects](https://docs.cloud.google.com/assured-workloads/docs/migrate-workload). Some possible next steps include the following:

    * Create a new project in the newly-created Assured Workloads folder, and then create a Compute Engine VM inside the project. The VM instance will be configured to meet the compliance requirements for US Data Boundary for Healthcare and Life Sciences. 
    * [Analyze an existing project](https://docs.cloud.google.com/assured-workloads/docs/migrate-workload) that you want to make compliant with US Data Boundary for Healthcare and Life Sciences, and make any of the required changes. Then, move the project to the newly-created Assured Workloads folder. 

### Enabling BigQuery in your folder

If your selected control package lists BigQuery as a supported service, BigQuery is supported, but it isn't automatically enabled when you create a new Assured Workloads folder due to an internal configuration process. This process normally finishes in ten minutes, but can take much longer in some circumstances. To check whether the process is finished and to enable BigQuery, complete the following steps:  

    1. In the Google Cloud console, go to the **Assured Workloads** page. 

[ Go to Assured Workloads](https://console.cloud.google.com/compliance/assuredworkloads)

    2. Select your new Assured Workloads folder from the list.
    3. On the **Folder Details** page in the **Allowed services** section, click **Review Available Updates**.
    4. In the **Allowed services** pane, review the services to be added to the [Resource Usage Restriction](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources) organization policy for the folder. If BigQuery services are listed, click **Allow Services** to add them.  
  
If BigQuery services are not listed, wait for the internal process to complete. If the services are not listed within 12 hours of folder creation, contact [Cloud Customer Care](https://docs.cloud.google.com/support). 

After the enablement process is completed, you can use BigQuery in your Assured Workloads folder.

Gemini in BigQuery is not supported by Assured Workloads.

  * ## Before you begin

If you haven't already, you must complete the following below to create an Assured Workloads folder for the [ US Data Boundary for Healthcare and Life Sciences with Support control package](https://docs.cloud.google.com/assured-workloads/docs/control-packages#hcls-support):

    1. Ensure that you understand [Assured Workloads concepts](https://docs.cloud.google.com/assured-workloads/docs/overview). 
    2. If [Access Transparency](https://docs.cloud.google.com/assured-workloads/docs/access-transparency) is not enabled on your organization, it will automatically be enabled when you create an Assured Workloads folder. Any projects you create or move into the folder will be configured to use Access Transparency. 
    3. Ensure that you understand [how to get support](https://docs.cloud.google.com/assured-workloads/docs/getting-support) for Assured Workloads. 
    4. Ensure that you understand the [additional cost](https://docs.cloud.google.com/assured-workloads/pricing) when using US Data Boundary for Healthcare and Life Sciences with Support in Assured Workloads. 
    5. [Set up Cloud Identity](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin) and [verify your domain](https://docs.cloud.google.com/identity/docs/verify-domain). 
    6. After Cloud Identity has been configured, [create an organization](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization). 

### Required IAM roles

To create an Assured Workloads folder, you must be granted the **Assured Workloads Administrator** (`roles/assuredworkloads.admin`) role, which contains the minimum IAM permissions to create and manage Assured Workloads folders.

## Create an Assured Workloads folder for US Data Boundary for Healthcare and Life Sciences with Support

    1. In the Google Cloud console, go to the **Assured Workloads** page. 

[ Go to Assured Workloads](https://console.cloud.google.com/compliance/assuredworkloads)

    2. If prompted, select your organization.
    3. Click add_box**CREATE** to go to the **Create an Assured Workloads folder** page.
    4. In the step to **Add folder details** : 
       * In **Folder name** , enter a unique name for the folder, such as `aw-my-folder-name`. The folder name must be a minimum of 4 characters in length and a maximum of 30, and can only contain letters, numbers, spaces, and hyphens. **Tip:** When you name your Assured Workloads folders, consider the following: 
         * To identify the folder as an Assured Workloads folder, include a prefix in its name (such as `aw-`). This identifier can help you locate the folder from a list of other resources. 
         * Do not include sensitive data or personally identifiable information (PII) in the folder name. 
       * In **Organization** , select the organization in which to create your folder. This location can't be changed later.
       * In **Folder location** , select the location in the resource hierarchy where the folder will be created. An Assured Workloads folder can be created as a child of an organization or of another folder.
       * Click **Next**.
    5. In the step to **Choose a control package option** , select **Regulatory Controls** from the drop-down menu.
    6. Select **US Data Boundary for Healthcare and Life Sciences with Support** from the drop-down menu. See [Control packages](https://docs.cloud.google.com/assured-workloads/docs/control-packages) to learn about other options.
    7. In **Select resource location** , choose the [location](https://docs.cloud.google.com/assured-workloads/docs/locations) where resource creation and usage will be enforced by the folder's [organization policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations). See [Resource locations supported services](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations-supported-services) for a list of all resources that can be restricted by the Resource Locations organization policy constraint, as some resources may be out of scope and unrestrictable. 
    8. Review the details about the control option you've selected, and click **Next**.
    9. (Optional) In the step to **Configure additional settings** , you can create a new project and a key ring for your [Customer Managed Encryption Keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek). No keys are created during this step, as Assured Workloads does not automatically create any cryptographic keys for you. See [Supporting compliance with key management](https://docs.cloud.google.com/assured-workloads/docs/key-management) for more information. **Note** : US Data Boundary for Healthcare and Life Sciences with Support does not require using CMEK; you can click **Next** to skip this step.
    10. In the step to **Review and create folder** , review the details about your new Assured Workloads folder and ensure that they are correct. Then, click **Create Folder**. 

After completing the steps above, Assured Workloads creates the following resources:

    * An Assured Workloads folder, which enforces security controls on [supported Google Cloud products](https://docs.cloud.google.com/assured-workloads/docs/supported-products) to adhere with the US Data Boundary for Healthcare and Life Sciences with Support control package. These controls include setting an organization policy that [restricts resource usage](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources) to only those supported products, and allows creating or using resources only in [allowed locations](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations). 
    * If you chose to create one, a CMEK project that contains the configured CMEK key ring. **Note** : Folder creation does not automatically create keys for you. After creating the folder, you must create an encryption key before adding any resources. See [Create and obtain a CMEK key](https://docs.cloud.google.com/assured-workloads/docs/create-and-obtain-cmek) to learn more. 

## Use your new Assured Workloads folder

To start using your Assured Workloads folder, it's important that you put the resources that you want to be compliant with US Data Boundary for Healthcare and Life Sciences with Support in the new folder. You can create projects inside of the folder along with [resources for supported products](https://docs.cloud.google.com/assured-workloads/docs/supported-products), or [migrate existing projects](https://docs.cloud.google.com/assured-workloads/docs/migrate-workload). Some possible next steps include the following:

    * Create a new project in the newly-created Assured Workloads folder, and then create a Compute Engine VM inside the project. The VM instance will be configured to meet the compliance requirements for US Data Boundary for Healthcare and Life Sciences with Support. 
    * [Analyze an existing project](https://docs.cloud.google.com/assured-workloads/docs/migrate-workload) that you want to make compliant with US Data Boundary for Healthcare and Life Sciences with Support, and make any of the required changes. Then, move the project to the newly-created Assured Workloads folder. 

### Enabling BigQuery in your folder

If your selected control package lists BigQuery as a supported service, BigQuery is supported, but it isn't automatically enabled when you create a new Assured Workloads folder due to an internal configuration process. This process normally finishes in ten minutes, but can take much longer in some circumstances. To check whether the process is finished and to enable BigQuery, complete the following steps:  

    1. In the Google Cloud console, go to the **Assured Workloads** page. 

[ Go to Assured Workloads](https://console.cloud.google.com/compliance/assuredworkloads)

    2. Select your new Assured Workloads folder from the list.
    3. On the **Folder Details** page in the **Allowed services** section, click **Review Available Updates**.
    4. In the **Allowed services** pane, review the services to be added to the [Resource Usage Restriction](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources) organization policy for the folder. If BigQuery services are listed, click **Allow Services** to add them.  
  
If BigQuery services are not listed, wait for the internal process to complete. If the services are not listed within 12 hours of folder creation, contact [Cloud Customer Care](https://docs.cloud.google.com/support). 

After the enablement process is completed, you can use BigQuery in your Assured Workloads folder.

Gemini in BigQuery is not supported by Assured Workloads.

  * ## Before you begin

If you haven't already, you must complete the following below to create an Assured Workloads folder for the [ Data Boundary for IL2 control package](https://docs.cloud.google.com/assured-workloads/docs/control-packages#il2):

    1. Ensure that you understand [Assured Workloads concepts](https://docs.cloud.google.com/assured-workloads/docs/overview). 
    2. If [Access Transparency](https://docs.cloud.google.com/assured-workloads/docs/access-transparency) is not enabled on your organization, it will automatically be enabled when you create an Assured Workloads folder. Any projects you create or move into the folder will be configured to use Access Transparency. 
    3. Ensure that you understand [how to get support](https://docs.cloud.google.com/assured-workloads/docs/getting-support) for Assured Workloads. 
    4. Ensure that you understand the [additional cost](https://docs.cloud.google.com/assured-workloads/pricing) when using Data Boundary for IL2 in Assured Workloads. 
    5. [Set up Cloud Identity](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin) and [verify your domain](https://docs.cloud.google.com/identity/docs/verify-domain). 
    6. After Cloud Identity has been configured, [create an organization](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization). 

### Required IAM roles

To create an Assured Workloads folder, you must be granted the **Assured Workloads Administrator** (`roles/assuredworkloads.admin`) role, which contains the minimum IAM permissions to create and manage Assured Workloads folders.

## Create an Assured Workloads folder for Data Boundary for IL2

    1. In the Google Cloud console, go to the **Assured Workloads** page. 

[ Go to Assured Workloads](https://console.cloud.google.com/compliance/assuredworkloads)

    2. If prompted, select your organization.
    3. Click add_box**CREATE** to go to the **Create an Assured Workloads folder** page.
    4. In the step to **Add folder details** : 
       * In **Folder name** , enter a unique name for the folder, such as `aw-my-folder-name`. The folder name must be a minimum of 4 characters in length and a maximum of 30, and can only contain letters, numbers, spaces, and hyphens. **Tip:** When you name your Assured Workloads folders, consider the following: 
         * To identify the folder as an Assured Workloads folder, include a prefix in its name (such as `aw-`). This identifier can help you locate the folder from a list of other resources. 
         * Do not include sensitive data or personally identifiable information (PII) in the folder name. 
       * In **Organization** , select the organization in which to create your folder. This location can't be changed later.
       * In **Folder location** , select the location in the resource hierarchy where the folder will be created. An Assured Workloads folder can be created as a child of an organization or of another folder.
       * Click **Next**.
    5. In the step to **Choose a control package option** , select **Regulatory Controls** from the drop-down menu.
    6. Select **Data Boundary for IL2** from the drop-down menu. See [Control packages](https://docs.cloud.google.com/assured-workloads/docs/control-packages) to learn about other options.
    7. In **Select resource location** , choose the [location](https://docs.cloud.google.com/assured-workloads/docs/locations) where resource creation and usage will be enforced by the folder's [organization policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations). See [Resource locations supported services](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations-supported-services) for a list of all resources that can be restricted by the Resource Locations organization policy constraint, as some resources may be out of scope and unrestrictable. 
    8. Review the details about the control option you've selected, and click **Next**.
    9. (Optional) In the step to **Configure additional settings** , you can create a new project and a key ring for your [Customer Managed Encryption Keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek). No keys are created during this step, as Assured Workloads does not automatically create any cryptographic keys for you. See [Supporting compliance with key management](https://docs.cloud.google.com/assured-workloads/docs/key-management) for more information. **Note** : Data Boundary for IL2 does not require using CMEK; you can click **Next** to skip this step.
    10. In the step to **Review and create folder** , review the details about your new Assured Workloads folder and ensure that they are correct. Then, click **Create Folder**. 

After completing the steps above, Assured Workloads creates the following resources:

    * An Assured Workloads folder, which enforces security controls on [supported Google Cloud products](https://docs.cloud.google.com/assured-workloads/docs/supported-products) to adhere with the Data Boundary for IL2 control package. These controls include setting an organization policy that [restricts resource usage](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources) to only those supported products, and allows creating or using resources only in [allowed locations](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations). 
    * If you chose to create one, a CMEK project that contains the configured CMEK key ring. **Note** : Folder creation does not automatically create keys for you. After creating the folder, you must create an encryption key before adding any resources. See [Create and obtain a CMEK key](https://docs.cloud.google.com/assured-workloads/docs/create-and-obtain-cmek) to learn more. 

## Use your new Assured Workloads folder

To start using your Assured Workloads folder, it's important that you put the resources that you want to be compliant with Data Boundary for IL2 in the new folder. You can create projects inside of the folder along with [resources for supported products](https://docs.cloud.google.com/assured-workloads/docs/supported-products), or [migrate existing projects](https://docs.cloud.google.com/assured-workloads/docs/migrate-workload). Some possible next steps include the following:

    * Create a new project in the newly-created Assured Workloads folder, and then create a Compute Engine VM inside the project. The VM instance will be configured to meet the compliance requirements for Data Boundary for IL2. 
    * [Analyze an existing project](https://docs.cloud.google.com/assured-workloads/docs/migrate-workload) that you want to make compliant with Data Boundary for IL2, and make any of the required changes. Then, move the project to the newly-created Assured Workloads folder. 

### Enabling BigQuery in your folder

If your selected control package lists BigQuery as a supported service, BigQuery is supported, but it isn't automatically enabled when you create a new Assured Workloads folder due to an internal configuration process. This process normally finishes in ten minutes, but can take much longer in some circumstances. To check whether the process is finished and to enable BigQuery, complete the following steps:  

    1. In the Google Cloud console, go to the **Assured Workloads** page. 

[ Go to Assured Workloads](https://console.cloud.google.com/compliance/assuredworkloads)

    2. Select your new Assured Workloads folder from the list.
    3. On the **Folder Details** page in the **Allowed services** section, click **Review Available Updates**.
    4. In the **Allowed services** pane, review the services to be added to the [Resource Usage Restriction](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources) organization policy for the folder. If BigQuery services are listed, click **Allow Services** to add them.  
  
If BigQuery services are not listed, wait for the internal process to complete. If the services are not listed within 12 hours of folder creation, contact [Cloud Customer Care](https://docs.cloud.google.com/support). 

After the enablement process is completed, you can use BigQuery in your Assured Workloads folder.

Gemini in BigQuery is not supported by Assured Workloads.

  * ## Before you begin

If you haven't already, you must complete the following below to create an Assured Workloads folder for the [ Data Boundary for IL4 control package](https://docs.cloud.google.com/assured-workloads/docs/control-packages#il4):

    1. Ensure that you understand [Assured Workloads concepts](https://docs.cloud.google.com/assured-workloads/docs/overview). 
    2. If [Access Transparency](https://docs.cloud.google.com/assured-workloads/docs/access-transparency) is not enabled on your organization, it will automatically be enabled when you create an Assured Workloads folder. Any projects you create or move into the folder will be configured to use Access Transparency. 
    3. Ensure that you understand [how to get support](https://docs.cloud.google.com/assured-workloads/docs/getting-support) for Assured Workloads. 
    4. Ensure that you understand the [additional cost](https://docs.cloud.google.com/assured-workloads/pricing) when using Data Boundary for IL4 in Assured Workloads. 
    5. [Set up Cloud Identity](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin) and [verify your domain](https://docs.cloud.google.com/identity/docs/verify-domain). 
    6. After Cloud Identity has been configured, [create an organization](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization). 

### Required IAM roles

To create an Assured Workloads folder, you must be granted the **Assured Workloads Administrator** (`roles/assuredworkloads.admin`) role, which contains the minimum IAM permissions to create and manage Assured Workloads folders.

## Create an Assured Workloads folder for Data Boundary for IL4

    1. In the Google Cloud console, go to the **Assured Workloads** page. 

[ Go to Assured Workloads](https://console.cloud.google.com/compliance/assuredworkloads)

    2. If prompted, select your organization.
    3. Click add_box**CREATE** to go to the **Create an Assured Workloads folder** page.
    4. In the step to **Add folder details** : 
       * In **Folder name** , enter a unique name for the folder, such as `aw-my-folder-name`. The folder name must be a minimum of 4 characters in length and a maximum of 30, and can only contain letters, numbers, spaces, and hyphens. **Tip:** When you name your Assured Workloads folders, consider the following: 
         * To identify the folder as an Assured Workloads folder, include a prefix in its name (such as `aw-`). This identifier can help you locate the folder from a list of other resources. 
         * Do not include sensitive data or personally identifiable information (PII) in the folder name. 
       * In **Organization** , select the organization in which to create your folder. This location can't be changed later.
       * In **Folder location** , select the location in the resource hierarchy where the folder will be created. An Assured Workloads folder can be created as a child of an organization or of another folder.
       * Click **Next**.
    5. In the step to **Choose a control package option** , select **Regulatory Controls** from the drop-down menu.
    6. Select **Data Boundary for IL4** from the drop-down menu. See [Control packages](https://docs.cloud.google.com/assured-workloads/docs/control-packages) to learn about other options.
    7. In **Select resource location** , choose the [location](https://docs.cloud.google.com/assured-workloads/docs/locations) where resource creation and usage will be enforced by the folder's [organization policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations). See [Resource locations supported services](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations-supported-services) for a list of all resources that can be restricted by the Resource Locations organization policy constraint, as some resources may be out of scope and unrestrictable. 
    8. Review the details about the control option you've selected, and click **Next**.
    9. (Optional) In the step to **Configure additional settings** , you can create a new project and a key ring for your [Customer Managed Encryption Keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek). No keys are created during this step, as Assured Workloads does not automatically create any cryptographic keys for you. See [Supporting compliance with key management](https://docs.cloud.google.com/assured-workloads/docs/key-management) for more information. **Note** : Data Boundary for IL4 does not require using CMEK; you can click **Next** to skip this step.
    10. In the step to **Review and create folder** , review the details about your new Assured Workloads folder and ensure that they are correct. Then, click **Create Folder**. 

After completing the steps above, Assured Workloads creates the following resources:

    * An Assured Workloads folder, which enforces security controls on [supported Google Cloud products](https://docs.cloud.google.com/assured-workloads/docs/supported-products) to adhere with the Data Boundary for IL4 control package. These controls include setting an organization policy that [restricts resource usage](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources) to only those supported products, and allows creating or using resources only in [allowed locations](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations). 
    * If you chose to create one, a CMEK project that contains the configured CMEK key ring. **Note** : Folder creation does not automatically create keys for you. After creating the folder, you must create an encryption key before adding any resources. See [Create and obtain a CMEK key](https://docs.cloud.google.com/assured-workloads/docs/create-and-obtain-cmek) to learn more. 

## Use your new Assured Workloads folder

To start using your Assured Workloads folder, it's important that you put the resources that you want to be compliant with Data Boundary for IL4 in the new folder. You can create projects inside of the folder along with [resources for supported products](https://docs.cloud.google.com/assured-workloads/docs/supported-products), or [migrate existing projects](https://docs.cloud.google.com/assured-workloads/docs/migrate-workload). Some possible next steps include the following:

    * Create a new project in the newly-created Assured Workloads folder, and then create a Compute Engine VM inside the project. The VM instance will be configured to meet the compliance requirements for Data Boundary for IL4. 
    * [Analyze an existing project](https://docs.cloud.google.com/assured-workloads/docs/migrate-workload) that you want to make compliant with Data Boundary for IL4, and make any of the required changes. Then, move the project to the newly-created Assured Workloads folder. 

### Enabling BigQuery in your folder

If your selected control package lists BigQuery as a supported service, BigQuery is supported, but it isn't automatically enabled when you create a new Assured Workloads folder due to an internal configuration process. This process normally finishes in ten minutes, but can take much longer in some circumstances. To check whether the process is finished and to enable BigQuery, complete the following steps:  

    1. In the Google Cloud console, go to the **Assured Workloads** page. 

[ Go to Assured Workloads](https://console.cloud.google.com/compliance/assuredworkloads)

    2. Select your new Assured Workloads folder from the list.
    3. On the **Folder Details** page in the **Allowed services** section, click **Review Available Updates**.
    4. In the **Allowed services** pane, review the services to be added to the [Resource Usage Restriction](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources) organization policy for the folder. If BigQuery services are listed, click **Allow Services** to add them.  
  
If BigQuery services are not listed, wait for the internal process to complete. If the services are not listed within 12 hours of folder creation, contact [Cloud Customer Care](https://docs.cloud.google.com/support). 

After the enablement process is completed, you can use BigQuery in your Assured Workloads folder.

Gemini in BigQuery is not supported by Assured Workloads.

  * ## Before you begin

If you haven't already, you must complete the following below to create an Assured Workloads folder for the [ Data Boundary for IL5 control package](https://docs.cloud.google.com/assured-workloads/docs/control-packages#il5):

    1. Ensure that you understand [Assured Workloads concepts](https://docs.cloud.google.com/assured-workloads/docs/overview). 
    2. If [Access Transparency](https://docs.cloud.google.com/assured-workloads/docs/access-transparency) is not enabled on your organization, it will automatically be enabled when you create an Assured Workloads folder. Any projects you create or move into the folder will be configured to use Access Transparency. 
    3. Ensure that you understand [how to get support](https://docs.cloud.google.com/assured-workloads/docs/getting-support) for Assured Workloads. 
    4. Ensure that you understand the [additional cost](https://docs.cloud.google.com/assured-workloads/pricing) when using Data Boundary for IL5 in Assured Workloads. 
    5. [Set up Cloud Identity](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin) and [verify your domain](https://docs.cloud.google.com/identity/docs/verify-domain). 
    6. After Cloud Identity has been configured, [create an organization](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization). 

### Required IAM roles

To create an Assured Workloads folder, you must be granted the **Assured Workloads Administrator** (`roles/assuredworkloads.admin`) role, which contains the minimum IAM permissions to create and manage Assured Workloads folders.

## Create an Assured Workloads folder for Data Boundary for IL5

    1. In the Google Cloud console, go to the **Assured Workloads** page. 

[ Go to Assured Workloads](https://console.cloud.google.com/compliance/assuredworkloads)

    2. If prompted, select your organization.
    3. Click add_box**CREATE** to go to the **Create an Assured Workloads folder** page.
    4. In the step to **Add folder details** : 
       * In **Folder name** , enter a unique name for the folder, such as `aw-my-folder-name`. The folder name must be a minimum of 4 characters in length and a maximum of 30, and can only contain letters, numbers, spaces, and hyphens. **Tip:** When you name your Assured Workloads folders, consider the following: 
         * To identify the folder as an Assured Workloads folder, include a prefix in its name (such as `aw-`). This identifier can help you locate the folder from a list of other resources. 
         * Do not include sensitive data or personally identifiable information (PII) in the folder name. 
       * In **Organization** , select the organization in which to create your folder. This location can't be changed later.
       * In **Folder location** , select the location in the resource hierarchy where the folder will be created. An Assured Workloads folder can be created as a child of an organization or of another folder.
       * Click **Next**.
    5. In the step to **Choose a control package option** , select **Regulatory Controls** from the drop-down menu.
    6. Select **Data Boundary for IL5** from the drop-down menu. See [Control packages](https://docs.cloud.google.com/assured-workloads/docs/control-packages) to learn about other options.
    7. In **Select resource location** , choose the [location](https://docs.cloud.google.com/assured-workloads/docs/locations) where resource creation and usage will be enforced by the folder's [organization policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations). See [Resource locations supported services](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations-supported-services) for a list of all resources that can be restricted by the Resource Locations organization policy constraint, as some resources may be out of scope and unrestrictable. 
    8. Review the details about the control option you've selected, and click **Next**.
    9. (Optional) In the step to **Configure additional settings** , you can create a new project and a key ring for your [Customer Managed Encryption Keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek). No keys are created during this step, as Assured Workloads does not automatically create any cryptographic keys for you. See [Supporting compliance with key management](https://docs.cloud.google.com/assured-workloads/docs/key-management) for more information. **Note** : Data Boundary for IL5 does not require using CMEK; you can click **Next** to skip this step.
    10. In the step to **Review and create folder** , review the details about your new Assured Workloads folder and ensure that they are correct. Then, click **Create Folder**. 

After completing the steps above, Assured Workloads creates the following resources:

    * An Assured Workloads folder, which enforces security controls on [supported Google Cloud products](https://docs.cloud.google.com/assured-workloads/docs/supported-products) to adhere with the Data Boundary for IL5 control package. These controls include setting an organization policy that [restricts resource usage](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources) to only those supported products, and allows creating or using resources only in [allowed locations](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations). 
    * If you chose to create one, a CMEK project that contains the configured CMEK key ring. **Note** : Folder creation does not automatically create keys for you. After creating the folder, you must create an encryption key before adding any resources. See [Create and obtain a CMEK key](https://docs.cloud.google.com/assured-workloads/docs/create-and-obtain-cmek) to learn more. 

## Use your new Assured Workloads folder

To start using your Assured Workloads folder, it's important that you put the resources that you want to be compliant with Data Boundary for IL5 in the new folder. You can create projects inside of the folder along with [resources for supported products](https://docs.cloud.google.com/assured-workloads/docs/supported-products), or [migrate existing projects](https://docs.cloud.google.com/assured-workloads/docs/migrate-workload). Some possible next steps include the following:

    * Create a new project in the newly-created Assured Workloads folder, and then create a Compute Engine VM inside the project. The VM instance will be configured to meet the compliance requirements for Data Boundary for IL5. 
    * [Analyze an existing project](https://docs.cloud.google.com/assured-workloads/docs/migrate-workload) that you want to make compliant with Data Boundary for IL5, and make any of the required changes. Then, move the project to the newly-created Assured Workloads folder. 

### Enabling BigQuery in your folder

If your selected control package lists BigQuery as a supported service, BigQuery is supported, but it isn't automatically enabled when you create a new Assured Workloads folder due to an internal configuration process. This process normally finishes in ten minutes, but can take much longer in some circumstances. To check whether the process is finished and to enable BigQuery, complete the following steps:  

    1. In the Google Cloud console, go to the **Assured Workloads** page. 

[ Go to Assured Workloads](https://console.cloud.google.com/compliance/assuredworkloads)

    2. Select your new Assured Workloads folder from the list.
    3. On the **Folder Details** page in the **Allowed services** section, click **Review Available Updates**.
    4. In the **Allowed services** pane, review the services to be added to the [Resource Usage Restriction](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources) organization policy for the folder. If BigQuery services are listed, click **Allow Services** to add them.  
  
If BigQuery services are not listed, wait for the internal process to complete. If the services are not listed within 12 hours of folder creation, contact [Cloud Customer Care](https://docs.cloud.google.com/support). 

After the enablement process is completed, you can use BigQuery in your Assured Workloads folder.

Gemini in BigQuery is not supported by Assured Workloads.

  * ## Before you begin

If you haven't already, you must complete the following below to create an Assured Workloads folder for the [ Data Boundary for ITAR control package](https://docs.cloud.google.com/assured-workloads/docs/control-packages#itar):

    1. Ensure that you understand [Assured Workloads concepts](https://docs.cloud.google.com/assured-workloads/docs/overview). 
    2. If [Access Transparency](https://docs.cloud.google.com/assured-workloads/docs/access-transparency) is not enabled on your organization, it will automatically be enabled when you create an Assured Workloads folder. Any projects you create or move into the folder will be configured to use Access Transparency. 
    3. Ensure that you understand [how to get support](https://docs.cloud.google.com/assured-workloads/docs/getting-support) for Assured Workloads. 
    4. Ensure that you understand the [additional cost](https://docs.cloud.google.com/assured-workloads/pricing) when using Data Boundary for ITAR in Assured Workloads. 
    5. [Set up Cloud Identity](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin) and [verify your domain](https://docs.cloud.google.com/identity/docs/verify-domain). 
    6. After Cloud Identity has been configured, [create an organization](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization). 

### Required IAM roles

To create an Assured Workloads folder, you must be granted the **Assured Workloads Administrator** (`roles/assuredworkloads.admin`) role, which contains the minimum IAM permissions to create and manage Assured Workloads folders.

## Create an Assured Workloads folder for Data Boundary for ITAR

    1. In the Google Cloud console, go to the **Assured Workloads** page. 

[ Go to Assured Workloads](https://console.cloud.google.com/compliance/assuredworkloads)

    2. If prompted, select your organization.
    3. Click add_box**CREATE** to go to the **Create an Assured Workloads folder** page.
    4. In the step to **Add folder details** : 
       * In **Folder name** , enter a unique name for the folder, such as `aw-my-folder-name`. The folder name must be a minimum of 4 characters in length and a maximum of 30, and can only contain letters, numbers, spaces, and hyphens. **Tip:** When you name your Assured Workloads folders, consider the following: 
         * To identify the folder as an Assured Workloads folder, include a prefix in its name (such as `aw-`). This identifier can help you locate the folder from a list of other resources. 
         * Do not include sensitive data or personally identifiable information (PII) in the folder name. 
       * In **Organization** , select the organization in which to create your folder. This location can't be changed later.
       * In **Folder location** , select the location in the resource hierarchy where the folder will be created. An Assured Workloads folder can be created as a child of an organization or of another folder.
       * Click **Next**.
    5. In the step to **Choose a control package option** , select **Regulatory Controls** from the drop-down menu.
    6. Select **Data Boundary for ITAR** from the drop-down menu. See [Control packages](https://docs.cloud.google.com/assured-workloads/docs/control-packages) to learn about other options.
    7. In **Select resource location** , choose the [location](https://docs.cloud.google.com/assured-workloads/docs/locations) where resource creation and usage will be enforced by the folder's [organization policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations). See [Resource locations supported services](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations-supported-services) for a list of all resources that can be restricted by the Resource Locations organization policy constraint, as some resources may be out of scope and unrestrictable. 
    8. Review the details about the control option you've selected, and click **Next**.
    9. (Optional) In the step to **Configure additional settings** , you can create a new project and a key ring for your [Customer Managed Encryption Keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek). No keys are created during this step, as Assured Workloads does not automatically create any cryptographic keys for you. See [Supporting compliance with key management](https://docs.cloud.google.com/assured-workloads/docs/key-management) for more information. **Note** : Data Boundary for ITAR does not require using CMEK; you can click **Next** to skip this step.
    10. In the step to **Review and create folder** , review the details about your new Assured Workloads folder and ensure that they are correct. Then, click **Create Folder**. 

After completing the steps above, Assured Workloads creates the following resources:

    * An Assured Workloads folder, which enforces security controls on [supported Google Cloud products](https://docs.cloud.google.com/assured-workloads/docs/supported-products) to adhere with the Data Boundary for ITAR control package. These controls include setting an organization policy that [restricts resource usage](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources) to only those supported products, and allows creating or using resources only in [allowed locations](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations). 
    * If you chose to create one, a CMEK project that contains the configured CMEK key ring. **Note** : Folder creation does not automatically create keys for you. After creating the folder, you must create an encryption key before adding any resources. See [Create and obtain a CMEK key](https://docs.cloud.google.com/assured-workloads/docs/create-and-obtain-cmek) to learn more. 

## Use your new Assured Workloads folder

To start using your Assured Workloads folder, it's important that you put the resources that you want to be compliant with Data Boundary for ITAR in the new folder. You can create projects inside of the folder along with [resources for supported products](https://docs.cloud.google.com/assured-workloads/docs/supported-products), or [migrate existing projects](https://docs.cloud.google.com/assured-workloads/docs/migrate-workload). Some possible next steps include the following:

    * Create a new project in the newly-created Assured Workloads folder, and then create a Compute Engine VM inside the project. The VM instance will be configured to meet the compliance requirements for Data Boundary for ITAR. 
    * [Analyze an existing project](https://docs.cloud.google.com/assured-workloads/docs/migrate-workload) that you want to make compliant with Data Boundary for ITAR, and make any of the required changes. Then, move the project to the newly-created Assured Workloads folder. 

### Enabling BigQuery in your folder

If your selected control package lists BigQuery as a supported service, BigQuery is supported, but it isn't automatically enabled when you create a new Assured Workloads folder due to an internal configuration process. This process normally finishes in ten minutes, but can take much longer in some circumstances. To check whether the process is finished and to enable BigQuery, complete the following steps:  

    1. In the Google Cloud console, go to the **Assured Workloads** page. 

[ Go to Assured Workloads](https://console.cloud.google.com/compliance/assuredworkloads)

    2. Select your new Assured Workloads folder from the list.
    3. On the **Folder Details** page in the **Allowed services** section, click **Review Available Updates**.
    4. In the **Allowed services** pane, review the services to be added to the [Resource Usage Restriction](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources) organization policy for the folder. If BigQuery services are listed, click **Allow Services** to add them.  
  
If BigQuery services are not listed, wait for the internal process to complete. If the services are not listed within 12 hours of folder creation, contact [Cloud Customer Care](https://docs.cloud.google.com/support). 

After the enablement process is completed, you can use BigQuery in your Assured Workloads folder.

Gemini in BigQuery is not supported by Assured Workloads.

  * ## Before you begin

If you haven't already, you must complete the following below to create an Assured Workloads folder for the [ Data Boundary for IRS Publication 1075 control package](https://docs.cloud.google.com/assured-workloads/docs/control-packages#irs-1075):

    1. Ensure that you understand [Assured Workloads concepts](https://docs.cloud.google.com/assured-workloads/docs/overview). 
    2. If [Access Transparency](https://docs.cloud.google.com/assured-workloads/docs/access-transparency) is not enabled on your organization, it will automatically be enabled when you create an Assured Workloads folder. Any projects you create or move into the folder will be configured to use Access Transparency. 
    3. Ensure that you understand [how to get support](https://docs.cloud.google.com/assured-workloads/docs/getting-support) for Assured Workloads. 
    4. Ensure that you understand the [additional cost](https://docs.cloud.google.com/assured-workloads/pricing) when using Data Boundary for IRS Publication 1075 in Assured Workloads. 
    5. [Set up Cloud Identity](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin) and [verify your domain](https://docs.cloud.google.com/identity/docs/verify-domain). 
    6. After Cloud Identity has been configured, [create an organization](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization). 

### Required IAM roles

To create an Assured Workloads folder, you must be granted the **Assured Workloads Administrator** (`roles/assuredworkloads.admin`) role, which contains the minimum IAM permissions to create and manage Assured Workloads folders.

## Create an Assured Workloads folder for Data Boundary for IRS Publication 1075

    1. In the Google Cloud console, go to the **Assured Workloads** page. 

[ Go to Assured Workloads](https://console.cloud.google.com/compliance/assuredworkloads)

    2. If prompted, select your organization.
    3. Click add_box**CREATE** to go to the **Create an Assured Workloads folder** page.
    4. In the step to **Add folder details** : 
       * In **Folder name** , enter a unique name for the folder, such as `aw-my-folder-name`. The folder name must be a minimum of 4 characters in length and a maximum of 30, and can only contain letters, numbers, spaces, and hyphens. **Tip:** When you name your Assured Workloads folders, consider the following: 
         * To identify the folder as an Assured Workloads folder, include a prefix in its name (such as `aw-`). This identifier can help you locate the folder from a list of other resources. 
         * Do not include sensitive data or personally identifiable information (PII) in the folder name. 
       * In **Organization** , select the organization in which to create your folder. This location can't be changed later.
       * In **Folder location** , select the location in the resource hierarchy where the folder will be created. An Assured Workloads folder can be created as a child of an organization or of another folder.
       * Click **Next**.
    5. In the step to **Choose a control package option** , select **Regulatory Controls** from the drop-down menu.
    6. Select **Data Boundary for IRS Publication 1075** from the drop-down menu. See [Control packages](https://docs.cloud.google.com/assured-workloads/docs/control-packages) to learn about other options.
    7. In **Select resource location** , choose the [location](https://docs.cloud.google.com/assured-workloads/docs/locations) where resource creation and usage will be enforced by the folder's [organization policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations). See [Resource locations supported services](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations-supported-services) for a list of all resources that can be restricted by the Resource Locations organization policy constraint, as some resources may be out of scope and unrestrictable. 
    8. Review the details about the control option you've selected, and click **Next**.
    9. (Optional) In the step to **Configure additional settings** , you can create a new project and a key ring for your [Customer Managed Encryption Keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek). No keys are created during this step, as Assured Workloads does not automatically create any cryptographic keys for you. See [Supporting compliance with key management](https://docs.cloud.google.com/assured-workloads/docs/key-management) for more information. **Note** : Data Boundary for IRS Publication 1075 does not require using CMEK; you can click **Next** to skip this step.
    10. In the step to **Review and create folder** , review the details about your new Assured Workloads folder and ensure that they are correct. Then, click **Create Folder**. 

After completing the steps above, Assured Workloads creates the following resources:

    * An Assured Workloads folder, which enforces security controls on [supported Google Cloud products](https://docs.cloud.google.com/assured-workloads/docs/supported-products) to adhere with the Data Boundary for IRS Publication 1075 control package. These controls include setting an organization policy that [restricts resource usage](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources) to only those supported products, and allows creating or using resources only in [allowed locations](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations). 
    * If you chose to create one, a CMEK project that contains the configured CMEK key ring. **Note** : Folder creation does not automatically create keys for you. After creating the folder, you must create an encryption key before adding any resources. See [Create and obtain a CMEK key](https://docs.cloud.google.com/assured-workloads/docs/create-and-obtain-cmek) to learn more. 

## Use your new Assured Workloads folder

To start using your Assured Workloads folder, it's important that you put the resources that you want to be compliant with Data Boundary for IRS Publication 1075 in the new folder. You can create projects inside of the folder along with [resources for supported products](https://docs.cloud.google.com/assured-workloads/docs/supported-products), or [migrate existing projects](https://docs.cloud.google.com/assured-workloads/docs/migrate-workload). Some possible next steps include the following:

    * Create a new project in the newly-created Assured Workloads folder, and then create a Compute Engine VM inside the project. The VM instance will be configured to meet the compliance requirements for Data Boundary for IRS Publication 1075. 
    * [Analyze an existing project](https://docs.cloud.google.com/assured-workloads/docs/migrate-workload) that you want to make compliant with Data Boundary for IRS Publication 1075, and make any of the required changes. Then, move the project to the newly-created Assured Workloads folder. 

### Enabling BigQuery in your folder

If your selected control package lists BigQuery as a supported service, BigQuery is supported, but it isn't automatically enabled when you create a new Assured Workloads folder due to an internal configuration process. This process normally finishes in ten minutes, but can take much longer in some circumstances. To check whether the process is finished and to enable BigQuery, complete the following steps:  

    1. In the Google Cloud console, go to the **Assured Workloads** page. 

[ Go to Assured Workloads](https://console.cloud.google.com/compliance/assuredworkloads)

    2. Select your new Assured Workloads folder from the list.
    3. On the **Folder Details** page in the **Allowed services** section, click **Review Available Updates**.
    4. In the **Allowed services** pane, review the services to be added to the [Resource Usage Restriction](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources) organization policy for the folder. If BigQuery services are listed, click **Allow Services** to add them.  
  
If BigQuery services are not listed, wait for the internal process to complete. If the services are not listed within 12 hours of folder creation, contact [Cloud Customer Care](https://docs.cloud.google.com/support). 

After the enablement process is completed, you can use BigQuery in your Assured Workloads folder.

Gemini in BigQuery is not supported by Assured Workloads.

  * ## Before you begin

If you haven't already, you must complete the following below to create an Assured Workloads folder for the [ Australia Data Boundary control package](https://docs.cloud.google.com/assured-workloads/docs/control-packages#au-data-boundary):

    1. Ensure that you understand [Assured Workloads concepts](https://docs.cloud.google.com/assured-workloads/docs/overview). 
    2. If [Access Transparency](https://docs.cloud.google.com/assured-workloads/docs/access-transparency) is not enabled on your organization, it will automatically be enabled when you create an Assured Workloads folder. Any projects you create or move into the folder will be configured to use Access Transparency. 
    3. Ensure that you understand [how to get support](https://docs.cloud.google.com/assured-workloads/docs/getting-support) for Assured Workloads. 
    4. [Set up Cloud Identity](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin) and [verify your domain](https://docs.cloud.google.com/identity/docs/verify-domain). 
    5. After Cloud Identity has been configured, [create an organization](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization). 

### Required IAM roles

To create an Assured Workloads folder, you must be granted the **Assured Workloads Administrator** (`roles/assuredworkloads.admin`) role, which contains the minimum IAM permissions to create and manage Assured Workloads folders.

## Create an Assured Workloads folder for Australia Data Boundary

    1. In the Google Cloud console, go to the **Assured Workloads** page. 

[ Go to Assured Workloads](https://console.cloud.google.com/compliance/assuredworkloads)

    2. If prompted, select your organization.
    3. Click add_box**CREATE** to go to the **Create an Assured Workloads folder** page.
    4. In the step to **Add folder details** : 
       * In **Folder name** , enter a unique name for the folder, such as `aw-my-folder-name`. The folder name must be a minimum of 4 characters in length and a maximum of 30, and can only contain letters, numbers, spaces, and hyphens. **Tip:** When you name your Assured Workloads folders, consider the following: 
         * To identify the folder as an Assured Workloads folder, include a prefix in its name (such as `aw-`). This identifier can help you locate the folder from a list of other resources. 
         * Do not include sensitive data or personally identifiable information (PII) in the folder name. 
       * In **Organization** , select the organization in which to create your folder. This location can't be changed later.
       * In **Folder location** , select the location in the resource hierarchy where the folder will be created. An Assured Workloads folder can be created as a child of an organization or of another folder.
       * Click **Next**.
    5. In the step to **Choose a control package option** , select **Regional Controls** from the drop-down menu.
    6. Select **Australia Data Boundary** from the drop-down menu. See [Control packages](https://docs.cloud.google.com/assured-workloads/docs/control-packages) to learn about other options.
    7. In **Select resource location** , choose the [location](https://docs.cloud.google.com/assured-workloads/docs/locations) where resource creation and usage will be enforced by the folder's [organization policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations). See [Resource locations supported services](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations-supported-services) for a list of all resources that can be restricted by the Resource Locations organization policy constraint, as some resources may be out of scope and unrestrictable. 
    8. Review the details about the control option you've selected, and click **Next**.
    9. (Optional) In the step to **Configure additional settings** , you can create a new project and a key ring for your [Customer Managed Encryption Keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek). No keys are created during this step, as Assured Workloads does not automatically create any cryptographic keys for you. See [Supporting compliance with key management](https://docs.cloud.google.com/assured-workloads/docs/key-management) for more information. **Note** : Australia Data Boundary does not require using CMEK; you can click **Next** to skip this step.
    10. In the step to **Review and create folder** , review the details about your new Assured Workloads folder and ensure that they are correct. Then, click **Create Folder**. 

After completing the steps above, Assured Workloads creates the following resources:

    * An Assured Workloads folder, which enforces security controls on [supported Google Cloud products](https://docs.cloud.google.com/assured-workloads/docs/supported-products) to adhere with the Australia Data Boundary control package. These controls include setting an organization policy that [restricts resource usage](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources) to only those supported products, and allows creating or using resources only in [allowed locations](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations). 
    * If you chose to create one, a CMEK project that contains the configured CMEK key ring. **Note** : Folder creation does not automatically create keys for you. After creating the folder, you must create an encryption key before adding any resources. See [Create and obtain a CMEK key](https://docs.cloud.google.com/assured-workloads/docs/create-and-obtain-cmek) to learn more. 

## Use your new Assured Workloads folder

To start using your Assured Workloads folder, it's important that you put the resources that you want to be compliant with Australia Data Boundary in the new folder. You can create projects inside of the folder along with [resources for supported products](https://docs.cloud.google.com/assured-workloads/docs/supported-products), or [migrate existing projects](https://docs.cloud.google.com/assured-workloads/docs/migrate-workload). Some possible next steps include the following:

    * Create a new project in the newly-created Assured Workloads folder, and then create a Compute Engine VM inside the project. The VM instance will be configured to meet the compliance requirements for Australia Data Boundary. 
    * [Analyze an existing project](https://docs.cloud.google.com/assured-workloads/docs/migrate-workload) that you want to make compliant with Australia Data Boundary, and make any of the required changes. Then, move the project to the newly-created Assured Workloads folder. 

### Enabling BigQuery in your folder

If your selected control package lists BigQuery as a supported service, BigQuery is supported, but it isn't automatically enabled when you create a new Assured Workloads folder due to an internal configuration process. This process normally finishes in ten minutes, but can take much longer in some circumstances. To check whether the process is finished and to enable BigQuery, complete the following steps:  

    1. In the Google Cloud console, go to the **Assured Workloads** page. 

[ Go to Assured Workloads](https://console.cloud.google.com/compliance/assuredworkloads)

    2. Select your new Assured Workloads folder from the list.
    3. On the **Folder Details** page in the **Allowed services** section, click **Review Available Updates**.
    4. In the **Allowed services** pane, review the services to be added to the [Resource Usage Restriction](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources) organization policy for the folder. If BigQuery services are listed, click **Allow Services** to add them.  
  
If BigQuery services are not listed, wait for the internal process to complete. If the services are not listed within 12 hours of folder creation, contact [Cloud Customer Care](https://docs.cloud.google.com/support). 

After the enablement process is completed, you can use BigQuery in your Assured Workloads folder.

Gemini in BigQuery is not supported by Assured Workloads.

  * ## Before you begin

If you haven't already, you must complete the following below to create an Assured Workloads folder for the [ Australia Data Boundary and Support control package](https://docs.cloud.google.com/assured-workloads/docs/control-packages#au-data-boundary-support):

    1. Ensure that you understand [Assured Workloads concepts](https://docs.cloud.google.com/assured-workloads/docs/overview). 
    2. If [Access Transparency](https://docs.cloud.google.com/assured-workloads/docs/access-transparency) is not enabled on your organization, it will automatically be enabled when you create an Assured Workloads folder. Any projects you create or move into the folder will be configured to use Access Transparency. 
    3. Ensure that you understand [how to get support](https://docs.cloud.google.com/assured-workloads/docs/getting-support) for Assured Workloads. 
    4. Ensure that you understand the [additional cost](https://docs.cloud.google.com/assured-workloads/pricing) when using Australia Data Boundary and Support in Assured Workloads. 
    5. [Set up Cloud Identity](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin) and [verify your domain](https://docs.cloud.google.com/identity/docs/verify-domain). 
    6. After Cloud Identity has been configured, [create an organization](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization). 

### Required IAM roles

To create an Assured Workloads folder, you must be granted the **Assured Workloads Administrator** (`roles/assuredworkloads.admin`) role, which contains the minimum IAM permissions to create and manage Assured Workloads folders.

## Create an Assured Workloads folder for Australia Data Boundary and Support

    1. In the Google Cloud console, go to the **Assured Workloads** page. 

[ Go to Assured Workloads](https://console.cloud.google.com/compliance/assuredworkloads)

    2. If prompted, select your organization.
    3. Click add_box**CREATE** to go to the **Create an Assured Workloads folder** page.
    4. In the step to **Add folder details** : 
       * In **Folder name** , enter a unique name for the folder, such as `aw-my-folder-name`. The folder name must be a minimum of 4 characters in length and a maximum of 30, and can only contain letters, numbers, spaces, and hyphens. **Tip:** When you name your Assured Workloads folders, consider the following: 
         * To identify the folder as an Assured Workloads folder, include a prefix in its name (such as `aw-`). This identifier can help you locate the folder from a list of other resources. 
         * Do not include sensitive data or personally identifiable information (PII) in the folder name. 
       * In **Organization** , select the organization in which to create your folder. This location can't be changed later.
       * In **Folder location** , select the location in the resource hierarchy where the folder will be created. An Assured Workloads folder can be created as a child of an organization or of another folder.
       * Click **Next**.
    5. In the step to **Choose a control package option** , select **Regional Controls** from the drop-down menu.
    6. Select **Australia Data Boundary and Support** from the drop-down menu. See [Control packages](https://docs.cloud.google.com/assured-workloads/docs/control-packages) to learn about other options.
    7. In **Select resource location** , choose the [location](https://docs.cloud.google.com/assured-workloads/docs/locations) where resource creation and usage will be enforced by the folder's [organization policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations). See [Resource locations supported services](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations-supported-services) for a list of all resources that can be restricted by the Resource Locations organization policy constraint, as some resources may be out of scope and unrestrictable. 
    8. Review the details about the control option you've selected, and click **Next**.
    9. (Optional) In the step to **Configure additional settings** , you can create a new project and a key ring for your [Customer Managed Encryption Keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek). No keys are created during this step, as Assured Workloads does not automatically create any cryptographic keys for you. See [Supporting compliance with key management](https://docs.cloud.google.com/assured-workloads/docs/key-management) for more information. **Note** : Australia Data Boundary and Support does not require using CMEK; you can click **Next** to skip this step.
    10. In the step to **Review and create folder** , review the details about your new Assured Workloads folder and ensure that they are correct. Then, click **Create Folder**. 

After completing the steps above, Assured Workloads creates the following resources:

    * An Assured Workloads folder, which enforces security controls on [supported Google Cloud products](https://docs.cloud.google.com/assured-workloads/docs/supported-products) to adhere with the Australia Data Boundary and Support control package. These controls include setting an organization policy that [restricts resource usage](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources) to only those supported products, and allows creating or using resources only in [allowed locations](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations). 
    * If you chose to create one, a CMEK project that contains the configured CMEK key ring. **Note** : Folder creation does not automatically create keys for you. After creating the folder, you must create an encryption key before adding any resources. See [Create and obtain a CMEK key](https://docs.cloud.google.com/assured-workloads/docs/create-and-obtain-cmek) to learn more. 

## Use your new Assured Workloads folder

To start using your Assured Workloads folder, it's important that you put the resources that you want to be compliant with Australia Data Boundary and Support in the new folder. You can create projects inside of the folder along with [resources for supported products](https://docs.cloud.google.com/assured-workloads/docs/supported-products), or [migrate existing projects](https://docs.cloud.google.com/assured-workloads/docs/migrate-workload). Some possible next steps include the following:

    * Create a new project in the newly-created Assured Workloads folder, and then create a Compute Engine VM inside the project. The VM instance will be configured to meet the compliance requirements for Australia Data Boundary and Support. 
    * [Analyze an existing project](https://docs.cloud.google.com/assured-workloads/docs/migrate-workload) that you want to make compliant with Australia Data Boundary and Support, and make any of the required changes. Then, move the project to the newly-created Assured Workloads folder. 

### Enabling BigQuery in your folder

If your selected control package lists BigQuery as a supported service, BigQuery is supported, but it isn't automatically enabled when you create a new Assured Workloads folder due to an internal configuration process. This process normally finishes in ten minutes, but can take much longer in some circumstances. To check whether the process is finished and to enable BigQuery, complete the following steps:  

    1. In the Google Cloud console, go to the **Assured Workloads** page. 

[ Go to Assured Workloads](https://console.cloud.google.com/compliance/assuredworkloads)

    2. Select your new Assured Workloads folder from the list.
    3. On the **Folder Details** page in the **Allowed services** section, click **Review Available Updates**.
    4. In the **Allowed services** pane, review the services to be added to the [Resource Usage Restriction](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources) organization policy for the folder. If BigQuery services are listed, click **Allow Services** to add them.  
  
If BigQuery services are not listed, wait for the internal process to complete. If the services are not listed within 12 hours of folder creation, contact [Cloud Customer Care](https://docs.cloud.google.com/support). 

After the enablement process is completed, you can use BigQuery in your Assured Workloads folder.

Gemini in BigQuery is not supported by Assured Workloads.

  * ## Before you begin

If you haven't already, you must complete the following below to create an Assured Workloads folder for the [ Brazil Data Boundary control package](https://docs.cloud.google.com/assured-workloads/docs/control-packages#br-data-boundary):

    1. Ensure that you understand [Assured Workloads concepts](https://docs.cloud.google.com/assured-workloads/docs/overview). 
    2. If [Access Transparency](https://docs.cloud.google.com/assured-workloads/docs/access-transparency) is not enabled on your organization, it will automatically be enabled when you create an Assured Workloads folder. Any projects you create or move into the folder will be configured to use Access Transparency. 
    3. Ensure that you understand [how to get support](https://docs.cloud.google.com/assured-workloads/docs/getting-support) for Assured Workloads. 
    4. [Set up Cloud Identity](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin) and [verify your domain](https://docs.cloud.google.com/identity/docs/verify-domain). 
    5. After Cloud Identity has been configured, [create an organization](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization). 

### Required IAM roles

To create an Assured Workloads folder, you must be granted the **Assured Workloads Administrator** (`roles/assuredworkloads.admin`) role, which contains the minimum IAM permissions to create and manage Assured Workloads folders.

## Create an Assured Workloads folder for Brazil Data Boundary

    1. In the Google Cloud console, go to the **Assured Workloads** page. 

[ Go to Assured Workloads](https://console.cloud.google.com/compliance/assuredworkloads)

    2. If prompted, select your organization.
    3. Click add_box**CREATE** to go to the **Create an Assured Workloads folder** page.
    4. In the step to **Add folder details** : 
       * In **Folder name** , enter a unique name for the folder, such as `aw-my-folder-name`. The folder name must be a minimum of 4 characters in length and a maximum of 30, and can only contain letters, numbers, spaces, and hyphens. **Tip:** When you name your Assured Workloads folders, consider the following: 
         * To identify the folder as an Assured Workloads folder, include a prefix in its name (such as `aw-`). This identifier can help you locate the folder from a list of other resources. 
         * Do not include sensitive data or personally identifiable information (PII) in the folder name. 
       * In **Organization** , select the organization in which to create your folder. This location can't be changed later.
       * In **Folder location** , select the location in the resource hierarchy where the folder will be created. An Assured Workloads folder can be created as a child of an organization or of another folder.
       * Click **Next**.
    5. In the step to **Choose a control package option** , select **Regional Controls** from the drop-down menu.
    6. Select **Brazil Data Boundary** from the drop-down menu. See [Control packages](https://docs.cloud.google.com/assured-workloads/docs/control-packages) to learn about other options.
    7. In **Select resource location** , choose the [location](https://docs.cloud.google.com/assured-workloads/docs/locations) where resource creation and usage will be enforced by the folder's [organization policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations). See [Resource locations supported services](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations-supported-services) for a list of all resources that can be restricted by the Resource Locations organization policy constraint, as some resources may be out of scope and unrestrictable. 
    8. Review the details about the control option you've selected, and click **Next**.
    9. (Optional) In the step to **Configure additional settings** , you can create a new project and a key ring for your [Customer Managed Encryption Keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek). No keys are created during this step, as Assured Workloads does not automatically create any cryptographic keys for you. See [Supporting compliance with key management](https://docs.cloud.google.com/assured-workloads/docs/key-management) for more information. **Note** : Brazil Data Boundary does not require using CMEK; you can click **Next** to skip this step.
    10. In the step to **Review and create folder** , review the details about your new Assured Workloads folder and ensure that they are correct. Then, click **Create Folder**. 

After completing the steps above, Assured Workloads creates the following resources:

    * An Assured Workloads folder, which enforces security controls on [supported Google Cloud products](https://docs.cloud.google.com/assured-workloads/docs/supported-products) to adhere with the Brazil Data Boundary control package. These controls include setting an organization policy that [restricts resource usage](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources) to only those supported products, and allows creating or using resources only in [allowed locations](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations). 
    * If you chose to create one, a CMEK project that contains the configured CMEK key ring. **Note** : Folder creation does not automatically create keys for you. After creating the folder, you must create an encryption key before adding any resources. See [Create and obtain a CMEK key](https://docs.cloud.google.com/assured-workloads/docs/create-and-obtain-cmek) to learn more. 

## Use your new Assured Workloads folder

To start using your Assured Workloads folder, it's important that you put the resources that you want to be compliant with Brazil Data Boundary in the new folder. You can create projects inside of the folder along with [resources for supported products](https://docs.cloud.google.com/assured-workloads/docs/supported-products), or [migrate existing projects](https://docs.cloud.google.com/assured-workloads/docs/migrate-workload). Some possible next steps include the following:

    * Create a new project in the newly-created Assured Workloads folder, and then create a Compute Engine VM inside the project. The VM instance will be configured to meet the compliance requirements for Brazil Data Boundary. 
    * [Analyze an existing project](https://docs.cloud.google.com/assured-workloads/docs/migrate-workload) that you want to make compliant with Brazil Data Boundary, and make any of the required changes. Then, move the project to the newly-created Assured Workloads folder. 

### Enabling BigQuery in your folder

If your selected control package lists BigQuery as a supported service, BigQuery is supported, but it isn't automatically enabled when you create a new Assured Workloads folder due to an internal configuration process. This process normally finishes in ten minutes, but can take much longer in some circumstances. To check whether the process is finished and to enable BigQuery, complete the following steps:  

    1. In the Google Cloud console, go to the **Assured Workloads** page. 

[ Go to Assured Workloads](https://console.cloud.google.com/compliance/assuredworkloads)

    2. Select your new Assured Workloads folder from the list.
    3. On the **Folder Details** page in the **Allowed services** section, click **Review Available Updates**.
    4. In the **Allowed services** pane, review the services to be added to the [Resource Usage Restriction](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources) organization policy for the folder. If BigQuery services are listed, click **Allow Services** to add them.  
  
If BigQuery services are not listed, wait for the internal process to complete. If the services are not listed within 12 hours of folder creation, contact [Cloud Customer Care](https://docs.cloud.google.com/support). 

After the enablement process is completed, you can use BigQuery in your Assured Workloads folder.

Gemini in BigQuery is not supported by Assured Workloads.

  * ## Before you begin

If you haven't already, you must complete the following below to create an Assured Workloads folder for the [ Data Boundary for Canada Controlled Goods control package](https://docs.cloud.google.com/assured-workloads/docs/control-packages#ca-controlled-goods):

    1. Ensure that you understand [Assured Workloads concepts](https://docs.cloud.google.com/assured-workloads/docs/overview). 
    2. If [Access Transparency](https://docs.cloud.google.com/assured-workloads/docs/access-transparency) is not enabled on your organization, it will automatically be enabled when you create an Assured Workloads folder. Any projects you create or move into the folder will be configured to use Access Transparency. 
    3. Ensure that you understand [how to get support](https://docs.cloud.google.com/assured-workloads/docs/getting-support) for Assured Workloads. 
    4. Ensure that you understand the [additional cost](https://docs.cloud.google.com/assured-workloads/pricing) when using Data Boundary for Canada Controlled Goods in Assured Workloads. 
    5. [Set up Cloud Identity](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin) and [verify your domain](https://docs.cloud.google.com/identity/docs/verify-domain). 
    6. After Cloud Identity has been configured, [create an organization](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization). 

### Required IAM roles

To create an Assured Workloads folder, you must be granted the **Assured Workloads Administrator** (`roles/assuredworkloads.admin`) role, which contains the minimum IAM permissions to create and manage Assured Workloads folders.

## Create an Assured Workloads folder for Data Boundary for Canada Controlled Goods

    1. In the Google Cloud console, go to the **Assured Workloads** page. 

[ Go to Assured Workloads](https://console.cloud.google.com/compliance/assuredworkloads)

    2. If prompted, select your organization.
    3. Click add_box**CREATE** to go to the **Create an Assured Workloads folder** page.
    4. In the step to **Add folder details** : 
       * In **Folder name** , enter a unique name for the folder, such as `aw-my-folder-name`. The folder name must be a minimum of 4 characters in length and a maximum of 30, and can only contain letters, numbers, spaces, and hyphens. **Tip:** When you name your Assured Workloads folders, consider the following: 
         * To identify the folder as an Assured Workloads folder, include a prefix in its name (such as `aw-`). This identifier can help you locate the folder from a list of other resources. 
         * Do not include sensitive data or personally identifiable information (PII) in the folder name. 
       * In **Organization** , select the organization in which to create your folder. This location can't be changed later.
       * In **Folder location** , select the location in the resource hierarchy where the folder will be created. An Assured Workloads folder can be created as a child of an organization or of another folder.
       * Click **Next**.
    5. In the step to **Choose a control package option** , select **Regulatory Controls** from the drop-down menu.
    6. Select **Data Boundary for Canada Controlled Goods** from the drop-down menu. See [Control packages](https://docs.cloud.google.com/assured-workloads/docs/control-packages) to learn about other options.
    7. In **Select resource location** , choose the [location](https://docs.cloud.google.com/assured-workloads/docs/locations) where resource creation and usage will be enforced by the folder's [organization policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations). See [Resource locations supported services](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations-supported-services) for a list of all resources that can be restricted by the Resource Locations organization policy constraint, as some resources may be out of scope and unrestrictable. 
    8. Review the details about the control option you've selected, and click **Next**.
    9. (Optional) In the step to **Configure additional settings** , you can create a new project and a key ring for your [Customer Managed Encryption Keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek). No keys are created during this step, as Assured Workloads does not automatically create any cryptographic keys for you. See [Supporting compliance with key management](https://docs.cloud.google.com/assured-workloads/docs/key-management) for more information. **Note** : Data Boundary for Canada Controlled Goods does not require using CMEK; you can click **Next** to skip this step.
    10. In the step to **Review and create folder** , review the details about your new Assured Workloads folder and ensure that they are correct. Then, click **Create Folder**. 

After completing the steps above, Assured Workloads creates the following resources:

    * An Assured Workloads folder, which enforces security controls on [supported Google Cloud products](https://docs.cloud.google.com/assured-workloads/docs/supported-products) to adhere with the Data Boundary for Canada Controlled Goods control package. These controls include setting an organization policy that [restricts resource usage](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources) to only those supported products, and allows creating or using resources only in [allowed locations](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations). 
    * If you chose to create one, a CMEK project that contains the configured CMEK key ring. **Note** : Folder creation does not automatically create keys for you. After creating the folder, you must create an encryption key before adding any resources. See [Create and obtain a CMEK key](https://docs.cloud.google.com/assured-workloads/docs/create-and-obtain-cmek) to learn more. 

## Use your new Assured Workloads folder

To start using your Assured Workloads folder, it's important that you put the resources that you want to be compliant with Data Boundary for Canada Controlled Goods in the new folder. You can create projects inside of the folder along with [resources for supported products](https://docs.cloud.google.com/assured-workloads/docs/supported-products), or [migrate existing projects](https://docs.cloud.google.com/assured-workloads/docs/migrate-workload). Some possible next steps include the following:

    * Create a new project in the newly-created Assured Workloads folder, and then create a Compute Engine VM inside the project. The VM instance will be configured to meet the compliance requirements for Data Boundary for Canada Controlled Goods. 
    * [Analyze an existing project](https://docs.cloud.google.com/assured-workloads/docs/migrate-workload) that you want to make compliant with Data Boundary for Canada Controlled Goods, and make any of the required changes. Then, move the project to the newly-created Assured Workloads folder. 

### Enabling BigQuery in your folder

If your selected control package lists BigQuery as a supported service, BigQuery is supported, but it isn't automatically enabled when you create a new Assured Workloads folder due to an internal configuration process. This process normally finishes in ten minutes, but can take much longer in some circumstances. To check whether the process is finished and to enable BigQuery, complete the following steps:  

    1. In the Google Cloud console, go to the **Assured Workloads** page. 

[ Go to Assured Workloads](https://console.cloud.google.com/compliance/assuredworkloads)

    2. Select your new Assured Workloads folder from the list.
    3. On the **Folder Details** page in the **Allowed services** section, click **Review Available Updates**.
    4. In the **Allowed services** pane, review the services to be added to the [Resource Usage Restriction](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources) organization policy for the folder. If BigQuery services are listed, click **Allow Services** to add them.  
  
If BigQuery services are not listed, wait for the internal process to complete. If the services are not listed within 12 hours of folder creation, contact [Cloud Customer Care](https://docs.cloud.google.com/support). 

After the enablement process is completed, you can use BigQuery in your Assured Workloads folder.

Gemini in BigQuery is not supported by Assured Workloads.

  * ## Before you begin

If you haven't already, you must complete the following below to create an Assured Workloads folder for the [ Data Boundary for Canada Protected B control package](https://docs.cloud.google.com/assured-workloads/docs/control-packages#ca-protected-b):

    1. Ensure that you understand [Assured Workloads concepts](https://docs.cloud.google.com/assured-workloads/docs/overview). 
    2. If [Access Transparency](https://docs.cloud.google.com/assured-workloads/docs/access-transparency) is not enabled on your organization, it will automatically be enabled when you create an Assured Workloads folder. Any projects you create or move into the folder will be configured to use Access Transparency. 
    3. Ensure that you understand [how to get support](https://docs.cloud.google.com/assured-workloads/docs/getting-support) for Assured Workloads. 
    4. Ensure that you understand the [additional cost](https://docs.cloud.google.com/assured-workloads/pricing) when using Data Boundary for Canada Protected B in Assured Workloads. 
    5. [Set up Cloud Identity](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin) and [verify your domain](https://docs.cloud.google.com/identity/docs/verify-domain). 
    6. After Cloud Identity has been configured, [create an organization](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization). 

### Required IAM roles

To create an Assured Workloads folder, you must be granted the **Assured Workloads Administrator** (`roles/assuredworkloads.admin`) role, which contains the minimum IAM permissions to create and manage Assured Workloads folders.

## Create an Assured Workloads folder for Data Boundary for Canada Protected B

    1. In the Google Cloud console, go to the **Assured Workloads** page. 

[ Go to Assured Workloads](https://console.cloud.google.com/compliance/assuredworkloads)

    2. If prompted, select your organization.
    3. Click add_box**CREATE** to go to the **Create an Assured Workloads folder** page.
    4. In the step to **Add folder details** : 
       * In **Folder name** , enter a unique name for the folder, such as `aw-my-folder-name`. The folder name must be a minimum of 4 characters in length and a maximum of 30, and can only contain letters, numbers, spaces, and hyphens. **Tip:** When you name your Assured Workloads folders, consider the following: 
         * To identify the folder as an Assured Workloads folder, include a prefix in its name (such as `aw-`). This identifier can help you locate the folder from a list of other resources. 
         * Do not include sensitive data or personally identifiable information (PII) in the folder name. 
       * In **Organization** , select the organization in which to create your folder. This location can't be changed later.
       * In **Folder location** , select the location in the resource hierarchy where the folder will be created. An Assured Workloads folder can be created as a child of an organization or of another folder.
       * Click **Next**.
    5. In the step to **Choose a control package option** , select **Regulatory Controls** from the drop-down menu.
    6. Select **Data Boundary for Canada Protected B** from the drop-down menu. See [Control packages](https://docs.cloud.google.com/assured-workloads/docs/control-packages) to learn about other options.
    7. In **Select resource location** , choose the [location](https://docs.cloud.google.com/assured-workloads/docs/locations) where resource creation and usage will be enforced by the folder's [organization policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations). See [Resource locations supported services](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations-supported-services) for a list of all resources that can be restricted by the Resource Locations organization policy constraint, as some resources may be out of scope and unrestrictable. 
    8. Review the details about the control option you've selected, and click **Next**.
    9. (Optional) In the step to **Configure additional settings** , you can create a new project and a key ring for your [Customer Managed Encryption Keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek). No keys are created during this step, as Assured Workloads does not automatically create any cryptographic keys for you. See [Supporting compliance with key management](https://docs.cloud.google.com/assured-workloads/docs/key-management) for more information. **Note** : Data Boundary for Canada Protected B does not require using CMEK; you can click **Next** to skip this step.
    10. In the step to **Review and create folder** , review the details about your new Assured Workloads folder and ensure that they are correct. Then, click **Create Folder**. 

After completing the steps above, Assured Workloads creates the following resources:

    * An Assured Workloads folder, which enforces security controls on [supported Google Cloud products](https://docs.cloud.google.com/assured-workloads/docs/supported-products) to adhere with the Data Boundary for Canada Protected B control package. These controls include setting an organization policy that [restricts resource usage](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources) to only those supported products, and allows creating or using resources only in [allowed locations](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations). 
    * If you chose to create one, a CMEK project that contains the configured CMEK key ring. **Note** : Folder creation does not automatically create keys for you. After creating the folder, you must create an encryption key before adding any resources. See [Create and obtain a CMEK key](https://docs.cloud.google.com/assured-workloads/docs/create-and-obtain-cmek) to learn more. 

## Use your new Assured Workloads folder

To start using your Assured Workloads folder, it's important that you put the resources that you want to be compliant with Data Boundary for Canada Protected B in the new folder. You can create projects inside of the folder along with [resources for supported products](https://docs.cloud.google.com/assured-workloads/docs/supported-products), or [migrate existing projects](https://docs.cloud.google.com/assured-workloads/docs/migrate-workload). Some possible next steps include the following:

    * Create a new project in the newly-created Assured Workloads folder, and then create a Compute Engine VM inside the project. The VM instance will be configured to meet the compliance requirements for Data Boundary for Canada Protected B. 
    * [Analyze an existing project](https://docs.cloud.google.com/assured-workloads/docs/migrate-workload) that you want to make compliant with Data Boundary for Canada Protected B, and make any of the required changes. Then, move the project to the newly-created Assured Workloads folder. 

### Enabling BigQuery in your folder

If your selected control package lists BigQuery as a supported service, BigQuery is supported, but it isn't automatically enabled when you create a new Assured Workloads folder due to an internal configuration process. This process normally finishes in ten minutes, but can take much longer in some circumstances. To check whether the process is finished and to enable BigQuery, complete the following steps:  

    1. In the Google Cloud console, go to the **Assured Workloads** page. 

[ Go to Assured Workloads](https://console.cloud.google.com/compliance/assuredworkloads)

    2. Select your new Assured Workloads folder from the list.
    3. On the **Folder Details** page in the **Allowed services** section, click **Review Available Updates**.
    4. In the **Allowed services** pane, review the services to be added to the [Resource Usage Restriction](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources) organization policy for the folder. If BigQuery services are listed, click **Allow Services** to add them.  
  
If BigQuery services are not listed, wait for the internal process to complete. If the services are not listed within 12 hours of folder creation, contact [Cloud Customer Care](https://docs.cloud.google.com/support). 

After the enablement process is completed, you can use BigQuery in your Assured Workloads folder.

Gemini in BigQuery is not supported by Assured Workloads.

  * ## Before you begin

If you haven't already, you must complete the following below to create an Assured Workloads folder for the [ Canada Data Boundary control package](https://docs.cloud.google.com/assured-workloads/docs/control-packages#ca-data-boundary):

    1. Ensure that you understand [Assured Workloads concepts](https://docs.cloud.google.com/assured-workloads/docs/overview). 
    2. If [Access Transparency](https://docs.cloud.google.com/assured-workloads/docs/access-transparency) is not enabled on your organization, it will automatically be enabled when you create an Assured Workloads folder. Any projects you create or move into the folder will be configured to use Access Transparency. 
    3. Ensure that you understand [how to get support](https://docs.cloud.google.com/assured-workloads/docs/getting-support) for Assured Workloads. 
    4. [Set up Cloud Identity](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin) and [verify your domain](https://docs.cloud.google.com/identity/docs/verify-domain). 
    5. After Cloud Identity has been configured, [create an organization](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization). 

### Required IAM roles

To create an Assured Workloads folder, you must be granted the **Assured Workloads Administrator** (`roles/assuredworkloads.admin`) role, which contains the minimum IAM permissions to create and manage Assured Workloads folders.

## Create an Assured Workloads folder for Canada Data Boundary

    1. In the Google Cloud console, go to the **Assured Workloads** page. 

[ Go to Assured Workloads](https://console.cloud.google.com/compliance/assuredworkloads)

    2. If prompted, select your organization.
    3. Click add_box**CREATE** to go to the **Create an Assured Workloads folder** page.
    4. In the step to **Add folder details** : 
       * In **Folder name** , enter a unique name for the folder, such as `aw-my-folder-name`. The folder name must be a minimum of 4 characters in length and a maximum of 30, and can only contain letters, numbers, spaces, and hyphens. **Tip:** When you name your Assured Workloads folders, consider the following: 
         * To identify the folder as an Assured Workloads folder, include a prefix in its name (such as `aw-`). This identifier can help you locate the folder from a list of other resources. 
         * Do not include sensitive data or personally identifiable information (PII) in the folder name. 
       * In **Organization** , select the organization in which to create your folder. This location can't be changed later.
       * In **Folder location** , select the location in the resource hierarchy where the folder will be created. An Assured Workloads folder can be created as a child of an organization or of another folder.
       * Click **Next**.
    5. In the step to **Choose a control package option** , select **Regional Controls** from the drop-down menu.
    6. Select **Canada Data Boundary** from the drop-down menu. See [Control packages](https://docs.cloud.google.com/assured-workloads/docs/control-packages) to learn about other options.
    7. In **Select resource location** , choose the [location](https://docs.cloud.google.com/assured-workloads/docs/locations) where resource creation and usage will be enforced by the folder's [organization policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations). See [Resource locations supported services](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations-supported-services) for a list of all resources that can be restricted by the Resource Locations organization policy constraint, as some resources may be out of scope and unrestrictable. 
    8. Review the details about the control option you've selected, and click **Next**.
    9. (Optional) In the step to **Configure additional settings** , you can create a new project and a key ring for your [Customer Managed Encryption Keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek). No keys are created during this step, as Assured Workloads does not automatically create any cryptographic keys for you. See [Supporting compliance with key management](https://docs.cloud.google.com/assured-workloads/docs/key-management) for more information. **Note** : Canada Data Boundary does not require using CMEK; you can click **Next** to skip this step.
    10. In the step to **Review and create folder** , review the details about your new Assured Workloads folder and ensure that they are correct. Then, click **Create Folder**. 

After completing the steps above, Assured Workloads creates the following resources:

    * An Assured Workloads folder, which enforces security controls on [supported Google Cloud products](https://docs.cloud.google.com/assured-workloads/docs/supported-products) to adhere with the Canada Data Boundary control package. These controls include setting an organization policy that [restricts resource usage](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources) to only those supported products, and allows creating or using resources only in [allowed locations](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations). 
    * If you chose to create one, a CMEK project that contains the configured CMEK key ring. **Note** : Folder creation does not automatically create keys for you. After creating the folder, you must create an encryption key before adding any resources. See [Create and obtain a CMEK key](https://docs.cloud.google.com/assured-workloads/docs/create-and-obtain-cmek) to learn more. 

## Use your new Assured Workloads folder

To start using your Assured Workloads folder, it's important that you put the resources that you want to be compliant with Canada Data Boundary in the new folder. You can create projects inside of the folder along with [resources for supported products](https://docs.cloud.google.com/assured-workloads/docs/supported-products), or [migrate existing projects](https://docs.cloud.google.com/assured-workloads/docs/migrate-workload). Some possible next steps include the following:

    * Create a new project in the newly-created Assured Workloads folder, and then create a Compute Engine VM inside the project. The VM instance will be configured to meet the compliance requirements for Canada Data Boundary. 
    * [Analyze an existing project](https://docs.cloud.google.com/assured-workloads/docs/migrate-workload) that you want to make compliant with Canada Data Boundary, and make any of the required changes. Then, move the project to the newly-created Assured Workloads folder. 

### Enabling BigQuery in your folder

If your selected control package lists BigQuery as a supported service, BigQuery is supported, but it isn't automatically enabled when you create a new Assured Workloads folder due to an internal configuration process. This process normally finishes in ten minutes, but can take much longer in some circumstances. To check whether the process is finished and to enable BigQuery, complete the following steps:  

    1. In the Google Cloud console, go to the **Assured Workloads** page. 

[ Go to Assured Workloads](https://console.cloud.google.com/compliance/assuredworkloads)

    2. Select your new Assured Workloads folder from the list.
    3. On the **Folder Details** page in the **Allowed services** section, click **Review Available Updates**.
    4. In the **Allowed services** pane, review the services to be added to the [Resource Usage Restriction](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources) organization policy for the folder. If BigQuery services are listed, click **Allow Services** to add them.  
  
If BigQuery services are not listed, wait for the internal process to complete. If the services are not listed within 12 hours of folder creation, contact [Cloud Customer Care](https://docs.cloud.google.com/support). 

After the enablement process is completed, you can use BigQuery in your Assured Workloads folder.

Gemini in BigQuery is not supported by Assured Workloads.

  * ## Before you begin

If you haven't already, you must complete the following below to create an Assured Workloads folder for the [ Canada Data Boundary and Support control package](https://docs.cloud.google.com/assured-workloads/docs/control-packages#ca-data-boundary-support):

    1. Ensure that you understand [Assured Workloads concepts](https://docs.cloud.google.com/assured-workloads/docs/overview). 
    2. If [Access Transparency](https://docs.cloud.google.com/assured-workloads/docs/access-transparency) is not enabled on your organization, it will automatically be enabled when you create an Assured Workloads folder. Any projects you create or move into the folder will be configured to use Access Transparency. 
    3. Ensure that you understand [how to get support](https://docs.cloud.google.com/assured-workloads/docs/getting-support) for Assured Workloads. 
    4. Ensure that you understand the [additional cost](https://docs.cloud.google.com/assured-workloads/pricing) when using Canada Data Boundary and Support in Assured Workloads. 
    5. [Set up Cloud Identity](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin) and [verify your domain](https://docs.cloud.google.com/identity/docs/verify-domain). 
    6. After Cloud Identity has been configured, [create an organization](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization). 

### Required IAM roles

To create an Assured Workloads folder, you must be granted the **Assured Workloads Administrator** (`roles/assuredworkloads.admin`) role, which contains the minimum IAM permissions to create and manage Assured Workloads folders.

## Create an Assured Workloads folder for Canada Data Boundary and Support

    1. In the Google Cloud console, go to the **Assured Workloads** page. 

[ Go to Assured Workloads](https://console.cloud.google.com/compliance/assuredworkloads)

    2. If prompted, select your organization.
    3. Click add_box**CREATE** to go to the **Create an Assured Workloads folder** page.
    4. In the step to **Add folder details** : 
       * In **Folder name** , enter a unique name for the folder, such as `aw-my-folder-name`. The folder name must be a minimum of 4 characters in length and a maximum of 30, and can only contain letters, numbers, spaces, and hyphens. **Tip:** When you name your Assured Workloads folders, consider the following: 
         * To identify the folder as an Assured Workloads folder, include a prefix in its name (such as `aw-`). This identifier can help you locate the folder from a list of other resources. 
         * Do not include sensitive data or personally identifiable information (PII) in the folder name. 
       * In **Organization** , select the organization in which to create your folder. This location can't be changed later.
       * In **Folder location** , select the location in the resource hierarchy where the folder will be created. An Assured Workloads folder can be created as a child of an organization or of another folder.
       * Click **Next**.
    5. In the step to **Choose a control package option** , select **Regional Controls** from the drop-down menu.
    6. Select **Canada Data Boundary and Support** from the drop-down menu. See [Control packages](https://docs.cloud.google.com/assured-workloads/docs/control-packages) to learn about other options.
    7. In **Select resource location** , choose the [location](https://docs.cloud.google.com/assured-workloads/docs/locations) where resource creation and usage will be enforced by the folder's [organization policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations). See [Resource locations supported services](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations-supported-services) for a list of all resources that can be restricted by the Resource Locations organization policy constraint, as some resources may be out of scope and unrestrictable. 
    8. Review the details about the control option you've selected, and click **Next**.
    9. (Optional) In the step to **Configure additional settings** , you can create a new project and a key ring for your [Customer Managed Encryption Keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek). No keys are created during this step, as Assured Workloads does not automatically create any cryptographic keys for you. See [Supporting compliance with key management](https://docs.cloud.google.com/assured-workloads/docs/key-management) for more information. **Note** : Canada Data Boundary and Support does not require using CMEK; you can click **Next** to skip this step.
    10. In the step to **Review and create folder** , review the details about your new Assured Workloads folder and ensure that they are correct. Then, click **Create Folder**. 

After completing the steps above, Assured Workloads creates the following resources:

    * An Assured Workloads folder, which enforces security controls on [supported Google Cloud products](https://docs.cloud.google.com/assured-workloads/docs/supported-products) to adhere with the Canada Data Boundary and Support control package. These controls include setting an organization policy that [restricts resource usage](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources) to only those supported products, and allows creating or using resources only in [allowed locations](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations). 
    * If you chose to create one, a CMEK project that contains the configured CMEK key ring. **Note** : Folder creation does not automatically create keys for you. After creating the folder, you must create an encryption key before adding any resources. See [Create and obtain a CMEK key](https://docs.cloud.google.com/assured-workloads/docs/create-and-obtain-cmek) to learn more. 

## Use your new Assured Workloads folder

To start using your Assured Workloads folder, it's important that you put the resources that you want to be compliant with Canada Data Boundary and Support in the new folder. You can create projects inside of the folder along with [resources for supported products](https://docs.cloud.google.com/assured-workloads/docs/supported-products), or [migrate existing projects](https://docs.cloud.google.com/assured-workloads/docs/migrate-workload). Some possible next steps include the following:

    * Create a new project in the newly-created Assured Workloads folder, and then create a Compute Engine VM inside the project. The VM instance will be configured to meet the compliance requirements for Canada Data Boundary and Support. 
    * [Analyze an existing project](https://docs.cloud.google.com/assured-workloads/docs/migrate-workload) that you want to make compliant with Canada Data Boundary and Support, and make any of the required changes. Then, move the project to the newly-created Assured Workloads folder. 

### Enabling BigQuery in your folder

If your selected control package lists BigQuery as a supported service, BigQuery is supported, but it isn't automatically enabled when you create a new Assured Workloads folder due to an internal configuration process. This process normally finishes in ten minutes, but can take much longer in some circumstances. To check whether the process is finished and to enable BigQuery, complete the following steps:  

    1. In the Google Cloud console, go to the **Assured Workloads** page. 

[ Go to Assured Workloads](https://console.cloud.google.com/compliance/assuredworkloads)

    2. Select your new Assured Workloads folder from the list.
    3. On the **Folder Details** page in the **Allowed services** section, click **Review Available Updates**.
    4. In the **Allowed services** pane, review the services to be added to the [Resource Usage Restriction](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources) organization policy for the folder. If BigQuery services are listed, click **Allow Services** to add them.  
  
If BigQuery services are not listed, wait for the internal process to complete. If the services are not listed within 12 hours of folder creation, contact [Cloud Customer Care](https://docs.cloud.google.com/support). 

After the enablement process is completed, you can use BigQuery in your Assured Workloads folder.

Gemini in BigQuery is not supported by Assured Workloads.

  * ## Before you begin

If you haven't already, you must complete the following below to create an Assured Workloads folder for the [ Chile Data Boundary control package](https://docs.cloud.google.com/assured-workloads/docs/control-packages#cl-data-boundary):

    1. Ensure that you understand [Assured Workloads concepts](https://docs.cloud.google.com/assured-workloads/docs/overview). 
    2. If [Access Transparency](https://docs.cloud.google.com/assured-workloads/docs/access-transparency) is not enabled on your organization, it will automatically be enabled when you create an Assured Workloads folder. Any projects you create or move into the folder will be configured to use Access Transparency. 
    3. Ensure that you understand [how to get support](https://docs.cloud.google.com/assured-workloads/docs/getting-support) for Assured Workloads. 
    4. [Set up Cloud Identity](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin) and [verify your domain](https://docs.cloud.google.com/identity/docs/verify-domain). 
    5. After Cloud Identity has been configured, [create an organization](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization). 

### Required IAM roles

To create an Assured Workloads folder, you must be granted the **Assured Workloads Administrator** (`roles/assuredworkloads.admin`) role, which contains the minimum IAM permissions to create and manage Assured Workloads folders.

## Create an Assured Workloads folder for Chile Data Boundary

    1. In the Google Cloud console, go to the **Assured Workloads** page. 

[ Go to Assured Workloads](https://console.cloud.google.com/compliance/assuredworkloads)

    2. If prompted, select your organization.
    3. Click add_box**CREATE** to go to the **Create an Assured Workloads folder** page.
    4. In the step to **Add folder details** : 
       * In **Folder name** , enter a unique name for the folder, such as `aw-my-folder-name`. The folder name must be a minimum of 4 characters in length and a maximum of 30, and can only contain letters, numbers, spaces, and hyphens. **Tip:** When you name your Assured Workloads folders, consider the following: 
         * To identify the folder as an Assured Workloads folder, include a prefix in its name (such as `aw-`). This identifier can help you locate the folder from a list of other resources. 
         * Do not include sensitive data or personally identifiable information (PII) in the folder name. 
       * In **Organization** , select the organization in which to create your folder. This location can't be changed later.
       * In **Folder location** , select the location in the resource hierarchy where the folder will be created. An Assured Workloads folder can be created as a child of an organization or of another folder.
       * Click **Next**.
    5. In the step to **Choose a control package option** , select **Regional Controls** from the drop-down menu.
    6. Select **Chile Data Boundary** from the drop-down menu. See [Control packages](https://docs.cloud.google.com/assured-workloads/docs/control-packages) to learn about other options.
    7. In **Select resource location** , choose the [location](https://docs.cloud.google.com/assured-workloads/docs/locations) where resource creation and usage will be enforced by the folder's [organization policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations). See [Resource locations supported services](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations-supported-services) for a list of all resources that can be restricted by the Resource Locations organization policy constraint, as some resources may be out of scope and unrestrictable. 
    8. Review the details about the control option you've selected, and click **Next**.
    9. (Optional) In the step to **Configure additional settings** , you can create a new project and a key ring for your [Customer Managed Encryption Keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek). No keys are created during this step, as Assured Workloads does not automatically create any cryptographic keys for you. See [Supporting compliance with key management](https://docs.cloud.google.com/assured-workloads/docs/key-management) for more information. **Note** : Chile Data Boundary does not require using CMEK; you can click **Next** to skip this step.
    10. In the step to **Review and create folder** , review the details about your new Assured Workloads folder and ensure that they are correct. Then, click **Create Folder**. 

After completing the steps above, Assured Workloads creates the following resources:

    * An Assured Workloads folder, which enforces security controls on [supported Google Cloud products](https://docs.cloud.google.com/assured-workloads/docs/supported-products) to adhere with the Chile Data Boundary control package. These controls include setting an organization policy that [restricts resource usage](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources) to only those supported products, and allows creating or using resources only in [allowed locations](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations). 
    * If you chose to create one, a CMEK project that contains the configured CMEK key ring. **Note** : Folder creation does not automatically create keys for you. After creating the folder, you must create an encryption key before adding any resources. See [Create and obtain a CMEK key](https://docs.cloud.google.com/assured-workloads/docs/create-and-obtain-cmek) to learn more. 

## Use your new Assured Workloads folder

To start using your Assured Workloads folder, it's important that you put the resources that you want to be compliant with Chile Data Boundary in the new folder. You can create projects inside of the folder along with [resources for supported products](https://docs.cloud.google.com/assured-workloads/docs/supported-products), or [migrate existing projects](https://docs.cloud.google.com/assured-workloads/docs/migrate-workload). Some possible next steps include the following:

    * Create a new project in the newly-created Assured Workloads folder, and then create a Compute Engine VM inside the project. The VM instance will be configured to meet the compliance requirements for Chile Data Boundary. 
    * [Analyze an existing project](https://docs.cloud.google.com/assured-workloads/docs/migrate-workload) that you want to make compliant with Chile Data Boundary, and make any of the required changes. Then, move the project to the newly-created Assured Workloads folder. 

### Enabling BigQuery in your folder

If your selected control package lists BigQuery as a supported service, BigQuery is supported, but it isn't automatically enabled when you create a new Assured Workloads folder due to an internal configuration process. This process normally finishes in ten minutes, but can take much longer in some circumstances. To check whether the process is finished and to enable BigQuery, complete the following steps:  

    1. In the Google Cloud console, go to the **Assured Workloads** page. 

[ Go to Assured Workloads](https://console.cloud.google.com/compliance/assuredworkloads)

    2. Select your new Assured Workloads folder from the list.
    3. On the **Folder Details** page in the **Allowed services** section, click **Review Available Updates**.
    4. In the **Allowed services** pane, review the services to be added to the [Resource Usage Restriction](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources) organization policy for the folder. If BigQuery services are listed, click **Allow Services** to add them.  
  
If BigQuery services are not listed, wait for the internal process to complete. If the services are not listed within 12 hours of folder creation, contact [Cloud Customer Care](https://docs.cloud.google.com/support). 

After the enablement process is completed, you can use BigQuery in your Assured Workloads folder.

Gemini in BigQuery is not supported by Assured Workloads.

  * ## Before you begin

If you haven't already, you must complete the following below to create an Assured Workloads folder for the [ EU Data Boundary control package](https://docs.cloud.google.com/assured-workloads/docs/control-packages#eu-data-boundary):

    1. Ensure that you understand [Assured Workloads concepts](https://docs.cloud.google.com/assured-workloads/docs/overview). 
    2. If [Access Transparency](https://docs.cloud.google.com/assured-workloads/docs/access-transparency) is not enabled on your organization, it will automatically be enabled when you create an Assured Workloads folder. Any projects you create or move into the folder will be configured to use Access Transparency. 
    3. Ensure that you understand [how to get support](https://docs.cloud.google.com/assured-workloads/docs/getting-support) for Assured Workloads. 
    4. [Set up Cloud Identity](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin) and [verify your domain](https://docs.cloud.google.com/identity/docs/verify-domain). 
    5. After Cloud Identity has been configured, [create an organization](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization). 

### Required IAM roles

To create an Assured Workloads folder, you must be granted the **Assured Workloads Administrator** (`roles/assuredworkloads.admin`) role, which contains the minimum IAM permissions to create and manage Assured Workloads folders.

## Create an Assured Workloads folder for EU Data Boundary

    1. In the Google Cloud console, go to the **Assured Workloads** page. 

[ Go to Assured Workloads](https://console.cloud.google.com/compliance/assuredworkloads)

    2. If prompted, select your organization.
    3. Click add_box**CREATE** to go to the **Create an Assured Workloads folder** page.
    4. In the step to **Add folder details** : 
       * In **Folder name** , enter a unique name for the folder, such as `aw-my-folder-name`. The folder name must be a minimum of 4 characters in length and a maximum of 30, and can only contain letters, numbers, spaces, and hyphens. **Tip:** When you name your Assured Workloads folders, consider the following: 
         * To identify the folder as an Assured Workloads folder, include a prefix in its name (such as `aw-`). This identifier can help you locate the folder from a list of other resources. 
         * Do not include sensitive data or personally identifiable information (PII) in the folder name. 
       * In **Organization** , select the organization in which to create your folder. This location can't be changed later.
       * In **Folder location** , select the location in the resource hierarchy where the folder will be created. An Assured Workloads folder can be created as a child of an organization or of another folder.
       * Click **Next**.
    5. In the step to **Choose a control package option** , select **Regional Controls** from the drop-down menu.
    6. Select **EU Data Boundary** from the drop-down menu. See [Control packages](https://docs.cloud.google.com/assured-workloads/docs/control-packages) to learn about other options.
    7. In **Select resource location** , choose the [location](https://docs.cloud.google.com/assured-workloads/docs/locations) where resource creation and usage will be enforced by the folder's [organization policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations). See [Resource locations supported services](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations-supported-services) for a list of all resources that can be restricted by the Resource Locations organization policy constraint, as some resources may be out of scope and unrestrictable. 
    8. Review the details about the control option you've selected, and click **Next**.
    9. (Optional) In the step to **Configure additional settings** , you can create a new project and a key ring for your [Customer Managed Encryption Keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek). No keys are created during this step, as Assured Workloads does not automatically create any cryptographic keys for you. See [Supporting compliance with key management](https://docs.cloud.google.com/assured-workloads/docs/key-management) for more information. **Note** : EU Data Boundary does not require using CMEK; you can click **Next** to skip this step.
    10. In the step to **Review and create folder** , review the details about your new Assured Workloads folder and ensure that they are correct. Then, click **Create Folder**. 

After completing the steps above, Assured Workloads creates the following resources:

    * An Assured Workloads folder, which enforces security controls on [supported Google Cloud products](https://docs.cloud.google.com/assured-workloads/docs/supported-products) to adhere with the EU Data Boundary control package. These controls include setting an organization policy that [restricts resource usage](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources) to only those supported products, and allows creating or using resources only in [allowed locations](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations). 
    * If you chose to create one, a CMEK project that contains the configured CMEK key ring. **Note** : Folder creation does not automatically create keys for you. After creating the folder, you must create an encryption key before adding any resources. See [Create and obtain a CMEK key](https://docs.cloud.google.com/assured-workloads/docs/create-and-obtain-cmek) to learn more. 

## Use your new Assured Workloads folder

To start using your Assured Workloads folder, it's important that you put the resources that you want to be compliant with EU Data Boundary in the new folder. You can create projects inside of the folder along with [resources for supported products](https://docs.cloud.google.com/assured-workloads/docs/supported-products), or [migrate existing projects](https://docs.cloud.google.com/assured-workloads/docs/migrate-workload). Some possible next steps include the following:

    * Create a new project in the newly-created Assured Workloads folder, and then create a Compute Engine VM inside the project. The VM instance will be configured to meet the compliance requirements for EU Data Boundary. 
    * [Analyze an existing project](https://docs.cloud.google.com/assured-workloads/docs/migrate-workload) that you want to make compliant with EU Data Boundary, and make any of the required changes. Then, move the project to the newly-created Assured Workloads folder. 

### Enabling BigQuery in your folder

If your selected control package lists BigQuery as a supported service, BigQuery is supported, but it isn't automatically enabled when you create a new Assured Workloads folder due to an internal configuration process. This process normally finishes in ten minutes, but can take much longer in some circumstances. To check whether the process is finished and to enable BigQuery, complete the following steps:  

    1. In the Google Cloud console, go to the **Assured Workloads** page. 

[ Go to Assured Workloads](https://console.cloud.google.com/compliance/assuredworkloads)

    2. Select your new Assured Workloads folder from the list.
    3. On the **Folder Details** page in the **Allowed services** section, click **Review Available Updates**.
    4. In the **Allowed services** pane, review the services to be added to the [Resource Usage Restriction](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources) organization policy for the folder. If BigQuery services are listed, click **Allow Services** to add them.  
  
If BigQuery services are not listed, wait for the internal process to complete. If the services are not listed within 12 hours of folder creation, contact [Cloud Customer Care](https://docs.cloud.google.com/support). 

After the enablement process is completed, you can use BigQuery in your Assured Workloads folder.

Gemini in BigQuery is not supported by Assured Workloads.

  * ## Before you begin

If you haven't already, you must complete the following below to create an Assured Workloads folder for the [ EU Data Boundary and Support control package](https://docs.cloud.google.com/assured-workloads/docs/control-packages#eu-data-boundary-support):

    1. Ensure that you understand [Assured Workloads concepts](https://docs.cloud.google.com/assured-workloads/docs/overview). 
    2. If [Access Transparency](https://docs.cloud.google.com/assured-workloads/docs/access-transparency) is not enabled on your organization, it will automatically be enabled when you create an Assured Workloads folder. Any projects you create or move into the folder will be configured to use Access Transparency. 
    3. Ensure that you understand [how to get support](https://docs.cloud.google.com/assured-workloads/docs/getting-support) for Assured Workloads. 
    4. Ensure that you understand the [additional cost](https://docs.cloud.google.com/assured-workloads/pricing) when using EU Data Boundary and Support in Assured Workloads. 
    5. [Set up Cloud Identity](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin) and [verify your domain](https://docs.cloud.google.com/identity/docs/verify-domain). 
    6. After Cloud Identity has been configured, [create an organization](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization). 

### Required IAM roles

To create an Assured Workloads folder, you must be granted the **Assured Workloads Administrator** (`roles/assuredworkloads.admin`) role, which contains the minimum IAM permissions to create and manage Assured Workloads folders.

## Create an Assured Workloads folder for EU Data Boundary and Support

    1. In the Google Cloud console, go to the **Assured Workloads** page. 

[ Go to Assured Workloads](https://console.cloud.google.com/compliance/assuredworkloads)

    2. If prompted, select your organization.
    3. Click add_box**CREATE** to go to the **Create an Assured Workloads folder** page.
    4. In the step to **Add folder details** : 
       * In **Folder name** , enter a unique name for the folder, such as `aw-my-folder-name`. The folder name must be a minimum of 4 characters in length and a maximum of 30, and can only contain letters, numbers, spaces, and hyphens. **Tip:** When you name your Assured Workloads folders, consider the following: 
         * To identify the folder as an Assured Workloads folder, include a prefix in its name (such as `aw-`). This identifier can help you locate the folder from a list of other resources. 
         * Do not include sensitive data or personally identifiable information (PII) in the folder name. 
       * In **Organization** , select the organization in which to create your folder. This location can't be changed later.
       * In **Folder location** , select the location in the resource hierarchy where the folder will be created. An Assured Workloads folder can be created as a child of an organization or of another folder.
       * Click **Next**.
    5. In the step to **Choose a control package option** , select **Regional Controls** from the drop-down menu.
    6. Select **EU Data Boundary and Support** from the drop-down menu. See [Control packages](https://docs.cloud.google.com/assured-workloads/docs/control-packages) to learn about other options.
    7. In **Select resource location** , choose the [location](https://docs.cloud.google.com/assured-workloads/docs/locations) where resource creation and usage will be enforced by the folder's [organization policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations). See [Resource locations supported services](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations-supported-services) for a list of all resources that can be restricted by the Resource Locations organization policy constraint, as some resources may be out of scope and unrestrictable. 
    8. Review the details about the control option you've selected, and click **Next**.
    9. (Optional) In the step to **Configure additional settings** , you can create a new project and a key ring for your [Customer Managed Encryption Keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek). No keys are created during this step, as Assured Workloads does not automatically create any cryptographic keys for you. See [Supporting compliance with key management](https://docs.cloud.google.com/assured-workloads/docs/key-management) for more information. **Note** : EU Data Boundary and Support does not require using CMEK; you can click **Next** to skip this step.
    10. In the step to **Review and create folder** , review the details about your new Assured Workloads folder and ensure that they are correct. Then, click **Create Folder**. 

After completing the steps above, Assured Workloads creates the following resources:

    * An Assured Workloads folder, which enforces security controls on [supported Google Cloud products](https://docs.cloud.google.com/assured-workloads/docs/supported-products) to adhere with the EU Data Boundary and Support control package. These controls include setting an organization policy that [restricts resource usage](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources) to only those supported products, and allows creating or using resources only in [allowed locations](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations). 
    * If you chose to create one, a CMEK project that contains the configured CMEK key ring. **Note** : Folder creation does not automatically create keys for you. After creating the folder, you must create an encryption key before adding any resources. See [Create and obtain a CMEK key](https://docs.cloud.google.com/assured-workloads/docs/create-and-obtain-cmek) to learn more. 

## Use your new Assured Workloads folder

To start using your Assured Workloads folder, it's important that you put the resources that you want to be compliant with EU Data Boundary and Support in the new folder. You can create projects inside of the folder along with [resources for supported products](https://docs.cloud.google.com/assured-workloads/docs/supported-products), or [migrate existing projects](https://docs.cloud.google.com/assured-workloads/docs/migrate-workload). Some possible next steps include the following:

    * Create a new project in the newly-created Assured Workloads folder, and then create a Compute Engine VM inside the project. The VM instance will be configured to meet the compliance requirements for EU Data Boundary and Support. 
    * [Analyze an existing project](https://docs.cloud.google.com/assured-workloads/docs/migrate-workload) that you want to make compliant with EU Data Boundary and Support, and make any of the required changes. Then, move the project to the newly-created Assured Workloads folder. 

### Enabling BigQuery in your folder

If your selected control package lists BigQuery as a supported service, BigQuery is supported, but it isn't automatically enabled when you create a new Assured Workloads folder due to an internal configuration process. This process normally finishes in ten minutes, but can take much longer in some circumstances. To check whether the process is finished and to enable BigQuery, complete the following steps:  

    1. In the Google Cloud console, go to the **Assured Workloads** page. 

[ Go to Assured Workloads](https://console.cloud.google.com/compliance/assuredworkloads)

    2. Select your new Assured Workloads folder from the list.
    3. On the **Folder Details** page in the **Allowed services** section, click **Review Available Updates**.
    4. In the **Allowed services** pane, review the services to be added to the [Resource Usage Restriction](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources) organization policy for the folder. If BigQuery services are listed, click **Allow Services** to add them.  
  
If BigQuery services are not listed, wait for the internal process to complete. If the services are not listed within 12 hours of folder creation, contact [Cloud Customer Care](https://docs.cloud.google.com/support). 

After the enablement process is completed, you can use BigQuery in your Assured Workloads folder.

Gemini in BigQuery is not supported by Assured Workloads.

  * ## Before you begin

If you haven't already, you must complete the following below to create an Assured Workloads folder for the [ EU Data Boundary with Access Justifications control package](https://docs.cloud.google.com/assured-workloads/docs/control-packages#eu-data-boundary-access-justifications):

    1. Ensure that you understand [Assured Workloads concepts](https://docs.cloud.google.com/assured-workloads/docs/overview). 
    2. If [Access Transparency](https://docs.cloud.google.com/assured-workloads/docs/access-transparency) is not enabled on your organization, it will automatically be enabled when you create an Assured Workloads folder. Any projects you create or move into the folder will be configured to use Access Transparency. 
    3. Ensure that you understand [how to get support](https://docs.cloud.google.com/assured-workloads/docs/getting-support) for Assured Workloads. 
    4. Ensure that you understand the [additional cost](https://docs.cloud.google.com/assured-workloads/pricing) when using EU Data Boundary with Access Justifications in Assured Workloads. 
    5. [Set up Cloud Identity](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin) and [verify your domain](https://docs.cloud.google.com/identity/docs/verify-domain). 
    6. After Cloud Identity has been configured, [create an organization](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization). 

### Required IAM roles

To create an Assured Workloads folder, you must be granted the **Assured Workloads Administrator** (`roles/assuredworkloads.admin`) role, which contains the minimum IAM permissions to create and manage Assured Workloads folders.

## Create an Assured Workloads folder for EU Data Boundary with Access Justifications

    1. In the Google Cloud console, go to the **Assured Workloads** page. 

[ Go to Assured Workloads](https://console.cloud.google.com/compliance/assuredworkloads)

    2. If prompted, select your organization.
    3. Click add_box**CREATE** to go to the **Create an Assured Workloads folder** page.
    4. In the step to **Add folder details** : 
       * In **Folder name** , enter a unique name for the folder, such as `aw-my-folder-name`. The folder name must be a minimum of 4 characters in length and a maximum of 30, and can only contain letters, numbers, spaces, and hyphens. **Tip:** When you name your Assured Workloads folders, consider the following: 
         * To identify the folder as an Assured Workloads folder, include a prefix in its name (such as `aw-`). This identifier can help you locate the folder from a list of other resources. 
         * Do not include sensitive data or personally identifiable information (PII) in the folder name. 
       * In **Organization** , select the organization in which to create your folder. This location can't be changed later.
       * In **Folder location** , select the location in the resource hierarchy where the folder will be created. An Assured Workloads folder can be created as a child of an organization or of another folder.
       * Click **Next**.
    5. In the step to **Choose a control package option** , select **Regional Controls** from the drop-down menu.
    6. Select **EU Data Boundary with Access Justifications** from the drop-down menu. See [Control packages](https://docs.cloud.google.com/assured-workloads/docs/control-packages) to learn about other options.
    7. In **Select resource location** , choose the [location](https://docs.cloud.google.com/assured-workloads/docs/locations) where resource creation and usage will be enforced by the folder's [organization policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations). See [Resource locations supported services](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations-supported-services) for a list of all resources that can be restricted by the Resource Locations organization policy constraint, as some resources may be out of scope and unrestrictable. 
    8. Review the details about the control option you've selected, and click **Next**.
    9. (Optional) In the step to **Configure additional settings** , you can create a new project and a key ring for your [Customer Managed Encryption Keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek). No keys are created during this step, as Assured Workloads does not automatically create any cryptographic keys for you. See [Supporting compliance with key management](https://docs.cloud.google.com/assured-workloads/docs/key-management) for more information. **Note** : EU Data Boundary with Access Justifications does not require using CMEK; you can click **Next** to skip this step.
    10. In the step to **Review and create folder** , review the details about your new Assured Workloads folder and ensure that they are correct. Then, click **Create Folder**. 

After completing the steps above, Assured Workloads creates the following resources:

    * An Assured Workloads folder, which enforces security controls on [supported Google Cloud products](https://docs.cloud.google.com/assured-workloads/docs/supported-products) to adhere with the EU Data Boundary with Access Justifications control package. These controls include setting an organization policy that [restricts resource usage](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources) to only those supported products, and allows creating or using resources only in [allowed locations](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations). 
    * If you chose to create one, a CMEK project that contains the configured CMEK key ring. **Note** : Folder creation does not automatically create keys for you. After creating the folder, you must create an encryption key before adding any resources. See [Create and obtain a CMEK key](https://docs.cloud.google.com/assured-workloads/docs/create-and-obtain-cmek) to learn more. 

## Use your new Assured Workloads folder

To start using your Assured Workloads folder, it's important that you put the resources that you want to be compliant with EU Data Boundary with Access Justifications in the new folder. You can create projects inside of the folder along with [resources for supported products](https://docs.cloud.google.com/assured-workloads/docs/supported-products), or [migrate existing projects](https://docs.cloud.google.com/assured-workloads/docs/migrate-workload). Some possible next steps include the following:

    * Create a new project in the newly-created Assured Workloads folder, and then create a Compute Engine VM inside the project. The VM instance will be configured to meet the compliance requirements for EU Data Boundary with Access Justifications. 
    * [Analyze an existing project](https://docs.cloud.google.com/assured-workloads/docs/migrate-workload) that you want to make compliant with EU Data Boundary with Access Justifications, and make any of the required changes. Then, move the project to the newly-created Assured Workloads folder. 

### Enabling BigQuery in your folder

If your selected control package lists BigQuery as a supported service, BigQuery is supported, but it isn't automatically enabled when you create a new Assured Workloads folder due to an internal configuration process. This process normally finishes in ten minutes, but can take much longer in some circumstances. To check whether the process is finished and to enable BigQuery, complete the following steps:  

    1. In the Google Cloud console, go to the **Assured Workloads** page. 

[ Go to Assured Workloads](https://console.cloud.google.com/compliance/assuredworkloads)

    2. Select your new Assured Workloads folder from the list.
    3. On the **Folder Details** page in the **Allowed services** section, click **Review Available Updates**.
    4. In the **Allowed services** pane, review the services to be added to the [Resource Usage Restriction](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources) organization policy for the folder. If BigQuery services are listed, click **Allow Services** to add them.  
  
If BigQuery services are not listed, wait for the internal process to complete. If the services are not listed within 12 hours of folder creation, contact [Cloud Customer Care](https://docs.cloud.google.com/support). 

After the enablement process is completed, you can use BigQuery in your Assured Workloads folder.

Gemini in BigQuery is not supported by Assured Workloads.

  * ## Before you begin

If you haven't already, you must complete the following below to create an Assured Workloads folder for the [ Hong Kong Data Boundary control package](https://docs.cloud.google.com/assured-workloads/docs/control-packages#hk-data-boundary):

    1. Ensure that you understand [Assured Workloads concepts](https://docs.cloud.google.com/assured-workloads/docs/overview). 
    2. If [Access Transparency](https://docs.cloud.google.com/assured-workloads/docs/access-transparency) is not enabled on your organization, it will automatically be enabled when you create an Assured Workloads folder. Any projects you create or move into the folder will be configured to use Access Transparency. 
    3. Ensure that you understand [how to get support](https://docs.cloud.google.com/assured-workloads/docs/getting-support) for Assured Workloads. 
    4. [Set up Cloud Identity](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin) and [verify your domain](https://docs.cloud.google.com/identity/docs/verify-domain). 
    5. After Cloud Identity has been configured, [create an organization](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization). 

### Required IAM roles

To create an Assured Workloads folder, you must be granted the **Assured Workloads Administrator** (`roles/assuredworkloads.admin`) role, which contains the minimum IAM permissions to create and manage Assured Workloads folders.

## Create an Assured Workloads folder for Hong Kong Data Boundary

    1. In the Google Cloud console, go to the **Assured Workloads** page. 

[ Go to Assured Workloads](https://console.cloud.google.com/compliance/assuredworkloads)

    2. If prompted, select your organization.
    3. Click add_box**CREATE** to go to the **Create an Assured Workloads folder** page.
    4. In the step to **Add folder details** : 
       * In **Folder name** , enter a unique name for the folder, such as `aw-my-folder-name`. The folder name must be a minimum of 4 characters in length and a maximum of 30, and can only contain letters, numbers, spaces, and hyphens. **Tip:** When you name your Assured Workloads folders, consider the following: 
         * To identify the folder as an Assured Workloads folder, include a prefix in its name (such as `aw-`). This identifier can help you locate the folder from a list of other resources. 
         * Do not include sensitive data or personally identifiable information (PII) in the folder name. 
       * In **Organization** , select the organization in which to create your folder. This location can't be changed later.
       * In **Folder location** , select the location in the resource hierarchy where the folder will be created. An Assured Workloads folder can be created as a child of an organization or of another folder.
       * Click **Next**.
    5. In the step to **Choose a control package option** , select **Regional Controls** from the drop-down menu.
    6. Select **Hong Kong Data Boundary** from the drop-down menu. See [Control packages](https://docs.cloud.google.com/assured-workloads/docs/control-packages) to learn about other options.
    7. In **Select resource location** , choose the [location](https://docs.cloud.google.com/assured-workloads/docs/locations) where resource creation and usage will be enforced by the folder's [organization policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations). See [Resource locations supported services](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations-supported-services) for a list of all resources that can be restricted by the Resource Locations organization policy constraint, as some resources may be out of scope and unrestrictable. 
    8. Review the details about the control option you've selected, and click **Next**.
    9. (Optional) In the step to **Configure additional settings** , you can create a new project and a key ring for your [Customer Managed Encryption Keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek). No keys are created during this step, as Assured Workloads does not automatically create any cryptographic keys for you. See [Supporting compliance with key management](https://docs.cloud.google.com/assured-workloads/docs/key-management) for more information. **Note** : Hong Kong Data Boundary does not require using CMEK; you can click **Next** to skip this step.
    10. In the step to **Review and create folder** , review the details about your new Assured Workloads folder and ensure that they are correct. Then, click **Create Folder**. 

After completing the steps above, Assured Workloads creates the following resources:

    * An Assured Workloads folder, which enforces security controls on [supported Google Cloud products](https://docs.cloud.google.com/assured-workloads/docs/supported-products) to adhere with the Hong Kong Data Boundary control package. These controls include setting an organization policy that [restricts resource usage](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources) to only those supported products, and allows creating or using resources only in [allowed locations](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations). 
    * If you chose to create one, a CMEK project that contains the configured CMEK key ring. **Note** : Folder creation does not automatically create keys for you. After creating the folder, you must create an encryption key before adding any resources. See [Create and obtain a CMEK key](https://docs.cloud.google.com/assured-workloads/docs/create-and-obtain-cmek) to learn more. 

## Use your new Assured Workloads folder

To start using your Assured Workloads folder, it's important that you put the resources that you want to be compliant with Hong Kong Data Boundary in the new folder. You can create projects inside of the folder along with [resources for supported products](https://docs.cloud.google.com/assured-workloads/docs/supported-products), or [migrate existing projects](https://docs.cloud.google.com/assured-workloads/docs/migrate-workload). Some possible next steps include the following:

    * Create a new project in the newly-created Assured Workloads folder, and then create a Compute Engine VM inside the project. The VM instance will be configured to meet the compliance requirements for Hong Kong Data Boundary. 
    * [Analyze an existing project](https://docs.cloud.google.com/assured-workloads/docs/migrate-workload) that you want to make compliant with Hong Kong Data Boundary, and make any of the required changes. Then, move the project to the newly-created Assured Workloads folder. 

### Enabling BigQuery in your folder

If your selected control package lists BigQuery as a supported service, BigQuery is supported, but it isn't automatically enabled when you create a new Assured Workloads folder due to an internal configuration process. This process normally finishes in ten minutes, but can take much longer in some circumstances. To check whether the process is finished and to enable BigQuery, complete the following steps:  

    1. In the Google Cloud console, go to the **Assured Workloads** page. 

[ Go to Assured Workloads](https://console.cloud.google.com/compliance/assuredworkloads)

    2. Select your new Assured Workloads folder from the list.
    3. On the **Folder Details** page in the **Allowed services** section, click **Review Available Updates**.
    4. In the **Allowed services** pane, review the services to be added to the [Resource Usage Restriction](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources) organization policy for the folder. If BigQuery services are listed, click **Allow Services** to add them.  
  
If BigQuery services are not listed, wait for the internal process to complete. If the services are not listed within 12 hours of folder creation, contact [Cloud Customer Care](https://docs.cloud.google.com/support). 

After the enablement process is completed, you can use BigQuery in your Assured Workloads folder.

Gemini in BigQuery is not supported by Assured Workloads.

  * ## Before you begin

If you haven't already, you must complete the following below to create an Assured Workloads folder for the [ India Data Boundary control package](https://docs.cloud.google.com/assured-workloads/docs/control-packages#in-data-boundary):

    1. Ensure that you understand [Assured Workloads concepts](https://docs.cloud.google.com/assured-workloads/docs/overview). 
    2. If [Access Transparency](https://docs.cloud.google.com/assured-workloads/docs/access-transparency) is not enabled on your organization, it will automatically be enabled when you create an Assured Workloads folder. Any projects you create or move into the folder will be configured to use Access Transparency. 
    3. Ensure that you understand [how to get support](https://docs.cloud.google.com/assured-workloads/docs/getting-support) for Assured Workloads. 
    4. [Set up Cloud Identity](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin) and [verify your domain](https://docs.cloud.google.com/identity/docs/verify-domain). 
    5. After Cloud Identity has been configured, [create an organization](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization). 

### Required IAM roles

To create an Assured Workloads folder, you must be granted the **Assured Workloads Administrator** (`roles/assuredworkloads.admin`) role, which contains the minimum IAM permissions to create and manage Assured Workloads folders.

## Create an Assured Workloads folder for India Data Boundary

    1. In the Google Cloud console, go to the **Assured Workloads** page. 

[ Go to Assured Workloads](https://console.cloud.google.com/compliance/assuredworkloads)

    2. If prompted, select your organization.
    3. Click add_box**CREATE** to go to the **Create an Assured Workloads folder** page.
    4. In the step to **Add folder details** : 
       * In **Folder name** , enter a unique name for the folder, such as `aw-my-folder-name`. The folder name must be a minimum of 4 characters in length and a maximum of 30, and can only contain letters, numbers, spaces, and hyphens. **Tip:** When you name your Assured Workloads folders, consider the following: 
         * To identify the folder as an Assured Workloads folder, include a prefix in its name (such as `aw-`). This identifier can help you locate the folder from a list of other resources. 
         * Do not include sensitive data or personally identifiable information (PII) in the folder name. 
       * In **Organization** , select the organization in which to create your folder. This location can't be changed later.
       * In **Folder location** , select the location in the resource hierarchy where the folder will be created. An Assured Workloads folder can be created as a child of an organization or of another folder.
       * Click **Next**.
    5. In the step to **Choose a control package option** , select **Regional Controls** from the drop-down menu.
    6. Select **India Data Boundary** from the drop-down menu. See [Control packages](https://docs.cloud.google.com/assured-workloads/docs/control-packages) to learn about other options.
    7. In **Select resource location** , choose the [location](https://docs.cloud.google.com/assured-workloads/docs/locations) where resource creation and usage will be enforced by the folder's [organization policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations). See [Resource locations supported services](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations-supported-services) for a list of all resources that can be restricted by the Resource Locations organization policy constraint, as some resources may be out of scope and unrestrictable. 
    8. Review the details about the control option you've selected, and click **Next**.
    9. (Optional) In the step to **Configure additional settings** , you can create a new project and a key ring for your [Customer Managed Encryption Keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek). No keys are created during this step, as Assured Workloads does not automatically create any cryptographic keys for you. See [Supporting compliance with key management](https://docs.cloud.google.com/assured-workloads/docs/key-management) for more information. **Note** : India Data Boundary does not require using CMEK; you can click **Next** to skip this step.
    10. In the step to **Review and create folder** , review the details about your new Assured Workloads folder and ensure that they are correct. Then, click **Create Folder**. 

After completing the steps above, Assured Workloads creates the following resources:

    * An Assured Workloads folder, which enforces security controls on [supported Google Cloud products](https://docs.cloud.google.com/assured-workloads/docs/supported-products) to adhere with the India Data Boundary control package. These controls include setting an organization policy that [restricts resource usage](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources) to only those supported products, and allows creating or using resources only in [allowed locations](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations). 
    * If you chose to create one, a CMEK project that contains the configured CMEK key ring. **Note** : Folder creation does not automatically create keys for you. After creating the folder, you must create an encryption key before adding any resources. See [Create and obtain a CMEK key](https://docs.cloud.google.com/assured-workloads/docs/create-and-obtain-cmek) to learn more. 

## Use your new Assured Workloads folder

To start using your Assured Workloads folder, it's important that you put the resources that you want to be compliant with India Data Boundary in the new folder. You can create projects inside of the folder along with [resources for supported products](https://docs.cloud.google.com/assured-workloads/docs/supported-products), or [migrate existing projects](https://docs.cloud.google.com/assured-workloads/docs/migrate-workload). Some possible next steps include the following:

    * Create a new project in the newly-created Assured Workloads folder, and then create a Compute Engine VM inside the project. The VM instance will be configured to meet the compliance requirements for India Data Boundary. 
    * [Analyze an existing project](https://docs.cloud.google.com/assured-workloads/docs/migrate-workload) that you want to make compliant with India Data Boundary, and make any of the required changes. Then, move the project to the newly-created Assured Workloads folder. 

### Enabling BigQuery in your folder

If your selected control package lists BigQuery as a supported service, BigQuery is supported, but it isn't automatically enabled when you create a new Assured Workloads folder due to an internal configuration process. This process normally finishes in ten minutes, but can take much longer in some circumstances. To check whether the process is finished and to enable BigQuery, complete the following steps:  

    1. In the Google Cloud console, go to the **Assured Workloads** page. 

[ Go to Assured Workloads](https://console.cloud.google.com/compliance/assuredworkloads)

    2. Select your new Assured Workloads folder from the list.
    3. On the **Folder Details** page in the **Allowed services** section, click **Review Available Updates**.
    4. In the **Allowed services** pane, review the services to be added to the [Resource Usage Restriction](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources) organization policy for the folder. If BigQuery services are listed, click **Allow Services** to add them.  
  
If BigQuery services are not listed, wait for the internal process to complete. If the services are not listed within 12 hours of folder creation, contact [Cloud Customer Care](https://docs.cloud.google.com/support). 

After the enablement process is completed, you can use BigQuery in your Assured Workloads folder.

Gemini in BigQuery is not supported by Assured Workloads.

  * ## Before you begin

If you haven't already, you must complete the following below to create an Assured Workloads folder for the [ Indonesia Data Boundary control package](https://docs.cloud.google.com/assured-workloads/docs/control-packages#id-data-boundary):

    1. Ensure that you understand [Assured Workloads concepts](https://docs.cloud.google.com/assured-workloads/docs/overview). 
    2. If [Access Transparency](https://docs.cloud.google.com/assured-workloads/docs/access-transparency) is not enabled on your organization, it will automatically be enabled when you create an Assured Workloads folder. Any projects you create or move into the folder will be configured to use Access Transparency. 
    3. Ensure that you understand [how to get support](https://docs.cloud.google.com/assured-workloads/docs/getting-support) for Assured Workloads. 
    4. [Set up Cloud Identity](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin) and [verify your domain](https://docs.cloud.google.com/identity/docs/verify-domain). 
    5. After Cloud Identity has been configured, [create an organization](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization). 

### Required IAM roles

To create an Assured Workloads folder, you must be granted the **Assured Workloads Administrator** (`roles/assuredworkloads.admin`) role, which contains the minimum IAM permissions to create and manage Assured Workloads folders.

## Create an Assured Workloads folder for Indonesia Data Boundary

    1. In the Google Cloud console, go to the **Assured Workloads** page. 

[ Go to Assured Workloads](https://console.cloud.google.com/compliance/assuredworkloads)

    2. If prompted, select your organization.
    3. Click add_box**CREATE** to go to the **Create an Assured Workloads folder** page.
    4. In the step to **Add folder details** : 
       * In **Folder name** , enter a unique name for the folder, such as `aw-my-folder-name`. The folder name must be a minimum of 4 characters in length and a maximum of 30, and can only contain letters, numbers, spaces, and hyphens. **Tip:** When you name your Assured Workloads folders, consider the following: 
         * To identify the folder as an Assured Workloads folder, include a prefix in its name (such as `aw-`). This identifier can help you locate the folder from a list of other resources. 
         * Do not include sensitive data or personally identifiable information (PII) in the folder name. 
       * In **Organization** , select the organization in which to create your folder. This location can't be changed later.
       * In **Folder location** , select the location in the resource hierarchy where the folder will be created. An Assured Workloads folder can be created as a child of an organization or of another folder.
       * Click **Next**.
    5. In the step to **Choose a control package option** , select **Regional Controls** from the drop-down menu.
    6. Select **Indonesia Data Boundary** from the drop-down menu. See [Control packages](https://docs.cloud.google.com/assured-workloads/docs/control-packages) to learn about other options.
    7. In **Select resource location** , choose the [location](https://docs.cloud.google.com/assured-workloads/docs/locations) where resource creation and usage will be enforced by the folder's [organization policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations). See [Resource locations supported services](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations-supported-services) for a list of all resources that can be restricted by the Resource Locations organization policy constraint, as some resources may be out of scope and unrestrictable. 
    8. Review the details about the control option you've selected, and click **Next**.
    9. (Optional) In the step to **Configure additional settings** , you can create a new project and a key ring for your [Customer Managed Encryption Keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek). No keys are created during this step, as Assured Workloads does not automatically create any cryptographic keys for you. See [Supporting compliance with key management](https://docs.cloud.google.com/assured-workloads/docs/key-management) for more information. **Note** : Indonesia Data Boundary does not require using CMEK; you can click **Next** to skip this step.
    10. In the step to **Review and create folder** , review the details about your new Assured Workloads folder and ensure that they are correct. Then, click **Create Folder**. 

After completing the steps above, Assured Workloads creates the following resources:

    * An Assured Workloads folder, which enforces security controls on [supported Google Cloud products](https://docs.cloud.google.com/assured-workloads/docs/supported-products) to adhere with the Indonesia Data Boundary control package. These controls include setting an organization policy that [restricts resource usage](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources) to only those supported products, and allows creating or using resources only in [allowed locations](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations). 
    * If you chose to create one, a CMEK project that contains the configured CMEK key ring. **Note** : Folder creation does not automatically create keys for you. After creating the folder, you must create an encryption key before adding any resources. See [Create and obtain a CMEK key](https://docs.cloud.google.com/assured-workloads/docs/create-and-obtain-cmek) to learn more. 

## Use your new Assured Workloads folder

To start using your Assured Workloads folder, it's important that you put the resources that you want to be compliant with Indonesia Data Boundary in the new folder. You can create projects inside of the folder along with [resources for supported products](https://docs.cloud.google.com/assured-workloads/docs/supported-products), or [migrate existing projects](https://docs.cloud.google.com/assured-workloads/docs/migrate-workload). Some possible next steps include the following:

    * Create a new project in the newly-created Assured Workloads folder, and then create a Compute Engine VM inside the project. The VM instance will be configured to meet the compliance requirements for Indonesia Data Boundary. 
    * [Analyze an existing project](https://docs.cloud.google.com/assured-workloads/docs/migrate-workload) that you want to make compliant with Indonesia Data Boundary, and make any of the required changes. Then, move the project to the newly-created Assured Workloads folder. 

### Enabling BigQuery in your folder

If your selected control package lists BigQuery as a supported service, BigQuery is supported, but it isn't automatically enabled when you create a new Assured Workloads folder due to an internal configuration process. This process normally finishes in ten minutes, but can take much longer in some circumstances. To check whether the process is finished and to enable BigQuery, complete the following steps:  

    1. In the Google Cloud console, go to the **Assured Workloads** page. 

[ Go to Assured Workloads](https://console.cloud.google.com/compliance/assuredworkloads)

    2. Select your new Assured Workloads folder from the list.
    3. On the **Folder Details** page in the **Allowed services** section, click **Review Available Updates**.
    4. In the **Allowed services** pane, review the services to be added to the [Resource Usage Restriction](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources) organization policy for the folder. If BigQuery services are listed, click **Allow Services** to add them.  
  
If BigQuery services are not listed, wait for the internal process to complete. If the services are not listed within 12 hours of folder creation, contact [Cloud Customer Care](https://docs.cloud.google.com/support). 

After the enablement process is completed, you can use BigQuery in your Assured Workloads folder.

Gemini in BigQuery is not supported by Assured Workloads.

  * ## Before you begin

If you haven't already, you must complete the following below to create an Assured Workloads folder for the [ Israel Data Boundary control package](https://docs.cloud.google.com/assured-workloads/docs/control-packages#il-data-boundary):

    1. Ensure that you understand [Assured Workloads concepts](https://docs.cloud.google.com/assured-workloads/docs/overview). 
    2. If [Access Transparency](https://docs.cloud.google.com/assured-workloads/docs/access-transparency) is not enabled on your organization, it will automatically be enabled when you create an Assured Workloads folder. Any projects you create or move into the folder will be configured to use Access Transparency. 
    3. Ensure that you understand [how to get support](https://docs.cloud.google.com/assured-workloads/docs/getting-support) for Assured Workloads. 
    4. [Set up Cloud Identity](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin) and [verify your domain](https://docs.cloud.google.com/identity/docs/verify-domain). 
    5. After Cloud Identity has been configured, [create an organization](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization). 

### Required IAM roles

To create an Assured Workloads folder, you must be granted the **Assured Workloads Administrator** (`roles/assuredworkloads.admin`) role, which contains the minimum IAM permissions to create and manage Assured Workloads folders.

## Create an Assured Workloads folder for Israel Data Boundary

    1. In the Google Cloud console, go to the **Assured Workloads** page. 

[ Go to Assured Workloads](https://console.cloud.google.com/compliance/assuredworkloads)

    2. If prompted, select your organization.
    3. Click add_box**CREATE** to go to the **Create an Assured Workloads folder** page.
    4. In the step to **Add folder details** : 
       * In **Folder name** , enter a unique name for the folder, such as `aw-my-folder-name`. The folder name must be a minimum of 4 characters in length and a maximum of 30, and can only contain letters, numbers, spaces, and hyphens. **Tip:** When you name your Assured Workloads folders, consider the following: 
         * To identify the folder as an Assured Workloads folder, include a prefix in its name (such as `aw-`). This identifier can help you locate the folder from a list of other resources. 
         * Do not include sensitive data or personally identifiable information (PII) in the folder name. 
       * In **Organization** , select the organization in which to create your folder. This location can't be changed later.
       * In **Folder location** , select the location in the resource hierarchy where the folder will be created. An Assured Workloads folder can be created as a child of an organization or of another folder.
       * Click **Next**.
    5. In the step to **Choose a control package option** , select **Regional Controls** from the drop-down menu.
    6. Select **Israel Data Boundary** from the drop-down menu. See [Control packages](https://docs.cloud.google.com/assured-workloads/docs/control-packages) to learn about other options.
    7. In **Select resource location** , choose the [location](https://docs.cloud.google.com/assured-workloads/docs/locations) where resource creation and usage will be enforced by the folder's [organization policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations). See [Resource locations supported services](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations-supported-services) for a list of all resources that can be restricted by the Resource Locations organization policy constraint, as some resources may be out of scope and unrestrictable. 
    8. Review the details about the control option you've selected, and click **Next**.
    9. (Optional) In the step to **Configure additional settings** , you can create a new project and a key ring for your [Customer Managed Encryption Keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek). No keys are created during this step, as Assured Workloads does not automatically create any cryptographic keys for you. See [Supporting compliance with key management](https://docs.cloud.google.com/assured-workloads/docs/key-management) for more information. **Note** : Israel Data Boundary does not require using CMEK; you can click **Next** to skip this step.
    10. In the step to **Review and create folder** , review the details about your new Assured Workloads folder and ensure that they are correct. Then, click **Create Folder**. 

After completing the steps above, Assured Workloads creates the following resources:

    * An Assured Workloads folder, which enforces security controls on [supported Google Cloud products](https://docs.cloud.google.com/assured-workloads/docs/supported-products) to adhere with the Israel Data Boundary control package. These controls include setting an organization policy that [restricts resource usage](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources) to only those supported products, and allows creating or using resources only in [allowed locations](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations). 
    * If you chose to create one, a CMEK project that contains the configured CMEK key ring. **Note** : Folder creation does not automatically create keys for you. After creating the folder, you must create an encryption key before adding any resources. See [Create and obtain a CMEK key](https://docs.cloud.google.com/assured-workloads/docs/create-and-obtain-cmek) to learn more. 

## Use your new Assured Workloads folder

To start using your Assured Workloads folder, it's important that you put the resources that you want to be compliant with Israel Data Boundary in the new folder. You can create projects inside of the folder along with [resources for supported products](https://docs.cloud.google.com/assured-workloads/docs/supported-products), or [migrate existing projects](https://docs.cloud.google.com/assured-workloads/docs/migrate-workload). Some possible next steps include the following:

    * Create a new project in the newly-created Assured Workloads folder, and then create a Compute Engine VM inside the project. The VM instance will be configured to meet the compliance requirements for Israel Data Boundary. 
    * [Analyze an existing project](https://docs.cloud.google.com/assured-workloads/docs/migrate-workload) that you want to make compliant with Israel Data Boundary, and make any of the required changes. Then, move the project to the newly-created Assured Workloads folder. 

### Enabling BigQuery in your folder

If your selected control package lists BigQuery as a supported service, BigQuery is supported, but it isn't automatically enabled when you create a new Assured Workloads folder due to an internal configuration process. This process normally finishes in ten minutes, but can take much longer in some circumstances. To check whether the process is finished and to enable BigQuery, complete the following steps:  

    1. In the Google Cloud console, go to the **Assured Workloads** page. 

[ Go to Assured Workloads](https://console.cloud.google.com/compliance/assuredworkloads)

    2. Select your new Assured Workloads folder from the list.
    3. On the **Folder Details** page in the **Allowed services** section, click **Review Available Updates**.
    4. In the **Allowed services** pane, review the services to be added to the [Resource Usage Restriction](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources) organization policy for the folder. If BigQuery services are listed, click **Allow Services** to add them.  
  
If BigQuery services are not listed, wait for the internal process to complete. If the services are not listed within 12 hours of folder creation, contact [Cloud Customer Care](https://docs.cloud.google.com/support). 

After the enablement process is completed, you can use BigQuery in your Assured Workloads folder.

Gemini in BigQuery is not supported by Assured Workloads.

  * ## Before you begin

If you haven't already, you must complete the following below to create an Assured Workloads folder for the [ Israel Data Boundary and Support control package](https://docs.cloud.google.com/assured-workloads/docs/control-packages#il-data-boundary-support):

    1. Ensure that you understand [Assured Workloads concepts](https://docs.cloud.google.com/assured-workloads/docs/overview). 
    2. If [Access Transparency](https://docs.cloud.google.com/assured-workloads/docs/access-transparency) is not enabled on your organization, it will automatically be enabled when you create an Assured Workloads folder. Any projects you create or move into the folder will be configured to use Access Transparency. 
    3. Ensure that you understand [how to get support](https://docs.cloud.google.com/assured-workloads/docs/getting-support) for Assured Workloads. 
    4. Ensure that you understand the [additional cost](https://docs.cloud.google.com/assured-workloads/pricing) when using Israel Data Boundary and Support in Assured Workloads. 
    5. [Set up Cloud Identity](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin) and [verify your domain](https://docs.cloud.google.com/identity/docs/verify-domain). 
    6. After Cloud Identity has been configured, [create an organization](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization). 

### Required IAM roles

To create an Assured Workloads folder, you must be granted the **Assured Workloads Administrator** (`roles/assuredworkloads.admin`) role, which contains the minimum IAM permissions to create and manage Assured Workloads folders.

## Create an Assured Workloads folder for Israel Data Boundary and Support

    1. In the Google Cloud console, go to the **Assured Workloads** page. 

[ Go to Assured Workloads](https://console.cloud.google.com/compliance/assuredworkloads)

    2. If prompted, select your organization.
    3. Click add_box**CREATE** to go to the **Create an Assured Workloads folder** page.
    4. In the step to **Add folder details** : 
       * In **Folder name** , enter a unique name for the folder, such as `aw-my-folder-name`. The folder name must be a minimum of 4 characters in length and a maximum of 30, and can only contain letters, numbers, spaces, and hyphens. **Tip:** When you name your Assured Workloads folders, consider the following: 
         * To identify the folder as an Assured Workloads folder, include a prefix in its name (such as `aw-`). This identifier can help you locate the folder from a list of other resources. 
         * Do not include sensitive data or personally identifiable information (PII) in the folder name. 
       * In **Organization** , select the organization in which to create your folder. This location can't be changed later.
       * In **Folder location** , select the location in the resource hierarchy where the folder will be created. An Assured Workloads folder can be created as a child of an organization or of another folder.
       * Click **Next**.
    5. In the step to **Choose a control package option** , select **Regional Controls** from the drop-down menu.
    6. Select **Israel Data Boundary and Support** from the drop-down menu. See [Control packages](https://docs.cloud.google.com/assured-workloads/docs/control-packages) to learn about other options.
    7. In **Select resource location** , choose the [location](https://docs.cloud.google.com/assured-workloads/docs/locations) where resource creation and usage will be enforced by the folder's [organization policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations). See [Resource locations supported services](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations-supported-services) for a list of all resources that can be restricted by the Resource Locations organization policy constraint, as some resources may be out of scope and unrestrictable. 
    8. Review the details about the control option you've selected, and click **Next**.
    9. (Optional) In the step to **Configure additional settings** , you can create a new project and a key ring for your [Customer Managed Encryption Keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek). No keys are created during this step, as Assured Workloads does not automatically create any cryptographic keys for you. See [Supporting compliance with key management](https://docs.cloud.google.com/assured-workloads/docs/key-management) for more information. **Note** : Israel Data Boundary and Support does not require using CMEK; you can click **Next** to skip this step.
    10. In the step to **Review and create folder** , review the details about your new Assured Workloads folder and ensure that they are correct. Then, click **Create Folder**. 

After completing the steps above, Assured Workloads creates the following resources:

    * An Assured Workloads folder, which enforces security controls on [supported Google Cloud products](https://docs.cloud.google.com/assured-workloads/docs/supported-products) to adhere with the Israel Data Boundary and Support control package. These controls include setting an organization policy that [restricts resource usage](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources) to only those supported products, and allows creating or using resources only in [allowed locations](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations). 
    * If you chose to create one, a CMEK project that contains the configured CMEK key ring. **Note** : Folder creation does not automatically create keys for you. After creating the folder, you must create an encryption key before adding any resources. See [Create and obtain a CMEK key](https://docs.cloud.google.com/assured-workloads/docs/create-and-obtain-cmek) to learn more. 

## Use your new Assured Workloads folder

To start using your Assured Workloads folder, it's important that you put the resources that you want to be compliant with Israel Data Boundary and Support in the new folder. You can create projects inside of the folder along with [resources for supported products](https://docs.cloud.google.com/assured-workloads/docs/supported-products), or [migrate existing projects](https://docs.cloud.google.com/assured-workloads/docs/migrate-workload). Some possible next steps include the following:

    * Create a new project in the newly-created Assured Workloads folder, and then create a Compute Engine VM inside the project. The VM instance will be configured to meet the compliance requirements for Israel Data Boundary and Support. 
    * [Analyze an existing project](https://docs.cloud.google.com/assured-workloads/docs/migrate-workload) that you want to make compliant with Israel Data Boundary and Support, and make any of the required changes. Then, move the project to the newly-created Assured Workloads folder. 

### Enabling BigQuery in your folder

If your selected control package lists BigQuery as a supported service, BigQuery is supported, but it isn't automatically enabled when you create a new Assured Workloads folder due to an internal configuration process. This process normally finishes in ten minutes, but can take much longer in some circumstances. To check whether the process is finished and to enable BigQuery, complete the following steps:  

    1. In the Google Cloud console, go to the **Assured Workloads** page. 

[ Go to Assured Workloads](https://console.cloud.google.com/compliance/assuredworkloads)

    2. Select your new Assured Workloads folder from the list.
    3. On the **Folder Details** page in the **Allowed services** section, click **Review Available Updates**.
    4. In the **Allowed services** pane, review the services to be added to the [Resource Usage Restriction](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources) organization policy for the folder. If BigQuery services are listed, click **Allow Services** to add them.  
  
If BigQuery services are not listed, wait for the internal process to complete. If the services are not listed within 12 hours of folder creation, contact [Cloud Customer Care](https://docs.cloud.google.com/support). 

After the enablement process is completed, you can use BigQuery in your Assured Workloads folder.

Gemini in BigQuery is not supported by Assured Workloads.

  * ## Before you begin

If you haven't already, you must complete the following below to create an Assured Workloads folder for the [ Japan Data Boundary control package](https://docs.cloud.google.com/assured-workloads/docs/control-packages#jp-data-boundary):

    1. Ensure that you understand [Assured Workloads concepts](https://docs.cloud.google.com/assured-workloads/docs/overview). 
    2. If [Access Transparency](https://docs.cloud.google.com/assured-workloads/docs/access-transparency) is not enabled on your organization, it will automatically be enabled when you create an Assured Workloads folder. Any projects you create or move into the folder will be configured to use Access Transparency. 
    3. Ensure that you understand [how to get support](https://docs.cloud.google.com/assured-workloads/docs/getting-support) for Assured Workloads. 
    4. [Set up Cloud Identity](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin) and [verify your domain](https://docs.cloud.google.com/identity/docs/verify-domain). 
    5. After Cloud Identity has been configured, [create an organization](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization). 

### Required IAM roles

To create an Assured Workloads folder, you must be granted the **Assured Workloads Administrator** (`roles/assuredworkloads.admin`) role, which contains the minimum IAM permissions to create and manage Assured Workloads folders.

## Create an Assured Workloads folder for Japan Data Boundary

    1. In the Google Cloud console, go to the **Assured Workloads** page. 

[ Go to Assured Workloads](https://console.cloud.google.com/compliance/assuredworkloads)

    2. If prompted, select your organization.
    3. Click add_box**CREATE** to go to the **Create an Assured Workloads folder** page.
    4. In the step to **Add folder details** : 
       * In **Folder name** , enter a unique name for the folder, such as `aw-my-folder-name`. The folder name must be a minimum of 4 characters in length and a maximum of 30, and can only contain letters, numbers, spaces, and hyphens. **Tip:** When you name your Assured Workloads folders, consider the following: 
         * To identify the folder as an Assured Workloads folder, include a prefix in its name (such as `aw-`). This identifier can help you locate the folder from a list of other resources. 
         * Do not include sensitive data or personally identifiable information (PII) in the folder name. 
       * In **Organization** , select the organization in which to create your folder. This location can't be changed later.
       * In **Folder location** , select the location in the resource hierarchy where the folder will be created. An Assured Workloads folder can be created as a child of an organization or of another folder.
       * Click **Next**.
    5. In the step to **Choose a control package option** , select **Regional Controls** from the drop-down menu.
    6. Select **Japan Data Boundary** from the drop-down menu. See [Control packages](https://docs.cloud.google.com/assured-workloads/docs/control-packages) to learn about other options.
    7. In **Select resource location** , choose the [location](https://docs.cloud.google.com/assured-workloads/docs/locations) where resource creation and usage will be enforced by the folder's [organization policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations). See [Resource locations supported services](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations-supported-services) for a list of all resources that can be restricted by the Resource Locations organization policy constraint, as some resources may be out of scope and unrestrictable. 
    8. Review the details about the control option you've selected, and click **Next**.
    9. (Optional) In the step to **Configure additional settings** , you can create a new project and a key ring for your [Customer Managed Encryption Keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek). No keys are created during this step, as Assured Workloads does not automatically create any cryptographic keys for you. See [Supporting compliance with key management](https://docs.cloud.google.com/assured-workloads/docs/key-management) for more information. **Note** : Japan Data Boundary does not require using CMEK; you can click **Next** to skip this step.
    10. In the step to **Review and create folder** , review the details about your new Assured Workloads folder and ensure that they are correct. Then, click **Create Folder**. 

After completing the steps above, Assured Workloads creates the following resources:

    * An Assured Workloads folder, which enforces security controls on [supported Google Cloud products](https://docs.cloud.google.com/assured-workloads/docs/supported-products) to adhere with the Japan Data Boundary control package. These controls include setting an organization policy that [restricts resource usage](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources) to only those supported products, and allows creating or using resources only in [allowed locations](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations). 
    * If you chose to create one, a CMEK project that contains the configured CMEK key ring. **Note** : Folder creation does not automatically create keys for you. After creating the folder, you must create an encryption key before adding any resources. See [Create and obtain a CMEK key](https://docs.cloud.google.com/assured-workloads/docs/create-and-obtain-cmek) to learn more. 

## Use your new Assured Workloads folder

To start using your Assured Workloads folder, it's important that you put the resources that you want to be compliant with Japan Data Boundary in the new folder. You can create projects inside of the folder along with [resources for supported products](https://docs.cloud.google.com/assured-workloads/docs/supported-products), or [migrate existing projects](https://docs.cloud.google.com/assured-workloads/docs/migrate-workload). Some possible next steps include the following:

    * Create a new project in the newly-created Assured Workloads folder, and then create a Compute Engine VM inside the project. The VM instance will be configured to meet the compliance requirements for Japan Data Boundary. 
    * [Analyze an existing project](https://docs.cloud.google.com/assured-workloads/docs/migrate-workload) that you want to make compliant with Japan Data Boundary, and make any of the required changes. Then, move the project to the newly-created Assured Workloads folder. 

### Enabling BigQuery in your folder

If your selected control package lists BigQuery as a supported service, BigQuery is supported, but it isn't automatically enabled when you create a new Assured Workloads folder due to an internal configuration process. This process normally finishes in ten minutes, but can take much longer in some circumstances. To check whether the process is finished and to enable BigQuery, complete the following steps:  

    1. In the Google Cloud console, go to the **Assured Workloads** page. 

[ Go to Assured Workloads](https://console.cloud.google.com/compliance/assuredworkloads)

    2. Select your new Assured Workloads folder from the list.
    3. On the **Folder Details** page in the **Allowed services** section, click **Review Available Updates**.
    4. In the **Allowed services** pane, review the services to be added to the [Resource Usage Restriction](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources) organization policy for the folder. If BigQuery services are listed, click **Allow Services** to add them.  
  
If BigQuery services are not listed, wait for the internal process to complete. If the services are not listed within 12 hours of folder creation, contact [Cloud Customer Care](https://docs.cloud.google.com/support). 

After the enablement process is completed, you can use BigQuery in your Assured Workloads folder.

Gemini in BigQuery is not supported by Assured Workloads.

  * ## Before you begin

If you haven't already, you must complete the following below to create an Assured Workloads folder for the [ Qatar Data Boundary control package](https://docs.cloud.google.com/assured-workloads/docs/control-packages#qa-data-boundary):

    1. Ensure that you understand [Assured Workloads concepts](https://docs.cloud.google.com/assured-workloads/docs/overview). 
    2. If [Access Transparency](https://docs.cloud.google.com/assured-workloads/docs/access-transparency) is not enabled on your organization, it will automatically be enabled when you create an Assured Workloads folder. Any projects you create or move into the folder will be configured to use Access Transparency. 
    3. Ensure that you understand [how to get support](https://docs.cloud.google.com/assured-workloads/docs/getting-support) for Assured Workloads. 
    4. [Set up Cloud Identity](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin) and [verify your domain](https://docs.cloud.google.com/identity/docs/verify-domain). 
    5. After Cloud Identity has been configured, [create an organization](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization). 

### Required IAM roles

To create an Assured Workloads folder, you must be granted the **Assured Workloads Administrator** (`roles/assuredworkloads.admin`) role, which contains the minimum IAM permissions to create and manage Assured Workloads folders.

## Create an Assured Workloads folder for Qatar Data Boundary

    1. In the Google Cloud console, go to the **Assured Workloads** page. 

[ Go to Assured Workloads](https://console.cloud.google.com/compliance/assuredworkloads)

    2. If prompted, select your organization.
    3. Click add_box**CREATE** to go to the **Create an Assured Workloads folder** page.
    4. In the step to **Add folder details** : 
       * In **Folder name** , enter a unique name for the folder, such as `aw-my-folder-name`. The folder name must be a minimum of 4 characters in length and a maximum of 30, and can only contain letters, numbers, spaces, and hyphens. **Tip:** When you name your Assured Workloads folders, consider the following: 
         * To identify the folder as an Assured Workloads folder, include a prefix in its name (such as `aw-`). This identifier can help you locate the folder from a list of other resources. 
         * Do not include sensitive data or personally identifiable information (PII) in the folder name. 
       * In **Organization** , select the organization in which to create your folder. This location can't be changed later.
       * In **Folder location** , select the location in the resource hierarchy where the folder will be created. An Assured Workloads folder can be created as a child of an organization or of another folder.
       * Click **Next**.
    5. In the step to **Choose a control package option** , select **Regional Controls** from the drop-down menu.
    6. Select **Qatar Data Boundary** from the drop-down menu. See [Control packages](https://docs.cloud.google.com/assured-workloads/docs/control-packages) to learn about other options.
    7. In **Select resource location** , choose the [location](https://docs.cloud.google.com/assured-workloads/docs/locations) where resource creation and usage will be enforced by the folder's [organization policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations). See [Resource locations supported services](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations-supported-services) for a list of all resources that can be restricted by the Resource Locations organization policy constraint, as some resources may be out of scope and unrestrictable. 
    8. Review the details about the control option you've selected, and click **Next**.
    9. (Optional) In the step to **Configure additional settings** , you can create a new project and a key ring for your [Customer Managed Encryption Keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek). No keys are created during this step, as Assured Workloads does not automatically create any cryptographic keys for you. See [Supporting compliance with key management](https://docs.cloud.google.com/assured-workloads/docs/key-management) for more information. **Note** : Qatar Data Boundary does not require using CMEK; you can click **Next** to skip this step.
    10. In the step to **Review and create folder** , review the details about your new Assured Workloads folder and ensure that they are correct. Then, click **Create Folder**. 

After completing the steps above, Assured Workloads creates the following resources:

    * An Assured Workloads folder, which enforces security controls on [supported Google Cloud products](https://docs.cloud.google.com/assured-workloads/docs/supported-products) to adhere with the Qatar Data Boundary control package. These controls include setting an organization policy that [restricts resource usage](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources) to only those supported products, and allows creating or using resources only in [allowed locations](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations). 
    * If you chose to create one, a CMEK project that contains the configured CMEK key ring. **Note** : Folder creation does not automatically create keys for you. After creating the folder, you must create an encryption key before adding any resources. See [Create and obtain a CMEK key](https://docs.cloud.google.com/assured-workloads/docs/create-and-obtain-cmek) to learn more. 

## Use your new Assured Workloads folder

To start using your Assured Workloads folder, it's important that you put the resources that you want to be compliant with Qatar Data Boundary in the new folder. You can create projects inside of the folder along with [resources for supported products](https://docs.cloud.google.com/assured-workloads/docs/supported-products), or [migrate existing projects](https://docs.cloud.google.com/assured-workloads/docs/migrate-workload). Some possible next steps include the following:

    * Create a new project in the newly-created Assured Workloads folder, and then create a Compute Engine VM inside the project. The VM instance will be configured to meet the compliance requirements for Qatar Data Boundary. 
    * [Analyze an existing project](https://docs.cloud.google.com/assured-workloads/docs/migrate-workload) that you want to make compliant with Qatar Data Boundary, and make any of the required changes. Then, move the project to the newly-created Assured Workloads folder. 

### Enabling BigQuery in your folder

If your selected control package lists BigQuery as a supported service, BigQuery is supported, but it isn't automatically enabled when you create a new Assured Workloads folder due to an internal configuration process. This process normally finishes in ten minutes, but can take much longer in some circumstances. To check whether the process is finished and to enable BigQuery, complete the following steps:  

    1. In the Google Cloud console, go to the **Assured Workloads** page. 

[ Go to Assured Workloads](https://console.cloud.google.com/compliance/assuredworkloads)

    2. Select your new Assured Workloads folder from the list.
    3. On the **Folder Details** page in the **Allowed services** section, click **Review Available Updates**.
    4. In the **Allowed services** pane, review the services to be added to the [Resource Usage Restriction](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources) organization policy for the folder. If BigQuery services are listed, click **Allow Services** to add them.  
  
If BigQuery services are not listed, wait for the internal process to complete. If the services are not listed within 12 hours of folder creation, contact [Cloud Customer Care](https://docs.cloud.google.com/support). 

After the enablement process is completed, you can use BigQuery in your Assured Workloads folder.

Gemini in BigQuery is not supported by Assured Workloads.

  * ## Before you begin

If you haven't already, you must complete the following below to create an Assured Workloads folder for the [ Singapore Data Boundary control package](https://docs.cloud.google.com/assured-workloads/docs/control-packages#sg-data-boundary):

    1. Ensure that you understand [Assured Workloads concepts](https://docs.cloud.google.com/assured-workloads/docs/overview). 
    2. If [Access Transparency](https://docs.cloud.google.com/assured-workloads/docs/access-transparency) is not enabled on your organization, it will automatically be enabled when you create an Assured Workloads folder. Any projects you create or move into the folder will be configured to use Access Transparency. 
    3. Ensure that you understand [how to get support](https://docs.cloud.google.com/assured-workloads/docs/getting-support) for Assured Workloads. 
    4. [Set up Cloud Identity](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin) and [verify your domain](https://docs.cloud.google.com/identity/docs/verify-domain). 
    5. After Cloud Identity has been configured, [create an organization](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization). 

### Required IAM roles

To create an Assured Workloads folder, you must be granted the **Assured Workloads Administrator** (`roles/assuredworkloads.admin`) role, which contains the minimum IAM permissions to create and manage Assured Workloads folders.

## Create an Assured Workloads folder for Singapore Data Boundary

    1. In the Google Cloud console, go to the **Assured Workloads** page. 

[ Go to Assured Workloads](https://console.cloud.google.com/compliance/assuredworkloads)

    2. If prompted, select your organization.
    3. Click add_box**CREATE** to go to the **Create an Assured Workloads folder** page.
    4. In the step to **Add folder details** : 
       * In **Folder name** , enter a unique name for the folder, such as `aw-my-folder-name`. The folder name must be a minimum of 4 characters in length and a maximum of 30, and can only contain letters, numbers, spaces, and hyphens. **Tip:** When you name your Assured Workloads folders, consider the following: 
         * To identify the folder as an Assured Workloads folder, include a prefix in its name (such as `aw-`). This identifier can help you locate the folder from a list of other resources. 
         * Do not include sensitive data or personally identifiable information (PII) in the folder name. 
       * In **Organization** , select the organization in which to create your folder. This location can't be changed later.
       * In **Folder location** , select the location in the resource hierarchy where the folder will be created. An Assured Workloads folder can be created as a child of an organization or of another folder.
       * Click **Next**.
    5. In the step to **Choose a control package option** , select **Regional Controls** from the drop-down menu.
    6. Select **Singapore Data Boundary** from the drop-down menu. See [Control packages](https://docs.cloud.google.com/assured-workloads/docs/control-packages) to learn about other options.
    7. In **Select resource location** , choose the [location](https://docs.cloud.google.com/assured-workloads/docs/locations) where resource creation and usage will be enforced by the folder's [organization policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations). See [Resource locations supported services](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations-supported-services) for a list of all resources that can be restricted by the Resource Locations organization policy constraint, as some resources may be out of scope and unrestrictable. 
    8. Review the details about the control option you've selected, and click **Next**.
    9. (Optional) In the step to **Configure additional settings** , you can create a new project and a key ring for your [Customer Managed Encryption Keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek). No keys are created during this step, as Assured Workloads does not automatically create any cryptographic keys for you. See [Supporting compliance with key management](https://docs.cloud.google.com/assured-workloads/docs/key-management) for more information. **Note** : Singapore Data Boundary does not require using CMEK; you can click **Next** to skip this step.
    10. In the step to **Review and create folder** , review the details about your new Assured Workloads folder and ensure that they are correct. Then, click **Create Folder**. 

After completing the steps above, Assured Workloads creates the following resources:

    * An Assured Workloads folder, which enforces security controls on [supported Google Cloud products](https://docs.cloud.google.com/assured-workloads/docs/supported-products) to adhere with the Singapore Data Boundary control package. These controls include setting an organization policy that [restricts resource usage](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources) to only those supported products, and allows creating or using resources only in [allowed locations](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations). 
    * If you chose to create one, a CMEK project that contains the configured CMEK key ring. **Note** : Folder creation does not automatically create keys for you. After creating the folder, you must create an encryption key before adding any resources. See [Create and obtain a CMEK key](https://docs.cloud.google.com/assured-workloads/docs/create-and-obtain-cmek) to learn more. 

## Use your new Assured Workloads folder

To start using your Assured Workloads folder, it's important that you put the resources that you want to be compliant with Singapore Data Boundary in the new folder. You can create projects inside of the folder along with [resources for supported products](https://docs.cloud.google.com/assured-workloads/docs/supported-products), or [migrate existing projects](https://docs.cloud.google.com/assured-workloads/docs/migrate-workload). Some possible next steps include the following:

    * Create a new project in the newly-created Assured Workloads folder, and then create a Compute Engine VM inside the project. The VM instance will be configured to meet the compliance requirements for Singapore Data Boundary. 
    * [Analyze an existing project](https://docs.cloud.google.com/assured-workloads/docs/migrate-workload) that you want to make compliant with Singapore Data Boundary, and make any of the required changes. Then, move the project to the newly-created Assured Workloads folder. 

### Enabling BigQuery in your folder

If your selected control package lists BigQuery as a supported service, BigQuery is supported, but it isn't automatically enabled when you create a new Assured Workloads folder due to an internal configuration process. This process normally finishes in ten minutes, but can take much longer in some circumstances. To check whether the process is finished and to enable BigQuery, complete the following steps:  

    1. In the Google Cloud console, go to the **Assured Workloads** page. 

[ Go to Assured Workloads](https://console.cloud.google.com/compliance/assuredworkloads)

    2. Select your new Assured Workloads folder from the list.
    3. On the **Folder Details** page in the **Allowed services** section, click **Review Available Updates**.
    4. In the **Allowed services** pane, review the services to be added to the [Resource Usage Restriction](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources) organization policy for the folder. If BigQuery services are listed, click **Allow Services** to add them.  
  
If BigQuery services are not listed, wait for the internal process to complete. If the services are not listed within 12 hours of folder creation, contact [Cloud Customer Care](https://docs.cloud.google.com/support). 

After the enablement process is completed, you can use BigQuery in your Assured Workloads folder.

Gemini in BigQuery is not supported by Assured Workloads.

  * ## Before you begin

If you haven't already, you must complete the following below to create an Assured Workloads folder for the [ South Africa Data Boundary control package](https://docs.cloud.google.com/assured-workloads/docs/control-packages#za-data-boundary):

    1. Ensure that you understand [Assured Workloads concepts](https://docs.cloud.google.com/assured-workloads/docs/overview). 
    2. If [Access Transparency](https://docs.cloud.google.com/assured-workloads/docs/access-transparency) is not enabled on your organization, it will automatically be enabled when you create an Assured Workloads folder. Any projects you create or move into the folder will be configured to use Access Transparency. 
    3. Ensure that you understand [how to get support](https://docs.cloud.google.com/assured-workloads/docs/getting-support) for Assured Workloads. 
    4. [Set up Cloud Identity](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin) and [verify your domain](https://docs.cloud.google.com/identity/docs/verify-domain). 
    5. After Cloud Identity has been configured, [create an organization](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization). 

### Required IAM roles

To create an Assured Workloads folder, you must be granted the **Assured Workloads Administrator** (`roles/assuredworkloads.admin`) role, which contains the minimum IAM permissions to create and manage Assured Workloads folders.

## Create an Assured Workloads folder for South Africa Data Boundary

    1. In the Google Cloud console, go to the **Assured Workloads** page. 

[ Go to Assured Workloads](https://console.cloud.google.com/compliance/assuredworkloads)

    2. If prompted, select your organization.
    3. Click add_box**CREATE** to go to the **Create an Assured Workloads folder** page.
    4. In the step to **Add folder details** : 
       * In **Folder name** , enter a unique name for the folder, such as `aw-my-folder-name`. The folder name must be a minimum of 4 characters in length and a maximum of 30, and can only contain letters, numbers, spaces, and hyphens. **Tip:** When you name your Assured Workloads folders, consider the following: 
         * To identify the folder as an Assured Workloads folder, include a prefix in its name (such as `aw-`). This identifier can help you locate the folder from a list of other resources. 
         * Do not include sensitive data or personally identifiable information (PII) in the folder name. 
       * In **Organization** , select the organization in which to create your folder. This location can't be changed later.
       * In **Folder location** , select the location in the resource hierarchy where the folder will be created. An Assured Workloads folder can be created as a child of an organization or of another folder.
       * Click **Next**.
    5. In the step to **Choose a control package option** , select **Regional Controls** from the drop-down menu.
    6. Select **South Africa Data Boundary** from the drop-down menu. See [Control packages](https://docs.cloud.google.com/assured-workloads/docs/control-packages) to learn about other options.
    7. In **Select resource location** , choose the [location](https://docs.cloud.google.com/assured-workloads/docs/locations) where resource creation and usage will be enforced by the folder's [organization policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations). See [Resource locations supported services](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations-supported-services) for a list of all resources that can be restricted by the Resource Locations organization policy constraint, as some resources may be out of scope and unrestrictable. 
    8. Review the details about the control option you've selected, and click **Next**.
    9. (Optional) In the step to **Configure additional settings** , you can create a new project and a key ring for your [Customer Managed Encryption Keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek). No keys are created during this step, as Assured Workloads does not automatically create any cryptographic keys for you. See [Supporting compliance with key management](https://docs.cloud.google.com/assured-workloads/docs/key-management) for more information. **Note** : South Africa Data Boundary does not require using CMEK; you can click **Next** to skip this step.
    10. In the step to **Review and create folder** , review the details about your new Assured Workloads folder and ensure that they are correct. Then, click **Create Folder**. 

After completing the steps above, Assured Workloads creates the following resources:

    * An Assured Workloads folder, which enforces security controls on [supported Google Cloud products](https://docs.cloud.google.com/assured-workloads/docs/supported-products) to adhere with the South Africa Data Boundary control package. These controls include setting an organization policy that [restricts resource usage](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources) to only those supported products, and allows creating or using resources only in [allowed locations](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations). 
    * If you chose to create one, a CMEK project that contains the configured CMEK key ring. **Note** : Folder creation does not automatically create keys for you. After creating the folder, you must create an encryption key before adding any resources. See [Create and obtain a CMEK key](https://docs.cloud.google.com/assured-workloads/docs/create-and-obtain-cmek) to learn more. 

## Use your new Assured Workloads folder

To start using your Assured Workloads folder, it's important that you put the resources that you want to be compliant with South Africa Data Boundary in the new folder. You can create projects inside of the folder along with [resources for supported products](https://docs.cloud.google.com/assured-workloads/docs/supported-products), or [migrate existing projects](https://docs.cloud.google.com/assured-workloads/docs/migrate-workload). Some possible next steps include the following:

    * Create a new project in the newly-created Assured Workloads folder, and then create a Compute Engine VM inside the project. The VM instance will be configured to meet the compliance requirements for South Africa Data Boundary. 
    * [Analyze an existing project](https://docs.cloud.google.com/assured-workloads/docs/migrate-workload) that you want to make compliant with South Africa Data Boundary, and make any of the required changes. Then, move the project to the newly-created Assured Workloads folder. 

### Enabling BigQuery in your folder

If your selected control package lists BigQuery as a supported service, BigQuery is supported, but it isn't automatically enabled when you create a new Assured Workloads folder due to an internal configuration process. This process normally finishes in ten minutes, but can take much longer in some circumstances. To check whether the process is finished and to enable BigQuery, complete the following steps:  

    1. In the Google Cloud console, go to the **Assured Workloads** page. 

[ Go to Assured Workloads](https://console.cloud.google.com/compliance/assuredworkloads)

    2. Select your new Assured Workloads folder from the list.
    3. On the **Folder Details** page in the **Allowed services** section, click **Review Available Updates**.
    4. In the **Allowed services** pane, review the services to be added to the [Resource Usage Restriction](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources) organization policy for the folder. If BigQuery services are listed, click **Allow Services** to add them.  
  
If BigQuery services are not listed, wait for the internal process to complete. If the services are not listed within 12 hours of folder creation, contact [Cloud Customer Care](https://docs.cloud.google.com/support). 

After the enablement process is completed, you can use BigQuery in your Assured Workloads folder.

Gemini in BigQuery is not supported by Assured Workloads.

  * ## Before you begin

If you haven't already, you must complete the following below to create an Assured Workloads folder for the [ South Korea Data Boundary control package](https://docs.cloud.google.com/assured-workloads/docs/control-packages#kr-data-boundary):

    1. Ensure that you understand [Assured Workloads concepts](https://docs.cloud.google.com/assured-workloads/docs/overview). 
    2. If [Access Transparency](https://docs.cloud.google.com/assured-workloads/docs/access-transparency) is not enabled on your organization, it will automatically be enabled when you create an Assured Workloads folder. Any projects you create or move into the folder will be configured to use Access Transparency. 
    3. Ensure that you understand [how to get support](https://docs.cloud.google.com/assured-workloads/docs/getting-support) for Assured Workloads. 
    4. [Set up Cloud Identity](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin) and [verify your domain](https://docs.cloud.google.com/identity/docs/verify-domain). 
    5. After Cloud Identity has been configured, [create an organization](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization). 

### Required IAM roles

To create an Assured Workloads folder, you must be granted the **Assured Workloads Administrator** (`roles/assuredworkloads.admin`) role, which contains the minimum IAM permissions to create and manage Assured Workloads folders.

## Create an Assured Workloads folder for South Korea Data Boundary

    1. In the Google Cloud console, go to the **Assured Workloads** page. 

[ Go to Assured Workloads](https://console.cloud.google.com/compliance/assuredworkloads)

    2. If prompted, select your organization.
    3. Click add_box**CREATE** to go to the **Create an Assured Workloads folder** page.
    4. In the step to **Add folder details** : 
       * In **Folder name** , enter a unique name for the folder, such as `aw-my-folder-name`. The folder name must be a minimum of 4 characters in length and a maximum of 30, and can only contain letters, numbers, spaces, and hyphens. **Tip:** When you name your Assured Workloads folders, consider the following: 
         * To identify the folder as an Assured Workloads folder, include a prefix in its name (such as `aw-`). This identifier can help you locate the folder from a list of other resources. 
         * Do not include sensitive data or personally identifiable information (PII) in the folder name. 
       * In **Organization** , select the organization in which to create your folder. This location can't be changed later.
       * In **Folder location** , select the location in the resource hierarchy where the folder will be created. An Assured Workloads folder can be created as a child of an organization or of another folder.
       * Click **Next**.
    5. In the step to **Choose a control package option** , select **Regional Controls** from the drop-down menu.
    6. Select **South Korea Data Boundary** from the drop-down menu. See [Control packages](https://docs.cloud.google.com/assured-workloads/docs/control-packages) to learn about other options.
    7. In **Select resource location** , choose the [location](https://docs.cloud.google.com/assured-workloads/docs/locations) where resource creation and usage will be enforced by the folder's [organization policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations). See [Resource locations supported services](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations-supported-services) for a list of all resources that can be restricted by the Resource Locations organization policy constraint, as some resources may be out of scope and unrestrictable. 
    8. Review the details about the control option you've selected, and click **Next**.
    9. (Optional) In the step to **Configure additional settings** , you can create a new project and a key ring for your [Customer Managed Encryption Keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek). No keys are created during this step, as Assured Workloads does not automatically create any cryptographic keys for you. See [Supporting compliance with key management](https://docs.cloud.google.com/assured-workloads/docs/key-management) for more information. **Note** : South Korea Data Boundary does not require using CMEK; you can click **Next** to skip this step.
    10. In the step to **Review and create folder** , review the details about your new Assured Workloads folder and ensure that they are correct. Then, click **Create Folder**. 

After completing the steps above, Assured Workloads creates the following resources:

    * An Assured Workloads folder, which enforces security controls on [supported Google Cloud products](https://docs.cloud.google.com/assured-workloads/docs/supported-products) to adhere with the South Korea Data Boundary control package. These controls include setting an organization policy that [restricts resource usage](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources) to only those supported products, and allows creating or using resources only in [allowed locations](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations). 
    * If you chose to create one, a CMEK project that contains the configured CMEK key ring. **Note** : Folder creation does not automatically create keys for you. After creating the folder, you must create an encryption key before adding any resources. See [Create and obtain a CMEK key](https://docs.cloud.google.com/assured-workloads/docs/create-and-obtain-cmek) to learn more. 

## Use your new Assured Workloads folder

To start using your Assured Workloads folder, it's important that you put the resources that you want to be compliant with South Korea Data Boundary in the new folder. You can create projects inside of the folder along with [resources for supported products](https://docs.cloud.google.com/assured-workloads/docs/supported-products), or [migrate existing projects](https://docs.cloud.google.com/assured-workloads/docs/migrate-workload). Some possible next steps include the following:

    * Create a new project in the newly-created Assured Workloads folder, and then create a Compute Engine VM inside the project. The VM instance will be configured to meet the compliance requirements for South Korea Data Boundary. 
    * [Analyze an existing project](https://docs.cloud.google.com/assured-workloads/docs/migrate-workload) that you want to make compliant with South Korea Data Boundary, and make any of the required changes. Then, move the project to the newly-created Assured Workloads folder. 

### Enabling BigQuery in your folder

If your selected control package lists BigQuery as a supported service, BigQuery is supported, but it isn't automatically enabled when you create a new Assured Workloads folder due to an internal configuration process. This process normally finishes in ten minutes, but can take much longer in some circumstances. To check whether the process is finished and to enable BigQuery, complete the following steps:  

    1. In the Google Cloud console, go to the **Assured Workloads** page. 

[ Go to Assured Workloads](https://console.cloud.google.com/compliance/assuredworkloads)

    2. Select your new Assured Workloads folder from the list.
    3. On the **Folder Details** page in the **Allowed services** section, click **Review Available Updates**.
    4. In the **Allowed services** pane, review the services to be added to the [Resource Usage Restriction](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources) organization policy for the folder. If BigQuery services are listed, click **Allow Services** to add them.  
  
If BigQuery services are not listed, wait for the internal process to complete. If the services are not listed within 12 hours of folder creation, contact [Cloud Customer Care](https://docs.cloud.google.com/support). 

After the enablement process is completed, you can use BigQuery in your Assured Workloads folder.

Gemini in BigQuery is not supported by Assured Workloads.

  * ## Before you begin

If you haven't already, you must complete the following below to create an Assured Workloads folder for the [ Kingdom of Saudi Arabia Data Boundary with Access Justifications control package](https://docs.cloud.google.com/assured-workloads/docs/control-packages#sa-data-boundary-access-justifications):

    1. Ensure that you understand [Assured Workloads concepts](https://docs.cloud.google.com/assured-workloads/docs/overview). 
    2. If [Access Transparency](https://docs.cloud.google.com/assured-workloads/docs/access-transparency) is not enabled on your organization, it will automatically be enabled when you create an Assured Workloads folder. Any projects you create or move into the folder will be configured to use Access Transparency. 
    3. Ensure that you understand [how to get support](https://docs.cloud.google.com/assured-workloads/docs/getting-support) for Assured Workloads. 
    4. [Set up Cloud Identity](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin) and [verify your domain](https://docs.cloud.google.com/identity/docs/verify-domain). 
    5. After Cloud Identity has been configured, [create an organization](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization). 

### Required IAM roles

To create an Assured Workloads folder, you must be granted the **Assured Workloads Administrator** (`roles/assuredworkloads.admin`) role, which contains the minimum IAM permissions to create and manage Assured Workloads folders.

## Create an Assured Workloads folder for Kingdom of Saudi Arabia Data Boundary with Access Justifications

    1. In the Google Cloud console, go to the **Assured Workloads** page. 

[ Go to Assured Workloads](https://console.cloud.google.com/compliance/assuredworkloads)

    2. If prompted, select your organization.
    3. Click add_box**CREATE** to go to the **Create an Assured Workloads folder** page.
    4. In the step to **Add folder details** : 
       * In **Folder name** , enter a unique name for the folder, such as `aw-my-folder-name`. The folder name must be a minimum of 4 characters in length and a maximum of 30, and can only contain letters, numbers, spaces, and hyphens. **Tip:** When you name your Assured Workloads folders, consider the following: 
         * To identify the folder as an Assured Workloads folder, include a prefix in its name (such as `aw-`). This identifier can help you locate the folder from a list of other resources. 
         * Do not include sensitive data or personally identifiable information (PII) in the folder name. 
       * In **Organization** , select the organization in which to create your folder. This location can't be changed later.
       * In **Folder location** , select the location in the resource hierarchy where the folder will be created. An Assured Workloads folder can be created as a child of an organization or of another folder.
       * Click **Next**.
    5. In the step to **Choose a control package option** , select **Regional Controls** from the drop-down menu.
    6. Select **Kingdom of Saudi Arabia Data Boundary with Access Justifications** from the drop-down menu. See [Control packages](https://docs.cloud.google.com/assured-workloads/docs/control-packages) to learn about other options.
    7. In **Select resource location** , choose the [location](https://docs.cloud.google.com/assured-workloads/docs/locations) where resource creation and usage will be enforced by the folder's [organization policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations). See [Resource locations supported services](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations-supported-services) for a list of all resources that can be restricted by the Resource Locations organization policy constraint, as some resources may be out of scope and unrestrictable. 
    8. Review the details about the control option you've selected, and click **Next**.
    9. (Optional) In the step to **Configure additional settings** , you can create a new project and a key ring for your [Customer Managed Encryption Keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek). No keys are created during this step, as Assured Workloads does not automatically create any cryptographic keys for you. See [Supporting compliance with key management](https://docs.cloud.google.com/assured-workloads/docs/key-management) for more information. **Note** : Kingdom of Saudi Arabia Data Boundary with Access Justifications does not require using CMEK; you can click **Next** to skip this step.
    10. In the step to **Review and create folder** , review the details about your new Assured Workloads folder and ensure that they are correct. Then, click **Create Folder**. 

After completing the steps above, Assured Workloads creates the following resources:

    * An Assured Workloads folder, which enforces security controls on [supported Google Cloud products](https://docs.cloud.google.com/assured-workloads/docs/supported-products) to adhere with the Kingdom of Saudi Arabia Data Boundary with Access Justifications control package. These controls include setting an organization policy that [restricts resource usage](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources) to only those supported products, and allows creating or using resources only in [allowed locations](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations). 
    * If you chose to create one, a CMEK project that contains the configured CMEK key ring. **Note** : Folder creation does not automatically create keys for you. After creating the folder, you must create an encryption key before adding any resources. See [Create and obtain a CMEK key](https://docs.cloud.google.com/assured-workloads/docs/create-and-obtain-cmek) to learn more. 

## Use your new Assured Workloads folder

To start using your Assured Workloads folder, it's important that you put the resources that you want to be compliant with Kingdom of Saudi Arabia Data Boundary with Access Justifications in the new folder. You can create projects inside of the folder along with [resources for supported products](https://docs.cloud.google.com/assured-workloads/docs/supported-products), or [migrate existing projects](https://docs.cloud.google.com/assured-workloads/docs/migrate-workload). Some possible next steps include the following:

    * Create a new project in the newly-created Assured Workloads folder, and then create a Compute Engine VM inside the project. The VM instance will be configured to meet the compliance requirements for Kingdom of Saudi Arabia Data Boundary with Access Justifications. 
    * [Analyze an existing project](https://docs.cloud.google.com/assured-workloads/docs/migrate-workload) that you want to make compliant with Kingdom of Saudi Arabia Data Boundary with Access Justifications, and make any of the required changes. Then, move the project to the newly-created Assured Workloads folder. 

### Enabling BigQuery in your folder

If your selected control package lists BigQuery as a supported service, BigQuery is supported, but it isn't automatically enabled when you create a new Assured Workloads folder due to an internal configuration process. This process normally finishes in ten minutes, but can take much longer in some circumstances. To check whether the process is finished and to enable BigQuery, complete the following steps:  

    1. In the Google Cloud console, go to the **Assured Workloads** page. 

[ Go to Assured Workloads](https://console.cloud.google.com/compliance/assuredworkloads)

    2. Select your new Assured Workloads folder from the list.
    3. On the **Folder Details** page in the **Allowed services** section, click **Review Available Updates**.
    4. In the **Allowed services** pane, review the services to be added to the [Resource Usage Restriction](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources) organization policy for the folder. If BigQuery services are listed, click **Allow Services** to add them.  
  
If BigQuery services are not listed, wait for the internal process to complete. If the services are not listed within 12 hours of folder creation, contact [Cloud Customer Care](https://docs.cloud.google.com/support). 

After the enablement process is completed, you can use BigQuery in your Assured Workloads folder.

Gemini in BigQuery is not supported by Assured Workloads.

  * ## Before you begin

If you haven't already, you must complete the following below to create an Assured Workloads folder for the [ Switzerland Data Boundary control package](https://docs.cloud.google.com/assured-workloads/docs/control-packages#ch-data-boundary):

    1. Ensure that you understand [Assured Workloads concepts](https://docs.cloud.google.com/assured-workloads/docs/overview). 
    2. If [Access Transparency](https://docs.cloud.google.com/assured-workloads/docs/access-transparency) is not enabled on your organization, it will automatically be enabled when you create an Assured Workloads folder. Any projects you create or move into the folder will be configured to use Access Transparency. 
    3. Ensure that you understand [how to get support](https://docs.cloud.google.com/assured-workloads/docs/getting-support) for Assured Workloads. 
    4. [Set up Cloud Identity](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin) and [verify your domain](https://docs.cloud.google.com/identity/docs/verify-domain). 
    5. After Cloud Identity has been configured, [create an organization](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization). 

### Required IAM roles

To create an Assured Workloads folder, you must be granted the **Assured Workloads Administrator** (`roles/assuredworkloads.admin`) role, which contains the minimum IAM permissions to create and manage Assured Workloads folders.

## Create an Assured Workloads folder for Switzerland Data Boundary

    1. In the Google Cloud console, go to the **Assured Workloads** page. 

[ Go to Assured Workloads](https://console.cloud.google.com/compliance/assuredworkloads)

    2. If prompted, select your organization.
    3. Click add_box**CREATE** to go to the **Create an Assured Workloads folder** page.
    4. In the step to **Add folder details** : 
       * In **Folder name** , enter a unique name for the folder, such as `aw-my-folder-name`. The folder name must be a minimum of 4 characters in length and a maximum of 30, and can only contain letters, numbers, spaces, and hyphens. **Tip:** When you name your Assured Workloads folders, consider the following: 
         * To identify the folder as an Assured Workloads folder, include a prefix in its name (such as `aw-`). This identifier can help you locate the folder from a list of other resources. 
         * Do not include sensitive data or personally identifiable information (PII) in the folder name. 
       * In **Organization** , select the organization in which to create your folder. This location can't be changed later.
       * In **Folder location** , select the location in the resource hierarchy where the folder will be created. An Assured Workloads folder can be created as a child of an organization or of another folder.
       * Click **Next**.
    5. In the step to **Choose a control package option** , select **Regional Controls** from the drop-down menu.
    6. Select **Switzerland Data Boundary** from the drop-down menu. See [Control packages](https://docs.cloud.google.com/assured-workloads/docs/control-packages) to learn about other options.
    7. In **Select resource location** , choose the [location](https://docs.cloud.google.com/assured-workloads/docs/locations) where resource creation and usage will be enforced by the folder's [organization policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations). See [Resource locations supported services](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations-supported-services) for a list of all resources that can be restricted by the Resource Locations organization policy constraint, as some resources may be out of scope and unrestrictable. 
    8. Review the details about the control option you've selected, and click **Next**.
    9. (Optional) In the step to **Configure additional settings** , you can create a new project and a key ring for your [Customer Managed Encryption Keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek). No keys are created during this step, as Assured Workloads does not automatically create any cryptographic keys for you. See [Supporting compliance with key management](https://docs.cloud.google.com/assured-workloads/docs/key-management) for more information. **Note** : Switzerland Data Boundary does not require using CMEK; you can click **Next** to skip this step.
    10. In the step to **Review and create folder** , review the details about your new Assured Workloads folder and ensure that they are correct. Then, click **Create Folder**. 

After completing the steps above, Assured Workloads creates the following resources:

    * An Assured Workloads folder, which enforces security controls on [supported Google Cloud products](https://docs.cloud.google.com/assured-workloads/docs/supported-products) to adhere with the Switzerland Data Boundary control package. These controls include setting an organization policy that [restricts resource usage](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources) to only those supported products, and allows creating or using resources only in [allowed locations](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations). 
    * If you chose to create one, a CMEK project that contains the configured CMEK key ring. **Note** : Folder creation does not automatically create keys for you. After creating the folder, you must create an encryption key before adding any resources. See [Create and obtain a CMEK key](https://docs.cloud.google.com/assured-workloads/docs/create-and-obtain-cmek) to learn more. 

## Use your new Assured Workloads folder

To start using your Assured Workloads folder, it's important that you put the resources that you want to be compliant with Switzerland Data Boundary in the new folder. You can create projects inside of the folder along with [resources for supported products](https://docs.cloud.google.com/assured-workloads/docs/supported-products), or [migrate existing projects](https://docs.cloud.google.com/assured-workloads/docs/migrate-workload). Some possible next steps include the following:

    * Create a new project in the newly-created Assured Workloads folder, and then create a Compute Engine VM inside the project. The VM instance will be configured to meet the compliance requirements for Switzerland Data Boundary. 
    * [Analyze an existing project](https://docs.cloud.google.com/assured-workloads/docs/migrate-workload) that you want to make compliant with Switzerland Data Boundary, and make any of the required changes. Then, move the project to the newly-created Assured Workloads folder. 

### Enabling BigQuery in your folder

If your selected control package lists BigQuery as a supported service, BigQuery is supported, but it isn't automatically enabled when you create a new Assured Workloads folder due to an internal configuration process. This process normally finishes in ten minutes, but can take much longer in some circumstances. To check whether the process is finished and to enable BigQuery, complete the following steps:  

    1. In the Google Cloud console, go to the **Assured Workloads** page. 

[ Go to Assured Workloads](https://console.cloud.google.com/compliance/assuredworkloads)

    2. Select your new Assured Workloads folder from the list.
    3. On the **Folder Details** page in the **Allowed services** section, click **Review Available Updates**.
    4. In the **Allowed services** pane, review the services to be added to the [Resource Usage Restriction](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources) organization policy for the folder. If BigQuery services are listed, click **Allow Services** to add them.  
  
If BigQuery services are not listed, wait for the internal process to complete. If the services are not listed within 12 hours of folder creation, contact [Cloud Customer Care](https://docs.cloud.google.com/support). 

After the enablement process is completed, you can use BigQuery in your Assured Workloads folder.

Gemini in BigQuery is not supported by Assured Workloads.

  * ## Before you begin

If you haven't already, you must complete the following below to create an Assured Workloads folder for the [ Switzerland Data Boundary with Access Justifications control package](https://docs.cloud.google.com/assured-workloads/docs/control-packages#ch-data-boundary-access-justifications):

    1. Ensure that you understand [Assured Workloads concepts](https://docs.cloud.google.com/assured-workloads/docs/overview). 
    2. If [Access Transparency](https://docs.cloud.google.com/assured-workloads/docs/access-transparency) is not enabled on your organization, it will automatically be enabled when you create an Assured Workloads folder. Any projects you create or move into the folder will be configured to use Access Transparency. 
    3. Ensure that you understand [how to get support](https://docs.cloud.google.com/assured-workloads/docs/getting-support) for Assured Workloads. 
    4. Ensure that you understand the [additional cost](https://docs.cloud.google.com/assured-workloads/pricing) when using Switzerland Data Boundary with Access Justifications in Assured Workloads. 
    5. [Set up Cloud Identity](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin) and [verify your domain](https://docs.cloud.google.com/identity/docs/verify-domain). 
    6. After Cloud Identity has been configured, [create an organization](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization). 

### Required IAM roles

To create an Assured Workloads folder, you must be granted the **Assured Workloads Administrator** (`roles/assuredworkloads.admin`) role, which contains the minimum IAM permissions to create and manage Assured Workloads folders.

## Create an Assured Workloads folder for Switzerland Data Boundary with Access Justifications

    1. In the Google Cloud console, go to the **Assured Workloads** page. 

[ Go to Assured Workloads](https://console.cloud.google.com/compliance/assuredworkloads)

    2. If prompted, select your organization.
    3. Click add_box**CREATE** to go to the **Create an Assured Workloads folder** page.
    4. In the step to **Add folder details** : 
       * In **Folder name** , enter a unique name for the folder, such as `aw-my-folder-name`. The folder name must be a minimum of 4 characters in length and a maximum of 30, and can only contain letters, numbers, spaces, and hyphens. **Tip:** When you name your Assured Workloads folders, consider the following: 
         * To identify the folder as an Assured Workloads folder, include a prefix in its name (such as `aw-`). This identifier can help you locate the folder from a list of other resources. 
         * Do not include sensitive data or personally identifiable information (PII) in the folder name. 
       * In **Organization** , select the organization in which to create your folder. This location can't be changed later.
       * In **Folder location** , select the location in the resource hierarchy where the folder will be created. An Assured Workloads folder can be created as a child of an organization or of another folder.
       * Click **Next**.
    5. In the step to **Choose a control package option** , select **Sovereign Controls** from the drop-down menu.
    6. Select **Switzerland Data Boundary with Access Justifications** from the drop-down menu. See [Control packages](https://docs.cloud.google.com/assured-workloads/docs/control-packages) to learn about other options.
    7. In **Select resource location** , choose the [location](https://docs.cloud.google.com/assured-workloads/docs/locations) where resource creation and usage will be enforced by the folder's [organization policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations). See [Resource locations supported services](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations-supported-services) for a list of all resources that can be restricted by the Resource Locations organization policy constraint, as some resources may be out of scope and unrestrictable. 
    8. Review the details about the control option you've selected, and click **Next**.
    9. In the step to **Configure additional settings** , you must create a new project and a key ring for your [Customer Managed Encryption Keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek). No keys are created during this step, as Assured Workloads does not automatically create any cryptographic keys for you. See [Supporting compliance with key management](https://docs.cloud.google.com/assured-workloads/docs/key-management) for more information. 
    10. In the step to **Review and create folder** , review the details about your new Assured Workloads folder and ensure that they are correct. Then, click **Create Folder**. 

After completing the steps above, Assured Workloads creates the following resources:

    * An Assured Workloads folder, which enforces security controls on [supported Google Cloud products](https://docs.cloud.google.com/assured-workloads/docs/supported-products) to adhere with the Switzerland Data Boundary with Access Justifications control package. These controls include setting an organization policy that [restricts resource usage](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources) to only those supported products, and allows creating or using resources only in [allowed locations](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations). 
    * A CMEK project that contains the configured CMEK key ring. **Note** : Folder creation does not automatically create keys for you. After creating the folder, you must create an encryption key before adding any resources. 

## Use your new Assured Workloads folder

To start using your Assured Workloads folder, it's important that you put the resources that you want to be compliant with Switzerland Data Boundary with Access Justifications in the new folder. You can create projects inside of the folder along with [resources for supported products](https://docs.cloud.google.com/assured-workloads/docs/supported-products), or [migrate existing projects](https://docs.cloud.google.com/assured-workloads/docs/migrate-workload). Some possible next steps include the following:

    * Create a new project in the newly-created Assured Workloads folder, and then create a Compute Engine VM inside the project. The VM instance will be configured to meet the compliance requirements for Switzerland Data Boundary with Access Justifications. 
    * [Analyze an existing project](https://docs.cloud.google.com/assured-workloads/docs/migrate-workload) that you want to make compliant with Switzerland Data Boundary with Access Justifications, and make any of the required changes. Then, move the project to the newly-created Assured Workloads folder. 

### Enabling BigQuery in your folder

If your selected control package lists BigQuery as a supported service, BigQuery is supported, but it isn't automatically enabled when you create a new Assured Workloads folder due to an internal configuration process. This process normally finishes in ten minutes, but can take much longer in some circumstances. To check whether the process is finished and to enable BigQuery, complete the following steps:  

    1. In the Google Cloud console, go to the **Assured Workloads** page. 

[ Go to Assured Workloads](https://console.cloud.google.com/compliance/assuredworkloads)

    2. Select your new Assured Workloads folder from the list.
    3. On the **Folder Details** page in the **Allowed services** section, click **Review Available Updates**.
    4. In the **Allowed services** pane, review the services to be added to the [Resource Usage Restriction](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources) organization policy for the folder. If BigQuery services are listed, click **Allow Services** to add them.  
  
If BigQuery services are not listed, wait for the internal process to complete. If the services are not listed within 12 hours of folder creation, contact [Cloud Customer Care](https://docs.cloud.google.com/support). 

After the enablement process is completed, you can use BigQuery in your Assured Workloads folder.

Gemini in BigQuery is not supported by Assured Workloads.

  * ## Before you begin

If you haven't already, you must complete the following below to create an Assured Workloads folder for the [ Taiwan Data Boundary control package](https://docs.cloud.google.com/assured-workloads/docs/control-packages#tw-data-boundary):

    1. Ensure that you understand [Assured Workloads concepts](https://docs.cloud.google.com/assured-workloads/docs/overview). 
    2. If [Access Transparency](https://docs.cloud.google.com/assured-workloads/docs/access-transparency) is not enabled on your organization, it will automatically be enabled when you create an Assured Workloads folder. Any projects you create or move into the folder will be configured to use Access Transparency. 
    3. Ensure that you understand [how to get support](https://docs.cloud.google.com/assured-workloads/docs/getting-support) for Assured Workloads. 
    4. [Set up Cloud Identity](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin) and [verify your domain](https://docs.cloud.google.com/identity/docs/verify-domain). 
    5. After Cloud Identity has been configured, [create an organization](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization). 

### Required IAM roles

To create an Assured Workloads folder, you must be granted the **Assured Workloads Administrator** (`roles/assuredworkloads.admin`) role, which contains the minimum IAM permissions to create and manage Assured Workloads folders.

## Create an Assured Workloads folder for Taiwan Data Boundary

    1. In the Google Cloud console, go to the **Assured Workloads** page. 

[ Go to Assured Workloads](https://console.cloud.google.com/compliance/assuredworkloads)

    2. If prompted, select your organization.
    3. Click add_box**CREATE** to go to the **Create an Assured Workloads folder** page.
    4. In the step to **Add folder details** : 
       * In **Folder name** , enter a unique name for the folder, such as `aw-my-folder-name`. The folder name must be a minimum of 4 characters in length and a maximum of 30, and can only contain letters, numbers, spaces, and hyphens. **Tip:** When you name your Assured Workloads folders, consider the following: 
         * To identify the folder as an Assured Workloads folder, include a prefix in its name (such as `aw-`). This identifier can help you locate the folder from a list of other resources. 
         * Do not include sensitive data or personally identifiable information (PII) in the folder name. 
       * In **Organization** , select the organization in which to create your folder. This location can't be changed later.
       * In **Folder location** , select the location in the resource hierarchy where the folder will be created. An Assured Workloads folder can be created as a child of an organization or of another folder.
       * Click **Next**.
    5. In the step to **Choose a control package option** , select **Regional Controls** from the drop-down menu.
    6. Select **Taiwan Data Boundary** from the drop-down menu. See [Control packages](https://docs.cloud.google.com/assured-workloads/docs/control-packages) to learn about other options.
    7. In **Select resource location** , choose the [location](https://docs.cloud.google.com/assured-workloads/docs/locations) where resource creation and usage will be enforced by the folder's [organization policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations). See [Resource locations supported services](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations-supported-services) for a list of all resources that can be restricted by the Resource Locations organization policy constraint, as some resources may be out of scope and unrestrictable. 
    8. Review the details about the control option you've selected, and click **Next**.
    9. (Optional) In the step to **Configure additional settings** , you can create a new project and a key ring for your [Customer Managed Encryption Keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek). No keys are created during this step, as Assured Workloads does not automatically create any cryptographic keys for you. See [Supporting compliance with key management](https://docs.cloud.google.com/assured-workloads/docs/key-management) for more information. **Note** : Taiwan Data Boundary does not require using CMEK; you can click **Next** to skip this step.
    10. In the step to **Review and create folder** , review the details about your new Assured Workloads folder and ensure that they are correct. Then, click **Create Folder**. 

After completing the steps above, Assured Workloads creates the following resources:

    * An Assured Workloads folder, which enforces security controls on [supported Google Cloud products](https://docs.cloud.google.com/assured-workloads/docs/supported-products) to adhere with the Taiwan Data Boundary control package. These controls include setting an organization policy that [restricts resource usage](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources) to only those supported products, and allows creating or using resources only in [allowed locations](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations). 
    * If you chose to create one, a CMEK project that contains the configured CMEK key ring. **Note** : Folder creation does not automatically create keys for you. After creating the folder, you must create an encryption key before adding any resources. See [Create and obtain a CMEK key](https://docs.cloud.google.com/assured-workloads/docs/create-and-obtain-cmek) to learn more. 

## Use your new Assured Workloads folder

To start using your Assured Workloads folder, it's important that you put the resources that you want to be compliant with Taiwan Data Boundary in the new folder. You can create projects inside of the folder along with [resources for supported products](https://docs.cloud.google.com/assured-workloads/docs/supported-products), or [migrate existing projects](https://docs.cloud.google.com/assured-workloads/docs/migrate-workload). Some possible next steps include the following:

    * Create a new project in the newly-created Assured Workloads folder, and then create a Compute Engine VM inside the project. The VM instance will be configured to meet the compliance requirements for Taiwan Data Boundary. 
    * [Analyze an existing project](https://docs.cloud.google.com/assured-workloads/docs/migrate-workload) that you want to make compliant with Taiwan Data Boundary, and make any of the required changes. Then, move the project to the newly-created Assured Workloads folder. 

### Enabling BigQuery in your folder

If your selected control package lists BigQuery as a supported service, BigQuery is supported, but it isn't automatically enabled when you create a new Assured Workloads folder due to an internal configuration process. This process normally finishes in ten minutes, but can take much longer in some circumstances. To check whether the process is finished and to enable BigQuery, complete the following steps:  

    1. In the Google Cloud console, go to the **Assured Workloads** page. 

[ Go to Assured Workloads](https://console.cloud.google.com/compliance/assuredworkloads)

    2. Select your new Assured Workloads folder from the list.
    3. On the **Folder Details** page in the **Allowed services** section, click **Review Available Updates**.
    4. In the **Allowed services** pane, review the services to be added to the [Resource Usage Restriction](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources) organization policy for the folder. If BigQuery services are listed, click **Allow Services** to add them.  
  
If BigQuery services are not listed, wait for the internal process to complete. If the services are not listed within 12 hours of folder creation, contact [Cloud Customer Care](https://docs.cloud.google.com/support). 

After the enablement process is completed, you can use BigQuery in your Assured Workloads folder.

Gemini in BigQuery is not supported by Assured Workloads.

  * ## Before you begin

If you haven't already, you must complete the following below to create an Assured Workloads folder for the [ UK Data Boundary control package](https://docs.cloud.google.com/assured-workloads/docs/control-packages#uk-data-boundary):

    1. Ensure that you understand [Assured Workloads concepts](https://docs.cloud.google.com/assured-workloads/docs/overview). 
    2. If [Access Transparency](https://docs.cloud.google.com/assured-workloads/docs/access-transparency) is not enabled on your organization, it will automatically be enabled when you create an Assured Workloads folder. Any projects you create or move into the folder will be configured to use Access Transparency. 
    3. Ensure that you understand [how to get support](https://docs.cloud.google.com/assured-workloads/docs/getting-support) for Assured Workloads. 
    4. [Set up Cloud Identity](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin) and [verify your domain](https://docs.cloud.google.com/identity/docs/verify-domain). 
    5. After Cloud Identity has been configured, [create an organization](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization). 

### Required IAM roles

To create an Assured Workloads folder, you must be granted the **Assured Workloads Administrator** (`roles/assuredworkloads.admin`) role, which contains the minimum IAM permissions to create and manage Assured Workloads folders.

## Create an Assured Workloads folder for UK Data Boundary

    1. In the Google Cloud console, go to the **Assured Workloads** page. 

[ Go to Assured Workloads](https://console.cloud.google.com/compliance/assuredworkloads)

    2. If prompted, select your organization.
    3. Click add_box**CREATE** to go to the **Create an Assured Workloads folder** page.
    4. In the step to **Add folder details** : 
       * In **Folder name** , enter a unique name for the folder, such as `aw-my-folder-name`. The folder name must be a minimum of 4 characters in length and a maximum of 30, and can only contain letters, numbers, spaces, and hyphens. **Tip:** When you name your Assured Workloads folders, consider the following: 
         * To identify the folder as an Assured Workloads folder, include a prefix in its name (such as `aw-`). This identifier can help you locate the folder from a list of other resources. 
         * Do not include sensitive data or personally identifiable information (PII) in the folder name. 
       * In **Organization** , select the organization in which to create your folder. This location can't be changed later.
       * In **Folder location** , select the location in the resource hierarchy where the folder will be created. An Assured Workloads folder can be created as a child of an organization or of another folder.
       * Click **Next**.
    5. In the step to **Choose a control package option** , select **Regional Controls** from the drop-down menu.
    6. Select **UK Data Boundary** from the drop-down menu. See [Control packages](https://docs.cloud.google.com/assured-workloads/docs/control-packages) to learn about other options.
    7. In **Select resource location** , choose the [location](https://docs.cloud.google.com/assured-workloads/docs/locations) where resource creation and usage will be enforced by the folder's [organization policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations). See [Resource locations supported services](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations-supported-services) for a list of all resources that can be restricted by the Resource Locations organization policy constraint, as some resources may be out of scope and unrestrictable. 
    8. Review the details about the control option you've selected, and click **Next**.
    9. (Optional) In the step to **Configure additional settings** , you can create a new project and a key ring for your [Customer Managed Encryption Keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek). No keys are created during this step, as Assured Workloads does not automatically create any cryptographic keys for you. See [Supporting compliance with key management](https://docs.cloud.google.com/assured-workloads/docs/key-management) for more information. **Note** : UK Data Boundary does not require using CMEK; you can click **Next** to skip this step.
    10. In the step to **Review and create folder** , review the details about your new Assured Workloads folder and ensure that they are correct. Then, click **Create Folder**. 

After completing the steps above, Assured Workloads creates the following resources:

    * An Assured Workloads folder, which enforces security controls on [supported Google Cloud products](https://docs.cloud.google.com/assured-workloads/docs/supported-products) to adhere with the UK Data Boundary control package. These controls include setting an organization policy that [restricts resource usage](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources) to only those supported products, and allows creating or using resources only in [allowed locations](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations). 
    * If you chose to create one, a CMEK project that contains the configured CMEK key ring. **Note** : Folder creation does not automatically create keys for you. After creating the folder, you must create an encryption key before adding any resources. See [Create and obtain a CMEK key](https://docs.cloud.google.com/assured-workloads/docs/create-and-obtain-cmek) to learn more. 

## Use your new Assured Workloads folder

To start using your Assured Workloads folder, it's important that you put the resources that you want to be compliant with UK Data Boundary in the new folder. You can create projects inside of the folder along with [resources for supported products](https://docs.cloud.google.com/assured-workloads/docs/supported-products), or [migrate existing projects](https://docs.cloud.google.com/assured-workloads/docs/migrate-workload). Some possible next steps include the following:

    * Create a new project in the newly-created Assured Workloads folder, and then create a Compute Engine VM inside the project. The VM instance will be configured to meet the compliance requirements for UK Data Boundary. 
    * [Analyze an existing project](https://docs.cloud.google.com/assured-workloads/docs/migrate-workload) that you want to make compliant with UK Data Boundary, and make any of the required changes. Then, move the project to the newly-created Assured Workloads folder. 

### Enabling BigQuery in your folder

If your selected control package lists BigQuery as a supported service, BigQuery is supported, but it isn't automatically enabled when you create a new Assured Workloads folder due to an internal configuration process. This process normally finishes in ten minutes, but can take much longer in some circumstances. To check whether the process is finished and to enable BigQuery, complete the following steps:  

    1. In the Google Cloud console, go to the **Assured Workloads** page. 

[ Go to Assured Workloads](https://console.cloud.google.com/compliance/assuredworkloads)

    2. Select your new Assured Workloads folder from the list.
    3. On the **Folder Details** page in the **Allowed services** section, click **Review Available Updates**.
    4. In the **Allowed services** pane, review the services to be added to the [Resource Usage Restriction](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources) organization policy for the folder. If BigQuery services are listed, click **Allow Services** to add them.  
  
If BigQuery services are not listed, wait for the internal process to complete. If the services are not listed within 12 hours of folder creation, contact [Cloud Customer Care](https://docs.cloud.google.com/support). 

After the enablement process is completed, you can use BigQuery in your Assured Workloads folder.

Gemini in BigQuery is not supported by Assured Workloads.

  * ## Before you begin

If you haven't already, you must complete the following below to create an Assured Workloads folder for the [ US Data Boundary control package](https://docs.cloud.google.com/assured-workloads/docs/control-packages#us-regions):

    1. Ensure that you understand [Assured Workloads concepts](https://docs.cloud.google.com/assured-workloads/docs/overview). 
    2. If [Access Transparency](https://docs.cloud.google.com/assured-workloads/docs/access-transparency) is not enabled on your organization, it will automatically be enabled when you create an Assured Workloads folder. Any projects you create or move into the folder will be configured to use Access Transparency. 
    3. Ensure that you understand [how to get support](https://docs.cloud.google.com/assured-workloads/docs/getting-support) for Assured Workloads. 
    4. [Set up Cloud Identity](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin) and [verify your domain](https://docs.cloud.google.com/identity/docs/verify-domain). 
    5. After Cloud Identity has been configured, [create an organization](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization). 

### Required IAM roles

To create an Assured Workloads folder, you must be granted the **Assured Workloads Administrator** (`roles/assuredworkloads.admin`) role, which contains the minimum IAM permissions to create and manage Assured Workloads folders.

## Create an Assured Workloads folder for US Data Boundary

    1. In the Google Cloud console, go to the **Assured Workloads** page. 

[ Go to Assured Workloads](https://console.cloud.google.com/compliance/assuredworkloads)

    2. If prompted, select your organization.
    3. Click add_box**CREATE** to go to the **Create an Assured Workloads folder** page.
    4. In the step to **Add folder details** : 
       * In **Folder name** , enter a unique name for the folder, such as `aw-my-folder-name`. The folder name must be a minimum of 4 characters in length and a maximum of 30, and can only contain letters, numbers, spaces, and hyphens. **Tip:** When you name your Assured Workloads folders, consider the following: 
         * To identify the folder as an Assured Workloads folder, include a prefix in its name (such as `aw-`). This identifier can help you locate the folder from a list of other resources. 
         * Do not include sensitive data or personally identifiable information (PII) in the folder name. 
       * In **Organization** , select the organization in which to create your folder. This location can't be changed later.
       * In **Folder location** , select the location in the resource hierarchy where the folder will be created. An Assured Workloads folder can be created as a child of an organization or of another folder.
       * Click **Next**.
    5. In the step to **Choose a control package option** , select **Regional Controls** from the drop-down menu.
    6. Select **US Data Boundary** from the drop-down menu. See [Control packages](https://docs.cloud.google.com/assured-workloads/docs/control-packages) to learn about other options.
    7. In **Select resource location** , choose the [location](https://docs.cloud.google.com/assured-workloads/docs/locations) where resource creation and usage will be enforced by the folder's [organization policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations). See [Resource locations supported services](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations-supported-services) for a list of all resources that can be restricted by the Resource Locations organization policy constraint, as some resources may be out of scope and unrestrictable. 
    8. Review the details about the control option you've selected, and click **Next**.
    9. (Optional) In the step to **Configure additional settings** , you can create a new project and a key ring for your [Customer Managed Encryption Keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek). No keys are created during this step, as Assured Workloads does not automatically create any cryptographic keys for you. See [Supporting compliance with key management](https://docs.cloud.google.com/assured-workloads/docs/key-management) for more information. **Note** : US Data Boundary does not require using CMEK; you can click **Next** to skip this step.
    10. In the step to **Review and create folder** , review the details about your new Assured Workloads folder and ensure that they are correct. Then, click **Create Folder**. 

After completing the steps above, Assured Workloads creates the following resources:

    * An Assured Workloads folder, which enforces security controls on [supported Google Cloud products](https://docs.cloud.google.com/assured-workloads/docs/supported-products) to adhere with the US Data Boundary control package. These controls include setting an organization policy that [restricts resource usage](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources) to only those supported products, and allows creating or using resources only in [allowed locations](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations). 
    * If you chose to create one, a CMEK project that contains the configured CMEK key ring. **Note** : Folder creation does not automatically create keys for you. After creating the folder, you must create an encryption key before adding any resources. See [Create and obtain a CMEK key](https://docs.cloud.google.com/assured-workloads/docs/create-and-obtain-cmek) to learn more. 

## Use your new Assured Workloads folder

To start using your Assured Workloads folder, it's important that you put the resources that you want to be compliant with US Data Boundary in the new folder. You can create projects inside of the folder along with [resources for supported products](https://docs.cloud.google.com/assured-workloads/docs/supported-products), or [migrate existing projects](https://docs.cloud.google.com/assured-workloads/docs/migrate-workload). Some possible next steps include the following:

    * Create a new project in the newly-created Assured Workloads folder, and then create a Compute Engine VM inside the project. The VM instance will be configured to meet the compliance requirements for US Data Boundary. 
    * [Analyze an existing project](https://docs.cloud.google.com/assured-workloads/docs/migrate-workload) that you want to make compliant with US Data Boundary, and make any of the required changes. Then, move the project to the newly-created Assured Workloads folder. 

### Enabling BigQuery in your folder

If your selected control package lists BigQuery as a supported service, BigQuery is supported, but it isn't automatically enabled when you create a new Assured Workloads folder due to an internal configuration process. This process normally finishes in ten minutes, but can take much longer in some circumstances. To check whether the process is finished and to enable BigQuery, complete the following steps:  

    1. In the Google Cloud console, go to the **Assured Workloads** page. 

[ Go to Assured Workloads](https://console.cloud.google.com/compliance/assuredworkloads)

    2. Select your new Assured Workloads folder from the list.
    3. On the **Folder Details** page in the **Allowed services** section, click **Review Available Updates**.
    4. In the **Allowed services** pane, review the services to be added to the [Resource Usage Restriction](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources) organization policy for the folder. If BigQuery services are listed, click **Allow Services** to add them.  
  
If BigQuery services are not listed, wait for the internal process to complete. If the services are not listed within 12 hours of folder creation, contact [Cloud Customer Care](https://docs.cloud.google.com/support). 

After the enablement process is completed, you can use BigQuery in your Assured Workloads folder.

Gemini in BigQuery is not supported by Assured Workloads.

  * ## Before you begin

If you haven't already, you must complete the following below to create an Assured Workloads folder for the [ US Data Boundary and Support control package](https://docs.cloud.google.com/assured-workloads/docs/control-packages#us-data-boundary-support):

    1. Ensure that you understand [Assured Workloads concepts](https://docs.cloud.google.com/assured-workloads/docs/overview). 
    2. If [Access Transparency](https://docs.cloud.google.com/assured-workloads/docs/access-transparency) is not enabled on your organization, it will automatically be enabled when you create an Assured Workloads folder. Any projects you create or move into the folder will be configured to use Access Transparency. 
    3. Ensure that you understand [how to get support](https://docs.cloud.google.com/assured-workloads/docs/getting-support) for Assured Workloads. 
    4. Ensure that you understand the [additional cost](https://docs.cloud.google.com/assured-workloads/pricing) when using US Data Boundary and Support in Assured Workloads. 
    5. [Set up Cloud Identity](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin) and [verify your domain](https://docs.cloud.google.com/identity/docs/verify-domain). 
    6. After Cloud Identity has been configured, [create an organization](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization). 

### Required IAM roles

To create an Assured Workloads folder, you must be granted the **Assured Workloads Administrator** (`roles/assuredworkloads.admin`) role, which contains the minimum IAM permissions to create and manage Assured Workloads folders.

## Create an Assured Workloads folder for US Data Boundary and Support

    1. In the Google Cloud console, go to the **Assured Workloads** page. 

[ Go to Assured Workloads](https://console.cloud.google.com/compliance/assuredworkloads)

    2. If prompted, select your organization.
    3. Click add_box**CREATE** to go to the **Create an Assured Workloads folder** page.
    4. In the step to **Add folder details** : 
       * In **Folder name** , enter a unique name for the folder, such as `aw-my-folder-name`. The folder name must be a minimum of 4 characters in length and a maximum of 30, and can only contain letters, numbers, spaces, and hyphens. **Tip:** When you name your Assured Workloads folders, consider the following: 
         * To identify the folder as an Assured Workloads folder, include a prefix in its name (such as `aw-`). This identifier can help you locate the folder from a list of other resources. 
         * Do not include sensitive data or personally identifiable information (PII) in the folder name. 
       * In **Organization** , select the organization in which to create your folder. This location can't be changed later.
       * In **Folder location** , select the location in the resource hierarchy where the folder will be created. An Assured Workloads folder can be created as a child of an organization or of another folder.
       * Click **Next**.
    5. In the step to **Choose a control package option** , select **Regional Controls** from the drop-down menu.
    6. Select **US Data Boundary and Support** from the drop-down menu. See [Control packages](https://docs.cloud.google.com/assured-workloads/docs/control-packages) to learn about other options.
    7. In **Select resource location** , choose the [location](https://docs.cloud.google.com/assured-workloads/docs/locations) where resource creation and usage will be enforced by the folder's [organization policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations). See [Resource locations supported services](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations-supported-services) for a list of all resources that can be restricted by the Resource Locations organization policy constraint, as some resources may be out of scope and unrestrictable. 
    8. Review the details about the control option you've selected, and click **Next**.
    9. (Optional) In the step to **Configure additional settings** , you can create a new project and a key ring for your [Customer Managed Encryption Keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek). No keys are created during this step, as Assured Workloads does not automatically create any cryptographic keys for you. See [Supporting compliance with key management](https://docs.cloud.google.com/assured-workloads/docs/key-management) for more information. **Note** : US Data Boundary and Support does not require using CMEK; you can click **Next** to skip this step.
    10. In the step to **Review and create folder** , review the details about your new Assured Workloads folder and ensure that they are correct. Then, click **Create Folder**. 

After completing the steps above, Assured Workloads creates the following resources:

    * An Assured Workloads folder, which enforces security controls on [supported Google Cloud products](https://docs.cloud.google.com/assured-workloads/docs/supported-products) to adhere with the US Data Boundary and Support control package. These controls include setting an organization policy that [restricts resource usage](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources) to only those supported products, and allows creating or using resources only in [allowed locations](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations). 
    * If you chose to create one, a CMEK project that contains the configured CMEK key ring. **Note** : Folder creation does not automatically create keys for you. After creating the folder, you must create an encryption key before adding any resources. See [Create and obtain a CMEK key](https://docs.cloud.google.com/assured-workloads/docs/create-and-obtain-cmek) to learn more. 

## Use your new Assured Workloads folder

To start using your Assured Workloads folder, it's important that you put the resources that you want to be compliant with US Data Boundary and Support in the new folder. You can create projects inside of the folder along with [resources for supported products](https://docs.cloud.google.com/assured-workloads/docs/supported-products), or [migrate existing projects](https://docs.cloud.google.com/assured-workloads/docs/migrate-workload). Some possible next steps include the following:

    * Create a new project in the newly-created Assured Workloads folder, and then create a Compute Engine VM inside the project. The VM instance will be configured to meet the compliance requirements for US Data Boundary and Support. 
    * [Analyze an existing project](https://docs.cloud.google.com/assured-workloads/docs/migrate-workload) that you want to make compliant with US Data Boundary and Support, and make any of the required changes. Then, move the project to the newly-created Assured Workloads folder. 

### Enabling BigQuery in your folder

If your selected control package lists BigQuery as a supported service, BigQuery is supported, but it isn't automatically enabled when you create a new Assured Workloads folder due to an internal configuration process. This process normally finishes in ten minutes, but can take much longer in some circumstances. To check whether the process is finished and to enable BigQuery, complete the following steps:  

    1. In the Google Cloud console, go to the **Assured Workloads** page. 

[ Go to Assured Workloads](https://console.cloud.google.com/compliance/assuredworkloads)

    2. Select your new Assured Workloads folder from the list.
    3. On the **Folder Details** page in the **Allowed services** section, click **Review Available Updates**.
    4. In the **Allowed services** pane, review the services to be added to the [Resource Usage Restriction](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources) organization policy for the folder. If BigQuery services are listed, click **Allow Services** to add them.  
  
If BigQuery services are not listed, wait for the internal process to complete. If the services are not listed within 12 hours of folder creation, contact [Cloud Customer Care](https://docs.cloud.google.com/support). 

After the enablement process is completed, you can use BigQuery in your Assured Workloads folder.

Gemini in BigQuery is not supported by Assured Workloads.




## What's next

  * Learn about each [control package](https://docs.cloud.google.com/assured-workloads/docs/control-packages).
  * Learn which [products are supported](https://docs.cloud.google.com/assured-workloads/docs/supported-products) for each control package.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
