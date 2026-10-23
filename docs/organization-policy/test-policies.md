---
url: https://docs.cloud.google.com/organization-policy/test-policies/
title: Test organization policies \u00a0|\u00a0 Organization Policy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:04:58.195458+00:00
---

# Test organization policies  |  Organization Policy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/organization-policy/test-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Organization Policy ](https://docs.cloud.google.com/organization-policy)
  * [ Guides ](https://docs.cloud.google.com/organization-policy/overview)



Send feedback 

#  Test organization policies Stay organized with collections  Save and categorize content based on your preferences. 

This page shows how to use an organization policy in dry-run mode to monitor how a policy change would impact your workflows before it is enforced.

An organization policy in dry-run mode is created and enforced similarly to other organization policies, and violations of the policy are audit logged, but the violating actions aren't denied.

## Before you begin

To use an organization policy in dry-run mode, you must have billing enabled for your Google Cloud project. For information about checking if billing is enabled for a project, see [Verify the billing status of your projects](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled).

For more information about what organization policies and constraints are and how they work, see [Introduction to the Organization Policy Service](https://docs.cloud.google.com/organization-policy/overview).

### Required roles

To get the permissions that you need to manage organization policies, ask your administrator to grant you the following IAM roles on the organization: 

  * [Organization policy administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/orgpolicy#orgpolicy.policyAdmin) (`roles/orgpolicy.policyAdmin`)
  * To create, delete, or modify aggregated sinks: [Logs Configuration Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.configWriter) (`roles/logging.configWriter`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

You can delegate the administration of organization policies by adding [IAM Conditions](https://docs.cloud.google.com/iam/docs/conditions-overview) to the Organization policy administrator role binding. To control the resources where a principal can manage organization policies, you can make the role binding conditional on a particular [tag](https://docs.cloud.google.com/iam/docs/tags-access-control). For more information, see [Create organization policies](https://docs.cloud.google.com/organization-policy/create-organization-policies#delegate-admin). 

## Limitations

The only organization policy constraints available to be used in dry-run organization policies are:

  * [Custom constraints](https://docs.cloud.google.com/organization-policy/create-custom-constraints)
  * [Managed constraints](https://docs.cloud.google.com/organization-policy/create-organization-policies#managed-constraints)
  * Certain legacy managed constraints: 
    * [Restrict service usage](https://docs.cloud.google.com/organization-policy/restrict-services)
    * [Restrict endpoint usage](https://docs.cloud.google.com/docs/security/compliance/restrict-endpoint-usage)
    * [Restrict TLS versions](https://docs.cloud.google.com/docs/security/compliance/restrict-tls-versions)
    * [Restrict TLS cipher suites](https://docs.cloud.google.com/docs/security/compliance/restrict-tls-cipher-suites)



Attempting to create an organization policy in dry-run mode using any other constraint results in an error.

## Create a dry-run policy with list parameters

You can create an organization policy in dry-run mode for a constraint using the Google Cloud console or Google Cloud CLI. The following examples demonstrate how to create an organization policy in dry-run mode that audits the effect of the `compute.managed.restrictProtocolForwardingCreationForTypes` managed constraint.

###  Console 

  1. In the Google Cloud console, go to the **Organization policies** page.

[Go to Organization policies](https://console.cloud.google.com/iam-admin/orgpolicies)

  2. From the project picker, select the resource for which you want to set the organization policy.

  3. Select the **Restricts the use of protocol forwarding** constraint from the list on the **Organization policies** page.

  4. Select the **Dry run** tab.

  5. Click **Manage dry run policy**.

  6. On the **Edit dry-run policy** page, select **Override parent's policy**.

  7. Click **Add rule**.

  8. Under **Enforcement** , select **On**.

  9. Under **Parameters** , select **Edit** edit.

  10. In the **Edit parameter values** pane, select **User-defined**.

  11. In the **User-defined values** box, enter `EXTERNAL`, and then click **Save**.

  12. Click **Test changes** to simulate the effect of this organization policy. For more information, see [Test organization policy changes with Policy Simulator](https://docs.cloud.google.com/policy-intelligence/docs/test-organization-policies).

  13. To enforce the organization policy in dry-run mode, click **Set dry run policy**. You can also set the live policy by clicking **Set policy**.




You can verify the status of your organization policy in dry-run mode by going to the **Dry run** tab of an organization policy constraint.

If the project has an organization policy in dry-run mode enforced, you can see the audit logs for the project by clicking **View dry-run logs**. For this organization policy, the audit logs display violations as if the **Restricts the use of protocol forwarding** constraint is enforced to allow only `EXTERNAL` protocol forwarding deployments.

###  gcloud 

To create an organization policy in dry-run mode, create a YAML file that defines the constraint with `dryRunSpec`. For example:
    
    
      name: RESOURCE_TYPE/RESOURCE_ID/policies/compute.managed.restrictProtocolForwardingCreationForTypes
      dryRunSpec:
        rules:
        - enforce: true
          parameters:
           allowedSchemes:
            - EXTERNAL

Replace the following:

  * `RESOURCE_TYPE` with `organizations`, `folders`, or `projects`.

  * `RESOURCE_ID` with your organization ID, folder ID, project ID, or project number, depending on the type of resource specified in `RESOURCE_TYPE`.




This organization policy won't enforce the `compute.managed.restrictProtocolForwardingCreationForTypes` constraint, but the audit logs display violations as if it did.

You can set a live organization policy and a dry-run organization policy in the same YAML file, if you define both `spec` and `dryRunSpec`. For example:
    
    
    name: RESOURCE_TYPE/RESOURCE_ID/policies/compute.managed.restrictProtocolForwardingCreationForTypes
    spec:
      rules:
      - values:
          allowedValues:
          - INTERNAL
          - EXTERNAL
    
    dryRunSpec:
      rules:
      - values:
          allowedValues:
          - INTERNAL

To enforce an organization policy in dry-run mode, use the `org-policies set policy` command. To update an existing organization policy in dry-run mode with new constraints, use the `--update-mask` flag. For example:
    
    
    gcloud org-policies set-policy POLICY_PATH \
      --update-mask=UPDATE_MASK

Replace the following:

  * `POLICY_PATH` with the full path to your organization policy YAML file.

  * `UPDATE_MASK` with `spec` to only update the live policy, or `dryRunSpec` to only update the organization policy in dry-run mode. You can also use `*` to update both the `spec` and `dryRunSpec` fields. If this field is not set when updating an existing organization policy, this command will result in an error and the organization policy won't update.




You can verify that the organization policy in dry-run mode is set by using the `org-policies describe` command. The `dryRunSpec` field appears only if it exists in the organization policy.

This organization policy would enforce the `compute.managed.restrictProtocolForwardingCreationForTypes` constraint such that all values are allowed. However, the audit logs display violations as if only `INTERNAL` protocol forwarding deployments were allowed.

## Create a dry-run policy with boolean rules

You can create an organization policy in dry-run mode for a constraint with boolean rules using the Google Cloud console or Google Cloud CLI. The following examples demonstrate how to create an organization policy in dry-run mode that audits the effect of a [custom organization policy](https://docs.cloud.google.com/organization-policy/create-custom-constraints).

###  Console 

  1. In the Google Cloud console, go to the **Organization policies** page.

[Go to Organization policies](https://console.cloud.google.com/iam-admin/orgpolicies)

  2. From the project picker, select the resource for which you want to set the organization policy.

  3. Select the custom organization policy you want to enforce from the list on the **Organization policies** page.

  4. Select the **Dry run** tab.

  5. Click **Manage dry run policy**.

  6. On the **Edit dry run policy** page, select **Override parent's policy**.

  7. Click **Add rule**.

  8. Under **Enforcement** , select **On** , and then click **Done**.

  9. To enforce the organization policy in dry-run mode, click **Set dry run policy**. Once you verify that the organization policy in dry-run mode works as intended, you can set the live policy by clicking **Set policy**.




You can verify the status of your organization policy in dry-run mode by going to the **Dry run** tab of an organization policy constraint.

For projects that have an organization policy in dry-run mode applied to them, you can see the audit logs by clicking **View rejection logs**. For this organization policy, the audit logs display violations as if the custom organization policy is enforced.

###  gcloud 

To create an organization policy in dry-run mode, create a YAML file that defines the constraint with `dryRunSpec`. For example:
    
    
      name: RESOURCE_TYPE/RESOURCE_ID/policies/CONSTRAINT_NAME
      dryRunSpec:
        rules:
        - enforce: true

Replace the following:

  * `RESOURCE_TYPE` with `organizations`, `folders`, or `projects`.

  * `RESOURCE_ID` with your organization ID, folder ID, project ID, or project number, depending on the type of resource specified in `RESOURCE_TYPE`.

  * `CONSTRAINT_NAME` with the name of your custom constraint. For example, `custom.disableGkeAutoUpgrade`.




This organization policy won't enforce the custom constraint, but the audit logs display violations as if it did.

You can set a live organization policy and an organization policy in dry-run mode in the same same YAML file, if you define both `spec` and `dryRunSpec`. For example:
    
    
    name: RESOURCE_TYPE/RESOURCE_ID/policies/CONSTRAINT_NAME
    spec:
      rules:
      - enforce: false
    
    dryRunSpec:
      rules:
      - enforce: true

To enforce an organization policy in dry-run mode, use the `org-policies set policy` command. To update an existing organization policy in dry-run mode with new constraints, use the `--update-mask` flag. For example:
    
    
    gcloud org-policies set-policy POLICY_PATH \
      --update-mask=UPDATE_MASK

Replace the following:

  * `POLICY_PATH` with the full path to your organization policy YAML file.

  * `UPDATE_MASK` with `spec` to only update the live policy, or `dryRunSpec` to only update the organization policy in dry-run mode. You can also use `*` to update both the `spec` and `dryRunSpec` fields. If this field is not set when updating an existing organization policy, this command will result in an error and the organization policy won't update.




You can verify that an organization policy in dry-run mode is set by using the `org-policies describe` command. The `dryRunSpec` field appears only if it exists in the organization policy.

This organization policy doesn't enforce the custom constraint. However, the audit logs display violations of the custom constraint.

## Create an organization policy in dry-run mode from a live policy

You can create an organization policy in dry-run mode from an existing policy. You may want to do this to see what impacts a change to your existing policy would have on your environment.

You can create an organization policy in dry-run mode based on an existing policy using the Google Cloud console or Google Cloud CLI.

###  Console 

  1. In the Google Cloud console, go to the **Organization policies** page.

[Go to Organization policies](https://console.cloud.google.com/iam-admin/orgpolicies)

  2. From the project picker, select a resource that already has the **Restrict Resource Service Usage** constraint configured on it.

  3. Select the **Restrict Resource Service Usage** constraint from the list on the **Organization policies** page.

  4. Select the **Live** tab.

  5. Click **Manage policy**.

  6. Click **Add rule**.

  7. From **Policy values** , select **Custom**.

  8. From **Policy type** , select **Deny**.

  9. In the **Custom values** box, enter `appengine.googleapis.com`.

  10. Click **Done** , and then **Set dry run policy**.




###  gcloud 

To create an organization policy in dry-run mode based on an existing live organization policy, get the current policy on the resource using the `org-policies describe` command. For example:
    
    
    gcloud org-policies describe gcp.restrictServiceUsage \
      --project=PROJECT_ID

Replace `PROJECT_ID` with the project ID or project number of the project where this organization policy is configured.

The output should look similar to the following:
    
    
      name: projects/123456789012/policies/gcp.restrictServiceUsage
      spec:
        etag: CJy93KEGEKCJw/QB
        rules:
        - values:
            allowedValues:
            - compute.googleapis.com
      updateTime: '2023-04-12T21:11:56.512804Z'

Copy the output of this command into a temporary file. Edit this file to remove the `etag` and `updateTime` fields, and change the `spec` field to `dryRunSpec`. Make any changes to the constraint configuration that you want to test in your organization policy in dry-run mode.

The finished YAML file should look similar to the following:
    
    
      name: projects/123456789012/policies/gcp.restrictServiceUsage
      dryRunSpec:
        rules:
        - values:
            allowedValues:
            - compute.googleapis.com
            - appengine.googleapis.com

To enforce the organization policy in dry-run mode, use the `org-policies set policy` with the `--update-mask` flag. For example:
    
    
    gcloud org-policies set-policy POLICY_PATH \
      --update-mask=dryRunSpec

Replace `POLICY_PATH` with the full path to your temporary organization policy YAML file.

## Delete an organization policy in dry-run mode

You can delete an organization policy in dry-run mode using the Google Cloud console or Google Cloud CLI.

###  Console 

  1. In the Google Cloud console, go to the **Organization policies** page.

[Go to Organization policies](https://console.cloud.google.com/iam-admin/orgpolicies)

  2. From the project picker, select the resource for which you want to set the organization policy.

  3. Select the **Restrict Resource Service Usage** constraint from the list on the **Organization policies** page.

  4. Select the **Dry run** tab.

  5. Click **Delete dry run policy**.




###  gcloud 

To delete an organization policy in dry-run mode, create a YAML file that defines the organization policy without a dry-run specification. For example:
    
    
      name: RESOURCE_TYPE/RESOURCE_ID/policies/gcp.restrictServiceUsage
      spec:
        rules:
        - values:
            allowedValues:
            - container.googleapis.com

Replace the following:

  * `RESOURCE_TYPE` with `organizations`, `folders` or `projects`.

  * `RESOURCE_ID` with your organization ID, folder ID, project ID, or project number, depending on the type of resource specified in `RESOURCE_TYPE`.




Then, use the `org-policies set policy` command with the `--update-mask` flag set to `dryRunSpec`. For example:
    
    
    gcloud org-policies set-policy POLICY_PATH \
      --update-mask=dryRunSpec

This updates the existing organization policy to remove the dry-run specification and ignores the live part of the specification.

To delete both live organization policies and organization policies in dry-run mode at the same time, use the `org-policies delete` command. For example:
    
    
    gcloud org-policies delete CONSTRAINT_NAME \
      --RESOURCE_TYPE=RESOURCE_ID

Replace the following:

  * `CONSTRAINT_NAME` with the name of the constraint you want to delete. For example, `gcp.restrictServiceUsage`.

  * `RESOURCE_TYPE` with `organizations`, `folders` or `projects`.

  * `RESOURCE_ID` with your organization ID, folder ID, project ID, or project number, depending on the type of resource specified in `RESOURCE_TYPE`.




## Effective evaluation of organization policies in dry-run mode

Organization policies in dry-run mode are inherited similarly to other organization policies. If an organization policy in dry-run mode is set on an organization resource, it is inherited by all descendant resources, unless it is overridden at a lower level in the hierarchy.

Effective policy evaluation shows the result of the organization policies that are merged on that resource. Therefore, adjustments to the live organization policy are reflected in the effective organization policy in dry-run mode, if the dry-run mode policy is inherited rather than set locally.

![Modifying a project's live organization policy also modifies its effective organization policy in dry-run mode.](https://docs.cloud.google.com/static/organization-policy/images/effective-dry-run-organization-policy.svg)

For example, consider an organization resource, `Organization A`, with a live organization policy set to `enforced: false`, and an organization policy in dry-run mode set to `enforced: true`. A child resource, `Folder B`, also sets the live organization policy to `enforced: false`, and inherits the organization policy in dry-run mode. On `Folder B`, the set live policy means the effective policy evaluation of the organization policy in dry-run mode is also `enforce: false`, overriding the organization policy in dry-run mode set in its parent organization.

A child resource of `Folder B`, `Project X`, sets the live policy to `enforced: true`. Similar to the behavior on `Folder B`, the effective evaluation of the organization policy in dry-run mode for `Project X` is `enforced: true`, because the live policy is set.

Another child resource of `Folder B`, `Project Y`, sets the organization policy in dry-run mode to `enforced: true`. It inherits the organization policy from its parent resource, and so the effective evaluation is `enforced: false` for the live policy, and `enforced: true` for the organization policy in dry-run mode.

Resource | Set live organization policy | Effective live organization policy | Set organization policy in dry-run mode | Effective organization policy in dry-run mode  
---|---|---|---|---  
Organization A | `enforced: false` | `enforced: false` | `enforced: true` | `enforced: true`  
Folder B | `enforced: false` | `enforced: false` | None | `enforced: false`  
Folder C | None | `enforced: false` | None | `enforced: true`  
Project X | `enforced: true` | `enforced: true` | None | `enforced: true`  
Project Y | None | `enforced: false` | `enforced: true` | `enforced: true`  
  
## Analyze the effects of an organization policy in dry-run mode

An organization policy in dry-run mode does not block any operations when enforced. To see the effect your organization policy would have, you can check the [organization policy audit logs](https://docs.cloud.google.com/organization-policy/audit-logging).

Organization policy audit logs for live organization policies and organization policies in dry-run mode are generated based on whether the operation is allowed or denied by the policies enforced on a given resource. The following table describes the situations in which an organization policy audit log is generated:

Live organization policy | Organization policy in dry-run mode | Audit log generated  
---|---|---  
Allow | Allow | No  
Allow | Deny | Audit log in dry-run mode only  
Deny | Allow | Audit log in live and dry-run mode  
Deny | Deny | Audit log in live and dry-run mode  
  
Organization policy in dry-run mode violations appear alongside violations in live mode in the audit logs. For example:
    
    
    {
      "protoPayload": {
        "@type": "type.googleapis.com/google.cloud.audit.AuditLog",
        "status": {
          "code": 7,
          "message": "PERMISSION_DENIED"
        },
        "authenticationInfo": {},
        "requestMetadata": {
          "callerIp": "1.2.3.4",
          "requestAttributes": {},
          "destinationAttributes": {}
        },
        "serviceName": "appengine.googleapis.com",
        "methodName": "google.api.appengine.v1.appengine.apps.services.get",
        "resourceName": "projects/sur-project-test-3",
        "metadata": {
          "constraint": "constraints/gcp.restrictServiceUsage",
          "checkedValue": "appengine.googleapis.com",
          "liveResult": "ALLOWED",
          "@type": "type.googleapis.com/google.cloud.audit.OrgPolicyDryRunAuditMetadata",
          "dryRunResult": "DENIED"
        }
      },
      "insertId": "1f2bvoxcmg1",
      "resource": {
        "type": "audited_resource",
        "labels": {
          "project_id": "sur-project-test-3",
          "service": "appengine.googleapis.com",
          "method": "google.api.appengine.v1.appengine.apps.services.get"
        }
      },
      "timestamp": "2022-06-16T19:42:58.244990928Z",
      "severity": "WARNING",
      "logName": "projects/sur-project-test-3/logs/cloudaudit.googleapis.com%2Fpolicy",
      "receiveTimestamp": "2022-06-16T19:42:59.572025716Z"
    }
    

You can use the Logs Explorer to query only organization policy in dry-run mode violations.

### Console

In the Google Cloud console, you can use the Logs Explorer to retrieve your audit log entries for your Google Cloud project, folder, or organization:

  1. In the Google Cloud console, go to the **Logging > Logs Explorer** page.

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Select an existing Google Cloud project, folder, or organization.

  3. In the **Query builder** pane, do the following:

     * In **Resource type** , select the Google Cloud resource whose audit logs you want to see.

     * In **Log name** , select the **policy** audit log type.

     * In the **Query** pane, enter the following: `protoPayload.metadata.dryRunResult = "DENIED" AND \ protoPayload.metadata.liveResult = "ALLOWED"`

If you're experiencing issues when trying to view logs in the Logs Explorer, see the [troubleshooting](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface#troubleshooting) information.

For more information about querying by using the Logs Explorer, see [Build queries in the Logs Explorer](https://docs.cloud.google.com/logging/docs/view/building-queries).




### gcloud

The Google Cloud CLI provides a command-line interface to the Logging API. Supply a valid resource identifier in each of the log names. For example, if your query includes a project ID, then the project identifier you supply must refer to the currently selected project name.

To read audit log entries for organization policy in dry-run mode violations, run the following command:
    
    
    gcloud logging read protoPayload.metadata.dryRunResult = "DENIED" AND \
          protoPayload.metadata.liveResult = "ALLOWED" \
        --RESOURCE_TYPE=RESOURCE_ID \
    

Replace the following:

  * `RESOURCE_TYPE` with `organization`, `folder` or `project`.

  * `RESOURCE_ID` with your organization ID, folder ID, project ID, or project number, depending on the type of resource specified in `RESOURCE_TYPE`.




Add the[`--freshness` flag](https://docs.cloud.google.com/sdk/gcloud/reference/logging/read#--freshness) to your command to read logs that are more than 1 day old.

For more information about using the gcloud CLI, see [`gcloud logging read`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/read).

## Aggregate audit log entries

If you have many projects under your organization, you can use aggregated sinks to aggregate and route the audit log entries from all projects under your organization to a BigQuery table.

  1. To create an aggregated sink, use the [`logging sinks create`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/sinks/create) command.

Before using the following command, replace the following:

     * `SINK_NAME`: The name of the log sink. You can't change the name of a sink after you create it.

     * `PROJECT_ID`: The ID of the project that contains your BigQuery dataset.

     * `DATASET_ID`: The ID of a write-enabled BigQuery dataset.

     * `ORGANIZATION_ID`: The ID of your organization.

Run the `gcloud logging sinks create` command:
    
    gcloud logging sinks create SINK_NAME \
      bigquery.googleapis.com/projects/PROJECT_ID/datasets/DATASET_ID \
      --include-children \
      --organization=ORGANIZATION_ID \
      --log-filter='logName="projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Fpolicy" AND protoPayload.metadata.@type:OrgPolicyDryRunAuditMetadata'
    

  2. To route log entries, you must grant the service account that's associated with the sink permission to route to its destination.

To find the service account that you need to grant permission to, use the [`gcloud logging sinks describe`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/sinks/describe) command.

Before using the following command, replace `SINK_NAME` with the name of the log sink that you previously created.

Run the [`gcloud logging sinks describe`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/sinks/describe) command:
         
         gcloud logging sinks describe SINK_NAME
         

  3. If the sink details contain a field labeled `writerIdentity`, then proceed to the next step. If the details don't include a `writerIdentity` field, you don't need to configure destination permissions for the sink.

  4. Copy the sink's writer identity into your clipboard. The following illustrates a writer identity:
         
         serviceAccount:service-123456789012@gcp-sa-logging.iam.gserviceaccount.com
         

  5. Use the [`gcloud projects add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding) command to grant the sink's writer identity permission to write log data to the destination.

Before using the following command, replace the following:

     * `PROJECT_ID`: The identifier of the project that stores the destination of the aggregated sink.

     * `PRINCIPAL_ID`: The writer identity of the sink that you previously copied.

Run the `gcloud projects add-iam-policy-binding` command:
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
      --member=PRINCIPAL_ID \
      --role=roles/bigquery.dataEditor
    

For more information about creating aggregated sinks, see [Collate and route organization-level logs to supported destinations](https://docs.cloud.google.com/logging/docs/export/aggregated_sinks).

  6. To view the logs routed to BigQuery, do the following:

     1. In the Google Cloud console, go to the **BigQuery** page: 

[Go to **BigQuery Studio**](https://console.cloud.google.com/bigquery)

You can also find this page by using the search bar.

     2. In the **Explorer** panel, expand your project and select a dataset.

The log entries are visible on the **Details** tab, or you can query the table to return your data.

     3. Create a query to analyze your dry-run organization policy. For example, the following query returns dry-run organization policy audit logs that include denials and were generated in the last seven days.
    
    SELECT protopayload_auditlog.serviceName as serviceName,
        protopayload_auditlog.methodName as methodName,
        JSON_EXTRACT_SCALAR(protopayload_auditlog.metadataJson, '$.constraint') as constraint,
        JSON_EXTRACT_SCALAR(protopayload_auditlog.metadataJson, '$.dryRunResult') as dryRunResult,
        JSON_EXTRACT_SCALAR(protopayload_auditlog.metadataJson, '$.liveResult') as liveResult
    FROM {PROJECT_ID}.{DATASET_ID}.cloudaudit_googleapis_com_policy_*
    WHERE JSON_EXTRACT_SCALAR(protopayload_auditlog.metadataJson, '$.dryRunResult') = "DENIED"
    AND `timestamp` > DATE_SUB(CURRENT_DATE(), INTERVAL 7 DAY)
    LIMIT 1000

Replace the following:

     * `PROJECT_ID`: The ID of the project that contains your BigQuery dataset.

     * `DATASET_ID`: The ID of a write-enabled BigQuery dataset.

For more information, see [View logs routed to BigQuery](https://docs.cloud.google.com/logging/docs/export/bigquery).




## What's next

For more information about how to create and manage organization policy constraints, see [Create organization policies](https://docs.cloud.google.com/organization-policy/create-organization-policies).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
