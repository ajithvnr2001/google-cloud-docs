---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/audit-policy/
title: Audit policy \u00a0|\u00a0 GKE security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:43:14.101537+00:00
---

# Audit policy  |  GKE security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/audit-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE security ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview)



Send feedback 

#  Audit policy Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document describes the audit logging policy in Google Kubernetes Engine (GKE). This document assumes that you know about the following:

  * [Audit logging in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/audit-logging)
  * [Auditing in Kubernetes](https://kubernetes.io/docs/tasks/debug/debug-cluster/audit/)



GKE captures and records events in your cluster, and several factors influence what information is logged, where that information is stored, and policies that influence what you view in your audit logs.

This document is for Security specialists who want to gain insight into activities occurring in your clusters so you can monitor for security threats, track changes, and troubleshoot issues. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

To learn how to enable and view the different types of audit logs, and to learn about the required IAM permissions, see [GKE audit logging information](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/audit-logging#enabling_audit_logging).

## Overview of audit policies

In a GKE cluster, the Kubernetes API server writes audit log entries to a backend that is managed by GKE. As GKE receives log entries from the Kubernetes API server, it writes them to your project's Admin Activity log and Data Access log.

There are two policies that influence what you see in your project's audit logs:

  * The Kubernetes audit policy defines rules for which events are recorded as log entries. It also specifies what data the log entries should include.

  * The GKE audit policy determines which entries are written to your Admin Activity log and which are written to your Data Access log.




The audit logs that are written to your Data Access log depend on your audit log configuration. Data Access logs use the [Google Cloud Observability pricing](https://cloud.google.com/stackdriver/pricing#google-clouds-operations-suite-pricing). Admin Activity logs are offered at no charge. GKE supports the following types of Data Access logs.

  * `ADMIN_READ`: operations that read metadata about Kubernetes resources, such as listing Pods.
  * `DATA_READ`: operations that read data in Kubernetes resources, such as reading the logs for a Pod.
  * `DATA_WRITE`: operations that write data to Kubernetes resources, such as updating Pod status.



For more information, see [Configure Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access).

## Kubernetes audit policy

The Kubernetes API server follows a policy that is specified in the `--audit-policy-file` flag of the [kube-apiserver](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-apiserver/) command.

When GKE starts the Kubernetes API server, it supplies an audit policy file by setting the value of the `--audit-policy-file` flag. In the open-source Kubernetes repository, you can see the [configure-helper.sh](https://github.com/kubernetes/kubernetes/blob/08ddda629e906633ffdba6ea4cd9ebf2cc21dd23/cluster/gce/gci/configure-helper.sh#L706) script, which generates the audit policy file. You can see most of the audit policy file by looking directly at the script.

### Events and stages

When a person or component makes a request to the Kubernetes API server, the request goes through one or more _stages_ :

Stage | Description | RequestReceived | The audit handler has received the request.  
---|---  
ResponseStarted | The response headers have been sent, but the response body has not been sent.  
ResponseComplete | The response body has been completed, and no more bytes will be sent.  
Panic | There was an internal server error, and the request did not complete..  
  
Each stage of a request generates an _event_ , which is processed according to a policy. The policy specifies whether the event should be recorded as a log entry and if so, what data should be included in the log entry.

## Audit levels

The Kubernetes audit policy file contains a list of rules. In the policy file, the first rule that matches an event sets the _audit level_ for the event.

A rule can specify one of these audit levels:

Level | Description | None | Do not create a log entry for the event.  
---|---  
Metadata | Create a log entry. Include metadata, but do not include the request body or the response body.  
Request | Create a log entry. Include metadata and the request body, but do not include the response body.  
RequestResponse | Create a log entry. Include metadata, the request body, and the response body.  
  
Here's an example of a rule. If an event matches the rule, the Kubernetes API server creates a log entry at the `Request` level.
    
    
    - level: Request
      userGroups: ["system:nodes"]
      verbs: ["update","patch"]
      resources:
        - group: "" # core
          resources: ["nodes/status", "pods/status"]
      omitStages:
        - "RequestReceived"
    

An event matches the rule if all of the following are true:

  * The event does not match any previous rule in the policy file.
  * The identity making the call is in the `system:nodes` user group.
  * The call is an `update` request or a `patch` request.
  * The request is on a `nodes/status` resource or a `pods/status` resource.
  * The event is not for the `RequestReceived` stage of the call.



## GKE audit policy

As GKE receives log entries from the Kubernetes API server, it applies its own policy to determine which entries get written to your project's Admin Activity log and which entries get written to your project's Data Access log.

For the most part, GKE applies the following rules to log entries that come from the Kubernetes API server:

  * Entries that represent `create`, `delete`, and `update` requests go to your Admin Activity log.

  * Entries that represent `get`, `list`, and `updateStatus` requests go to your Data Access log.




For information about pricing and which types of logs are enabled by default, see [Logging details](https://cloud.google.com/stackdriver/pricing#logging-costs).

## Kubernetes audit policy file for GKE clusters

For GKE clusters, the Kubernetes audit policy file starts with rules that specify that certain events should not be logged at all. For example, this rule says that any `get` request by `kubelet` on a `nodes` resource or a `nodes/status` resource should not be logged. Recall that a level of `None` means that any matching event should not be logged:
    
    
    - level: None
      users: ["kubelet"] # legacy kubelet identity
      verbs: ["get"]
      resources:
        - group: "" # core
        resources: ["nodes", "nodes/status"]
    

After the list of `level: None` rules, the policy file has a list of rules that are special cases. For example, here's a special-case rule says to log certain requests at the `Metadata` level:
    
    
    - level: Metadata
        resources:
          - group: "" # core
            resources: ["secrets", "configmaps"]
          - group: authentication.k8s.io
            resources: ["tokenreviews"]
        omitStages:
          - "RequestReceived"
    

An event matches the rule if all of the following are true:

  * The event does not match any previous rule in the policy file.
  * The request is on a resource of type `secrets`, `configmaps`, or `tokenreviews`.
  * The event is not for the `RequestReceived` stage of the call.



After the list of special-case rules, the policy file has some general rules. To see the general rules in the [script](https://github.com/kubernetes/kubernetes/blob/release-1.10/cluster/gce/gci/configure-helper.sh#L706), you have to substitute the value of `known_apis` for `${known_apis}`. After the substitution, you get a rule like this:
    
    
    - level: Request
      verbs: ["get", "list", "watch"]
      resources:
        - group: "" # core
        - group: "admissionregistration.k8s.io"
        - group: "apiextensions.k8s.io"
        - group: "apiregistration.k8s.io"
        - group: "apps"
        - group: "authentication.k8s.io"
        - group: "authorization.k8s.io"
        - group: "autoscaling"
        - group: "batch"
        - group: "certificates.k8s.io"
        - group: "extensions"
        - group: "metrics.k8s.io"
        - group: "networking.k8s.io"
        - group: "policy"
        - group: "rbac.authorization.k8s.io"
        - group: "settings.k8s.io"
        - group: "storage.k8s.io"
      omitStages:
        - "RequestReceived"
    

The rule applies to events that do not match any previous rule in the policy file and are not at the `RequestReceived` stage. The rule says that `get`, `list`, and `watch` requests on any resource that belongs to one of the listed groups should be logged at the `Request` level.

**Note:** The `get`, `list`, and `watch` requests don't actually have a request body, so in effect, the rule says to create log entries at the `Metadata` level.

The next rule in the policy file looks like this:
    
    
    - level: RequestResponse
      resources:
        - group: "" # core
        - group: "admissionregistration.k8s.io"
        - group: "apiextensions.k8s.io"
        - group: "apiregistration.k8s.io"
        - group: "apps"
        - group: "authentication.k8s.io"
        - group: "authorization.k8s.io"
        - group: "autoscaling"
        - group: "batch"
        - group: "certificates.k8s.io"
        - group: "extensions"
        - group: "metrics.k8s.io"
        - group: "networking.k8s.io"
        - group: "policy"
        - group: "rbac.authorization.k8s.io"
        - group: "settings.k8s.io"
        - group: "storage.k8s.io"
      omitStages:
        - "RequestReceived"
    

The rule applies to events that do not match any previous rule in the policy file and are not at the `RequestReceived` stage. In particular, the rule does not apply to the read requests: `get`, `list`, and `watch`. Instead, the rule applies to write requests like `create`, `update`, and `delete`. The rule says that write requests should be logged at the `RequestResponse` level.

## Summary of Kubernetes audit policy for GKE clusters

The following list summarizes the Kubernetes audit policy for GKE clusters:

  * In general, write requests like `create`, `update`, and `delete` are logged at the `RequestResponse` level.

  * In general, `get`, `list`, and `watch` events are logged at the `Metadata` level.

  * Some events are treated as special cases. For a definitive list of requests that are treated as special cases, see the policy [script](https://github.com/kubernetes/kubernetes/blob/release-1.10/cluster/gce/gci/configure-helper.sh#L706) Special cases include the following:

    * Update and patch requests by `kubelet`, `system:node-problem-detector`, or `system:serviceaccount:kube-system:node-problem-detector` on a `nodes/status` resource or a `pods/status` resource are logged at the Request level.

    * Update and patch requests by any identity in the `system:nodes` group on a `nodes/status` resource or a `pods/status` resource are logged at the Request level.

    * `deletecollection` requests by `system:serviceaccount:kube-system:namespace-controller` are logged at the Request level.

    * Requests on a `secrets` resource, a `configmaps` resource, or a `tokenreviews` resource are logged at the Metadata level.

  * Certain requests are not logged at all. For a definitive list of requests that are not logged, see the `level: None` rules in the policy [script](https://github.com/kubernetes/kubernetes/blob/release-1.10/cluster/gce/gci/configure-helper.sh#L706). The following requests are not logged:

    * Requests by `system:kube-proxy` to watch an `endpoints` resource, a `services` resource, or a `services/status` resource.

    * Get requests by `system:unsecured` on a `configmaps` resource in the `kube-system` namespace.

    * Get requests by `kubelet` on a `nodes` resource or a `nodes/status` resource.

    * Get requests by any identity in the `system:nodes` group on a `nodes` resource or a `nodes/status` resource.

    * Get and update requests by `system:kube-controller-manager`, `system:kube-scheduler`, or `system:serviceaccount:endpoint-controller` on an `endpoints` resource in the `kube-system` namespace.

    * Get requests by `system:apiserver` on a `namespaces` resource, a `namespaces/status` resource, or a `namespaces/finalize` resource.

    * Get and list requests by `system:kube-controller-manager` on any resource in the `metrics.k8s.io` group.

    * Requests to URLs that match `/healthz*`, `/version`, or `/swagger*`.




## What's next

  * [Kubernetes Auditing](https://kubernetes.io/docs/tasks/debug/debug-cluster/audit/)
  * [Accessing audit logs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/audit-logging)
  * [GKE Security overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview)
  * [Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
