---
url: https://docs.cloud.google.com/vpc-service-controls/docs/violation-analyzer/
title: Diagnose an access denial in violation analyzer \u00a0|\u00a0 VPC Service Controls \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:39:17.115139+00:00
---

# Diagnose an access denial in violation analyzer  |  VPC Service Controls  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc-service-controls/docs/violation-analyzer/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ VPC Service Controls ](https://docs.cloud.google.com/vpc-service-controls/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc-service-controls/docs/overview)



Send feedback 

#  Diagnose an access denial in violation analyzer Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to use the VPC Service Controls violation analyzer to understand and diagnose access denials from service perimeters in your organization.

VPC Service Controls generates a unique ID and a troubleshooting token when denying an access request. The violation analyzer lets you diagnose the access denial using this unique ID and troubleshooting token. VPC Service Controls logs all the information about an access denial event in Cloud Audit Logs, including the unique ID and troubleshooting token.

You can generate a comprehensive evaluation report for an access denial in the violation analyzer using the unique ID or troubleshooting token. This report evaluates the access denial event at a specific point in time against all perimeter configurations that protect the resources from the evaluated access request.

You can also use the violation analyzer to [view and apply automated remediation suggestions](https://docs.cloud.google.com/vpc-service-controls/docs/remediation-suggestions) that resolve access denials and enforce the principle of least privilege.

You can also diagnose an access denial and [view its classic evaluation report in the violation analyzer](https://docs.cloud.google.com/vpc-service-controls/docs/troubleshooter), which provides a short summary of why the access denial occurred.

You can also use the violation analyzer to diagnose access denials from the dry run configuration of a service perimeter.

## Before you begin

  * Verify that you have the permissions required to use the violation analyzer and apply remediation suggestions.
  * To understand the device policies in an access level and retrieve the device context details, make sure that you have the required permissions in Google Workspace to view the device details. Without the required permissions, troubleshooting access denials involving [device attributes](https://docs.cloud.google.com/access-context-manager/docs/overview#device-type) in access levels might yield inconsistent troubleshooting results.

To get these permissions, make sure that you have any one of the following Google Workspace roles:

    * [Super Admin, Services Admin, or Mobile Admin role](https://support.google.com/a/answer/2405986).

    * A [custom administrator role](https://support.google.com/a/answer/2406043) that contains the [Manage Devices and Settings](https://support.google.com/a/answer/1219251#mobiledevice&zippy=%2Cmobile-device-management) privilege. You can find this privilege under **Services > Mobile Device Management**.

For more information about assigning roles, see [Assign specific admin roles](https://support.google.com/a/answer/9807615).

You can use the violation analyzer without these permissions in Google Workspace. However, the troubleshooting result might differ as specified earlier.




### Required roles

To get the permissions that you need to use the violation analyzer and apply remediation suggestions, ask your administrator to grant you the following IAM roles: 

  * Diagnose an access denial event using the violation analyzer: [Access Context Manager Reader ](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.policyReader) (`roles/accesscontextmanager.policyReader`) on your access policy 
  * Fetch troubleshooting tokens from Cloud Audit Logs: [Logs Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewer) (`roles/logging.viewer`) on the projects that have VPC Service Controls audit logs 
  * Apply suggested remediation fixes: [Access Context Manager Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.editor) (`roles/accesscontextmanager.editor`) on your access policy 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to use the violation analyzer and apply remediation suggestions. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to use the violation analyzer and apply remediation suggestions:

  * Diagnose an access denial event using the violation analyzer: 
    * `accesscontextmanager.accessLevels.list` on your access policy
    * `accesscontextmanager.policies.get` on your access policy
    * `accesscontextmanager.servicePerimeters.list` on your access policy
  * Fetch troubleshooting tokens from Cloud Audit Logs: `logging.logEntries.list` on the projects that have VPC Service Controls audit logs 
  * Apply suggested remediation fixes: 
    * `accesscontextmanager.accessLevels.create` on your access policy
    * `accesscontextmanager.accessLevels.get` on your access policy
    * `accesscontextmanager.accessLevels.list` on your access policy
    * `accesscontextmanager.policies.get` on your access policy
    * `accesscontextmanager.servicePerimeters.get` on your access policy
    * `accesscontextmanager.servicePerimeters.update` on your access policy



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Troubleshoot an access denial event

When VPC Service Controls denies an access request, it generates a unique ID and logs an encrypted troubleshooting token in Cloud Audit Logs. The error returned by the Google Cloud CLI for a VPC Service Controls denial includes the event's [unique ID](https://docs.cloud.google.com/vpc-service-controls/docs/retrieve-troubleshoot-errors#unique-id).

Before you begin, [obtain the unique ID](https://docs.cloud.google.com/vpc-service-controls/docs/retrieve-troubleshoot-errors#unique-id) for the denial that you want to troubleshoot.

Note: If you set up the VPC Service Controls violation dashboard in your organization, the violation dashboard displays access denials by your service perimeters, including the troubleshooting tokens. To diagnose an access denial event, click the troubleshooting token for the event listed in the **Violations** table of the violation dashboard. VPC Service Controls opens the violation analyzer and displays the troubleshooting result of the access denial.

For more information, see [Set up and view the violation dashboard](https://docs.cloud.google.com/vpc-service-controls/docs/violation-dashboard).

Note: You can search for the troubleshooting token in Cloud Audit Logs [using the unique ID](https://docs.cloud.google.com/vpc-service-controls/docs/retrieve-troubleshoot-errors#unique-id). The `vpcServiceControlsTroubleshootToken` field in the log entry contains the troubleshooting token.

### Access the violation analyzer

The violation analyzer is available only in the Google Cloud console. You can access the violation analyzer using either the [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-summary) or the VPC Service Controls page.

#### Use the Logs Explorer

By using the [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-summary), you can move directly from a log entry for a VPC Service Controls denial to the violation analyzer.

To access the violation analyzer from a log entry, do the following:

  1. In the Google Cloud console, go to the **Logs Explorer** page. 

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. On the **Logs Explorer** page, use the denial's [unique ID to access the log entry](https://docs.cloud.google.com/vpc-service-controls/docs/retrieve-troubleshoot-errors#unique-id).
  3. In the **Query Results** box, in the row for the denial that you want to troubleshoot, click **VPC Service Controls** , and then click **Troubleshoot denial**.



#### Use the VPC Service Controls page

To access the violation analyzer from the **VPC Service Controls** page, do the following:

  1. In the Google Cloud console navigation menu, click **Security** , and then click **VPC Service Controls**.

[Go to VPC Service Controls](https://console.cloud.google.com/security/service-perimeter)

  2. If you're prompted, select your organization. You can access the **VPC Service Controls** page only at the organization level.

  3. On the **VPC Service Controls** page, click **Violation analyzer**.

  4. On the **Violation analyzer** page, in the **Troubleshooting token (or unique ID)** field, enter the unique ID of the denial that you want to troubleshoot.

  5. Click **Continue**.




The violation analyzer evaluates the audit logs of the access denial and displays detailed diagnostics on the troubleshooting result page.

If you want to [diagnose the access denial and view its classic evaluation report](https://docs.cloud.google.com/vpc-service-controls/docs/troubleshooter), click **Switch to classic view** in the troubleshooting result page.

## Understand the troubleshooting result

Before you read the troubleshooting result of an access denial event, make sure that you refer to the following considerations.

### Sensitive information redaction

To protect sensitive data, the violation analyzer redacts the following information in the troubleshooting result:

  * **IP address:** When an access request originates from a Google Cloud service inside an internal production network, the violation analyzer redacts the IP address of the access request as `private`.

  * **Network information:** The violation analyzer redacts the network information of the access request as `redacted_network`, except in the following scenarios:

    * When you are from the same organization as the network.

    * When you have the necessary permission to view the network information.

  * **Principal:** The violation analyzer redacts the email address of a principal with `...` (for example, `cl...o@gm...m`), except in the following scenarios:

    * When you are from the same organization as the access-denied principal.

    * When the access-denied principal is a service agent or service account.

Some Google Cloud services don't collect identity information. For example, the legacy App Engine API doesn't collect the [caller identities](https://docs.cloud.google.com/logging/docs/audit#user-id). When the violation analyzer observes that the principal information is missing in the logs, the troubleshooting result displays the principal as `no information available`.




### Evaluation status

The violation analyzer evaluates an access denial event against all the perimeter components and assigns an evaluation status for each component.

The violation analyzer might display the following evaluation statuses in the troubleshooting result:

Status | Description  
---|---  
check_circle Granted | This status indicates that the perimeter component allows the evaluated access request.  
error Denied | This status indicates that the perimeter component denies the evaluated access request.  
info Not applicable | This status indicates that the perimeter component doesn't restrict the resource or service from the evaluated access request or doesn't enforce the VPC accessible services feature.  
warning Unsupported or Unknown | This status indicates that the perimeter component uses features or attributes that the violation analyzer doesn't support. For more information about the unsupported features in the violation analyzer, see [Limitations](https://docs.cloud.google.com/vpc-service-controls/docs/violation-analyzer#limitations).  
  
## View the troubleshooting result

The troubleshooting result page provides a detailed assessment of an access denial event. This result presents the assessment of the event at the specific point in time when you requested the violation analyzer to diagnose the event. The troubleshooting result page categorizes the assessment information under different sections.

The troubleshooting result of an access denial event can have the following sections:

  * Violation details

  * Violation evaluation

  * Restricted resources

  * Restricted services

  * Ingress

  * Egress

  * VPC accessible services




To view the assessment of a specific perimeter component, select the perimeter component from the list or click the arrow_right expander arrow next to the perimeter component. For example, to view the troubleshooting assessment for an egress rule, select the egress rule or click the arrow_right expander arrow next to the egress rule.

**Note:** When you click an access level in the troubleshooting result, the violation analyzer opens a pane that displays the assessment of the access denial event against the access level.

After you review the troubleshooting result of an access denial event, you can modify the necessary perimeter components and configuration to resolve the denial. To edit the selected perimeter, click edit **Edit enforced config** or **Edit dry run config** in the troubleshooting result page. For more information, see [Update a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/manage-service-perimeters#update).

### Remediation suggestions

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

For supported access denial events, the violation analyzer provides automated remediation suggestions to resolve the denial.

To view the recommendation, select the denied perimeter in the **Protected resources accessed** section and click **Review recommendation**. The violation analyzer displays the proposed ingress rules, egress rules, or access level options. Access level options might include selecting an existing access level or creating a new one. If you have the Access Context Manager Editor role, click **Apply remediation** to automatically update your service perimeter and access policy. For more information, see [Resolve access denials with remediation suggestions](https://docs.cloud.google.com/vpc-service-controls/docs/remediation-suggestions).

### Violation details

The **Violation details** section lists the following information about the access denial event:

  * The time of the access denial event.

  * The identity of the principal that requested access.

  * The service for which the principal requested access.

  * The service method for which the principal requested access.

  * The IP address of the principal that requested access. This IP address is the same as the `caller_ip` value of the access denial event's log entry in Cloud Audit Logs. For more information, see [IP address of the caller in audit logs](https://docs.cloud.google.com/logging/docs/audit#caller-ip).

  * The troubleshooting token of the access denial event.

  * The unique ID of the access denial event.

  * The details of the involved device and region. To view this information, click **View device info**.

  * The log entry details associated with the access denial event. To view this information, click **View log entry**.

If the log entry exceeds the Cloud Audit Logs [retention period](https://docs.cloud.google.com/logging/docs/audit#audit_log_retention), the violation analyzer can't display these details.




### Violation evaluation

The **Violation evaluation** section shows the overall assessment of the access denial event. The assessment includes both the enforced and dry run mode troubleshooting results of the perimeter.

The troubleshooting results for an access denial event can vary over time if there are changes in service perimeters or access policies after VPC Service Controls logs the access denial event. This behavior is due to the fact that the violation analyzer fetches the latest information from the relevant service perimeters and access policies for assessment.

#### Outcome

The **Outcome** section shows the assessment of the access denial event against all the perimeters involved. The value can be `Granted`, `Denied`, or `Not applicable`.

#### Protected resources accessed

The **Protected resources accessed** section lists the perimeters with the corresponding evaluation status against the access denial event. In this section, you can view the following information:

  * A list of all resources involved in this access denial event:

    * The **Resources accessed** column displays all involved resources protected by the perimeter.

    * When you don't have sufficient permissions to view the restricted resources, the **Protected resources accessed** section doesn't list the perimeter name and the **Resources accessed** column displays the involved project with a warning icon.

    * The **Other resources accessed** section lists all the other involved resources, grouped under one of the following states:

State | Description  
---|---  
Unrestricted | This state indicates that the resource is not protected by any service perimeter.  
Info denied | This state indicates that you don't have sufficient permissions to view the service perimeters protecting the resource.  
Error | This state indicates that an internal error has occurred while trying to view the service perimeters protecting the resource.  
  * When you select a perimeter from the list, you can view the troubleshooting result for the access denial event against the selected perimeter.

  * You can view the troubleshooting results for different enforcement modes of the perimeter as well. By default, the troubleshooting result page displays the **Enforced** mode troubleshooting result. If you want to view the dry run mode troubleshooting result, click **Dry run**. For more information about the perimeter enforcement modes, see [Service perimeter details and configuration](https://docs.cloud.google.com/vpc-service-controls/docs/service-perimeters).

Because the enforced mode and dry run mode configurations of a perimeter can be different, the violation analyzer can generate different troubleshooting results for the enforced mode and dry run mode configurations.




### Restricted resources

In this section, you can view the following information:

  * The **Involved in evaluation** row shows only the resources involved in this violation and protected by the selected perimeter.

  * The **Restricted by perimeter** row shows all the resources that are protected by the selected perimeter.




### Restricted services

In this section, you can view the following information:

  * The **Involved in evaluation** row shows only the services involved in this violation and protected by the selected perimeter.

Even if you have already removed the violating service from the perimeter, the **Involved in evaluation** row still lists the service and displays a warning message.

  * The **Restricted by perimeter** row shows all the services that are protected by the selected perimeter.




### Ingress

The **Ingress** section shows the assessment of the access denial event against all the ingress rules and access levels involved. For each access request, the violation analyzer evaluates the service agents or networks and the corresponding target resources against the ingress rules and access levels.

The violation analyzer groups and displays the ingress rule assessment information based on the ingress rules and access levels. Clicking each rule or access level in this section expands it to display the target resource names assessed against that rule or access level.

If you want to resolve a denial by modifying an existing ingress rule, click edit **Edit** next to the rule in the troubleshooting result page. For information about the ingress rule attributes, see [Ingress rules reference](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules#ingress-rules-reference).

### Egress

The **Egress** section shows the assessment of the access denial event against all the egress rules involved. The violation analyzer evaluates the source and target resource pairs of the access request against the egress rules.

The violation analyzer groups and displays the egress rule assessment information based on the egress rules. Clicking each rule in this section expands it to display the detailed assessment of the resources against that rule.

If you want to resolve a denial by modifying an existing egress rule, click edit **Edit** next to the rule in the troubleshooting result page. For information about the egress rule attributes, see [Egress rules reference](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules#egress-rules-reference).

### VPC accessible services

The **VPC accessible services** section shows the status of the services that are accessible from network endpoints inside the perimeter. These statuses correspond to the time when the access denial event occurred. If the evaluation status for a service is `Denied`, you can't access the service from network endpoints inside the perimeter.

In this section, you can view the following information:

  * The **Involved in evaluation** row shows only the services involved in this violation and not accessible from network endpoints inside the selected perimeter. This row also displays services that are not on the perimeter's list of VPC accessible services, either because these services were removed or were never included.

  * The **Accessible within perimeter** row shows all the services that are accessible from network endpoints inside the selected perimeter.




For more information, see [VPC accessible services](https://docs.cloud.google.com/vpc-service-controls/docs/vpc-accessible-services).

## Compare the enforced and dry run mode results

You can compare the troubleshooting results of an access denial event between the enforced and dry run modes of the selected perimeter. To compare the troubleshooting results, click compare_arrows **Compare to dry run** on the enforced mode troubleshooting result page of a perimeter.

If the dry run mode inherits the configuration from the enforced mode of the perimeter, the dry run mode also inherits the enforced mode troubleshooting result.

**Note:** The enforced mode and dry run mode configurations of a perimeter might not restrict the same resources and services.

## Limitations

  * The violation analyzer does not support the [VPC Service Controls service patterns](https://docs.cloud.google.com/vpc-service-controls/docs/vpc-accessible-services#service-patterns).

  * The violation analyzer doesn't support evaluating folders or organizations in [ingress or egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules).

  * You must use the violation analyzer only at the organization scope, and the violation analyzer is not accessible at the project scope.

  * If VPC Service Controls [audit logs](https://docs.cloud.google.com/vpc-service-controls/docs/audit-logging#available-logs) are inaccessible, excluded, or stored outside the default location, the violation analyzer fails to evaluate an access denial using the unique ID. In these cases, you can use the troubleshooting token instead.

  * The violation analyzer fetches the latest information from the relevant service perimeters and access policies for assessment. So the troubleshooting results for an access denial event can vary over time if there are changes in service perimeters or access policies after VPC Service Controls logs the access denial event.

    * Also, if you diagnose an access denial event multiple times, the troubleshooting results might vary for each diagnosis if the access policy has changed.
  * The troubleshooting result of an access denial event might differ in the following scenarios:

    * When you have defined [device attribute](https://docs.cloud.google.com/access-context-manager/docs/overview#device-type) based conditions in an access level and used the access level in your service perimeter, but you don't have the [permissions required to view the device details](https://docs.cloud.google.com/chrome-enterprise-premium/docs/troubleshooter#before_you_begin).

    * When an ingress or egress rule of the service perimeter uses a `principalSet` identifier to grant access to third-party identities from workforce or workload identity pools. For more information about all identity types and their formats, see [Supported identities for ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/supported-identities#supported-identities).

    * When you have configured a [credential strength policy](https://docs.cloud.google.com/access-context-manager/docs/create-credential-strength-policy) in the access level.

    * When an [ingress or egress rule](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules) of the service perimeter uses a service permission as an API operation condition.




## What's next

  * [Resolve access denials with remediation suggestions](https://docs.cloud.google.com/vpc-service-controls/docs/remediation-suggestions)
  * [Diagnose an access denial and view the classic report](https://docs.cloud.google.com/vpc-service-controls/docs/troubleshooter)
  * [Debugging requests blocked by VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/troubleshooting#debugging)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
