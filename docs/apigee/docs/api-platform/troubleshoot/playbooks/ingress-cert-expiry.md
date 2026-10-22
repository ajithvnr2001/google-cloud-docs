---
url: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/ingress-cert-expiry/
title: Ingress cert expiry \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:26:22.474120+00:00
---

# Ingress cert expiry  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/ingress-cert-expiry/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Support ](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support)



Send feedback 

#  Ingress cert expiry Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_There is no equivalent[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/get-started) documentation for this topic._

**Note:** This document is applicable for Apigee hybrid users only. 

## Symptom

An `ApigeeIssue` with `Reason` `AIS_INGRESS_CERT_EXPIREY` is shown when viewing resources in the `apigee` namespace. 

## Error messages

After running `kubectl -n apigee get apigeeissues`, an error like the following is displayed: 
    
    
    NAME                                         SEVERITY   REASON                     DOCUMENTATION                                                                          AGE
    ingress-cert-expired-my-org-my-virtualhost   ERROR      AIS_INGRESS_CERT_EXPIREY   https://cloud.google.com/apigee/docs/hybrid/troubleshooting/AIS_INGRESS_CERT_EXPIREY   5h18m

## Possible causes

Cause | Description  
---|---  
Ingress certificate is expiring soon | The configured ingress certificate is expiring within 14 days.  
Ingress certificate is expired | The configured ingress certificate is expired.  
  
## Cause: Ingress certificate is expiring soon

The ingress certificate stored in the Kubernetes secret referenced by an `ApigeeRouteConfig` is expiring within the next 14 days. 

### Diagnosis

Run the following command: 
    
    
    kubectl -n apigee describe apigeeissue ISSUE_NAME

Where ISSUE_NAME is the name of the issue. For example, `ingress-cert-expiring-soon-my-org-my-virtualhost`. 

The output should look similar to the following: 
    
    
    Name:         ingress-cert-expiring-soon-my-org-my-virtualhost
    Namespace:    apigee
    Labels:       ais-reason=AIS_INGRESS_CERT_EXPIREY
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
      Details:        Ingress certificate in secret "my-org-my-virtualhost" for ApigeeRouteConfig "my-org-my-virtualhost" is expiring in 5.409373245s at 2024-03-11 19:04:12 +0000 UTC
      Documentation:  https://cloud.google.com/apigee/docs/hybrid/troubleshooting/AIS_INGRESS_CERT_EXPIREY
      Reason:         AIS_INGRESS_CERT_EXPIREY
      Severity:       WARNING
    Events:           <none>
    
    
    Spec:
      Details:        Ingress certificate in secret "my-org-my-virtualhost" for ApigeeRouteConfig "my-org-my-virtualhost" is expiring in 5.409373245s at 2024-03-11 19:04:12 +0000 UTC

The contents of `Spec.Details` explains the name of the `ApigeeRouteConfig` that refers to the Kubernetes secret containing the ingress certificate which is expiring soon. 

### Resolution

  1. Use `kubectl describe` to display the name of the `ApigeeRouteConfig` which has the ingress cert which is expiring soon: 
         
         kubectl -n apigee describe apigeeissue ISSUE_NAME

Where ISSUE_NAME is the name of the issue. For example, `ingress-cert-expiring-soon-my-org-my-virtualhost`. 

In this example, the `ApigeeRouteConfig` `my-org-my-virtualhost` is referencing the secret `my-org-my-virtualhost`. 

  2. Determine the `virtualhost` name from the `ApigeeRouteConfig`. 

The `ApigeeRouteConfig`'s name is in the format: `<Apigee organization>-<virtualhost name>`. 

In this example, `my-org` is the Apigee organization and the virtualhost name is `my-virtualhost`. 

  3. Find the corresponding virtualhost in your `overrides.yaml`.
         
         virtualhosts:
         ...
         - name: my-virtualhost
           selector:
             app: apigee-ingressgateway
           sslCertPath: ./certs/vhost.pem
           sslKeyPath: ./certs/vhost.key
         ...

  4. Update the certificate and key listed in the `sslCertPath` and `sslKeyPath` files. 

  5. Apply the changes to the virtualhost:
         
         helm upgrade ENV_GROUP_NAME apigee-virtualhost/ \
           --namespace apigee \
           --set envgroup=ENV_GROUP_NAME \
           -f overrides.yaml




## Cause: Ingress certificate is expired

The ingress certificate stored in the Kubernetes secret referenced by an `ApigeeRouteConfig` has expired. 

### Diagnosis

Run the following command: 
    
    
    kubectl -n apigee describe apigeeissue ISSUE_NAME

Where ISSUE_NAME is the name of the issue. For example, `ingress-cert-expired-my-org-my-virtualhost`. 

Something similar to the following is returned: 
    
    
    Name:         ingress-cert-expired-my-org-my-virtualhost
    Namespace:    apigee
    Labels:       ais-reason=AIS_INGRESS_CERT_EXPIREY
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
      Details:        Ingress certificate in secret "my-org-my-virtualhost" for ApigeeRouteConfig "my-org-my-virtualhost" expired at: 2024-03-11 19:12:10 +0000 UTC
      Documentation:  https://cloud.google.com/apigee/docs/hybrid/troubleshooting/AIS_INGRESS_CERT_EXPIREY
      Reason:         AIS_INGRESS_CERT_EXPIREY
      Severity:       ERROR
    Events:           <none>
    
    
    Spec:
      Details:        Ingress certificate in secret "my-org-my-virtualhost" for ApigeeRouteConfig "my-org-my-virtualhost" expired at: 2024-03-11 19:12:10 +0000 UTC

The contents of `Spec.Details` explains the name of the `ApigeeRouteConfig` that refers to the Kubernetes secret containing the ingress certificate which has expired. 

### Resolution

  1. Use `kubectl describe` to display the name of the `ApigeeRouteConfig` which has the expired ingress cert: 
         
         kubectl -n apigee describe apigeeissue ISSUE_NAME

Where ISSUE_NAME is the name of the issue. For example, `ingress-cert-expired-my-org-my-virtualhost`. 

In this example, the `ApigeeRouteConfig` `my-org-my-virtualhost` is referencing the secret `my-org-my-virtualhost`. 

  2. Determine the `virtualhost` name from the `ApigeeRouteConfig`. 

The `ApigeeRouteConfig`'s name is in the format: `<Apigee organization>-<virtualhost name>`. 

In this example, `my-org` is the Apigee organization and the virtualhost name is `my-virtualhost`. 

  3. Find the corresponding virtualhost in your `overrides.yaml`.
         
         virtualhosts:
         ...
         - name: my-virtualhost
           selector:
             app: apigee-ingressgateway
           sslCertPath: ./certs/vhost.pem
           sslKeyPath: ./certs/vhost.key
         ...

  4. Update the certificate and key listed in the `sslCertPath` and `sslKeyPath` files. 

  5. Apply the changes to the virtualhost:
         
         helm upgrade ENV_GROUP_NAME apigee-virtualhost/ \
           --namespace apigee \
           --set envgroup=ENV_GROUP_NAME \
           -f overrides.yaml




## Must gather diagnostic information

If the problem persists even after following the above instructions, gather the following diagnostic information and then contact [Google Cloud Customer Care](https://cloud.google.com/support-hub/): 

  1. The Google Cloud Project ID.
  2. The name of the Apigee hybrid organization.
  3. The `Spec.Details` field of the `ApigeeIssue`.
  4. (optional) Files referenced by `sslCertPath` and `sslKeyPath` for the affected virtualhost. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
