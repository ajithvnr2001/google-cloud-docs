---
url: https://docs.cloud.google.com/security-command-center/docs/iac-validation-tutorial/
title: Create a sample IaC validation report \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:44:16.809903+00:00
---

# Create a sample IaC validation report  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/iac-validation-tutorial/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Create a sample IaC validation report Stay organized with collections  Save and categorize content based on your preferences. 

Standard-legacy, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) (requires [organization-level activation](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation)) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

This tutorial describes how you can verify that your infrastructure as code (IaC) doesn't violate your organization policies or Security Health Analytics detectors.

## Objectives

  * Create a security posture.
  * Deploy the posture on a project.
  * Check an example Terraform file for violations.
  * Fix the violations in the Terraform file, and check the file again to verify the fix.



## Before you begin

### Set up permissions

Make sure that you have the following role or roles on the organization: Project Creator and Security Posture Admin 

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



### Set up Cloud Shell

In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  1. Find your organization ID: 
         
         gcloud organizations list




## Prepare the environment

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  3. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  4. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  5. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Security posture service and Security Command Center management APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable securityposture.googleapis.com  securitycentermanagement.googleapis.com

  8. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  9. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  10. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  11. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  12. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  13. Enable the Security posture service and Security Command Center management APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable securityposture.googleapis.com  securitycentermanagement.googleapis.com

  14. Copy the project number. You will need the project number to set the target resource while deploying the posture. 
         
         gcloud projects describe PROJECT_ID

  15. Initialize Terraform: 
         
         terraform init




