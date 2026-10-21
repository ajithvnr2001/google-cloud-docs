---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/org-policy/
title: Configure organization policies \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:07:05.107304+00:00
---

# Configure organization policies  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/org-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Configure organization policies Stay organized with collections  Save and categorize content based on your preferences. 

Organization policies give you centralized and programmatic control over your organization's resources. As the organization policy administrator, you can configure policies across your entire organization to achieve the following benefits:

  * Centralize control to configure restrictions on how to use your organization's resources.
  * Define and establish guardrails for your development teams to stay within compliance boundaries.
  * Help project owners and their teams move quickly without breaking compliance.



Google Distributed Cloud (GDC) air-gapped doesn't provide a console UI or dedicated CLI to create and manage organization policies. You must use the Kubernetes API or the kubectl CLI.

**Note:** The organization policies system leverages Open Policy Agent - Gatekeeper, an open-source project whose API is marked as beta (`constraints.gatekeeper.sh/v1beta1`).

## Differences from Identity and access management

[Identity and access management (IAM)](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/get-started/authorization-access-control) and organization policies serve complementary access and governance functions:

  * **IAM** focuses on granting permissions. It defines _who_ (members such as users, groups, or service accounts) can perform _what actions_ (roles) on _which resources_ (resource scope). Permissions granted through IAM roles are additive and don't have deny rules.
  * **Organization policies** focus on establishing guardrails. They let administrators configure programmatic restrictions on resources across the entire organization, such as disabling specific services or restricting resource modifications based on subject attributes using attribute-based access control (ABAC). Organization policies take precedence to block operations even if a member holds an IAM role.



## Before you begin

Before configuring organization policies, you must request the necessary permissions and prepare your environment.

### Request IAM roles

Contact your Organization IAM Admin to request the following IAM roles based on the tasks you need to perform:

  * **Restricted Service Policy Admin** (`gdchrestrictedservice-policy-admin`): create, update, and delete restricted service policies.
  * **Restrict By Attributes Policy Admin** (`gdchrestrictbyattributes-policy-admin`): create, update, and delete attribute-based access control policies.



