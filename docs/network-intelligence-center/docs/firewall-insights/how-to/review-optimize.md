---
url: https://docs.cloud.google.com/network-intelligence-center/docs/firewall-insights/how-to/review-optimize/
title: Review and optimize firewall rules \u00a0|\u00a0 Network Intelligence Center - Firewall Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:56:13.117837+00:00
---

# Review and optimize firewall rules  |  Network Intelligence Center - Firewall Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/firewall-insights/how-to/review-optimize/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Firewall Insights ](https://docs.cloud.google.com/network-intelligence-center/docs/firewall-insights)
  * [ Guides ](https://docs.cloud.google.com/network-intelligence-center/docs/firewall-insights/how-to/using-firewall-insights)



Send feedback 

#  Review and optimize firewall rules Stay organized with collections  Save and categorize content based on your preferences. 

This page describes some common Firewall Insights tasks for reviewing and optimizing your Virtual Private Cloud (VPC) firewall usage. Perform these tasks to optimize your firewall rule configurations and tighten security boundaries.

For example, you're a network administrator or a network security engineer that supports several large Shared VPC networks with many projects and applications. You want to review and optimize a large volume of firewall rules accumulated over time to ensure that they are consistent with the expected state of your network. You can use the following tasks to review and optimize your firewall rules.

## Required roles and permissions

To get the permissions that you need to use Firewall Insights, ask your administrator to grant you the following IAM roles on your project: 

  * [Firewall Recommender Admin role ](https://docs.cloud.google.com/iam/docs/roles-permissions/recommender#recommender.firewallAdmin) (`roles/recommender.firewallAdmin`)
  * [Firewall Recommender Viewer role ](https://docs.cloud.google.com/iam/docs/roles-permissions/recommender#recommender.firewallViewer) (`roles/recommender.firewallViewer`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to use Firewall Insights. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to use Firewall Insights:

  * `recommender.computeFirewallInsights.list`
  * `recommender.computeFirewallInsights.update`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## View rules applied to a VM in the last 30 days

To review rules that help you avoid misconfigurations and unnecessary shadowed rules, do the following:

###  Console 

  1. In the Google Cloud console, go to the **Compute Engine VM instances** page.

[Go to Compute Engine VM instances](https://console.cloud.google.com/compute/instances)

  2. In the **filter_list Filter** field, filter the instances by entering one of the following key-value pairs to find relevant VMs.

**Note:** You can also click values that appear after entering a key such as `Network tags`. For more information, see [Network tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags) and [IP addresses](https://docs.cloud.google.com/compute/docs/ip-addresses).
         
         Network tags:TAG_NAME

Replace `TAG_NAME` with a tag assigned to a VPC network.
         
         Internal IP:INTERNAL_IP_ADDRESS

Replace `INTERNAL_IP_ADDRESS` with an internal IP address for a VM interface.
         
         External IP:EXTERNAL_IP_ADDRESS

Replace `EXTERNAL_IP_ADDRESS` with an external IP address for a VM interface.

  3. In the search results for a VM interface, select a VM and click the more_vert**more actions** menu.

  4. On the menu, select **View network details**.

  5. On the **Network interface details** page, complete the following steps:

     1. In the **Firewall and routes details** section, click **Firewalls** and then **filter_list Filter**.
     2. Enter `last hit after:YYYY-MM-DD` to filter the firewall rules. This filter expression finds firewall rules with recent hits.

     3. For a firewall rule, click the number in the **Hit count** column to open the firewall log and review traffic details, as in the following example query. To enter a query, click **Submit filter**.
            
            jsonPayload.rule_details.reference:("network:network1/firewall:allow-tcp") AND
            jsonPayload.instance.project_id:("p6ntest-firewall-intelligence") AND
            jsonPayload.instance.zone:("us-central1-c") AND
            jsonPayload.instance.vm_name:("instance2")
            

     4. Add one or more additional Cloud Logging filters to further filter the firewall log detail. For example, the following example query adds an additional filter that filters by source IP address (`src_ip`). To enter a query, click **Submit filter**.
            
            jsonPayload.rule_details.reference:("network:network1/firewall:allow-tcp") AND
            jsonPayload.instance.project_id:("p6ntest-firewall-intelligence") AND
            jsonPayload.instance.zone:("us-central1-c") AND
            jsonPayload.instance.vm_name:("instance2") AND
            jsonPayload.connection.src_ip:("10.0.1.2")
            




## Detect sudden increases in the hit count for `deny` firewall rules

You can configure Cloud Monitoring to detect changes in the hit count of your VPC `deny` firewall rules. For example, you can choose to be alerted when the hit count of a particular rule increases by a certain percentage. Setting this alert helps you detect possible attacks on your Google Cloud resources.

To set an alert, do the following:

###  Console 

  1. In the Google Cloud console, go to the **Monitoring** page.

[Go to Monitoring](https://console.cloud.google.com/monitoring)

  2. In the navigation pane, click **notifications Alerting** and then **add Create policy**.

  3. On the **Create alerting policy** page, click **add Add alert condition**. A new condition is added.

  4. Expand the **New condition** section and select **Configure trigger**. The **Configure alert trigger** page opens.

  5. Configure the alert conditions. For example, use the following values to trigger an alert when the hit count for the rule that you identified increases by 10% for six hours:

     * **Condition types:** Set to `Threshold`.
     * **Alert trigger:** Set to `Any time series violates`.
     * **Threshold position:** Set to `Above threshold`.
     * **Threshold value:** Set to `10`.
  6. In the **Advanced options** section, enter a name for the condition and click **Next**.

  7. On the **Multi-condition trigger** page, specify the condition and click **Next**.

  8. On the **Configure notifications** page, select **Notification channels** and then **Manage notification channels**.

  9. In the **Notification channels** window, add the new notification channel—for example, an email address, and click **Save**.

  10. In the **Notification channels** list, select the added notifications and then click **OK**.

  11. In the **Name the alert policy** section, enter the name and click **Next**. The alert condition is added.




## Clean up shadowed firewall rules

To clean up firewall rules that are shadowed by other rules, do the following:

###  Console 

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. In the **VPC firewall rules** section, click **filter_list Filter** and then select **Insight type > Shadowed rules**.

  3. For each rule in the search results, click the **Name** of the rule and view its details page. Review and clean up each rule as needed.




For more information about shadowed rules, see [Examples of shadowed rules](https://docs.cloud.google.com/network-intelligence-center/docs/firewall-insights/concepts/insights-categories-states#shadowed-rule-example).

## Remove an unused `allow` rule

To evaluate and remove an unused `allow` rule, do the following:

###  Console 

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. In the **VPC firewall rules** section, click **filter_list Filter**, and then select **Type > Ingress > last hit before MM/DD/YYYY**.

Replace `MM/DD/YYYY` with the date that you want to use. For example, `08/31/2021`.

  3. For each rule in the search results, review the information in the **Insights** column. This column provides a percentage that indicates the likelihood that this rule will be hit in the future. If the percentage is high, you might want to keep this rule. However, if it is low, continue reviewing the information generated by the insight.

  4. Click the insight link to display the **Insight details** pane.

  5. In the **Insight details** pane, review the attributes of this rule and the attributes of any similar rules that are listed.

  6. If the rule has a low probability of being hit in the future, and if that prediction is supported by the hit pattern of similar rules, consider removing the rule. To remove the rule, click **Rule name**. The **Firewall rule details** page opens.

  7. Click **Delete**.

  8. In the confirmation dialog, click **Delete**.




## Remove an unused attribute from an `allow` rule

To evaluate and remove an unused attribute, do the following:

###  Console 

  1. In the Google Cloud console, go to the **Firewall Insights** page.

[Go to Firewall Insights](https://console.cloud.google.com/net-intelligence/firewalls)

  2. On the card named **Allow rules with unused attributes** , click **View full list**. In response, the Google Cloud console displays the **Allow rules with unused attributes** page. This page lists all the rules that had unused attributes during the observation period.

  3. Click the text that's displayed in the **Insight** column. The **Insight Details** page opens.

  4. Review the details at the top of the page. The summary includes the following details:

     * The name of the insight.
     * The number of unused attributes that this rule has.
     * The time that the insight was last updated.
     * The names of other rules in the project that use similar attributes.
     * The length of the observation period.
  5. Assess whether you could remove the attribute:

     1. Review the **Firewall rule with unhit attributes** card. Look at the field labeled **Attribute with no hit (with future hit prediction)**. This field provides a percentage that describes the likelihood of whether the attribute will be hit in the future.
     2. Review the **Similar firewall rule in the same project** card. Review the data displayed about whether this rule's attribute was used.
  6. If the attribute has a low probability of being hit in the future, and if that prediction is supported by the hit pattern of similar rules, consider removing the attribute from the rule. To remove the attribute, click the name of the rule, which appears at the top of the **Insight Detail** page. The **Firewall rule details** page opens.

  7. Click **Edit** , make the needed changes, and then click **Save**.




## Narrow an `allow` rule's IP address range

Be aware that your project might have firewall rules that allow access from certain IP address blocks for load balancer health checks or for other Google Cloud functionality. These IP addresses might not be hit, but they should not be removed from your firewall rules. For more information about these ranges, see the [Compute Engine documentation](https://docs.cloud.google.com/compute/docs/faq#find_ip_range). 

To evaluate and tighten an overly permissive IP address range, do the following:

###  Console 

  1. In the Google Cloud console, go to the **Firewall Insights** page.

[Go to Firewall Insights](https://console.cloud.google.com/net-intelligence/firewalls)

  2. On the card named **Allow rules with overly permissive IP address or port ranges** , click **View full list**. In response, the Google Cloud console displays a list of all the rules that had overly permissive ranges during the observation period.

  3. Find any rule in the list, and click the text that's displayed in the **Insight** column. The **Insight Details** page opens.

  4. Review the details at the top of the page. The summary includes the following details:

     * The name of the rule.
     * The number of IP address ranges that could be narrowed.
     * The time that the insight was last updated.
     * The length of the observation period.
  5. Assess whether you could narrow the IP address range: Review the **Firewall rule with overly permissive IP address or port ranges** card. Review the proposed list of new IP address ranges.

  6. If appropriate, consider using the recommendations in the insight to make the IP address range more narrow. Click the name of the rule, which appears at the top of the **Insight Detail** page. The **Firewall rule details** page opens.

  7. Click **Edit** , make the needed changes, and then click **Save**.




## What's next

  * [View Firewall Insights metrics](https://docs.cloud.google.com/network-intelligence-center/docs/firewall-insights/how-to/view-metrics)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
