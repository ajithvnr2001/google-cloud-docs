---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/automated-issue-surfacing/
title: Automated issue surfacing \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T09:16:39.278700+00:00
---

# Automated issue surfacing  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/automated-issue-surfacing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Automated issue surfacing Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.16 of the Apigee hybrid documentation. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.16 keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/automated-issue-surfacing.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/automated-issue-surfacing.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/automated-issue-surfacing.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/automated-issue-surfacing.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/automated-issue-surfacing.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/automated-issue-surfacing.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/automated-issue-surfacing.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/automated-issue-surfacing.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/automated-issue-surfacing.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/automated-issue-surfacing.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/automated-issue-surfacing.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/automated-issue-surfacing.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/automated-issue-surfacing.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/automated-issue-surfacing.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/automated-issue-surfacing.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/automated-issue-surfacing.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/automated-issue-surfacing.html)



## Overview

Automated issue surfacing (AIS) provides quick information about ongoing issues detected within your Hybrid cluster. This information includes links to documentation for troubleshooting and resolution. Automated issue surfacing only looks for known, common, system detectable issues and cannot detect all the issues within a cluster. 

Starting with Apigee hybrid v1.10, the Apigee runtime watcher component automatically scans the control plane and Kubernetes API server state to determine if there are any configuration issues. By default, the scanning happens every 60 seconds. You can change the interval or disable scanning if you prefer.

When AIS detects an issue, it creates a new instance of `ApigeeIssue` within the Kubernetes API server. These instances contain information about the issues and links to documentation on the specific issues.

When you resolve issues, they will automatically be deleted from the Kubernetes API server when the scanning determines they are no longer occurring.

## Using Automated issue surfacing.

Check for any existing issues with the `kubectl get apigeeissues` command: 
    
    
    kubectl -n APIGEE_NAMESPACE get apigeeissues

For example:
    
    
    kubectl -n APIGEE_NAMESPACE get apigeeissues
    
    NAME                                 SEVERITY    AGE URL
    **vhost-missing-eg-nonprod**             Error       1hr https://cloud.google.com/apigee/docs/hybrid/MISSING_ENV_GROUP
    **control-plane-connectivity-failure**   Error       1d  https://cloud.google.com/apigee/docs/hybrid/OLD_TLS_VERSION
    

For more detailed information about a specific issue, use the `kubectl describe` command with the issue name. The name must be preceded by `apigeeissues/` for example: `apigeeissues **vhost-missing-eg-nonprod**`.
    
    
    kubectl -n APIGEE_NAMESPACE describe apigeeissues **vhost-missing-eg-nonprod**
    
    Name:         vhost-missing-eg-nonprod
    Namespace:    apigee
    Labels:       
    Annotations:  
    API Version:  apigee.cloud.google.com/v1alpha1
    Kind:         ApigeeIssue
    Metadata:
      Creation Timestamp:  2022-08-25T20:41:56Z
      Managed Fields:
        API Version:  apigee.cloud.google.com/v3
      Resource Version:  12345678
      UID:               aaaaaaaa-bbbb-cccc-dddd-eeeeffffgggg
    Spec:
      Severity: Error
      Reason: MISSING_ENV_GROUP
      Details: Expected envgroup "nonprod" for ApigeeRouteConfig "my-org-nonprod"
      Documentation: https://cloud.google.com/apigee/docs/hybrid/MISSING_ENV_GROUP
      Ignore: false
      IgnoreReason:
    Events: 

## Changing the scan interval

By default, Watcher scans the control plane for issues once every 60 seconds. To change the scan interval, specify the new interval in seconds with the [`watcher.args.issueScanInterval`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#watcher-args-issuescaninterval) property in your overrides file. For example:
    
    
    watcher:
      args:
        issueScanInterval: **120**
    

Apply the configuration. 

Upgrade the `apigee-env` chart for each Apigee environment.
    
    
    helm upgrade $ORG_NAME apigee-org/ \
      --namespace APIGEE_NAMESPACE \
      -f OVERRIDES_FILE 
    

## Disabling automated issue surfacing

You can disable Automated issue surfacing by setting the [`watcher.args.enableIssueScanning`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#watcher-args-enableissuescanning) property to `false` in your overrides file. For example:
    
    
    watcher:
      args:
        enableIssueScanning: **false**
    

Apply the configuration. 

Upgrade the `apigee-env` chart for each Apigee environment.
    
    
    helm upgrade $ORG_NAME apigee-org/ \
      --namespace APIGEE_NAMESPACE \
      -f OVERRIDES_FILE 
    

## Related troubleshooting guides

Automated issue surfacing can provide links directly to the troubleshooting guides, including: 

  * [No network connectivity between runtime plane and control plane](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/no-network-connectivity)
  * [Virtual host missing environment group](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/vh-missing-env-group)
  * [Ingress cert mismatch](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/ingress-cert-mismatch)

See [Introduction to Apigee X and Apigee hybrid playbooks](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/introduction) for an overview and list of Apigee troubleshooting guides. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
