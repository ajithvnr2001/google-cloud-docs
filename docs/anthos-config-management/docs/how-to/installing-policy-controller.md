---
url: https://docs.cloud.google.com/anthos-config-management/docs/how-to/installing-policy-controller/
title: Install Policy Controller \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T09:56:53.300128+00:00
---

# Install Policy Controller  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos-config-management/docs/how-to/installing-policy-controller/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Policy Controller ](https://docs.cloud.google.com/kubernetes-engine/policy-controller)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/overview)



Send feedback 

#  Install Policy Controller Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to install [Policy Controller](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/overview). Policy Controller checks, audits, and enforces your clusters' compliance with policies related to security, regulations, or business rules.

This page is for IT administrators and Operators who want to ensure that all resources running within the cloud platform meet organizational compliance requirements by providing and maintaining automation to audit or enforce. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

Policy Controller is available if you use Google Kubernetes Engine. To learn more, see [Google Kubernetes Engine pricing](https://cloud.google.com/kubernetes-engine/pricing).

**Note:** The Policy Controller webhook fails to open when Policy Controller is not running. This is to avoid interfering with cluster operations while the controller is down (for example, during upgrades). When the controller becomes available, the audit logs record the resources that don't comply with [constraints](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/creating-policy-controller-constraints).**Caution:** Don't use these steps for Config Controller-created clusters because Policy Controller is already included. See the [Config Controller overview](https://docs.cloud.google.com/kubernetes-engine/config-controller/docs/overview) for more information.

## Before you begin

Before you start, make sure you have performed the following tasks:

  1. Install and initialize the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs), which provides the `gcloud`, `kubectl`, and `nomos` commands used in these instructions. If you previously installed the gcloud CLI, get the latest version by running `gcloud components update`. If you use [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works), Google Cloud CLI comes pre-installed.
  2. Ensure open source Open Policy Agent Gatekeeper is not installed on your cluster. If it is, [uninstall Gatekeeper](https://open-policy-agent.github.io/gatekeeper/website/docs/install#uninstallation) before installing Policy Controller.

  3. Enable the required APIs:

###  console 

Enable the Policy Controller API.

[Enable Policy Controller API](https://console.cloud.google.com/apis/enableflow?apiid=anthospolicycontroller.googleapis.com)

###  gcloud 

Run the following command:
         
         gcloud services enable anthospolicycontroller.googleapis.com
         

  4. Create, or make sure you have access to, a cluster running a Kubernetes version of 1.14.x or later. Policy Controller might appear to run on versions of Kubernetes earlier than 1.14.x, but the product does not behave correctly.

  5. [Grant the required IAM roles to the user registering the cluster](https://docs.cloud.google.com/anthos/multicluster-management/connect/prerequisites#grant_iam_roles).

  6. If you plan to use the Google Cloud CLI to configure Policy Controller, [register your cluster](https://docs.cloud.google.com/anthos/multicluster-management/connect/registering-a-cluster#register_cluster) to a [fleet](https://docs.cloud.google.com/anthos/multicluster-management/fleets) now. If you plan to use the Google Cloud console, register your clusters when you install Policy Controller.

  7. If you're using GKE attached clusters, ensure that your AKS cluster does not have the Azure Policy add-on and avoid labeling namespaces with the key [`control-plane`](https://learn.microsoft.com/en-us/azure/aks/faq#can-i-use-admission-controller-webhooks-on-aks).

  8. If you're using Google Distributed Cloud on VMware or bare metal, ensure that you are installing Policy Controller on a user cluster. Policy Controller can't be installed on an admin cluster.




## Install Policy Controller

**Note:** When you install Config Sync using the Google Cloud console or the Google Cloud CLI, you cannot later use `kubectl` commands to modify your configuration.

### Console

To install Policy Controller in the Google Cloud console, complete the following steps:

  1. In the Google Cloud console, go to the **Policy** page under the **Posture Management** section. 

[Go to Policy](https://console.cloud.google.com/kubernetes/policy_controller)

  2. Click _add_ **Configure Policy Controller**.

  3. Optional: To change the default fleet settings, click **Customize fleet settings**. In the dialog that appears, do the following:

     1. In the **Add/Edit policy bundles** section, include or exclude a policy bundle by clicking the relevant toggle. **Warning:** After you choose a method to apply policy bundles (manual, gcloud CLI, or Google Cloud console), using a different method to install policy bundles can cause errors in your environment. 
     2. In the **Edit Policy Controller configuration** section, do the following:

        1. To enable the [mutation webhook](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/mutation), select the **Enable mutation webhook** checkbox. This feature is not compatible with Autopilot clusters.
        2. In the **Audit interval** box, enter the period in seconds between two consecutive audits.
        3. In the **Exemptible namespaces** box, enter a list of namespaces. Policy Controller ignores objects in these namespaces. This feature is not compatible with Autopilot clusters.

**Best practice** : 

Exempt system namespaces to avoid errors in your environment. You can find the instructions to exempt namespaces and a list of common namespaces created by Google Cloud services on the [Exclude namespaces page](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/policy-controller-exclude-namespaces).

        4. To enable [referential constraints](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/creating-policy-controller-constraints#referential), select the **Enable Constraint Templates that reference to objects other than the object currently being evaluated** checkbox.

        5. In the **Version** list, select the Policy Controller version that you want to use.

     3. Click **Save changes**.

  4. Click **Configure**.

  5. In the confirmation dialog, click **Confirm**. If you haven't previously enabled Policy Controller, clicking **Confirm** enables the `anthospolicycontroller.googleapis.com` API and installs Policy Controller on your clusters.

  6. Optional: Sync existing clusters to the default settings:

     1. In the **Settings** tab, click **Sync to fleet settings**.
     2. In the **Clusters in the fleet** list, select the clusters that you want to sync and then click **Sync to fleet settings**. This operation can take a few minutes to complete.



You are redirected to the Policy Controller **Settings** tab. When Policy Controller is installed and configured on your clusters, the status columns show **Installed** _check_circle_. This can take several minutes.

### gcloud

Enable Policy Controller by running the following command:
    
    
    gcloud container fleet policycontroller enable \
        --memberships=MEMBERSHIP_NAME
    

You can set additional fields to configure Policy Controller. For example, you might want to tell Policy Controller to exempt some namespaces from enforcement. For a full list of fields you can configure, see the [Policy Controller Google Cloud CLI documentation](https://docs.cloud.google.com/sdk/gcloud/reference/container/fleet/policycontroller) or run `gcloud container fleet policycontroller enable --help`.

Set fleet-level settings for Policy Controller by completing the following steps:

  1. Create a file named `fleet-default.yaml` that contains the default configurations for Policy Controller. The `installSpec` field is required to enable fleet-level defaults. This example shows the options you can configure:
         
         # cat fleet-default.yaml
         
         ** policyControllerHubConfig:
           installSpec: INSTALL_SPEC_ENABLED **
           # Uncomment to set default deployment-level configurations.
           # deploymentConfigs:
           #   admission:
           #     containerResources:
           #       limits:
           #         cpu: 1000m
           #         memory: 8Gi
           #       requests:
           #         cpu: 500m
           #         memory: 4Gi
           # Uncomment to set policy bundles that you want to install by default.
           # policyContent:
           #   bundles:
           #     cis-k8s-v1.5.1:
           #       exemptedNamespaces:
           #       - "namespace-name"
           # Uncomment to exempt namespaces from admission.
           # exemptableNamespaces:
           # - "namespace-name"
           # Uncomment to enable support for referential constraints
           # referentialRulesEnabled: true
           # Uncomment to disable audit, adjust value to set audit interval
           # auditIntervalSeconds: 0
           # Uncomment to log all denies and dryrun failures
           # logDeniesEnabled: true
           # Uncomment to enable mutation
           # mutationEnabled: true
           # Uncomment to adjust the value to set the constraint violation limit
           # constraintViolationLimit: 20
           # ... other fields ...
         

**Best practice** : 

Exempt system namespaces to avoid errors in your environment. You can find the instructions to exempt namespaces and a list of common namespaces created by Google Cloud services on the [Exclude namespaces page](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/policy-controller-exclude-namespaces).

  2. Apply the default configuration to your fleet:
         
         gcloud container fleet policycontroller enable \
           --fleet-default-member-config=fleet-default.yaml
         

  3. To verify that the configuration was applied, run the following command:
         
         gcloud container fleet policycontroller describe
         

  4. To remove the fleet-level default configuration, run the following command:
         
         gcloud container fleet policycontroller enable \
           --no-fleet-default-member-config
         




###  Terraform 

To enable Policy Controller across your fleet with the default template library installed, refer to the following example:
    
    
    resource "google_gke_hub_feature" "policycontroller" {
      name     = "policycontroller"
      location = "global"
      project  = data.google_project.default.project_id
    
      fleet_default_member_config {
        policycontroller {
          policy_controller_hub_config {
            install_spec = "INSTALL_SPEC_ENABLED"
            policy_content {
              bundles {
                bundle = "pss-baseline-v2022"
              }
              template_library {
                installation = "ALL"
              }
            }
          }
        }
      }
    }

You can pass multiple `bundle` blocks to install any of the bundles listed in the [Policy Controller bundles overview](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/concepts/policy-controller-bundles).

To learn more about using Terraform, see [Terraform support for Policy Controller](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/concepts/terraform).

## Verify the Policy Controller installation

After installing Policy Controller, you can verify that it completed successfully.

### Console

Complete the following steps:

  1. In the Google Cloud console, go to the **Policy** page under the **Posture Management** section. 

[Go to Policy](https://console.cloud.google.com/kubernetes/policy_controller)

  2. Under the **Settings** tab, in the cluster table, check the **Policy controller status** column. A successful installation has a status of **Installed** _check_circle_.



### gcloud

Run the following command:
    
    
    gcloud container fleet policycontroller describe --memberships=MEMBERSHIP_NAME
    

A successful installation shows `membershipStates: MEMBERSHIP_NAME: policycontroller: state: ACTIVE`.

### Verify the constraint template library installation

When you install Policy Controller, the constraint template library is installed by default. This installation can take several minutes to complete. You can verify that the template library completed successfully.

### Console

Complete the following steps:

  1. In the Google Cloud console, go to the **Policy** page under the **Posture Management** section. 

[Go to Policy](https://console.cloud.google.com/kubernetes/policy_controller)

  2. Under the **Settings** tab, in the cluster table, select the number listed in the **Bundles installed** column. In the **Policy content status** pane, a successful installation of the template library has a status of **Installed** _check_circle_.



###  gcloud 

Run the following command:
    
    
    kubectl get constrainttemplates
    

You should see output similar to the following example:
    
    
    NAME                                      AGE
    k8sallowedrepos                           84s
    k8scontainerlimits                        84s
    k8spspallowprivilegeescalationcontainer   84s
    ...[OUTPUT TRUNCATED]...
    

When an individual constraint template is installed correctly, its `status.created` field is `true`.

## Policy Controller interactions with Config Sync

If you're using Policy Controller with Config Sync, you should be aware of the following interactions with resources stored in your source of truth, like a Git repository, that are synced by Config Sync:

  * You cannot sync a constraint template that is also part of the template library unless the constraint template library is disabled.

**Caution:** Disabling the template library might remove some of your constraint's dependencies. For more information, see [Create constraints](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/creating-policy-controller-constraints).
  * If you want to sync the `Config` resource stored in the `gatekeeper-system` namespace, then you must only define the `Config` resource in the source of truth. The `gatekeeper-system` `Namespace` must not be defined with it.




## Configure metrics

By default, Policy Controller attempts to export metrics to both Prometheus and Cloud Monitoring. You might need to complete additional configuration steps, such as granting permissions, to allow Policy Controller to export metrics. For more information, see [Use Policy Controller metrics](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/policy-controller-metrics).

## Manage the constraint template library

For information on uninstalling or installing constraint templates, their associated constraints, or the constraint template library, see [Create constraints](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/creating-policy-controller-constraints#constraint-template-library).

## Exempt namespaces from enforcement

You can configure Policy Controller to ignore objects within a namespace. For more information, see [Exclude namespaces from Policy Controller](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/policy-controller-exclude-namespaces).

## Mutate resources

Policy Controller also acts as a mutating webhook. For more information, see [Mutate resources](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/mutation).

## View the Policy Controller version

To discover which version of Gatekeeper Policy Controller is using, view the image tag by running the following command:
    
    
    kubectl get deployments -n gatekeeper-system gatekeeper-controller-manager \
      -o="jsonpath={.spec.template.spec.containers[0].image}"
    

The Git tag (or hash) used to build Gatekeeper and the ConfigManagement Operator version number are included in the image tag as follows:
    
    
    .../gatekeeper:VERSION_NUMBER-GIT_TAG.gBUILD_NUMBER
    

For example, for the following image:
    
    
    gcr.io/config-management-release/gatekeeper:anthos1.3.2-480baac.g0
    

  * `anthos1.3.2` is the version number.
  * `480baac` is the Git tag.
  * `0` is the build number.



## Upgrade Policy Controller

Before you upgrade Policy Controller, check the [release notes](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/release-notes) for details on what's changed between versions.

**Note:** If you use Config Controller to install and manage Policy Controller, you don't need to manually upgrade. Config Controller is a managed service, so Google upgrades it automatically. For details on Config Controller changes, see the [Config Controller release notes](https://docs.cloud.google.com/kubernetes-engine/config-controller/docs/release-notes).

To upgrade Policy Controller, complete the following steps:

### Console

  1. In the Google Cloud console, go to the **Policy** page under the **Posture Management** section. 

[Go to Policy](https://console.cloud.google.com/kubernetes/policy_controller)

  2. Under the **Settings** tab, next to the cluster whose version you want to upgrade, select _edit_ **Edit configuration**.
  3. Expand the **Edit Policy Controller configuration** menu.
  4. From the **Version** drop-down list, select the version that you want to upgrade to.
  5. Click **Save changes**.



###  gcloud 

Run the following command:
    
    
    gcloud container fleet policycontroller update \
      --version=VERSION \
      --memberships=MEMBERSHIP_NAME
    

Replace the following:

  * `VERSION`: the version that you want to upgrade to
  * `MEMBERSHIP_NAME`: the membership name that you chose when you registered your cluster. You can find the membership name by running `gcloud container fleet memberships list`.



## Uninstall Policy Controller

Follow these steps to uninstall Policy Controller from your clusters.

### Console

To disable Policy Controller on your clusters, complete the following tasks:

  1. In the Google Cloud console, go to the **Policy** page under the **Posture Management** section. 

[Go to Policy](https://console.cloud.google.com/kubernetes/policy_controller)

  2. Under the **Settings** tab, in the cluster table, select **Edit** _edit_ in the **Edit configuration** column.
  3. In the cluster pane, expand the **About Policy Controller** menu.
  4. Select **Uninstall Policy Controller**.
  5. Confirm the uninstall by following the instructions in the confirmation dialog and selecting **Confirm**.



When Policy Controller is uninstalled, the status columns show **Not installed** _do_not_disturb_on_.

### gcloud

To uninstall Policy Controller, run the following command:
    
    
    gcloud container fleet policycontroller disable \
      --memberships=MEMBERSHIP_NAME
    

Replace `MEMBERSHIP_NAME` with the membership name of the registered cluster to disable Policy Controller on. You can specify multiple memberships separated by a comma.

## Policy Controller RBAC and permissions

Policy Controller includes highly privileged workloads. The permissions for these workloads are covered in the [Open Policy Agent Gatekeeper](https://open-policy-agent.github.io/gatekeeper/website/docs/operations) operations documentation.

## What's next

  * Learn more about [Policy Controller](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/overview).
  * Lean more about [Policy Controller bundles](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/concepts/policy-controller-bundles).
  * Learn how to [create a constraint](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/creating-policy-controller-constraints).
  * [Troubleshoot Policy Controller](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/troubleshoot-policy-controller).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
