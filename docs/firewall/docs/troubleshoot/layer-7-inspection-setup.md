---
url: https://docs.cloud.google.com/firewall/docs/troubleshoot/layer-7-inspection-setup/
title: Troubleshoot application layer inspection \u00a0|\u00a0 Cloud Next Generation Firewall \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:40:32.399706+00:00
---

# Troubleshoot application layer inspection  |  Cloud Next Generation Firewall  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firewall/docs/troubleshoot/layer-7-inspection-setup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NGFW ](https://docs.cloud.google.com/firewall/docs)
  * [ Guides ](https://docs.cloud.google.com/firewall/docs/about-firewalls)



Send feedback 

#  Troubleshoot application layer inspection Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to troubleshoot common issues that you might encounter when setting up application layer (Layer 7) inspection in your network. These issues might be related to [security profiles](https://docs.cloud.google.com/firewall/docs/about-security-profiles), [security profile groups](https://docs.cloud.google.com/firewall/docs/about-security-profile-groups), [firewall endpoints](https://docs.cloud.google.com/firewall/docs/about-firewall-endpoints), or [firewall policies](https://docs.cloud.google.com/firewall/docs/firewall-policies-overview).

## Generic troubleshooting steps

To troubleshoot common configuration errors related to Layer 7 inspection in your network, complete the tasks mentioned in the following sections.

### Enable firewall policy rules logging

To enable logging for the Layer 7 inspection firewall rules in your firewall policies, do the following:

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. Click the name of the firewall policy that has Layer 7 inspection firewall rules.

  3. In the **Priority** column, click the priority of the firewall policy rule for which you want to enable logs.

  4. Click **Edit**.

  5. For **Logs** , select **On**.

  6. Click **Save**.




Repeat the preceding steps for all the network firewall policies and hierarchical firewall policies that contain Layer 7 inspection firewall rules.

### Verify your firewall policy rules configuration

  1. Make sure that the firewall policies with the Layer 7 inspection firewall rules are associated with the Virtual Private Cloud (VPC) network where your virtual machine (VM) workloads are located. For more information, see [Associate a policy with the network](https://docs.cloud.google.com/firewall/docs/use-network-firewall-policies#associate).
  2. Verify that the [firewall endpoints](https://docs.cloud.google.com/firewall/docs/configure-firewall-endpoints) are associated with the VPC network where your VM workloads reside.
  3. Check the rule enforcement order to make sure that the rules applied to the traffic are in the correct sequence. For more information, see [Policy and rule evaluation order](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-eval-order).
  4. Check the [effective firewall rules](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-eval-order#effective-firewall-rules) at the network and VM instance level. Make sure that the firewall policy rules for Layer 7 inspection firewall rules are getting hit for the network traffic.



## All connections are allowed or denied but not intercepted

This scenario is encountered when you have configured all the components for Layer 7 inspection firewall rules, but the traffic is not intercepted and inspected for any threats or malicious activity.

To resolve this issue, follow these steps:

  1. Verify that the firewall endpoint and the VM workloads to be inspected are in the same zone.
  2. Verify that the logging is enabled for the firewall policy rule. For more information, see the Enable firewall policy rules logging section of this document.
  3. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  4. Click the firewall policy that contains the rule for Layer 7 inspection.

  5. In the **Hit count** column, view the number of unique connections used for the firewall rule.

  6. If the hit count is zero, the rule is not applied to the traffic. To verify if the setup is correct, see Generic troubleshooting steps section of this document.

  7. If the hit count is not a zero, click the count to go to the **Log explorer** page and follow these steps:

     1. Expand individual logs to view the `connection`, `disposition`, and `remote location` details.
     2. If the `disposition` is not set to `intercepted` and the `fallback_action = ALLOW`, check out the Generic troubleshooting steps section of this document to verify if the setup is correct.



## Ingress firewall policy rule does not intercept incoming traffic

This scenario is encountered when the Layer 7 inspection firewall rules are not applied to the incoming traffic. It happens when the incoming traffic matches the other firewall rules before it hits the Layer 7 inspection firewall policy rules.

To resolve this issue, follow these steps:

  1. Verify that the logging is enabled for the firewall policy rule with Layer 7 inspection. For more information, see Enable firewall policy rules logging section of this document.
  2. Make sure that the firewall policy with the Layer 7 inspection firewall rule is associated with the VPC network where your VM workloads are located. For more information, see [Associate a policy with the network](https://docs.cloud.google.com/firewall/docs/use-network-firewall-policies#associate).
  3. Verify that the [firewall endpoints](https://docs.cloud.google.com/firewall/docs/configure-firewall-endpoints) are associated with the VPC network where your VM workloads reside.
  4. To verify that the Layer 7 inspection firewall rule is applied, run the connectivity tests based on the source and destination you defined in the rule. To learn how to run Connectivity Tests, see [Create and run Connectivity Tests](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/running-connectivity-tests).
  5. Check the sequence in which the rules are applied to the incoming traffic. To change this sequence, see [Evaluation order for firewall policies and rules](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-eval-order).



## A threat is not detected on some or all of the connections

This scenario might be encountered when your traffic is encrypted, or the threat prevention policy is not set to detect the threat.

If your traffic is encrypted, make sure that you have enabled Transport Layer Security (TLS) inspection on your network. To learn more about how to enable TLS inspection, see [Set up TLS inspection](https://docs.cloud.google.com/firewall/docs/setup-tls-inspection).

If TLS inspection is enabled, distinguish between messages seen from the client versus error messages when Cloud Next Generation Firewall (Cloud NGFW) blocks a threat. For more information, see Error messages.

Make sure that the threat prevention policy is set to detect this threat:

  1. Review your [threat prevention security profile](https://docs.cloud.google.com/firewall/docs/configure-security-profiles#list-overrides) to identify that the override actions for this threat are set as expected.
  2. [Add override actions in a threat prevention security profile](https://docs.cloud.google.com/firewall/docs/configure-security-profiles#add-overrides) to make sure that the threat is captured.



## Misconfigured intrusion detection and prevention service firewall rules

This scenario occurs when there is no valid firewall endpoint or the endpoint is not associated with the VPC network where your VM workloads are located. As a default fallback action, Cloud NGFW allows the traffic, and adds `apply_security_profile_fallback_action = ALLOW` to the firewall logs. To view the firewall logs, see [View logs](https://docs.cloud.google.com/firewall/docs/using-firewall-rules-logging#viewing-logs).

To resolve this issue, follow these steps:

  1. To enable logging for the Layer 7 inspection firewall policy rules in your network, see the Enable firewall policy rules logging section of this document.

  2. Create the [log-based metrics](https://docs.cloud.google.com/logging/docs/logs-based-metrics), [log-based alerts](https://docs.cloud.google.com/logging/docs/alerting/log-based-alerts), or both by using the following filters.
         
         jsonPayload.rule_details.action="APPLY_SECURITY_PROFILE_GROUP"
           jsonPayload.rule_details.apply_security_profile_fallback_action="ALLOW"
         




The filter generates incident details, which helps you to understand the log match condition, notification rate limit, incident auto-close duration, log labels, and log severity with the summary.

## URL filtering service does not allow or deny traffic as expected

You might encounter this scenario if you configure all components for Layer 7 inspection and URL filtering, but traffic to a URL is not allowed or denied as expected.

To resolve this issue, follow these steps:

  1. Follow the instructions in the All connections are allowed or denied but not intercepted section of this document to determine if the firewall rule for Layer 7 inspection is applied to the traffic and if the traffic is successfully intercepted.

If the rule is not applied or the traffic is not intercepted, revisit the All connections are allowed or denied but not intercepted section.

  2. If the rule is applied and the traffic is intercepted, view the URL filtering logs by going to the [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface) and entering the following query in the **Query** pane. Replace `PROJECT_ID` with the ID of your project.
         
         resource.type="networksecurity.googleapis.com/FirewallEndpoint" logName="projects/PROJECT_ID/logs/networksecurity.googleapis.com%2Ffirewall_url_filter"
         

  3. Expand the log entry and determine the value of the field `ruleIndex`. This field indicates the priority of the URL filter against which the firewall endpoint detected a match.

  4. In the Google Cloud console, go to the **Security profiles** page.

[Go to Security profiles](https://console.cloud.google.com/net-security/security-profiles/profiles/list)

  5. In the **Security profiles** tab, click the security profile associated with the firewall rule to view the profile details.

  6. Verify if the allowed or denied URL is listed against the priority that you obtained earlier, which helps you determine if the firewall endpoint detected a match against a different URL filter with a higher priority. Therefore, your security profile might contain multiple URL filters that include the same URL.




## Advanced malware sandbox health metric indicates an infrastructure issue

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

If your traffic matches rules for Advanced malware sandbox (WildFire) but files aren't inspected or logged, an infrastructure issue might be the cause. You can verify this by checking the Advanced malware sandbox health metric.

An unhealthy Advanced malware sandbox health metric indicates an underlying infrastructure issue that prevents the Advanced malware sandbox service from working.

To resolve this issue, do the following:

  1. In the Google Cloud console, go to the _leaderboard_ **Metrics explorer** page: 

[Go to **Metrics explorer**](https://console.cloud.google.com/monitoring/metrics-explorer)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the project selector list, select the project.
  3. In the toolbar of the query pane, do the following:

     1. In the **Metric** menu, click **Select a metric**. Use the search bar and filters in the **Select a metric** menu to find available metric types.
     2. In the search bar, enter **Firewall endpoint**.
     3. Click **Firewall endpoint > Firewall_endpoint > Advanced malware sandbox health**.
     4. Click **Apply**.
  4. In the **Results** section, click the **Table** tab. You can view the Advanced malware sandbox health metric.


**Note:** If the metric is unhealthy, wait for the infrastructure to recover or check for ongoing incidents by using [Personalized service health](https://docs.cloud.google.com/service-health).

## Error messages

This section describes the common error messages you get when the TLS trust is improper or Cloud NGFW blocks a threat. To learn how to set up TLS inspection, see [Set up TLS inspection](https://docs.cloud.google.com/firewall/docs/setup-tls-inspection).

### Firewall policy rule is blocked

You received an error message similar to the following error from a client during an SSH session.
    
    
          curl: (56) OpenSSL SSL_read: Connection reset by peer, errno 104
    

To resolve this error, view the log and validate it. For more information, see [Use VPC firewall rules logging](https://docs.cloud.google.com/firewall/docs/using-firewall-rules-logging).

### Misconfigured trust

You received an error message similar to the following error from a client during an SSH session.
    
    
          curl: (35) OpenSSL SSL_connect: Connection reset by peer in connection
    

This error indicates a misconfigured trust issue. This issue is caused either due to an incorrect configuration or the absence of a certificate authority (CA). To resolve this error, enable [Certificate Authority Service](https://docs.cloud.google.com/certificate-authority-service).

## Endpoint policies are ignored

Only firewall policy rules are being evaluated and traffic is not mirrored to [Cloud Intrusion Detection System](https://docs.cloud.google.com/intrusion-detection-system/docs/overview) for inspection while using Cloud Next Generation Firewall L7 inspection policies.

To resolve this, you must ensure that your Cloud NGFW L7 inspection policies (rules with the `apply_security_profile_group` action) don't apply to packets that you need to inspect with Cloud IDS.

## What's next

  * For conceptual information about intrusion detection and prevention service, see [Intrusion detection and prevention service overview](https://docs.cloud.google.com/firewall/docs/about-intrusion-prevention).
  * For conceptual information about firewall policy rules, see [Firewall policy rule components](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details).
  * To determine costs, see [Cloud NGFW pricing](https://cloud.google.com/firewall/pricing).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