## Create and deploy a posture

  1. In Cloud Shell, launch the Cloud Shell Editor. To launch the editor, click ![Code Editor Button](https://docs.cloud.google.com/static/shell/docs/images/open-editor.png)**Open Editor** on the toolbar of the Cloud Shell window.

  2. Create a YAML file named `example-standard.yaml`.

  3. Paste the following code into your file:



    
    
    name: organizations/ORGANIZATION_ID/locations/global/postures/example-standard
    state: ACTIVE
    policySets:
    - policies:
      - constraint:
          orgPolicyConstraintCustom:
            customConstraint:
              actionType: ALLOW
              condition: "resource.initialNodeCount == 3"
              description: Set initial node count to be exactly 3.
              displayName: fixedNodeCount
              methodTypes:
              - CREATE
              name: organizations/ORGANIZATION_ID/customConstraints/custom.fixedNodeCount
              resourceTypes:
              - container.googleapis.com/NodePool
            policyRules:
            - enforce: true
        policyId: fixedNodeCount
      - constraint:
          securityHealthAnalyticsCustomModule:
            config:
              customOutput: {}
              description: Set MTU for a network to be exactly 1000.
              predicate:
                expression: "!(resource.mtu == 1000)"
              recommendation: Only create networks whose MTU is 1000.
              resourceSelector:
                resourceTypes:
                - compute.googleapis.com/Network
              severity: HIGH
            displayName: fixedMTU
            moduleEnablementState: ENABLED
        policyId: fixedMTU
      - constraint:
          securityHealthAnalyticsModule:
            moduleEnablementState: ENABLED
            moduleName: BUCKET_POLICY_ONLY_DISABLED
        policyId: bucket_policy_only_disabled
      - constraint:
          securityHealthAnalyticsModule:
            moduleEnablementState: ENABLED
            moduleName: BUCKET_LOGGING_DISABLED
        policyId: bucket_logging_disabled
      policySetId: policySet1

Replace `ORGANIZATION_ID` with your organization ID.

  1. In Cloud Shell, create the posture:
         
         gcloud scc postures create organizations/ORGANIZATION_ID/locations/global/postures/example-standard --posture-from-file=example-standard.yaml
         

  2. Copy the posture revision ID that the command generates.

  3. Deploy the posture to your project:
         
         gcloud scc posture-deployments create organizations/ORGANIZATION_ID/locations/global/postureDeployments/example-standard \
         --posture-name=organizations/ORGANIZATION_ID/locations/global/postures/example-standard \
         --posture-revision-id="POSTURE_REVISION_ID" \
         --target-resource=projects/PROJECT_NUMBER
         

Replace the following:

     * `ORGANIZATION_ID`: your organization ID.
     * `POSTURE REVISION_ID`: your posture revision ID that you copied.
     * `PROJECT_NUMBER`: your project number.



## Create the Terraform file and validate

  1. In Cloud Shell, launch the Cloud Shell Editor.

  2. Create a Terraform file named `main.tf`.

  3. Paste the following code into your file:
         
         terraform {
           required_providers {
             google = {
               source  = "hashicorp/google"
             }
           }
         }
         
         provider "google" {
           region  = "us-central1"
           zone    = "us-central1-c"
         }
         
         resource "google_compute_network" "example_network"{
           name                            = "example-network-1"
           delete_default_routes_on_create = false
           auto_create_subnetworks         = false
           routing_mode                    = "REGIONAL"
           mtu                             = 100
           project                         = "PROJECT_ID"
         }
         
         resource "google_container_node_pool" "example_node_pool" {
           name               = "example-node-pool-1"
           cluster            = "example-cluster-1"
           project            = "PROJECT_ID"
           initial_node_count = 2
         
           node_config {
             preemptible  = true
             machine_type = "e2-medium"
           }
         }
         
         resource "google_storage_bucket" "example_bucket" {
           name          = "example-bucket-1"
           location      = "EU"
           force_destroy = true
         
           project = "PROJECT_ID"
         
           uniform_bucket_level_access = false
         }
         

Replace `PROJECT_ID` with the project ID of the project that you created.

  4. In Cloud Shell, create the Terraform plan file and convert it to JSON format:
         
         terraform plan -out main.plan
         terraform show -json main.plan > mainplan.json
         

  5. Create the IaC validation report for `mainplan.json`:
         
         gcloud scc iac-validation-reports create organizations/ORGANIZATION_ID/locations/global --tf-plan-file=mainplan.json
         

This command returns an IaC validation report that describes the following violations:

     * The `mtu` for `example_network` isn't 1000.
     * The `initial_node_count` for `example_node_pool` isn't 3.
     * The `example_bucket` doesn't have uniform bucket level access enabled.
     * The `example_bucket` doesn't have logging enabled.



## Resolve violations

  1. In Cloud Shell, launch the Cloud Shell Editor.

  2. Update the `main.tf` file with the following changes:
         
         terraform {
           required_providers {
             google = {
               source  = "hashicorp/google"
             }
           }
         }
         
         provider "google" {
           region  = "us-central1"
           zone    = "us-central1-c"
         }
         
         resource "google_compute_network" "example_network"{
           name                            = "example-network-1"
           delete_default_routes_on_create = false
           auto_create_subnetworks         = false
           routing_mode                    = "REGIONAL"
           **mtu                             = 1000**
           project                         = "PROJECT_ID"
         }
         
         resource "google_container_node_pool" "example_node_pool" {
           name               = "example-node-pool-1"
           cluster            = "example-cluster-1"
           project            = "PROJECT_ID"
           **initial_node_count = 3**
         
           node_config {
             preemptible  = true
             machine_type = "e2-medium"
           }
         }
         
         resource "google_storage_bucket" "example_bucket" {
           name          = "example-bucket-1"
           location      = "EU"
           force_destroy = true
         
           project = "PROJECT_ID"
           **uniform_bucket_level_access = true**
         
           **logging {
             log_bucket   = "my-unique-logging-bucket" // Create a separate bucket for logs
             log_object_prefix = "tf-logs/"             // Optional prefix for better structure
           }**
         }
         

Replace `PROJECT_ID` with the project ID of the project that you created.

  3. In Cloud Shell, create the Terraform plan file and convert it to JSON format:
         
         terraform plan -out main.plan
         terraform show -json main.plan > mainplan.json
         

  4. Recreate the IaC validation report for `mainplan.json`:
         
         gcloud scc iac-validation-reports create organizations/ORGANIZATION_ID/locations/global --tf-plan-file=mainplan.json
         




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

### Delete the project

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

Delete a Google Cloud project:
    
    gcloud projects delete PROJECT_ID




## What's next

  * Review [Validate your IaC against your organization's policies](https://docs.cloud.google.com/security-command-center/docs/validate-iac).
  * Explore reference architectures, diagrams, and best practices about Google Cloud. Take a look at our [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
