---
url: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/get-started/target-project/
title: Add a target project \u00a0|\u00a0 Migrate to Virtual Machines \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:56:25.513478+00:00
---

# Add a target project  |  Migrate to Virtual Machines  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/get-started/target-project/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Virtual Machines ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0)
  * [ Guides ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/discover/lifecycle)



Send feedback 

#  Add a target project Stay organized with collections  Save and categorize content based on your preferences. 

With Migrate to Virtual Machines, you work with two types of projects: 

  * **Host project** Use the _host_ project to perform migrations and to host the Compute Engine instances running your migrated workloads. You **must** create and configure a host project as described [Enable Migrate to Virtual Machines services](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/get-started/enable-services).

  * **Target project**

A _target_ project defines a destination project for a Compute Engine instance running your migrated VM. Your **host** project can be used as a target project. If you want to migrate VMs to additional projects, you must add them as **target** projects to Migrate to Virtual Machines.

You typically don't add target projects to Migrate to Virtual Machines until you are ready to start deploying migrated workloads.




Perform the following steps to add a target project to Migrate to Virtual Machines:

  1. Identify and configure the target project.
  2. Set required permissions.
  3. Add the target project.



If necessary, you can later Remove a target project.

## Identify and configure the target project

You must identify the Google Cloud project that you want to use as the **target** project:

  1. In the [Google Cloud console](https://console.cloud.google.com/), on the project selector page, select or create a Google Cloud project to use as a **target** project:

[Go to the project selector page](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. Note the name and ID of the selected project.

  3. Enable the following services on the target project:

Name | Title  
---|---  
`servicemanagement.googleapis.com` | Service Management API   
`servicecontrol.googleapis.com` | Service Control API   
`iam.googleapis.com` | Identity and Access Management (IAM) API   
`cloudresourcemanager.googleapis.com` | Cloud Resource Manager API   
`compute.googleapis.com` | Compute Engine API   
  
To enable the required services:

     1. Ensure that you have set the default project to the **target** project. Replace PROJECT_ID with the project ID of your target project:
            
            gcloud config set project PROJECT_ID

     2. View the list of services already enabled:
            
            gcloud services list

     3. If you don't see all of the required services listed, enable them:
            
            gcloud services enable servicemanagement.googleapis.com servicecontrol.googleapis.com iam.googleapis.com cloudresourcemanager.googleapis.com compute.googleapis.com




## Set required permissions

For a user to be able to add a target project, and to configure the details of the Compute Engine instance on the target project, that user requires the necessary [IAM](https://docs.cloud.google.com/iam/docs/overview) roles and permissions.

Because you perform these actions in the [Google Cloud console](https://console.cloud.google.com/), the user account that requires these permissions is the account that you use to sign in to the Google Cloud console:

  * To **add** a target project to Migrate to Virtual Machines, the user account you use to sign in to the Google Cloud console requires the permissions described in Set permissions to add a target project.

  * To **configure the target details** of the Compute Engine instance running on the target project, the user account you use to sign in to the Google Cloud console requires permissions to access data in the target project, such as networks, instance types, and more. For more information, see Set permissions to configure a target instance.




Depending on how you configure IAM for your environment, you might configure a single user to perform both actions, or configure two separate users.

### Set permissions to add a target project

To add a target project, the user account you use on the Google Cloud console requires:

  * The role `vmmigration.admin` on the **host** project

  * The role `resourcemanager.projectIamAdmin` on the **target** project

**Note:** If your user account does not have the `resourcemanager.projectIamAdmin` role on the target project, or you are forbidden from adding it for security reasons, you can still add the target project. However, a warning icon, _warning_ , appears next to the project name when you add it and you won't be able to deploy Compute Engine instances on the target project.

As a workaround, contact the security administrator for the target project to get your user account configured with the `resourcemanager.projectIamAdmin` role, and then try to add the target project. 

Alternatively, after you add the target project, assign the role `vmmigration.serviceAgent` on the target project to the Migrate to Virtual Machines default service account using the following steps.




To add these roles:

  1. Determine the email address of your user account. In the [Google Cloud console](https://console.cloud.google.com/), you can see all users in your project on the **IAM** page:

[Go to the project selector page](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. Grant your user account the `vmmigration.admin` role on the **host** project:
         
         gcloud projects add-iam-policy-binding HOST_PROJECT_ID --member=user:USER_EMAIL_ADDRESS --role=roles/vmmigration.admin

**Note:** Depending on the security configuration of your project, you might be prompted to select a [condition](https://docs.cloud.google.com/iam/docs/conditions-overview). Often selecting the option of **None** is correct, but confirm that with your security team.
  3. Grant your user account the `resourcemanager.projectIamAdmin` role on the **target** project:
         
         gcloud projects add-iam-policy-binding TARGET_PROJECT_ID --member=user:USER_EMAIL_ADDRESS --role=roles/resourcemanager.projectIamAdmin




If you are unable to assign role `resourcemanager.projectIamAdmin` on the target project to your user account, you can assign the role `vmmigration.serviceAgent` on the target project to the Migrate to Virtual Machines default service account.

To add this role:

  1. Open the Migrate to Virtual Machines page in the Google Cloud console:

[Go to the Migrate to Virtual Machines page](https://console.cloud.google.com/compute/mfce)

  2. Select the **Targets** tab.

At the top of the page is an information box showing the email address of the Migrate to Virtual Machines default service account in the form:

`service-HOST_PROJECT_NUMBER@gcp-sa-vmmigration.iam.gserviceaccount.com`

  3. Copy the email address.

  4. Use that email address to grant the `vmmigration.serviceAgent` role on the target project to the Migrate to Virtual Machines default service account:
         
         gcloud projects add-iam-policy-binding TARGET_PROJECT_ID \
            --member=serviceAccount:service-HOST_PROJECT_NUMBER@gcp-sa-vmmigration.iam.gserviceaccount.com \
            --role=roles/vmmigration.serviceAgent




### Set permissions to configure target details

To configure the target details of the Compute Engine instance on the target project, the user account you use on the Google Cloud console requires:

  * The role `compute.viewer` and the role `iam.serviceAccountUser` on the **target** project

**Note:** If your environment uses a [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc), then the user account only requires the `compute.viewer` role on the **Shared VPC host project**.



To add this role:

  1. Determine the email address of your user account. In the [Google Cloud console](https://console.cloud.google.com/), you can see all users in your project on the **IAM** page:

[Go to the project selector page](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. Grant your user account the `compute.viewer` role and the `iam.serviceAccountUser` role on the **target** project:
         
         gcloud projects add-iam-policy-binding TARGET_PROJECT_ID --member=user:USER_EMAIL_ADDRESS --role=roles/compute.viewer
         
         gcloud projects add-iam-policy-binding TARGET_PROJECT_ID --member=user:USER_EMAIL_ADDRESS --role=roles/iam.serviceAccountUser

  3. (**Shared VPC environment only**) Grant your user account the `compute.viewer` role on the **Shared VPC host** project:
         
         gcloud projects add-iam-policy-binding VPC_HOST_PROJECT_ID --member=user:USER_EMAIL_ADDRESS --role=roles/compute.viewer




## Add the target project

After you have configured the target project, and assigned the necessary roles to the user account, you can add it to Migrate to Virtual Machines.

**Note:** Adding a target project adds permissions to the default Migrate to Virtual Machines service account to perform operations on the target project.

To add a target project to Migrate to Virtual Machines:

  1. Open the Migrate to Virtual Machines page in the Google Cloud console:

[Go to the Migrate to Virtual Machines page](https://console.cloud.google.com/compute/mfce)

  2. Select the **Targets** tab. A list of projects already added appears.

  3. Select **Add Projects**.

A panel opens listing the available projects.

  4. Select one or more projects.

**Note:** If your user account does not have the necessary permissions to add the project, a warning icon, _warning_ , appears next to the project name. Hold the pointer over over the icon to see the associated error message. See Set permissions to add a target project to add the necessary permissions, then retry this step.
  5. Select **Add**.

The new project appears in the projects table.




## Remove a target project

You can remove a target project from Migrate to Virtual Machines. Removing the target project means you can no longer perform a test-clone or cut-over operation that uses the target project to host Compute Engine instances.

**Note:** Compute Engine instances on the target project already running your migrated VMs are not affected when you remove the target project from Migrate to Virtual Machines.

When you add a target project to Migrate to Virtual Machines, Migrate to Virtual Machines automatically adds permissions to the default Migrate to Virtual Machines service account on the host project that allows the host project to perform operations on the target project.

When you later remove the target project, Migrate to Virtual Machines attempts to remove those permissions on the service account. However, if there has been a change that prevents those permissions from being removed, the target project is still removed from Migrate to Virtual Machines. If necessary you can manually update the service account to remove those permissions.

To remove a target project from Migrate to Virtual Machines:

  1. Open the Migrate to Virtual Machines page in the Google Cloud console:

[Go to the Migrate to Virtual Machines page](https://console.cloud.google.com/compute/mfce)

  2. Select the **Targets** tab. A list of projects already added appears.

  3. Select one or more projects.

  4. Select **Remove Projects**.

  5. Confirm that you want to remove the projects.




## What's next

  * [Migrating individual VMs](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/migrating-vms)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
