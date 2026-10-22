---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/billing/manage-billing-accounts/
title: Create and link billing accounts \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:58:51.028579+00:00
---

# Create and link billing accounts  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/billing/manage-billing-accounts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Create and link billing accounts Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the steps to create a Google Distributed Cloud (GDC) air-gapped billing account to track resource usage.

Distributed Cloud environments require a billing account to track usage costs for projects and organizations. All billing accounts within an organization use a single price sheet to charge service usage to the customer. If you don't link a billing account to an organization or project, you'll lose cost data associated with the resource, resulting in cost discrepancies.

This document is for developers in platform administrator or application operator groups that create and administer billing accounts in GDC. For more information, see [Audiences for GDC air-gapped](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences) documentation.

## Before you begin

### Request IAM roles

Contact your Organization IAM Admin to request the following roles on your project:

  * Global Organization Billing Account Admin (`organization-billing-account-admin`): create, manage, and bind the `BillingAccount` resource.

  * Global Organization Billing Account User (`organization-billing-account-user`): read, list, and bind the `BillingAccount` resource.

  * Global Organization Billing Account Manager (`organization-billing-manager`): read, list, create, and update the `BillingAccountBinding` resource.




These roles bind to either the project namespace for project-level billing, or the platform namespace for organization-level billing.

**Note:** The same IAM role manages billing for all projects. To separate billing administration for different projects, you must use one dedicated role for each project. Contact your Organization IAM Admin to [create additional roles](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/custom-roles) for individual project administration requirements.

### Get the kubeconfig file

