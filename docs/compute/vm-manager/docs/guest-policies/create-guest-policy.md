---
url: https://docs.cloud.google.com/compute/vm-manager/docs/guest-policies/create-guest-policy/
title: Create a guest policy (legacy) \u00a0|\u00a0 VM Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:45:57.958824+00:00
---

# Create a guest policy (legacy)  |  VM Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/vm-manager/docs/guest-policies/create-guest-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ VM Manager ](https://docs.cloud.google.com/compute/vm-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/vm-manager/docs/overview)



Send feedback 

#  Create a guest policy (legacy) Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** This page includes instructions about the legacy OS guest policies. A later version of OS policies is now [Generally Available (GA)](https://cloud.google.com/products/#product-launch-stages). To use the later GA version, see [Creating an OS policy assignment](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/create-os-policy-assignment)

To view a comparison of the two versions, see [Comparing OS policies versions](https://docs.cloud.google.com/compute/vm-manager/docs/guest-policies/comparing_policy_options). 

Use guest policies to maintain [consistent software configurations](https://docs.cloud.google.com/compute/vm-manager/docs/guest-policies) across Linux and Windows virtual machines (VM) instances.

To set up a guest policy on a set of VMs, complete the following steps:

  1. Assign the required permissions to users.
  2. Set up your VM.
  3. Configure the guest policy JSON or YAML file.
  4. Create the guest policy.



**Beta**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

## Before you begin

  * Review [OS Config quotas](https://docs.cloud.google.com/compute/vm-manager/docs/os-config-quotas).
  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

### gcloud

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
           
           gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
    2. [ Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




## Limitations

  * For targeted VMs, the guest policy updates each time the agent checks in with the service. This check happens every 10 to 15 minutes.
  * There are no compliance dashboards, notifications, or alerting services available with this legacy OS guest policies. VMs that are not running the OS Config agent don't report failure. For best results, use this feature with the [OS inventory management](https://docs.cloud.google.com/compute/vm-manager/docs/os-inventory/os-inventory-management) service or any other compliance monitoring tool.
  * A software recipe, with a specific name, only runs once when you create a guest policy. To rerun a software recipe, you must do the following:

    1. Rename the software recipe.
    2. Delete and recreate the guest policy using the renamed software recipe.



## Permissions

Because you can use guest policies to install and manage software packages on a VM, the creation and management of guest policies is equivalent to granting remote code execution access on a VM.

When you set up guest policies, IAM permissions are used to control access to the policy resource and activities are audit logged. However, users can still run code on the VM which poses a potential security risk. To mitigate this, we recommend that you provide only the required access to each user.

Owners of a project have full access to create and manage policies. For all other users, you need to grant permissions. You can grant one of the following granular roles:

  * GuestPolicy Admin (`roles/osconfig.guestPolicyAdmin`). Contains permissions to create, delete, update, get, and list guest policies.
  * GuestPolicy Editor (`roles/osconfig.guestPolicyEditor`). Contains permissions to get, update, and list guest policies.
  * GuestPolicy Viewer (`roles/osconfig.guestPolicyViewer`). Contains permissions for read-only access to get and list guest policies.



For example, to grant a user administrator access to guest policies, run the following command:
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member user:USER_ID@gmail.com \
        --role roles/osconfig.guestPolicyAdmin
    

Replace the following:

  * `PROJECT_ID`: the project ID.
  * `USER_ID`: the user's Google Workspace username.

**Note:** To view the configurations that apply to a VM, you must have the `osconfig.guestPolicies.get` permission.

## Set up your VM

To use guest policies, you need to [set up VM Manager](https://docs.cloud.google.com/compute/vm-manager/docs/setup).

## Configure a guest policy yaml or JSON file

You must provide guest policy specifications by using either a JSON or YAML file. To view sample configurations, see example guest policy YAML files.

The YAML or JSON file contains the following two main sections:

  * The assignment section which contains the list of target VMs.
  * The required configuration section which contains the state that you want to maintain on the VMs.



### Assignments

You can assign guest policies to all the VMs in your project or you can use the `assignment` key in your JSON or YAML file to target a specific group of VMs.

For example, you can target a group of VMs by using any of the following characteristics:

  * Instance name. See example 1.
  * Instance name prefix. See example 2.
  * Instance label. See example 3.
  * Zone. See example 4.
  * Operating system information, which contains OS name, version, and architecture. See example 5. The [os-inventory describe](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/instances/os-inventory/describe) command can be used to determine OS name, version, and architecture of VMs.



To assign a guest policy using operating system information, the OS Configuration agent must send operating system information to the guest attributes endpoint for the VM. To ensure privacy, by default, operating system information for VMs is unavailable. To group VMs by operating system information, you must ensure that the guest attributes and OS Inventory Management services are enabled. To enable these services, see Set up your VM.

Guest policy configurations are automatically applied to all new VMs that match the assignment.

### Required configuration

The required configuration can be accomplished by using any or a combination of the following tasks:

  * Install, remove, and auto-update software packages. See example 1.
  * Configure software package repositories. See example 1 or example 3.
  * Install software using software recipes. 
    * For Linux VMs, see example 5.
    * For Windows VMs, see example 4 or example 6.



### Example guest policy YAML files

### Example 1

Install the package `my-package` which must be kept up to date on the following VM instances: `my-instance-1` and `my-instance-2`.
    
    
    assignment:
      instances:
      - zones/us-east1-c/instances/my-instance-1
      - zones/us-east1-c/instances/my-instance-2
    packages:
    - name: "my-package"
      desiredState: UPDATED
    

For more information about assigning guest policies for packages, see the [Package JSON representation](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.guestPolicies#package) reference document.

### Example 2

Install the Cloud Monitoring agent, using the yum package manager, on all VM instances that have either of the following instance name prefixes: `test-instance-` or `dev-instance-`. 
    
    
    assignment:
      instanceNamePrefixes:
      - "test-instance-"
      - "dev-instance-"
    packages:
    - name: "stackdriver-agent"
      desiredState: INSTALLED
      manager: YUM
    packageRepositories:
    - yum:
        id: google-cloud-monitoring
        displayName: "Google Cloud Monitoring Agent Repository"
        baseUrl: https://packages.cloud.google.com/yum/repos/google-cloud-monitoring-el7-x86_64-all
        gpgKeys:
        - https://packages.cloud.google.com/yum/doc/yum-key.gpg
        - https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg
    

For more information about assigning guest policies for pacakage repositories, see the [PackageRepository JSON representation](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.guestPolicies#packagerepository) reference document.

### Example 3

Install `my-package` and remove `bad-package-1` and `bad-package-2` from instances with a specific set of labels. Also add repositories for the apt and yum package managers.
    
    
    assignment:
      # Assign to VM instances where `(label.color=red AND label.env=test) OR (label.color=blue AND label.env=test)`
      groupLabels:
      - labels:
          color: red
          env: test
      - labels:
          color: blue
          env: test
    packages:
    - name: "my-package"
      desiredState: INSTALLED
    - name: "bad-package-1"
      desiredState: REMOVED
    - name: "bad-package-2"
      desiredState: REMOVED
      manager: APT  # Only apply this to systems with APT.
    packageRepositories:
    - apt:  # Only apply this to systems with APT.
        uri: "https://packages.cloud.google.com/apt"
        archiveType: DEB
        distribution: cloud-sdk-stretch
        components:
        - main
    - yum:  # Only apply this to systems with YUM.
        id: google-cloud-sdk
        displayName: "Google Cloud SDK"
        baseUrl: https://packages.cloud.google.com/yum/repos/cloud-sdk-el7-x86_64
        gpgKeys:
        - https://packages.cloud.google.com/yum/doc/yum-key.gpg
        - https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg
    

  * For more information about assigning guest policies for packages, see the [Package JSON representation](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.guestPolicies#package) reference document.
  * For more information about assigning guest policies for pacakage repositories, see the [PackageRepository JSON representation](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.guestPolicies#packagerepository) reference document.



### Example 4

Install software from an MSI hosted on Cloud Storage to all instances in `us-east1-b` and `us-east1-d`.
    
    
    assignment:
      zones:
      - us-east1-b
      - us-east1-d
    recipes:
    - name: "swr-msi-gcs"
      desiredState: INSTALLED
      artifacts:
      - id: "the-msi"
        gcs:
          bucket: "my-bucket"
          object: "executable.msi"  # full URI gs://my-bucket/executable.msi#nnnnn
          generation: 1546030865175603
      installSteps:
      - msiInstallation:
          artifactId: "the-msi"
    

For more information about configuring recipe policies, see the [SoftwareRecipe JSON representation](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.guestPolicies#softwarerecipe) reference document.

### Example 5

Install software by running an inline script on all VM instances that meet the following requirements:

  * Operating system: Red Hat Enterprise Linux 7
  * Label: `color=red`


    
    
    assignment:
      osTypes:
      - osShortName: rhel
        osVersion: "7"
      groupLabels:
      - labels:
          color: red
    recipes:
    - name: recipe-runscript
      desiredState: INSTALLED
      installSteps:
      - scriptRun:
          script: |-
            #!/bin/bash
            touch /TOUCH_FILE
    

For more information about configuring recipe policies, see the [SoftwareRecipe JSON representation](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.guestPolicies#softwarerecipe) reference document.

### Example 6

Installs application on all Windows instances using an executable installer that has the following instance name prefix: `test-instance-`.
    
    
    assignment:
      instanceNamePrefixes:
      - "test-instance-"
      osTypes:
      - osShortName: WINDOWS
    recipes:
    - name: windows-install-exe-example
      desiredState: INSTALLED
      artifacts:
      - id: installer
        gcs:
          bucket: my-bucket
          generation: '1597013478912389'
          object: MyApp.Installer.x64.exe
      installSteps:
      - fileExec:
          artifactId: installer
          args:
          - /S # Installation must be silent
    

For more information about configuring recipe policies, see the [SoftwareRecipe JSON representation](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.guestPolicies#softwarerecipe) reference document.

## Create a guest policy

When you create a guest policy, the name of the guest policy must meet the following naming requirements:

  * Contain only lowercase letters, numbers, and hyphens
  * Start with a letter
  * End with a number or a letter
  * Be between 1 and 63 characters
  * Each policy ID must be unique within a project



Use one of the following methods to create a guest policy.

###  gcloud 

Use the [`os-config guest-policies create`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/os-config/guest-policies/create) command to create a guest policy.
    
    
    gcloud beta compute os-config guest-policies create POLICY_ID \
        --file=FILE
    

Replace the following:

  * `POLICY_ID`: the name for the guest policy that you want to create.
  * `FILE`: JSON or YAML file that contains the guest policy specifications. To view sample configurations, see Example guest policy YAML files.



###  REST 

In the API, create a `POST` request to the [`projects.guestPolicies.create`](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.guestPolicies/create) method.
    
    
    POST https://osconfig.googleapis.com/v1beta/projects/PROJECT_ID/guestPolicies?guestPolicyId=POLICY_ID
    
    {
     For more information, see [Guest policy JSON](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.guestPolicies#GuestPolicy)
    }
    

Replace the following:

  * `PROJECT_ID`: your project ID.
  * `POLICY_ID`: the name for your guest policy.



To view sample configurations, see example guest policy YAML files.

## Troubleshooting

To troubleshoot a guest policy, see [Debugging a guest policy](https://docs.cloud.google.com/compute/vm-manager/docs/guest-policies/manage-guest-policy#debug-policy).

## What's next?

  * Learn more about the [OS guest policies (legacy)](https://docs.cloud.google.com/compute/vm-manager/docs/guest-policies).
  * [Manage guest policies](https://docs.cloud.google.com/compute/vm-manager/docs/guest-policies/manage-guest-policy).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
