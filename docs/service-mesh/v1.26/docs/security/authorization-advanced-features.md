---
url: https://docs.cloud.google.com/service-mesh/v1.26/docs/security/authorization-advanced-features/
title: Configure authorization policy advanced features \u00a0|\u00a0 Cloud Service Mesh v1.26 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:39:50.219300+00:00
---

# Configure authorization policy advanced features  |  Cloud Service Mesh v1.26  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.26/docs/security/authorization-advanced-features/

You are viewing archived v1.26 Service Mesh documentation.

Available versions

[Cloud Service Mesh latest](https://docs.cloud.google.com/service-mesh/docs)  
[Cloud Service Mesh 1.28 archive](https://docs.cloud.google.com/service-mesh/v1.28/docs)  
[Cloud Service Mesh 1.27 archive](https://docs.cloud.google.com/service-mesh/v1.27/docs)  
[Cloud Service Mesh 1.26 archive](https://docs.cloud.google.com/service-mesh/v1.26/docs)  
[Cloud Service Mesh 1.25 archive](https://docs.cloud.google.com/service-mesh/v1.25/docs)  
[Cloud Service Mesh 1.24 archive](https://docs.cloud.google.com/service-mesh/v1.24/docs)  
[Cloud Service Mesh 1.23 archive](https://docs.cloud.google.com/service-mesh/v1.23/docs)  
[Cloud Service Mesh 1.22 archive](https://docs.cloud.google.com/service-mesh/v1.22/docs)  
[Cloud Service Mesh 1.21 archive](https://docs.cloud.google.com/service-mesh/v1.21/docs)  
[Cloud Service Mesh 1.20 archive](https://docs.cloud.google.com/service-mesh/v1.20/docs)  
[Anthos Service Mesh 1.19 archive](https://docs.cloud.google.com/service-mesh/v1.19/docs)  


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ v1.26 ](https://docs.cloud.google.com/service-mesh/v1.26/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.26/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure authorization policy advanced features

Cloud Service Mesh authorization policy provides mesh-, namespace-, and workload-level access control for your workloads in the mesh. This page describes details about configuring Cloud Service Mesh authorization policy advanced features, including _dry-run mode_ and _denial logging_. The features described on this page assume that you are familiar with the fundamental authorization policy concepts described in [Authorization policy overview](https://cloud.google.com/service-mesh/v1.26/docs/security/authorization-policy-overview).

## Dry-run mode

The Cloud Service Mesh authorization policy supports dry-run mode, which lets you to test an authorization policy with real production traffic without enforcing it. The dry-run mode allows you to better understand the effect of an authorization policy before enforcing it. This helps to reduce the risk of breaking the production traffic caused by an incorrect authorization policy.

You use the `"istio.io/dry-run": "true"` annotation in the authorization policy to change it to dry-run mode.

### Dry-run mode example

The following example, `deny-path-headers`, shows a policy with the `dry-run` annotation set to `"true`. The authorization policy denies requests to the path `headers` and allows all other requests.
    
    
    apiVersion: security.istio.io/v1beta1
    kind: AuthorizationPolicy
    metadata:
      name: deny-path-headers
      annotations:
        "istio.io/dry-run": "true"
    spec:
      selector:
        matchLabels:
          app: httpbin
      action: DENY
      rules:
      - to:
        - operation:
            paths: ["/headers"]
    

When you apply an authorization policy in dry-run mode, Cloud Service Mesh logs the enforcement result to [Cloud Logging](https://docs.cloud.google.com/service-mesh/v1.26/docs/observability/accessing-logs) but doesn't enforce the policy. The request is always allowed, and you can check Logs Explorer to decide whether or not the authorization policy is working as expected.

### Dry-run logging details

After applying an authorization policy in dry-run mode, you can see the results of the policy in Logs Explorer.

  1. Go to Logs Explorer. In the following URL, replace `PROJECT_ID` with your project ID:
         
         https://console.cloud.google.com/logs/query?project=PROJECT_ID
         

  2. In the **Query-builder** field, enter a query to find the dry-run mode authorization policy. In the following query, replace `NAMESPACE` with your namespace:
         
         logName="projects/PROJECT_ID/logs/server-accesslog-stackdriver" labels.destination_namespace="NAMESPACE" labels.dry_run_result="AuthzDenied"
         

  3. Click **Run query**.

  4. Adjust the time range as needed.




The following screenshot shows the dry-run labels in the traffic log in Logs Explorer after the example `deny-path-headers` policy was applied:

![image](https://docs.cloud.google.com/service-mesh/v1.26/docs/images/dry-run-log.png)

The dry-run mode supports `ALLOW` and `DENY` authorization policies, in addition to the [Istio dry-run results](https://istio.io/v1.26/docs/tasks/security/authorization/authz-dry-run/). Cloud Service Mesh stores the dry-run results to Cloud Logging in the following labels:

  * **dry_run_result** : The dry-run result is either "AuthzAllowed" or "AuthzDenied".
  * **dry_run_policy_name** : The namespace and name of the matched authorization policy making the dry-run decision.
  * **dry_run_policy_rule** : The index of the matched authorization policy rule making the dry-run decision.



The following table shows the details that are logged for an authorization policy in dry-run mode:

**Authorization policy applied in dry-run mode** | **Match result** | **Dry-run result** | Cloud Logging  
---|---|---|---  
Only `DENY` policy | Not Matched | allowed | **dry_run_result** : "AuthzAllowed"  
Matched | rejected | **dry_run_result** : "AuthzDenied"  
**dry_run_policy_name** : .  
**dry_run_policy_rule** :   
Only `ALLOW` policy | Not Matched | rejected | **dry_run_result** : "AuthzDenied"  
Matched | allowed | **dry_run_result** : "AuthzAllowed"  
**dry_run_policy_name** : .  
**dry_run_policy_rule** :   
Both `ALLOW` and `DENY` policy | Neither Matched | rejected | **dry_run_result** : "AuthzDenied"  
Only Matched `DENY` policy | rejected | **dry_run_result** : "AuthzDenied"  
**dry_run_policy_name** : .  
**dry_run_policy_rule** :   
Only Matched `ALLOW` policy | allowed | **dry_run_result** : "AuthzAllowed"  
**dry_run_policy_name** : .  
**dry_run_policy_rule** :   
Matched both policy | rejected | **dry_run_result** : "AuthzDenied"  
**dry_run_policy_name** : .  
**dry_run_policy_rule** :   
  
When you are confident about the dry-run result, you can disable dry-run mode using one of the following approaches:

  * Remove the dry-run annotation completely; or

  * Change the value of the dry-run annotation to `false`.




After you apply the policy with dry-run mode disabled, Cloud Service Mesh enforces the policy.

## Denial logging

The authorization policy denies a request if it is not allowed by the policy. For HTTP (including gRPC) protocols, the request is denied with status code 403\. For non-HTTP protocols, the connection is terminated directly. The Cloud Logging traffic log includes additional information which is useful to understand why traffic is being denied. For example, the log indicates how many requests are denied by the authorization policy, which can help you determine which policy rule caused the denial versus denials from the backend application.

In the following example, the `dry-run` annotation is set to `"false`. When you apply the `DENY` authorization policy, Cloud Service Mesh enforces it.
    
    
    apiVersion: security.istio.io/v1beta1
    kind: AuthorizationPolicy
    metadata:
      name: deny-path-headers
      annotations:
        "istio.io/dry-run": "false"
    spec:
      selector:
        matchLabels:
          app: httpbin
      action: DENY
      rules:
      - to:
        - operation:
            paths: ["/headers"]
    

After applying a`DENY` authorization policy, you can see the results of the policy in Logs Explorer.

  1. Go to Logs Explorer. In the following URL, replace `PROJECT_ID` with your project ID:
         
         https://console.cloud.google.com/logs/query?project=PROJECT_ID
         

  2. In the **Query-builder** field, enter a query to find the `DENY` authorization policy. In the following query, replace `NAMESPACE` with your namespace:
         
         logName="projects/PROJECT_ID/logs/server-accesslog-stackdriver" labels.destination_namespace="NAMESPACE" labels.response_details="AuthzDenied"
         

  3. Click **Run query**.

  4. Adjust the time range as needed.




The following screenshot shows a log entry in Logs Explorer after the example `deny-path-headers` policy was applied to enforce the policy. You can tell that the authorization policy was responsible for the 403 by looking at the labels:

![image](https://docs.cloud.google.com/service-mesh/v1.26/docs/images/denied-log.png)

The Logs Explorer traffic log includes the following labels for the authorization denial:

  * **response_details** : Is set to "AuthzDenied" if the denial is caused by an authorization policy.
  * **policy_name** : Contains the namespace and name of the authorization `DENY` policy causing the denial. The value is in the format of `<Namespace>.<Name>`, for example, `foo.deny-path-headers` means the authorization policy `deny-path-headers` in the `foo` namespace.
  * **policy_rule** : Contains the index of the rule inside the authorization policy causing the denial, for example, 0 means the first rule inside the policy.



## What's next?

For a list of all the authorization policies in the service mesh:
    
    
    kubectl get authorizationpolicy --all-namespaces
    

If there is an authorization policy in force, you can delete it with `kubectl delete`:
    
    
    kubectl delete authorizationpolicy -n NAMESPACE AUTH_POLICY_NAME
    

For more information about how to get the traffic log, see [Access logs](https://docs.cloud.google.com/service-mesh/v1.26/docs/observability/access-logs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