To run commands against the Org Global cluster, ensure you have the following resources:

  1. [Sign in and generate](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/iam/sign-in#global-resources-kubeconfig) the kubeconfig file for the Org Global cluster if you don't have one.

  2. Use the path to the kubeconfig file of the Org Global cluster to replace `ORG_GLOBAL_CLUSTER_KUBECONFIG` in these instructions.




## Create a new billing account

###  kubectl 

A billing account is uniquely identified by its `name` and `namespace`. To create a billing account, use a custom resource to establish the `name` and `namespace`:

  1. Create a YAML file, and add the `BillingAccount` custom resource and the following contents:
         
         apiVersion: billing.global.gdc.goog/v1
         kind: BillingAccount
         metadata:
           namespace: platform
           name: BIL_ACCOUNT_NAME
         spec:
           displayName: BIL_DISPLAY_NAME
           paymentSystemConfig:
             cloudBillingConfig:
               accountID: "012345-6789AB-CDEF01"
         

Replace the following variables:

     * `BIL_ACCOUNT_NAME`: the name of the billing account, for example, `test-billing-account`.
     * `BIL_DISPLAY_NAME`: the billing account display name, for example, `"Test Billing Account"`.
  2. Verify your payment configuration type. Distributed Cloud billing accounts must have one of the following payment configurations:

     * `cloudBillingConfig`: the default payment configuration. This configuration stores a Cloud Billing account ID.

     * `customConfig`: a custom configuration for partners to store their payment configuration to bill the organization. `customConfig` supports a dictionary of key-value strings, with a mandatory key `payment-config-type`.

The following examples show `BillingAccount` YAML file snippets for different payment configurations:

`cloudBillingConfig` example:
    
    spec:
      paymentSystemConfig:
        cloudBillingConfig:
          accountID: CLOUD_BILLING_ACCOUNT_ID
    

Replace `CLOUD_BILLING_ACCOUNT_ID` with your Google Cloud billing account ID.

`customConfig` example:
    
    spec:
     paymentSystemConfig:
       customConfig:
          "payment-config-type": PAYMENT_CONFIG_TYPE
    

Replace `PAYMENT_CONFIG_TYPE` with your chosen payment configuration type for your custom billing configuration.

If you don't have the information for your organization's `customConfig` configuration, enter the following details:
    
    spec:
     paymentSystemConfig:
       customConfig:
          "payment-config-type": "N/A"
    

The following YAML file shows a complete `BillingAccount` resource with the `cloudBillingConfig` configuration:
    
    apiVersion: billing.global.gdc.goog/v1
    kind: BillingAccount
    metadata:
      namespace: platform
      name: test-billing-account
    spec:
      displayName: "Test Billing Account"
      paymentSystemConfig:
        cloudBillingConfig:
          accountID: "012345-6789AB-CDEF01"
    

  3. Save the YAML file. Run the `kubectl` CLI to apply the resource in the Org Global cluster:
         
         kubectl --kubeconfig ORG_GLOBAL_CLUSTER_KUBECONFIG apply -f billingaccount.yaml
         

Replace `ORG_GLOBAL_CLUSTER_KUBECONFIG` with the Org Global cluster kubeconfig file.




###  CLI 

To create a billing account, use the `gdcloud billing accounts create` command.

For more information, see [gdcloud billing accounts create](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-billing-accounts-create).

## Link an organization or project to a billing account

You must link a billing account to the organization before creating any projects. This ensures that all projects created within the organization inherit a valid billing account by default.

You can also explicitly link a project to a specific billing account if you want it to differ from the organization's billing account.

###  Link an organization 

To link an organization to a `BillingAccount`, do the following:

  1. Add the following content to the YAML file `billingaccountbinding.yaml`:

     * In the `billingAccountRef` section, populate the `name` field with the content from the `name` field in the `BillingAccount` you want to link.
     * In the `metadata` section, populate the `namespace` field with the value from the identical field in the `BillingAccount` resource. In this example, the organization namespace from the `BillingAccount` resource is `platform`:
    
    apiVersion: billing.global.gdc.goog/v1
    kind: BillingAccountBinding
    metadata:
      name: billing
      namespace: platform
    spec:
      billingAccountRef:
        name: BIL_ACCOUNT_NAME
        namespace: platform
    

  2. Run the following `kubectl` command to apply the `billingaccountbinding.yaml` file:
         
         kubectl --kubeconfig ORG_GLOBAL_CLUSTER_KUBECONFIG apply -f billingaccountbinding.yaml
         

  3. Check the status of the `BillingAccountBinding` and verify that there are no errors:
         
         kubectl --kubeconfig ORG_GLOBAL_CLUSTER_KUBECONFIG describe billingaccountbinding billing -n platform
         




###  Link a project 

To link a project to a `BillingAccount`, do the following:

  1. Add the following contents to the file: `billingaccountbinding.yaml`:

     * In the `billingAccountRef` section, populate the `name` field with the content from the `name` field in the `BillingAccount` you want to link.
     * In the `metadata` section, populate the `namespace` field with the content from the identical field in the `BillingAccount` resource.
    
    apiVersion: billing.global.gdc.goog/v1
    kind: BillingAccountBinding
    metadata:
      name: billing
      namespace: PROJECT_NAME
    spec:
      billingAccountRef:
        name: BIL_ACCOUNT_NAME
        namespace: platform
    

Replace the following variables:

     * `PROJECT_NAME` with the name of the project bound to the billing account.
     * `BIL_ACCOUNT_NAME`: the name of the billing account, for example, `test-billing-account`.
  2. Run the following `kubectl` command to apply the `billingaccountbinding.yaml` file:
         
         kubectl --kubeconfig ORG_GLOBAL_CLUSTER_KUBECONFIG apply -f billingaccountbinding.yaml
         

  3. Check the status of the `BillingAccountBinding` and verify that there are no errors:
         
         kubectl --kubeconfig ORG_GLOBAL_CLUSTER_KUBECONFIG describe billingaccountbinding billing -n PROJECT_NAME
         

Replace `PROJECT_NAME` with the name of the project bound to the billing account.


**Note:** After 15 minutes of project creation, a default account binding is created for the project with the billing account of the parent organization.

### List billing account bindings

View a list of all deployed `BillingAccountBinding` resources and their current status across all namespaces in the organization:
    
    
      kubectl --kubeconfig ORG_GLOBAL_CLUSTER_KUBECONFIG get billingaccountbinding -A -o 'custom-columns=NAME:metadata.name,NAMESPACE:metadata.namespace,BillingAccountName:spec.billingAccountRef.name,STATUS:status.conditions[0].status'
    

This command outputs the `NAME`, `NAMESPACE`, `BillingAccountName`, and `STATUS` of each `BillingAccountBinding`. The `STATUS` field indicates whether the binding is active or if there are any errors.

### Billing account hierarchy and behavior

When linking billing accounts to organizations and projects, the following hierarchy and behaviors apply:

  * **Project-level association takes precedence:** If a specific project, such as `project-A`, is explicitly linked to a `BillingAccount`, for example, `billing-account-1`, then all costs for `project-A` bill exclusively to `billing-account-1`. This project-level association remains valid regardless of any organization-level billing account settings.

  * **Organization-level association for unlinked projects:** If your organization links to a `BillingAccount`, for example, `billing-account-0`, all projects _within that organization that don't have their own explicit`BillingAccountBinding`_ automatically associate with and charge to `billing-account-0`. This association typically takes effect after approximately 15 minutes.

  * **Changing organization billing accounts:** If the billing account linked to an organization changes, for example, `billing-account-0` changes to `billing-account-new`, `billing-account-0` projects _don't_ automatically switch to `billing-account-new`. These projects remain bound to `billing-account-0`, and you must manually update the billing account to have the projects use `billing-account-new`.




## Change the linked billing account

In Distributed Cloud, you can't delete a billing account. If you need to change to your billing configuration, you must change the billing account that is linked to the organization or project by modifying the `BillingAccountBinding`. Some scenarios for this use case include the following examples:

  * Accounting rules within your company require you split charges associated with developer and production-level workloads into separate accounts.
  * You create a billing account to charge a customer contract for a one year period. When the contract expires, you must charge for the remaining period that exceeds a year.




###  For a project 

Follow these steps to change the linked billing account for a project:

  1. Create a new `BillingAccount` to link to the project. This account replaces the old account.

  2. Locate the `BillingAccountBinding` resource YAML file in the project namespace to see which billing account is linked:
         
         kubectl --kubeconfig ORG_GLOBAL_CLUSTER_KUBECONFIG describe billingaccountbinding billing -n PROJECT_NAME
         

  3. Modify the `BillingAccountBinding` to link to the new billing account. In the `billingAccountRef` section, populate the `name` field with a new `BillingAccount` name created in step 1 of this section.
         
         kubectl --kubeconfig ORG_GLOBAL_CLUSTER_KUBECONFIG edit billingaccountbinding billing -n PROJECT_NAME
         

  4. After making the changes, ensure that the billing account is correctly updated:
         
         kubectl --kubeconfig ORG_GLOBAL_CLUSTER_KUBECONFIG describe billingaccountbinding billing -n PROJECT_NAME
         




The following example shows a `BillingAccountBinding` YAML file with the account `expired-billing-account` linked to the project `project-one`:
    
    
      apiVersion: billing.global.gdc.goog/v1
      kind: BillingAccountBinding
      metadata:
        # The name of a BillingAccountBinding will typically always be `billing`.
        name: billing
        # This is the project.
        namespace: project-one
      spec:
        billingAccountRef:
          # This is an example of a BillingAccount that has expired.
          name: expired-billing-account
          namespace: platform
    

The following example shows the `BillingAccountBinding` YAML file from the earlier example modified to link a new account called `new-billing-account`:
    
    
      apiVersion: billing.global.gdc.goog/v1
      kind: BillingAccountBinding
      metadata:
        name: billing
        # This is the project.
        namespace: project-one
      spec:
        billingAccountRef:
          # This is the example of the new BillingAccount.
          name: new-billing-account
          namespace: platform
    

###  For an organization 

Follow these steps to change the linked billing account for an organization:

  1. Create a new `BillingAccount` to link to the organization. This account replaces the old account.

  2. Locate the `BillingAccountBinding` resource YAML file in the `platform` namespace to see which billing account is linked:
         
         kubectl --kubeconfig ORG_GLOBAL_CLUSTER_KUBECONFIG describe billingaccountbinding billing -n platform
         

  3. Modify the `BillingAccountBinding` to link to the new billing account. In the `billingAccountRef` section, populate the `name` field with a new `BillingAccount` name created in step 1.
         
         kubectl --kubeconfig ORG_GLOBAL_CLUSTER_KUBECONFIG edit billingaccountbinding billing -n platform
         

  4. After making the changes, ensure that the billing account is correctly updated:
         
         kubectl --kubeconfig ORG_GLOBAL_CLUSTER_KUBECONFIG describe billingaccountbinding billing -n platform
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