### Prepare your environment

  * [Download](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-download) and [install](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-install) the gdcloud CLI, if you haven't already done so.

  * [Install the kubectl CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/get-started/kubectl).

  * [Generate a kubeconfig file](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-auth#get-kubeconfig) to configure kubectl CLI access.




## Configure a policy

You can configure two types of organization policies in GDC:

  * **Restricted service policy** (`GDCHRestrictedService`): restricts which services you can use or modify in a cluster.
  * **Attribute-based access control policy** (`GDCHRestrictByAttributes`): conditionally restricts access to resources in a cluster based on subject attributes mapped from your identity provider.



### Configure a restricted service policy

The `GDCHRestrictedService` policy type lets you restrict which services you can use or modify in a cluster by blocking specific APIs, such as restricting a service to certain projects or blocking access to a new service while you test it. Create this policy in the same cluster as the service resources. You can create multiple policy instances in a cluster for different services or projects.

`GDCHRestrictedService` supports `CREATE`, `UPDATE`, and `DELETE` operations. To restrict `GET` and `LIST` read operations, use IAM role bindings to [grant and revoke access](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/set-up-role-bindings).

Configure a restricted service policy:

  1. Define the policy manifest:
         
         apiVersion: constraints.gatekeeper.sh/v1beta1
         kind: GDCHRestrictedService
         metadata:
           name: POLICY_NAME
         spec:
           match:
             kinds:
               - apiGroups:
                   - "API_GROUP"
                 kinds:
                   - "KIND"
           parameters:
             disabledOperations:
               - DISABLED_OPERATION
         

Replace the following:

     * `POLICY_NAME`: the name of the organization policy.

     * `API_GROUP`: the API group of the service to restrict, as listed in the following supported services table.

     * `KIND`: the resource kind to restrict, as listed in the following supported services table.

     * `DISABLED_OPERATION`: the groups of operations that this policy blocks. The allowed values are `CREATE`, `UPDATE`, and `DELETE`. The default value for the `disabledOperations` field is `*`. To completely disable a service, list `CREATE`, `UPDATE`, and `DELETE` (and specify all of its kinds).

By default, the policy applies across all namespaces in the cluster. To scope the policy to specific namespaces or projects, see Define the scope of an organization policy within a cluster.

The `GDCHRestrictedService` policy supports the following subset of services on GDC:

**Service** | **API Group** | **kinds**  
---|---|---  
Marketplace | `marketplace.gdc.goog` | `MarketplaceService`  
Vertex AI Workbench | `aiplatform.gdc.goog` | `Notebook`  
Database Service - Postgres | `postgresql.dbadmin.gdc.goog` | 
     * `DBCluster`
     * `BackupPlan`
     * `Import`
     * `Restore`  
Transfer Appliance | `system.gpc.gke.io` | `TransferApplianceRequest`  
Backup | `backup.gdc.goog` | `BackupRepositoryManager`  
Dataproc Container for Spark (Marketplace service) | `sparkoperator.k8s.io` | `SparkApplication`  
  
If a service lists multiple kinds in the table (such as Database Service), you can specify only the individual kinds you want to restrict. For example, you can block `Restore` operations while continuing to allow `DBCluster` operations.

**Warning:** Always specify kinds for a given API group, and ensure they are singular and use the correct case. Do not use kinds that are not listed in this table; doing so might cause unintended consequences.

The following example restricts updates to marketplace services:
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: GDCHRestrictedService
    metadata:
      name: no-update-to-marketplace-service
    spec:
      match:
        kinds:
        - apiGroups:
          - "marketplace.gdc.goog"
          kinds:
          - MarketplaceService
      parameters:
        disabledOperations:
          - "UPDATE"
    

  2. Apply the policy using the kubectl CLI:
         
         kubectl --kubeconfig CLUSTER_KUBECONFIG apply -f POLICY_NAME.yaml
         

Replace the following:

     * `CLUSTER_KUBECONFIG`: the kubeconfig file of the cluster where you want to apply the policy
     * `POLICY_NAME`: the name of the organization policy file



### Configure an attribute-based access control policy

The `GDCHRestrictByAttributes` policy type lets you create ABAC policies to conditionally restrict access to resources based on subject attributes. For example, you can use this policy type to restrict write or modify operations on storage buckets so that only users or service accounts with specific identity attributes (such as `citizenship=USA` or `citizenship=UK`) can perform them.

Create this policy in the same cluster as the resources. You can create multiple policy instances in a cluster for different resources or projects.

Configure an attribute-based access control policy:

  1. Create a patch JSON file to map custom identity attributes for your `IdentityProviderConfig` resource:
         
         cat <<EOF > attributeMapping-patch.json
         {
           "CUSTOM_ATTRIBUTE": "assertion[\"CUSTOM_ATTRIBUTE\"]"
         }
         EOF
         

Replace `CUSTOM_ATTRIBUTE` with the name of the identity attribute to map, such as `citizenship`.

  2. Patch the `IdentityProviderConfig` resource in the `platform` namespace:
         
         kubectl --kubeconfig CLUSTER_KUBECONFIG patch \
             IdentityProviderConfig IDENTITY_PROVIDER_CONFIG_NAME \
             -n platform --type=json \
             -p '[{"op":"add","path":"/spec/oidc/attributeMapping", "value": '"$(cat attributeMapping-patch.json)"'}]'
         

Replace the following:

     * `CLUSTER_KUBECONFIG`: the kubeconfig file of the cluster where the identity provider resides
     * `IDENTITY_PROVIDER_CONFIG_NAME`: the name of the `IdentityProviderConfig` resource
  3. Define the policy manifest:
         
         apiVersion: constraints.global.gatekeeper.sh/v1beta1
         kind: GDCHRestrictByAttributes
         metadata:
           name: POLICY_NAME
         spec:
           match:
             kinds:
               - apiGroups:
                   - "API_GROUP"
                 kinds:
                   - "KIND"
           parameters:
             attributes:
               - CUSTOM_ATTRIBUTE
             attributeValues:
               - ALLOWED_ATTRIBUTE_VALUE
         

Replace the following:

     * `POLICY_NAME`: the name of the organization policy.

     * `API_GROUP`: the API group of the resources to restrict, such as `object.gdc.goog`.

     * `KIND`: the resource kind to restrict, such as `Bucket`.

     * `CUSTOM_ATTRIBUTE`: the custom subject attribute mapped from the identity provider, such as `citizenship`.

     * `ALLOWED_ATTRIBUTE_VALUE`: the allowed value for the custom attribute, such as `USA`. Requests from subjects whose attribute doesn't match one of the allowed values are denied.

By default, the policy applies across all namespaces in the cluster. To scope the policy to specific namespaces or projects, see Define the scope of an organization policy within a cluster.

The following example restricts modification of `Bucket` resources in the `project-foo` namespace to subjects with the attribute `citizenship=USA` or `citizenship=UK`:
    
    apiVersion: constraints.global.gatekeeper.sh/v1beta1
    kind: GDCHRestrictByAttributes
    metadata:
      name: restrict-by-citizenship
    spec:
      match:
        scope: Namespaced
        kinds:
          - apiGroups:
              - "object.gdc.goog"
            kinds:
              - Bucket
        namespaces:
          - project-foo
      parameters:
        attributes:
          - "citizenship"
        attributeValues:
          - "USA"
          - "UK"
    

  4. Apply the policy using the kubectl CLI:
         
         kubectl --kubeconfig CLUSTER_KUBECONFIG apply -f POLICY_NAME.yaml
         

Replace the following:

     * `CLUSTER_KUBECONFIG`: the kubeconfig file of the cluster where you want to apply the policy
     * `POLICY_NAME`: the name of the organization policy file



## Define the scope of an organization policy within a cluster

When defining an organization policy, decide if it should impact all namespaces, only specific namespaces, or all namespaces except a given list. To achieve this, use a combination of the `.spec.match.excludedNamespaces`, `.spec.match.namespaceSelector`, `.spec.match.namespaces`, and `.spec.match.scope` parameters of the policy definition.

Read the [organization policy match section](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/policy-match-section) page to learn more about these parameters. For example, to allow the creation of databases only in namespaces that have the label `owner: dba-team`, create the following policy:
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: GDCHRestrictedService
    metadata:
      name: db-restricted-to-dbas
    spec:
      match:
        scope: Namespaced
        namespaceSelector:
          matchExpressions:
          # We are restricting the use of the service in namespaces that
          # don't have the owner: dba-team label
          - key: owner
            operator: NotIn
            values:
            - dba-team
        kinds:
        - apiGroups:
          - "postgresql.dbadmin.gdc.goog"
          kinds:
          - DBCluster
          - BackupPlan
          - Import
          - Restore
      parameters:
        disabledOperations:
          - "UPDATE"
          - "CREATE"
          - "DELETE"
    

## Roll back an existing policy

To stop enforcing an existing policy, delete it using the kubectl CLI. Use a kubeconfig file that gives you access to the cluster where the policy is defined and the IAM role corresponding to the policy type (such as `gdchrestrictedservice-policy-admin` or `gdchrestrictbyattributes-policy-admin`).

Delete an organization policy:
    
    
    kubectl --kubeconfig CLUSTER_KUBECONFIG delete \
        POLICY_TYPE/POLICY_NAME
    

Replace the following:

  * `CLUSTER_KUBECONFIG`: the kubeconfig file of the cluster where the organization policy resides

  * `POLICY_TYPE`: the type of the organization policy to delete, such as `GDCHRestrictedService` or `GDCHRestrictByAttributes`

  * `POLICY_NAME`: the name of the organization policy to delete




## Test a policy in an audit mode

You can test a policy without enforcing it. Test a policy to make sure that a policy doesn't break existing systems before rolling it out, or to get an estimation of how widespread a behavior is. To add a test, add an `enforcementAction` to your policy definition. There are three possible values for this parameter:

  * `deny`: the policy is enforced. This is the default setting.
  * `dryrun`: the action is allowed, but you can see that there is a policy violation in both the audit logs and the policy status. Examine the violation with `kubectl --kubeconfig CLUSTER_KUBECONFIG get POLICY_TYPE/POLICY_NAME`.
  * `warn`: equivalent to `dryrun` except the test also shows a warning in response to the request that triggered a policy violation.



For example, to test a policy that disables the Marketplace, create the following policy:
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: GDCHRestrictedService
    metadata:
      name: disable-marketplace-service-project-alice
    spec:
      enforcementAction: warn
      match:
        kinds:
          - apiGroups: ["marketplace.gdc.goog"]
            kinds: ["MarketplaceService"]
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
