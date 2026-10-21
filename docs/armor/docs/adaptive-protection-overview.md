---
url: https://docs.cloud.google.com/armor/docs/adaptive-protection-overview/
title: Adaptive Protection overview \u00a0|\u00a0 Google Cloud Armor \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:42:19.449362+00:00
---

# Adaptive Protection overview  |  Google Cloud Armor  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/armor/docs/adaptive-protection-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Google Cloud Armor ](https://docs.cloud.google.com/armor/docs)
  * [ Guides ](https://docs.cloud.google.com/armor/docs/cloud-armor-overview)



Send feedback 

#  Adaptive Protection overview Stay organized with collections  Save and categorize content based on your preferences. 

Google Cloud Armor Adaptive Protection helps you protect your Google Cloud applications, websites, and services against L7 distributed denial-of-service (DDoS) attacks such as HTTP floods and other high-frequency layer 7 (application-level) malicious activity. Adaptive Protection builds machine-learning models that do the following:

  1. Detect and alert on anomalous activity
  2. Generate a signature describing the potential attack
  3. Generate a custom Google Cloud Armor WAF rule to block the signature



You enable or disable Adaptive Protection on a per-security-policy basis.

Alerts about anomalous traffic (potential attacks), which include the signatures of the attacks, appear in the Adaptive Protection event dashboard with event logs sent to Cloud Logging, where they can be directly analyzed or forwarded to a downstream log or security event monitoring workflow. Alerts of potential attacks are also generated as findings in the [Security Command Center](https://console.cloud.google.com/projectselector2/security/command-center/welcome).

## Availability of Adaptive Protection

Full Adaptive Protection alerts are available only if you subscribe to Google Cloud Armor Enterprise. Otherwise, you receive only a basic alert. A basic alert contains only minimal information, such as a confidence score of the detection and the attack size. A basic alert includes no attack signature or suggested rule for users to deploy.

If your projects are not already enrolled in Cloud Armor Enterprise, read [Using Cloud Armor Enterprise](https://docs.cloud.google.com/armor/docs/armor-enterprise-using) for information about how to enroll.

## Cloud Logging and Cloud Monitoring

Because using Adaptive Protection effectively requires you to understand how logging and alerting work in Google Cloud, we recommend that you familiarize yourself with Cloud Logging, alerting, and alerting policies.

  * For general logging information, see the [Cloud Logging documentation](https://docs.cloud.google.com/logging/docs/overview).
  * For information about alerting, see the [Cloud Monitoring documentation](https://docs.cloud.google.com/monitoring/alerts).
  * For Cloud Armor-specific logging information, see [Using request logging](https://docs.cloud.google.com/armor/docs/request-logging).



In order to ensure proper logging and reporting, Cloud Armor requires access to the following logs. These must be stored in Cloud Logging, or routed to a [logging bucket](https://docs.cloud.google.com/logging/docs/buckets) which Cloud Armor can access.

  * `networksecurity.googleapis.com/dos_attack`
  * `networksecurity.googleapis.com/network_dos_attack`
  * `networksecurity.googleapis.com/network_dos_attack_mitigations`



## Configure and tune alerts

You can enable Adaptive Protection in projects where Cloud Armor security policies already protect your applications. When you enable Adaptive Protection for a particular security policy, Adaptive Protection is in effect for all backend services with which the security policy is associated.

After Adaptive Protection is enabled, there's a training period of at least one hour before Adaptive Protection develops a reliable baseline and begins monitoring traffic and generating alerts. During the training period, Adaptive Protection models incoming traffic and usage patterns that are specific to each backend service, so that it develops the baseline for each backend service. When the training period is over, you receive real-time alerts when Adaptive Protection identifies high frequency or high volume anomalies in the traffic directed to any of the backend services associated with that security policy.

**Warning:** When you create a new security policy, Adaptive Protection must re-train to develop a new baseline, and your old baseline is discarded. We strongly recommend that you not create new security policies during an attack.

You can tune Adaptive Protection alerts based on several metrics. The alerts, which are sent to Cloud Logging, include a _confidence level_ , an _attack signature_ , a suggested rule, and an estimated _impacted baseline rate_ associated with the suggested rule.

  * The confidence level indicates the confidence with which Adaptive Protection models predict that the observed change in traffic pattern is anomalous.
  * The impacted baseline rates associated with the suggested rule represent the percentage of existing baseline traffic that is caught by the rule. Two rates are provided. The first is the percentage relative to the traffic into the specific backend service under attack. The second is the percentage relative to all the traffic going through the security policy including all configured backend service targets (not just the one being attacked).



You can filter alerts in Cloud Logging based on the confidence level or the impacted baseline rates, or both. For more information about tuning alerts, see [Managing alerting policies](https://docs.cloud.google.com/monitoring/alerts/using-alerting-ui).

Adaptive Protection aims to protect backend services from high volume Layer 7 DDoS attacks. In the following scenarios, requests are not counted in Adaptive Protection:

  * Requests directly served from Cloud CDN
  * Requests rejected by a Cloud Armor security policy



### Granular models

By default, Adaptive Protection detects an attack and suggests mitigations based on the typical traffic directed to each backend service. This means that a backend behind a backend service can become overloaded, but Adaptive Protection takes no action because the attack traffic is not anomalous to the backend service.

The granular models feature lets you configure specific hosts or paths as the granular units that Adaptive Protection analyzes. When you use granular models, Adaptive Protection's suggested mitigations filter traffic based on matched host or URL path prefixes, helping to reduce false positives. Each of these hosts or paths is called a _granular traffic unit_.

The identified attack signatures only target the attack traffic coming into the granular traffic unit; however, the filtering still applies to all of the requests matched by the deployed rule, like it would without the granular configurations. For example, if you want an auto-deployed rule to only match a specific traffic granular unit, consider using a match condition like `evaluateAdaptiveProtectionAutoDeploy() && request.headers['host'] == ... && request.path == ...`.

In addition to host and URL path prefixes, you can configure alert thresholds based on some or all of the following options. You can apply these thresholds to the granular traffic units or to the backend service as a whole, except for the load threshold which can only be applied to the backend service:

  * Load: the maximum load for the backend service, according to the configured Application Load Balancer. This option is not available to granular traffic units and is not available to serverless backends like Cloud Run, Cloud Run functions, or external origin backends.
  * Absolute queries per second (QPS): the peak traffic amount, in queries per second, that the backend service or traffic unit receives.
  * Relative to the baseline QPS: a multiple of the average long-term baseline traffic volume. For example, a value of `2` represents a QPS of double the baseline traffic volume.



For more information about configuring granular models, see [Configure Google Cloud Armor Adaptive Protection](https://docs.cloud.google.com/armor/docs/configure-adaptive-protection#granular-models).

## Consume and interpret alerts

As soon as Adaptive Protection detects a suspected attack, it generates an event in the Adaptive Protection event dashboard and generates a log item in Cloud Logging. The alert is in the JSON payload of the log item. The log item is generated under the **Network Security Policy** resource in Cloud Logging. The log message identifies the backend service under attack and includes a confidence score indicating how strongly Adaptive Protection rates the identified traffic pattern change as anomalous. The log message also includes an _attack signature_ that illustrates the characteristics of the attack traffic, along with suggested Cloud Armor rules that you might apply to mitigate the attack.

### Understand attack signatures

An Adaptive Protection alert includes an _attack signature_ , which is a description of the traffic attributes of the potential attack. You use the signature to identify and potentially block the attack. The signature takes two forms: as a user-readable table and as a preconstructed Cloud Armor WAF rule that you can deploy in the relevant security policy. If you are not subscribed to Cloud Armor Enterprise, an _attack signature_ is not included in the basic alert.

The signature consists of a set of attributes, such as client IP address, geographical regions, cookies, user agents, referers and other HTTP request headers, and the set of values for those attributes thought to be associated with the potential attack traffic. The set of attributes is not user- configurable. The attribute values depend on the values in the incoming traffic to your backend service.

For each attribute value that Adaptive Protection believes indicates the potential attack, Adaptive Protection lists the following:

  * The attack likelihood
  * The proportion of the attribute in the attack, which is the percentage of potential attack traffic that had this value at the time that the attack was detected
  * The proportion of the attribute in baseline, which is the percentage of baseline traffic that possessed this attribute value at time that the attack was detected



[Cloud Logging entry specification](https://docs.cloud.google.com/armor/docs/adaptive-protection-overview#logging-entry) contains details about the information in each alert.

The following is an example of a user-readable table that contains the signature of a potential attack:

Attribute name | Value | Match type | Attack likelihood | Proportion in attack | Proportion in baseline  
---|---|---|---|---|---  
`UserAgent` | "foo" | Exact match | 0.7 | 0.85 | 0.12  
`UserAgent` | "bar" | Exact match | 0.6 | 0.7 | 0.4  
Client IP | "a.b.c.d" | Exact match | 0.95 | 0.1 | 0.01  
Client IP | a.b.c.e | Exact match | 0.95 | 0.1 | 0.01  
Client IP | a.b.c.f | Exact match | 0.05 | 0.1 | 0.1  
`RegionCode` | UK | Exact match | 0.64 | 0.3 | 0.1  
`RegionCode` | IN | Exact match | 0.25 | 0.2 | 0.3  
`RequestUri` | /urlpart | Substring | 0.7 | 0.85 | 0.12  
  
An Adaptive Protection alert and the relevant Cloud Logging event log contain the following:

  * A unique alert ID, or `alertID`, which is used to refer to a specific alert when it reports user feedback (more below)
  * The backend service under attack, or `backendService`
  * The confidence score, or `confidence`, which is a number between 0 and 1 that indicates how strongly the Adaptive Protection system rates the detected event as a malicious attack



You also receive a set of signatures and rules characterizing the detected attack. Specifically, the set provides a list of `headerSignatures`, each corresponding to one HTTP header and containing a list of `significantValues` for the specific header. Each significant value is either an observed header value or a substring of it.

The following is an example signature:
    
    
    ...
    headerSignatures: [
      0: {
       name: "Referer"
       significantValues: [
        0: {
         attackLikelihood: 0.95
         matchType: "MATCH_TYPE_EQUALS"
         proportionInAttack: 0.6
         proportionInBaseline: 0.01
         value: "foo.attacker.com"
        }
       ]
      }
    ...
    

The alert suggests that the value `foo.attacker.com` in the header `Referer` is important in characterizing the attack. More specifically, 60% of the attack traffic (`proportionInAttack`) has this `Referer` value and only 1% of baseline traffic among all traffic (`proportionInBaseline`) has the same `Referer` value. Moreover, among all traffic matching this `Referer` value, 95% is attack traffic (`attackLikelihood`).

These values suggest that if you were to block all requests with `foo.attacker.com` in the `Referer` header field, you would successfully block 60% of the attack and also 1% of the baseline traffic.

The property `matchType` specifies the relationship between the attribute in the attack traffic and the significant value. It can be either `MATCH_TYPE_CONTAINS` or `MATCH_TYPE_EQUALS`.

The next signature matches traffic with a substring `/api?` in the request URI:
    
    
    ...
    headerSignatures: [
      0: {
       name: "RequestUri"
       significantValues: [
        0: {
         attackLikelihood: 0.95
         matchType: "MATCH_TYPE_CONTAINS"
         proportionInAttack: 0.9
         proportionInBaseline: 0.01
         value: "/api?"
        }
       ]
      }
    ...
    

### Deploy suggested rules

Adaptive Protection alerts also provide a suggested Cloud Armor rule expressed in the [custom rules language](https://docs.cloud.google.com/armor/docs/rules-language-reference). This rule can be used to create a rule in a Cloud Armor security policy to mitigate the attack. In addition to the signature, the alert includes a rate of impacted baseline traffic to help you evaluate the impact of deploying the rule. The rate of impacted baseline traffic is a projected proportion of baseline traffic that matches the attack signature identified by Adaptive Protection. If you are not subscribed to Cloud Armor Enterprise, _basic alerts_ sent by Adaptive Protection do not include a suggested Cloud Armor rule that you can apply.

You can find some of the alert signature as well as the impacted baseline rate in the log message sent to Cloud Logging. The following example is the JSON payload of a sample alert along with the resource labels on which you can filter the logs.
    
    
    ...
     jsonPayload: {
       alertId: "11275630857957031521"
       backendService: "test-service"
       confidence: 0.71828485
       headerSignatures: [
    
        0: {
         name: "RequestUri"
         significantValues: [
          0: {
           attackLikelihood: 0.88
           matchType: "MATCH_TYPE_EQUALS"
           proportionInAttack: 0.85
           proportionInBaseline: 0.01
           value: "/"
          }
         ]
        }
        1: {
         name: "RegionCode"
         significantValues: [
          0: {
           attackLikelihood: 0.08
           matchType: "MATCH_TYPE_EQUALS"
           proportionInAttack: 0.17
           proportionInBaseline: 0.28
           value: "US"
          }
          1: {
           attackLikelihood: 0.68
           matchType: "MATCH_TYPE_EQUALS"
           proportionInAttack: 0.09
           proportionInBaseline: 0.01
           value: "DE"
          }
          2: {
           attackLikelihood: 0.74
           matchType: "MATCH_TYPE_EQUALS"
           proportionInAttack: 0.05
           proportionInBaseline: 0
           value: "MD"
          }
         ]
        }
         2: {
         name: "UserAgent"
         significantValues: [
          0: {
           attackLikelihood: 0.92
           matchType: "MATCH_TYPE_EQUALS"
           proportionInAttack: 0.85
           proportionInBaseline: 0
           value: "Unusual browser"
          }
          1: {
           attackLikelihood: 0.87
           proportionInAttack: 0.7
           proportionInBaseline: 0.1
           missing: true
          }
         ]
        }
       ]
       suggestedRule: [
        0: {
         action: "DENY"
         evaluation: {
           impactedAttackProportion: 0.95
           impactedBaselineProportion: 0.001
           impactedBaselinePolicyProportion: 0.001
         }
         expression: "evaluateAdaptiveProtection('11275630857957031521')"
        }
       ]
       ruleStatus: RULE_GENERATED
       attackSize: 5000
     }
     resource: {
        type: "network_security_policy",
        labels: {
          project_id: "your-project",
          policy_name: "your-security-policy-name"
        }
     },
    }
    }
    ...
    

You can deploy suggested rules by copying the CEL expression from the rule signature and pasting the expression into the match condition of a newly created rule, or by clicking the **Apply** button on the Adaptive Protection dashboard in the Cloud Armor UI.

To deploy the rule, you create a new rule in the Cloud Armor security policy that protects the targeted backend services identified by the alert. Next, during rule configuration, copy and paste the CEL expression from the alert into the **Match condition** field of the rule and set the rule action to `deny`. In the above example, you copy the expression `evaluateAdaptiveProtection('11275630857957031521')` from the `suggestedRule` section of the alert.

We strongly recommend that you initially deploy the rule in [preview mode](https://docs.cloud.google.com/armor/docs/security-policy-overview#preview_mode) so that you can evaluate the impact of the rule on production traffic. When you do this, Cloud Armor logs the action and the associated traffic whenever the rule is triggered, but no action is taken on the matched traffic.

In addition, if your security policy is attached to multiple backend services, note whether the effects of the new rule have unwanted effects in any of the backend services. If this happens, configure new security policies to mitigate the unwanted effects, and attach them to the correct backend services.

We recommend that you set the priority for the new rule higher than any rules with the action set to allow. This is because, to have the projected impact and have maximal effect in mitigating the attack, the rule should be deployed in the highest logical priority position to ensure that all matching traffic is blocked by the rule. Rules in a Cloud Armor security policy are evaluated in priority order with evaluation terminating after the first matching rule is triggered and the associated rule action is taken. If you need to grant an exception for some traffic or specific clients from this rule, an "allow" rule can be created with higher priority, that is, with a lower numerical value. For more information about rule priority, see [Rule evaluation order](https://docs.cloud.google.com/armor/docs/security-policy-overview#eval-order).

### Automatically deploy suggested rules

You can also configure Adaptive Protection to automatically deploy suggested rules. To enable automatic rule deployment, you create a placeholder rule with your choice of priority and action by using the expression `evaluateAdaptiveProtectionAutoDeploy()` in the match condition. This rule evaluates to `true` for requests that Adaptive Protection identifies as attack traffic, and Cloud Armor applies the action to the attacking request. All Cloud Armor action types, like `allow`, `deny`, `throttle`, and `redirect` are supported. In addition, you can use preview mode to log that the rule was triggered, without taking the configured action.

If you use an upstream proxy such as a third-party CDN in front of your external Application Load Balancer, we recommend that you configure the [`userIpRequestHeaders` field](https://docs.cloud.google.com/compute/docs/reference/rest/beta/securityPolicies) to add your provider's IP address (or IP address ranges) to an allowlist. This prevents Adaptive Protection from mistakenly identifying the proxy's client IP address as participating in an attack. Instead, it looks at the user-configured field for the client IP address of the traffic before it arrived at the proxy.

For more information about configuring automatic rule deployment, see [Automatically deploy Adaptive Protection suggested rules](https://docs.cloud.google.com/armor/docs/adaptive-protection-auto-deploy).

### Rule status

If no rule is presented when you attempt to deploy a suggested rule, you can use the `ruleStatus` field to determine the cause.

The value of the `attackSize` field is in queries per second (QPS).
    
    
     ]
    ruleStatus: RULE_GENERATED
    attackSize: 5000
    }
    

The following table describes the possible values of the field and what they mean.

Rule status | Description  
---|---  
RULE_GENERATED | A usable rule was generated normally.  
BASELINE_TOO_RECENT | Not enough time to accumulate reliable baseline traffic. Up to one hour is necessary to generate rules.  
NO_SIGNIFICANT_VALUE_DETECTED | No headers have significant values associated with attack traffic, so no rule could be generated.  
NO_USABLE_RULE_FOUND | No usable rule could be created.  
ERROR | An unspecified error occurred when creating the rule.  
  
### Monitoring, feedback, and reporting event errors

You need the following permissions to view or interact with the Adaptive Protection dashboard.

  * `compute.securityPolicies.list`
  * `compute.backendServices.list`
  * `logging.logEntries.list`



After you enable Adaptive Protection on any Cloud Armor security policy, you can see the following page under **Network Security > Cloud Armor** panel. It displays the traffic volume over time for the selected security policy and backend service, and the selected duration. Any instances of potential attacks alerted by Adaptive Protection are annotated on the graph and listed below the graph. When you click a specific attack event, a side window is displayed with the attack signature and suggested rule shown in tabular format. This is same information that's in the Cloud Logging log entries that are described in Cloud Logging entry specification. Click the **Apply** button to add the suggested rule to the same security policy.

[ ![Adaptive Protection dashboard](https://docs.cloud.google.com/static/armor/images/caap-dashboard.svg)](https://docs.cloud.google.com/static/armor/images/caap-dashboard.svg) Adaptive Protection dashboard (click to enlarge)[ ![Adaptive Protection alert details](https://docs.cloud.google.com/static/armor/images/alert-details.svg)](https://docs.cloud.google.com/static/armor/images/alert-details.svg) Adaptive Protection dashboard (click to enlarge)

Not every Adaptive Protection finding is deemed an attack, given the protected backend service's unique context and environmental factors. If you determine that the potential attack described by the alert is normal or accepted behavior, then you can report an event error to help train the Adaptive Protection models. Next to each attack event listed under the graph is a button that pops up an interactive window to allow you to report an event error with some optional context. Reporting an event error helps reduce the likelihood of similar errors in the future. Over time, this increases Adaptive Protection's accuracy.

### Monitoring, alerting, and logging

Adaptive Protection telemetry is sent to Cloud Logging as well as the Security Command Center. The Adaptive Protection log message sent to Cloud Logging is described in the previous sections of this document. A log entry is generated every time Adaptive Protection detects a potential attack and each entry contains a confidence score describing how confident the models are that the observed traffic is anomalous. To fine-tune alerting, an alerting policy can be configured in Cloud Logging to trigger an alert only when an Adaptive Protection log message has a confidence score above a user-specified threshold. We recommend that you start with a low threshold, with confidence > 0.5, to avoid missing warnings of potential attacks. The confidence threshold in the alerting policy can be increased over time if the alerts have an unacceptable impacted baseline rate.

The Security Command Center dashboard also contains findings from Adaptive Protection. They are located in the Cloud Armor card under the **Application DDoS Attacks** category. Each finding includes the details of the service, the attack confidence, the signature associated with the attack, and a link to the specific alert on the Adaptive Protection dashboard. The following screenshot is an example of an application DDoS attack attempt finding:

[ ![Application DDoS attack finding.](https://docs.cloud.google.com/static/armor/images/ca-cscc-app-ddos.png)](https://docs.cloud.google.com/static/armor/images/ca-cscc-app-ddos.png) **Application DDoS attack** finding (click to enlarge).

### Cloud Logging entry specification

The Adaptive Protection alert sent to Cloud Logging consists of a log entry containing the following elements:

  * Alert confidence: Adaptive Protection confidence that the event observed is an attack.
  * Automatically deployed: the flag indicates whether the criteria for automatic defense was triggered _at the time of detection_. Note that it does _not_ necessarily suggest a traffic impacting action was already taken. Automatic defense is dynamic, continuously evaluating trigger criteria and identifying attackers. To see the specific actions taken, check the relevant fields in the Cloud Armor [request logging](https://docs.cloud.google.com/armor/docs/request-logging#security_policy_log_entries).
  * Attack signature 
    * Attribute name: the name of the attribute which matches to the `Value` below, such as a particular request header name or a geographic origin.
    * Value: the value to which the attribute in malicious traffic matches.
    * Match type: the relationship between `Value` and the attribute in attack traffic. the value is either equal to or a substring of an attribute in attack traffic.
    * Attack likelihood: the likelihood that a given request is malicious, given that the relevant attribute of this request matches `Value`.
    * Proportion in attack: the percent of potential attack traffic that matches `Value`.
    * Proportion in baseline: the percent of normal, baseline traffic that matches `Value`.
  * Suggested rule 
    * Match condition: the expression to be used in the rules match condition to identify malicious traffic.
    * Impacted baseline rate: the projected percentage of good traffic to the specific backend service under attack that is captured by the suggested rule.
    * Impacted baseline rate across policy: the projected percentage of good traffic to all the backend services in the same security policy that is captured by the suggested rule.
    * Impacted attack rate: the projected percentage of attack traffic that is captured by the suggested rule.
  * Rule status: additional details about rule generation.



## Machine learning overview and privacy

  * Training data and detection data 
    * Adaptive Protection builds several models to detect potential attacks and identify their signatures. The signals used by these models to determine if an attack is ongoing are derived from the observed metadata of incoming request traffic from your projects. Such metadata includes: client IP address, client geography, and the values of some HTTP request headers.
    * The actual features used by the models are derived statistical properties of the above-mentioned signals. That is, the training data for the models do not include the actual values of any metadata, such as IP addresses and/or request header values.
    * A common set of detection models, trained with only artificial data are shared across all customers, to determine whether an attack is taking place, when Adaptive Protection is first enabled. Once you report any false attack event and the models are updated using traffic signals specific from your projects, these models are local to your projects and are not used for any other customers.
  * Signature generation data 
    * After Adaptive Protection determines that a potential attack is taking place, it generates an attack signature that's effective to help the target mitigate the attack quickly. To achieve the above, after you enable Adaptive Protection on a security policy, traffic metrics and request metadata to a backend service (associated with the security policy) are continually recorded to learn baseline traffic characteristics.
    * Because Adaptive Protection needs to learn about the baseline traffic, Adaptive Protection might require up to one hour before generating rules to mitigate potential attacks.



## What's next

  * [Learn about common use cases for Adaptive Protection](https://docs.cloud.google.com/armor/docs/adaptive-protection-use-cases)
  * [Learn about the features in Cloud Armor Enterprise tiers](https://docs.cloud.google.com/armor/docs/armor-enterprise-overview)
  * [Learn how to enable Cloud Armor Enterprise](https://docs.cloud.google.com/armor/docs/armor-enterprise-using)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
