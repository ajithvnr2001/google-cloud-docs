---
url: https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/create-os-policy-assignment/
title: Create an OS policy assignment \u00a0|\u00a0 VM Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:45:19.941624+00:00
---

# Create an OS policy assignment  |  VM Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/create-os-policy-assignment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ VM Manager ](https://docs.cloud.google.com/compute/vm-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/vm-manager/docs/overview)



Send feedback 

#  Create an OS policy assignment Stay organized with collections  Save and categorize content based on your preferences. 

Use OS policies to maintain [consistent software configurations](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies) across Linux and Windows virtual machine (VM) instances.

## Before you begin

  * Review [OS policy and OS policy assignment](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/working-with-os-policies).
  * Review [OS Config quotas](https://docs.cloud.google.com/compute/vm-manager/docs/os-config-quotas).
  * To generate audit logs for VM Manager events, [enable data access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access).
  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
           
           gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
    2. [ Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).

### Terraform

To use the Terraform samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

    2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

    3. If you're using a local shell, then create local authentication credentials for your user account: 
           
           gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [ Set up authentication for a local development environment](https://docs.cloud.google.com/compute/docs/authentication#local-development). 

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




## Supported operating systems

For a full list of operating systems and versions that support OS policies, see [Operating system details](https://docs.cloud.google.com/compute/docs/images/os-details#vm-manager).

## Permissions

Because you can use OS policies to install and manage software packages on a VM, the creation and management of OS policies is equivalent to granting remote code execution access on a VM. When you set up OS policies, IAM permissions are used to control access to the policy resources and activities are audit logged.

Owners of a project have full access to create and manage OS policy assignments. For all other users, you need to grant permissions. You can grant one of the following granular roles:

**Caution:** The OSPolicyAssignment Admin and OSPolicyAssignment Editor roles include the `osconfig.osPolicyAssignments.update` permission that provides access to manage software packages on the VMs. By granting these roles, you risk granting users unintended access to run code on VMs. To mitigate this risk, we recommend that you follow [ the principle of least privilege](https://docs.cloud.google.com/iam/docs/using-iam-securely#least_privilege) and provide only the required access to each user and monitor the usage of this IAM permission by users. 

  * OSPolicyAssignment Admin (`roles/osconfig.osPolicyAssignmentAdmin`). Contains permissions to create, delete, update, get and list OS policy assignments.
  * OSPolicyAssignment Editor (`roles/osconfig.osPolicyAssignmentEditor`). Contains permissions to update, get, and list OS policy assignments.
  * OSPolicyAssignment Viewer (`roles/osconfig.osPolicyAssignmentViewer`). Contains permissions for read-only access to get and list OS policy assignments.



#### Example command to set permissions

To grant admin access to a user for OS policy assignments, run the following command:
    
    
        gcloud projects add-iam-policy-binding PROJECT_ID \
            --member user:USER_ID@gmail.com \
            --role roles/osconfig.osPolicyAssignmentAdmin
    

Replace the following:

  * `PROJECT_ID`: the project ID
  * `USER_ID`: the user's Google Workspace username



## Create an OS policy assignment

To create and roll out an OS policy assignment, complete the following steps:

  1. [Set up VM Manager](https://docs.cloud.google.com/compute/docs/manage-os).
  2. Assign the required permissions to users.
  3. Review [OS policy and OS policy assignment](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/working-with-os-policies).
  4. Create the [OS policy resources](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.locations.osPolicyAssignments#OSPolicy).
  5. To create and roll out the OS policy assignment, use one of the following methods:

###  Console 

To create and roll out an OS policy assignment, complete the following steps:

     1. On your local client, create or download an OS policy. This must be a JSON or YAML file. For more information about creating OS policies or to view sample OS policies, see [OS policies](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/working-with-os-policies#os-policy).
     2. In the Google Cloud console, go to the **OS policies** page.

[Go to OS policies](https://console.cloud.google.com/compute/config/assignments/)

     3. Click **Create zonal**.

     4. In the **Assignment ID** section, provide a name for the OS policy assignment. See [Resource naming convention](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format).

     5. In the **OS policies** section, upload the OS policy file.

     6. In the **Target VM instances** section, specify the target VMs.

        * Select the zone that contains the VMs that you want to apply the policy to.
        * Select the OS families.
        * Optional: You can further filter the VMs by specifying include, and exclude labels.

For example, you can select all the Ubuntu VMs in your test environment, and exclude those that are running Google Kubernetes Engine, by specifying the following: 

        * OS short name: `ubuntu`
        * Include: `env:test`, `env:staging`
        * Exclude: `goog-gke-node`

![Select target VMs.](https://docs.cloud.google.com/static/compute/images/os-config/target-vms.png)

     7. Specify a rollout plan.

        * Specify the wave size (also referred to as the disruption budget). For example, 10%.
        * Specify the wait time. For example, 15 minutes. 

![Rollout configuration.](https://docs.cloud.google.com/static/compute/images/os-config/rollout.png)

     8. Click **Start rollout**.

###  gcloud 

To create and roll out an OS policy assignment in a zone, complete the following steps:

     1. Create an OS policy assignment resource in the JSON or YAML format. This file defines the OS policies that you want to apply to your VMs, the target VMs that you want to apply the policies to, and the rollout rate at which to apply the OS policies. For more information about this file and sample assignments, see [OS policy assignment](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/working-with-os-policies#os-policy-assignment).

     2. Use the [`os-config os-policy-assignments create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/os-config/os-policy-assignments/create) to create and roll out the OS policy assignment in a specified location.
            
            gcloud compute os-config os-policy-assignments create OS_POLICY_ASSIGNMENT_ID \
               --location=ZONE \
               --file=OS_POLICY_ASSIGNMENT_FILE \
               --async
            

Replace the following:

        * `OS_POLICY_ASSIGNMENT_ID`: name for the OS policy assignment. See [Resource naming convention](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format).
        * `ZONE`: zone to create the OS policy assignment in.
        * `OS_POLICY_ASSIGNMENT_FILE`: the absolute path to the OS policy assignment file that you created in the previous step.

**Example**
    
    gcloud compute os-config os-policy-assignments create my-os-policy-assignment \
        --location=asia-south1-a \
        --file=/downloads/assignment-config.yaml \
        --async
    

The output is similar to the following:
    
    Create request issued for: [my-os-policy-assignment]
    Check operation [projects/384123488288/locations/asia-south1-a/osPolicyAssignments/my-os-policy-assignment/operations/fb2011d6-61de-46f1-afdb-bc96bdb3fbaa] for status.
    

     3. Make note of the fully qualified resource name for the operation. In the previous example the fully qualified resource name is:
            
            projects/384123488288/locations/asia-south1-a/osPolicyAssignments/my-os-policy-assignment/operations/fb2011d6-61de-46f1-afdb-bc96bdb3fbaa
            

You can use this fully qualified resource name to get details for a rollout, or to cancel a rollout. See Rollouts.

###  Terraform 

To create an OS policy assignment, use the [`google_os_config_os_policy_assignment` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/os_config_os_policy_assignment).

The following example verifies if the Apache web server is running on CentOS VMs.
    
    resource "google_os_config_os_policy_assignment" "my_os_policy_assignment" {
    
      name        = "my-os-policy-assignment"
      location    = "us-west1-a"
      description = "An OS policy assignment that verifies if the Apache web server is running on CentOS VMs."
    
      instance_filter {
        # filter to select VMs
        all = false
    
        exclusion_labels {
          labels = {
            label-one = "goog-gke-node"
          }
        }
    
        inclusion_labels {
          labels = {
            env = "test",
          }
        }
    
        inventories {
          os_short_name = "centos"
          os_version    = "7*"
        }
      }
    
      os_policies {
        #list of OS policies to be applied to VMs
        id   = "apache-always-up-policy"
        mode = "ENFORCEMENT"
    
        resource_groups { #list of resource groups for the policy
          resources {
            id = "ensure-apache-is-up"
    
            exec {
              validate {
                interpreter = "SHELL"
                script      = "if systemctl is-active --quiet httpd; then exit 100; else exit 101; fi"
              }
    
              enforce {
                interpreter = "SHELL"
                script      = "systemctl start httpd && exit 100"
              }
            }
          }
    
          inventory_filters {
            os_short_name = "centos"
            os_version    = "7*"
          }
        }
    
        allow_no_resource_group_match = false #OS policy compliance status
        description                   = "An OS policy that verifies if the Apache web server is running on Linux VMs."
      }
    
      rollout {
        #define rollout parameters
        disruption_budget {
          fixed = 1
        }
        min_wait_duration = "3.5s"
      }
    }

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

###  REST 

To create an OS policy assignment on your local client, complete the following steps:

     1. Create an OS policy assignment. This must be a JSON file. For more information about creating OS policy assignments or to view sample OS policy assignments, see [OS policy assignment](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/working-with-os-policies#os-policy-assignment).

If you want to use the sample YAML OS policy assignment, you must convert it to JSON.

     2. In the API, create a `POST` request to the [`projects.locations.osPolicyAssignments.create` method](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.locations.osPolicyAssignments/create).

In the request body, paste the OS policy assignment specifications from the previous step.
            
            POST https://osconfig.googleapis.com/v1/projects/PROJECT_ID/locations/ZONE/osPolicyAssignments?osPolicyAssignmentId=OS_POLICY_ASSIGNMENT_ID
            
            {
             JSON_OS_POLICY
            }
            

Replace the following:

        * `PROJECT_ID`: your project ID
        * `OS_POLICY_ASSIGNMENT_ID`: name for the OS policy assignment
        * `JSON_OS_POLICY`: the OS policy assignment specifications created in the previous step. This must be in JSON format. For more information about the parameters and format, see [`Resource: OSPolicyAssignment`](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.locations.osPolicyAssignments#OSPolicyAssignment).
        * `ZONE`: zone to create the OS policy assignment in

**Example**

For example, to create an OS policy assignment for Google Cloud Observability that installs monitoring and logging agents on selected VMs by using the [Sample OS policy assignment](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/working-with-os-policies#example-policy-assignment), complete the following steps:

        1. Convert the sample to JSON
        2. Make the following request:
    
    POST https://osconfig.googleapis.com/v1/projects/PROJECT_ID/locations/ZONE/osPolicyAssignments?osPolicyAssignmentId=OS_POLICY_ASSIGNMENT_ID
    
    {
      "osPolicies": [
        {
          "id": "setup-repo-and-install-package-policy",
          "mode": "ENFORCEMENT",
          "resourceGroups": [
            {
              "resources": [
                {
                  "id": "setup-repo",
                  "repository": {
                    "yum": {
                      "id": "google-cloud-monitoring",
                      "displayName": "Google Cloud Monitoring Agent Repository",
                      "baseUrl": "https://packages.cloud.google.com/yum/repos/google-cloud-monitoring-el8-x86_64-all",
                      "gpgKeys": [
                        "https://packages.cloud.google.com/yum/doc/yum-key.gpg",
                        "https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg"
                      ]
                    }
                  }
                },
                {
                  "id": "install-pkg",
                  "pkg": {
                    "desiredState": "INSTALLED",
                    "yum": {
                      "name": "stackdriver-agent"
                    }
                  }
                }
              ]
            }
          ]
        }
      ],
      "instanceFilter": {
        "inclusionLabels": [
          {
            "labels": {
              "used_for": "testing"
            }
          }
        ]
      },
      "rollout": {
        "disruptionBudget": {
          "fixed": 10
        },
        "minWaitDuration": {
          "seconds": 300
        }
      }
    }
    




## Rollouts

OS policy assignments are deployed according to a rollout rate. This means that assignments that target a set of VMs can be deployed gradually and aren't applied to all the VMs immediately. Changes are rolled out gradually to give you an opportunity to intervene and cancel a rollout if new changes cause regressions.

When method calls to an API might take a long time to complete, the API returns a long-running operations (LRO). For more information about LROs, see [Long-running operations](https://google.aip.dev/151).

The OS Config API creates an LRO every time you create, update, or delete an OS policy assignment. Each LRO returns an operation resource. This operation resource is similar to the following:
    
    
    Create request issued for: [my-os-policy-assignment]
    Check operation [projects/384123488288/locations/asia-south1-a/osPolicyAssignments/my-os-policy-assignment/operations/fb2011d6-61de-46f1-afdb-bc96bdb3fbaa] for status.
    

Each create, update, or delete operation also generates a new OS policy assignment revision. To view the revisions for an OS policy assignment, see [List OS policy assignment revisions](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/manage-os-policy#list-revisions).

You can use the Google Cloud CLI to get the details of a rollout, or to cancel a rollout.

### Get details for a rollout

To get details for a rollout, use the [`os-config os-policy-assignments operations describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/os-config/os-policy-assignments/operations/describe).
    
    
    gcloud compute os-config os-policy-assignments operations describe FULLY_QUALIFIED_OPERATION_NAME
    

Replace `FULLY_QUALIFIED_OPERATION_NAME` with the fully qualified resource name for the operation that is returned from the create, update, or delete operation.

**Example**
    
    
    gcloud compute os-config os-policy-assignments operations describe \
        projects/384123488288/locations/asia-south1-a/osPolicyAssignments/my-os-policy-assignment/operations/fb2011d6-61de-46f1-afdb-bc96bdb3fbaa
    

#### Example output
    
    
    done: true
    metadata:
      '@type': type.googleapis.com/google.cloud.osconfig.$$api-version$$.OSPolicyAssignmentOperationMetadata
      apiMethod: CREATE
      osPolicyAssignment: projects/3841234882888/locations/asia-south1-a/osPolicyAssignments/my-os-policy-assignment@cfb78790-41d8-40d1-b8a1-1eaf6011b909
      rolloutStartTime: '2021-04-15T00:53:52.963569Z'
      rolloutState: SUCCEEDED
      rolloutUpdateTime: '2021-04-15T00:53:53.094041Z'
    name: projects/3841234882888/locations/asia-south1-a/osPolicyAssignments/my-os-policy-assignment/operations/cfb78790-41d8-40d1-b8a1-1eaf6011b909
    response:
      '@type': type.googleapis.com/google.cloud.osconfig.$$api-version$$.OSPolicyAssignment
      baseline: true
      description: My test policy
      instanceFilter:
        inclusionLabels:
        - labels:
            label-key-not-targeting-instances: label-value-not-targeting-instances
      name: projects/3841234882888/locations/asia-south1-a/osPolicyAssignments/my-os-policy-assignment
      osPolicies:
      - id: q-test-policy
        mode: ENFORCEMENT
        resourceGroups:
        - osFilter:
            osShortName: centos
            osVersion: '7'
          resources:
          - id: add-repo
            repository:
              yum:
                baseUrl: https://packages.cloud.google.com/yum/repos/google-cloud-ops-agent-el7-x86_64-all
    

### Cancel a rollout

**Note:** After a cancellation, you cannot automatically rollback to the previous revision of an OS policy assignment. If you cancel an OS policy assignment update that is in progress, you must start a new update to make sure all VMs have the same assignment revision.

###  Console 

  1. In the Google Cloud console, go to the **OS policies** page.

[Go to OS policies](https://console.cloud.google.com/compute/config/assignments/)

  2. Click the **Zonal assignments** tab.

  3. For the OS policy assignment that you want to cancel the rollout, click **Action ( more_vert) > Cancel rollout**.

  4. Click **Cancel rollout**.




###  gcloud 

To cancel a rollout, use the [`gcloud compute os-config os-policy-assignments operations cancel` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/os-config/os-policy-assignments/operations/cancel).
    
    
    gcloud compute os-config os-policy-assignments operations cancel FULLY_QUALIFIED_OPERATION_NAME
    

Replace `FULLY_QUALIFIED_OPERATION_NAME` with the fully qualified resource name for the operation that is returned from the create, update, or delete operation.

**Example**
    
    
    gcloud compute os-config os-policy-assignments operations cancel \
        projects/384123488288/locations/asia-south1-a/osPolicyAssignments/my-os-policy-assignment/operations/fb2011d6-61de-46f1-afdb-bc96bdb3fbaa
    

If the command is successful, no output is returned.

## What's next?

  * Learn more about the [OS policies](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies).
  * [Manage OS policy assignments](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/manage-os-policy).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
