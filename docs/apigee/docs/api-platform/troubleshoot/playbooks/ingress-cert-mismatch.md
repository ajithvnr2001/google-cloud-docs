---
url: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/ingress-cert-mismatch/
title: Ingress cert mismatch \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:59:54.206786+00:00
---

# Ingress cert mismatch  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/ingress-cert-mismatch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Support ](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support)



Send feedback 

#  Ingress cert mismatch Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_There is no equivalent[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/get-started) documentation for this topic._

**Note:** This document is applicable for Apigee hybrid users only. 

## Symptom

An `ApigeeIssue` with `Reason` `AIS_INGRESS_CERT_MISMATCH` is shown when viewing resources in the `apigee` namespace. 

## Error messages

After running `kubectl -n apigee get apigeeissues`, the following error is displayed: 
    
    
    NAME                                          SEVERITY   REASON                      DOCUMENTATION                                                                           AGE
    ingress-cert-mismatch-my-org-my-virtualhost   ERROR      AIS_INGRESS_CERT_MISMATCH   https://cloud.google.com/apigee/docs/hybrid/troubleshooting/AIS_INGRESS_CERT_MISMATCH   5h18m

## Cause: Ingress cert mismatch

The private key and certificate stored in the Kubernetes secret referenced by an `ApigeeRouteConfig` do not match. 

### Diagnosis

Run the following command: 
    
    
    kubectl -n apigee describe apigeeissue ISSUE_NAME

Where ISSUE_NAME is the name of the issue. For example, `ingress-cert-mismatch-my-org-my-virtualhost`. 

Something similar to the following is returned: 
    
    
    Name:         ingress-cert-mismatch-my-org-my-virtualhost
    Namespace:    apigee
    Labels:       ais-reason=AIS_INGRESS_CERT_MISMATCH
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
      Details:        Ingress cert and private key in secret "my-org-my-virtualhost" for ApigeeRouteConfig "my-org-my-virtualhost" do not match
      Documentation:  https://cloud.google.com/apigee/docs/hybrid/troubleshooting/AIS_INGRESS_CERT_MISMATCH
      Reason:         AIS_INGRESS_CERT_MISMATCH
      Severity:       ERROR
    Events:           <none>
    
    
    Spec:
      Details:        Ingress cert and private key in secret "my-org-my-virtualhost" for ApigeeRouteConfig "my-org-my-virtualhost" do not match

The contents of `Spec.Details` explains the name of the `ApigeeRouteConfig` that refers to the Kubernetes secret containing the ingress certificate and private key. 

### Resolution

  1. Use `kubectl describe` to display the name of the `ApigeeRouteConfig` which has the mismatched ingress cert and key: 
         
         kubectl -n apigee describe apigeeissue ISSUE_NAME

Where ISSUE_NAME is the name of the issue. For example, `ingress-cert-mismatch-my-org-my-virtualhost`. 

In this example, the `ApigeeRouteConfig` `my-org-my-virtualhost` is referencing the secret `my-org-my-virtualhost`. 

  2. Determine the `virtualhost` name from the `ApigeeRouteConfig`. 

The `ApigeeRouteConfig`'s name is in the format: `<Apigee organization>-<virtualhost name>`. 

In this example, `my-org` is the Apigee organization and the virtualhost name is `my-virtualhost`. 

  3. Find the corresponding virtualhost in your `overrides.yaml` file:
         
         virtualhosts:
         ...
         - name: my-virtualhost
           selector:
             app: apigee-ingressgateway
           sslCertPath: ./certs/vhost.pem
           sslKeyPath: ./certs/vhost.key
         ...

  4. Validate that the certificate and key files being used match.

Using the `sslCertPath` and `sslKeyPath` from the previous step, validate the MD5 sums match using `openssl`: 
         
         openssl x509 -noout -modulus -in SSL_CERT_PATH | openssl md5
         
         openssl rsa -noout -modulus -in SSL_KEY_PATH | openssl md5

     * Where SSL_CERT_PATH is the `sslCertPath` from the previous step. For example, `./certs/vhost.pem`. 
     * Where SSL_KEY_PATH is the `sslKeyPath` from the previous step. For example, `./certs/vhost.key`. 

The output of the above two commands should match:
    
    openssl x509 -noout -modulus -in ./certs/vhost.pem | openssl md5
    MD5(stdin)= 40ba189dbe9d6fbfbdde1a8ef803d2d4
    
    openssl rsa -noout -modulus -in ./certs/vhost.key | openssl md5
    MD5(stdin)= 40ba189dbe9d6fbfbdde1a8ef803d2d4

  5. If the output from the previous commands did not match, use one of the following methods to correct the problem: 

     * Update the virtualhost's `sslCertPath` and `sslKeyPath` to point to the correct file paths. 
     * Fix the `sslCertPath` or `sslKeyPath` file contents to contain the correct matching certificate and key pair. 
  6. Apply the changes to the virtualhost using [Helm](https://docs.cloud.google.com/apigee/docs/hybrid/latest/helm-reference):
         
         helm upgrade ENV_GROUP_NAME apigee-virtualhost/ \
           --namespace APIGEE_NAMESPACE \
           --atomic \
           --set envgroup=ENV_GROUP_NAME \
           -f OVERRIDES_FILE

Make sure to include all of the settings shown, including `--atomic` so that the action rolls back on failure.




## Must gather diagnostic information

If the problem persists even after following the above instructions, gather the following diagnostic information and then contact [Google Cloud Customer Care](https://cloud.google.com/support-hub/): 

  1. The Google Cloud Project ID.
  2. The name of the Apigee hybrid organization.
  3. The `Spec.Details` field of the `ApigeeIssue`.
  4. (optional) Files referenced by `sslCertPath` and `sslKeyPath` for the affected virtualhost. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
