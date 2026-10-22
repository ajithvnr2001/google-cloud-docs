---
url: https://docs.cloud.google.com/config-connector/docs/known-issues/
title: Known issues \u00a0|\u00a0 Config Connector \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:09:50.994820+00:00
---

# Known issues  |  Config Connector  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/config-connector/docs/known-issues/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Config Connector ](https://docs.cloud.google.com/config-connector/docs)
  * [ Guides ](https://docs.cloud.google.com/config-connector/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Known issues

This page lists known issues for Config Connector.

Many of the issues listed here have been fixed. The **Fixed version** column indicates the version in which the fix was introduced. To receive this fix, upgrade to the listed version or later.

If you're part of the Google Developer Program, save this page to receive notifications when a release note related to this page is published. To learn more, see [Saved Pages](https://developers.google.com/profile/help/saved-pages).

To filter the known issues by a product version or category, select your filters from the following drop-down menus.

Select your Config Connector version:

1.134.11.1341.131Kubernetes 1.19

Select your problem category:

InstallationNetworkingResourcesDirect Reconciler

Or, filter the known issues:

Category | Earliest identified version | Fixed version | Issue and workaround  
---|---|---|---  
Resources | 1.126.0 | [1.134.1](https://docs.cloud.google.com/config-connector/docs/release-notes#September_24_2025) | 

### Fixed: Resource creation blocked by webhook TLS error: "`x509: certificate signed by unknown authority`"

When attempting to create or apply new Config Connector resources, the Kubernetes API server rejects the request and blocks resource creation. You are unable to deploy new resources, but existing resources might continue to reconcile normally. This issue is caused by a known race condition within the `cnrm-webhook-manager` component in Config Connector versions earlier than 1.134.1. You might see an error similar to the following in your deployment outputs or API server logs:
    
    
    failed calling webhook "container-annotation-handler.cnrm.cloud.google.com": failed to call webhook: Post "https://cnrm-validating-webhook.cnrm-system.svc:443/...": tls: failed to verify certificate: x509: certificate signed by unknown authority
          

Additionally, the `cnrm-webhook-manager` Pod logs might display the following:
    
    
    http: TLS handshake error ... remote error: tls: bad certificate.
          

  
**Workaround:** To immediately unblock resource creation, you can force the webhook manager Pods to synchronize and pull the correct certificate data by restarting the deployment with the following command:
    
    
    kubectl rollout restart deployment cnrm-webhook-manager -n cnrm-system
            
  
Resources | 1.134 | 1.134.2 | 

### Fixed: SQLInstance stuck in Updating state with "merge" annotation error

Affected `SQLInstance` resources might become stuck in an `Updating` state with an error message regarding the `state-into-spec` annotation.
    
    
    invalid value "merge" for "cnrm.cloud.google.com/state-into-spec" annotation
          

This issue occurs because a stricter validation introduced in version 1.134.0 incorrectly rejected the "merge" strategy for `SQLInstance` resources, even when applied as a default. This is fixed in later versions.  
Direct Reconciler | 1.131 | 1.134 | 

### Fixed: Issues with direct reconcilers

Config Connector version 1.132.0 introduced issues affecting resources that use the direct reconciler.

#### Duplicate controller name error

In version 1.132.0, resources such as `SpannerInstance` and `SecretManagerSecret` might fail to reconcile with an error indicating that a controller with the same name already exists:
    
    
    error registering controller: error adding direct controller for SpannerInstance to a manager: error creating new controller: controller with name spannerinstance-controller already exists.
          

#### SecretManagerSecret "last-applied-configuration" error

If you enable the direct reconciler for a `SecretManagerSecret` (using the `alpha.cnrm.cloud.google.com/reconciler: direct` annotation) in versions 1.131.0 through 1.133, reconciliation might fail with an API error:
    
    
    [kubectl.kubernetes.io/last-applied-configuration] must follow pattern [a-z0-9A-Z]+([_\.\-]*[a-z0-9A-Z]+)*), be less than 64 characters, and must have a UTF encoding of less than 128 bytes
          

This occurs because Config Connector incorrectly attempts to pass internal Kubernetes annotations as labels to the Secret Manager API.  
Installation, Networking | Kubernetes 1.19 | 1.43 | 

### Fixed: Failed calling webhook x509: certificate relies on legacy Common Name field error

If you see an error similar to the following example, you might be experiencing an issue with certificates:
    
    
    Error from server (InternalError): error when creating "/mnt/set-weaver-dns-record.yml": Internal error occurred: failed calling webhook "annotation-defaulter.cnrm.cloud.google.com": Post "https://cnrm-validating-webhook.cnrm-system.svc:443/annotation-defaulter?timeout=30s": x509: certificate relies on legacy Common Name field, use SANs or temporarily enable Common Name matching with GODEBUG=x509ignoreCN=0
          

This issue occurs with Kubernetes versions 1.19 and later. Config Connector versions 1.43 and later support the automatic generation of the certificate, which should prevent this issue.   
**Workaround:** To workaround this issue, you can delete the relevant certificates and the Pods:
    
    
    kubectl delete -n cnrm-system secrets cnrm-webhook-cert-abandon-on-uninstall
    kubectl delete -n cnrm-system secrets cnrm-webhook-cert-cnrm-validating-webhook
    kubectl delete -n cnrm-system pods -l "cnrm.cloud.google.com/component=cnrm-webhook-manager"
          

After you have deleted these resources, the correct certificate should regenerate.  
  
Back to top

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
