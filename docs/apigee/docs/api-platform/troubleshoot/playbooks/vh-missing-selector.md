---
url: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/vh-missing-selector/
title: Virtual host missing selector \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:00:58.607797+00:00
---

# Virtual host missing selector  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/vh-missing-selector/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Support ](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support)



Send feedback 

#  Virtual host missing selector Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_There is no equivalent[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/get-started) documentation for this topic._

**Note:** This document is applicable for Apigee hybrid users only. 

## Symptom

An `ApigeeIssue` with `Reason` `AIS_VIRTUALHOST_MISSING_SELECTOR` is shown when viewing resources in the `apigee` namespace. 

## Error messages

After running `kubectl -n apigee get apigeeissues`, an error like the following is displayed: 
    
    
    NAME                                           SEVERITY   REASON                             DOCUMENTATION                                                                                  AGE
    vhost-missing-selector-my-org-my-virtualhost   ERROR      AIS_VIRTUALHOST_MISSING_SELECTOR   https://cloud.google.com/apigee/docs/hybrid/troubleshooting/AIS_VIRTUALHOST_MISSING_SELECTOR   5h18m

## Cause: Virtualhost is missing ingress selector

A virtualhost declared in `overrides.yaml` does not have the ingress selector field set. 

### Diagnosis

Run the following command: 
    
    
    kubectl -n apigee describe apigeeissue ISSUE_NAME

Where ISSUE_NAME is the name of the issue. For example, `vhost-missing-selector-my-org-my-virtualhost`. 

The output should look similar to the following: 
    
    
    Name:         vhost-missing-selector-my-org-my-virtualhost
    Namespace:    apigee
    Labels:       ais-reason=AIS_VIRTUALHOST_MISSING_SELECTOR
    Annotations:  <none>
    API Version:  apigee.cloud.google.com/v1alpha1
    Kind:         ApigeeIssue
    Metadata:
      Creation Timestamp:  2023-06-12T17:03:43Z
      Generation:          1
      Owner References:
        API Version:     apigee.cloud.google.com/v1alpha2
        Kind:            ApigeeOrganization
        Name:            my-org
        UID:             7e83a52c-ce00-4bed-98be-55835ada1817
      Resource Version:  3281563
      UID:               adc775c2-376d-4bf9-9860-500b2b2b8273
    Spec:
      Details:        Expected ingress selector in ApigeeRouteConfig "my-org-my-virtualhost". Environment Group/virtual host "my-virtualhost" is missing an ingress selector.
      Documentation:  https://cloud.google.com/apigee/docs/hybrid/troubleshooting/AIS_VIRTUALHOST_MISSING_SELECTOR
      Reason:         AIS_VIRTUALHOST_MISSING_SELECTOR
      Severity:       WARNING
    Events:           <none>
    
    
    Spec:
      Details:        Expected ingress selector in ApigeeRouteConfig "my-org-my-virtualhost". Environment Group/virtual host "my-virtualhost" is missing an ingress selector.

The contents of `Spec.Details` explains the name of the virtualhost which is missing the ingress selector. 

### Resolution

  1. Use `kubectl describe` to check the details of the issue: 
         
         kubectl -n apigee describe apigeeissue ISSUE_NAME

Where ISSUE_NAME is the name of the issue. For example, `vhost-missing-selector-my-org-my-virtualhost`. 

  2. Determine the `virtualhost` name from the `Spec.Details` field. 

In this example, the virtualhost is called `my-virtualhost`. 

  3. Find the corresponding virtualhost in your `overrides.yaml`.
         
         virtualhosts:
         ...
         - name: my-virtualhost
           sslCertPath: ./certs/vhost.pem
           sslKeyPath: ./certs/vhost.key
         ...

  4. Update the virtualhost and add the ingress selector: 
         
         virtualhosts:
         ...
         - name: my-virtualhost
           selector:
             app: apigee-ingressgateway
           sslCertPath: ./certs/vhost.pem
           sslKeyPath: ./certs/vhost.key
         ...

  5. Apply the change to the virtualhost:
         
         helm upgrade ENV_GROUP_NAME apigee-virtualhost/ \
           --namespace apigee \
           --set envgroup=ENV_GROUP_NAME \
           -f overrides.yaml




## Must gather diagnostic information

If the problem persists even after following the above instructions, gather the following diagnostic information and then contact [Google Cloud Customer Care](https://cloud.google.com/support-hub/): 

  1. The Google Cloud Project ID.
  2. The name of the Apigee hybrid organization.
  3. The `Spec.Details` field of the `ApigeeIssue`.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
