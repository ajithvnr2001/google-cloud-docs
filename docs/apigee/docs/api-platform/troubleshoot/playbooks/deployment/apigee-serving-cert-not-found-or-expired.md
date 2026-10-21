---
url: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/deployment/apigee-serving-cert-not-found-or-expired/
title: API proxy deployments fail with apigee-serving-cert is not found or expired \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:22:22.917398+00:00
---

# API proxy deployments fail with apigee-serving-cert is not found or expired  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/deployment/apigee-serving-cert-not-found-or-expired/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Support ](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support)



Send feedback 

#  API proxy deployments fail with apigee-serving-cert is not found or expired Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/troubleshoot/support-d) documentation._

**Note:** This document is applicable for Apigee hybrid users only. 

## Symptoms

API proxy deployments fail with the following error messages. 

## Error Messages

If the TLS certificate of the `apigee-webhook-service.apigee-system.svc` service has expired or is not yet valid, the following error message will be shown on `apigee-watcher` logs: 
    
    
    {"level":"error","ts":1687991930.7745812,"caller":"watcher/watcher.go:60",
    "msg":"error during watch","name":"ingress","error":"INTERNAL: INTERNAL: failed
    to update ApigeeRoute [org-env]-group-84a6bb5, namespace apigee:
    **Internal error occurred: failed calling webhook**
    \"mapigeeroute.apigee.cloud.google.com\": Post
    \"https://apigee-webhook-service.apigee-system.svc:443/mutate-apigee-cloud-google-com-v1alpha1-apigeeroute?timeout=30s\":
    x509:
    **certificate has expired or is not yet valid:** current time
    2023-06-28T22:38:50Z is after 2023-06-17T17:14:13Z, INTERNAL: failed to update
    ApigeeRoute [org-env]-group-e7b3ff6, namespace apigee 

## Possible Causes

Cause | Description  
---|---  
The apigee-serving-cert is not found | If the `apigee-serving-cert` is not found in the `apigee-system` namespace, this issue could occur.  
Duplicate certificate requests were created for renewing `apigee-serving-cert` |  If there are duplicate certificate requests created for renewing the `apigee-serving-cert` certificate, the `apigee-serving-cert` certificate may not get renewed.   
cert-manager is not healthy |  If `cert-manager` is not healthy, the `apigee-serving-cert` certificate may not get renewed.   
  
### Cause: The apigee-serving-cert is not found

#### Diagnosis

  1. Check the availability of the `apigee-serving-cert` certificate in the `apigee-system` namespace: 
         
         kubectl -n apigee-system get certificates apigee-serving-cert
         

If this certificate is available, an output similar to following should be seen: 
         
         NAME                  READY   SECRET                AGE
         apigee-serving-cert   True    webhook-server-cert   2d10h

  2. If the apigee-serving-cert certificate is not found in the `apigee-system` namespace, that could be the reason for this issue. 



#### Resolution

  1. Update the `apigee-serving-cert` using [Helm](https://docs.cloud.google.com/apigee/docs/hybrid/latest/helm-reference): 
         
         helm upgrade ENV_NAME apigee-env/ \
           --namespace APIGEE_NAMESPACE \
           --set env=ENV_NAME \
           --atomic \
           -f OVERRIDES_FILE

Make sure to include all of the settings shown, including `--atomic` so that the action rolls back on failure.

  2. Verify that the `apigee-serving-cert` certificate has been created: 
         
         kubectl -n apigee-system get certificates apigee-serving-cert




### Cause: Duplicate certificate requests were created for renewing apigee-serving-cert

#### Diagnosis

  1. Check `cert-manager` controller logs and see whether an error message similar to the following has been returned. 

List all `cert-manager` pods:
         
         kubectl -n cert-manager get pods

An example output:
         
         NAME                                       READY   STATUS    RESTARTS        AGE
         cert-manager-66d9545484-772cr              1/1     Running   0               6d19h
         cert-manager-cainjector-7d8b6bd6fb-fpz6r   1/1     Running   0               6d19h
         cert-manager-webhook-669b96dcfd-6mnm2      1/1     Running   0               6d19h

Check `cert-manager` controller logs:
         
         kubectl -n cert-manager logs cert-manager-66d9545484-772cr | grep "issuance is skipped until there are no more duplicates"

Example outputs:
         
         1 controller.go:163] cert-manager/certificates-readiness "msg"="re-queuing item due to error processing" "error"="multiple CertificateRequests were found for the 'next' revision 3, issuance is skipped until there are no more duplicates" "key"="apigee-system/apigee-serving-cert"
         
         1 controller.go:167] cert-manager/certificates-readiness "msg"="re-queuing item due to error processing" "error"="multiple CertificateRequests were found for the 'next' revision 683, issuance is skipped until there are no more duplicates" "key"="apigee/apigee-istiod"

If you see either of the messages shown above, the `apigee-serving-cert` and the `apigee-istiod-cert` certificates will not be renewed. 

  2. List all certificate requests in the `apigee-system` namespace or the `apigee` namespace depending on the namespace printed in the log entries above and check to see if there are multiple certificate requests created for renewing the same `apigee-serving-cert` or `apigee-istiod-cert` certificate revisions: 
         
         kubectl -n apigee-system get certificaterequests




See the `cert-manager` issue relevant to this problem at [ cert-manager created multiple CertificateRequest objects with the same certificate-revision](https://github.com/cert-manager/cert-manager/issues/4956). 

#### Resolution

**Note:** Execute the following commands for the `apigee` or `apigee-system` namespace depending on the namespace where the duplicate certificate requests were found. 

  1. Delete all certificate requests in `apigee-system` namespace: 
         
         kubectl -n apigee-system delete certificaterequests --all

  2. Verify that duplicated certificate requests have been deleted and only one certificate request is available for the `apigee-serving-cert` certificate in `apigee-system` namespace: 
         
         kubectl -n apigee-system get certificaterequests

  3. Verify that the `apigee-serving-cert` certificate has been renewed: 
         
         kubectl -n apigee-system get certificates apigee-serving-cert -o yaml

An example output:
         
         apiVersion: cert-manager.io/v1
         kind: Certificate
         metadata:
           creationTimestamp: "2023-06-26T13:25:10Z"
           generation: 1
           name: apigee-serving-cert
           namespace: apigee-system
           resourceVersion: "11053"
           uid: e7718341-b3ca-4c93-a6d4-30cf70a33e2b
         spec:
           dnsNames:
           - apigee-webhook-service.apigee-system.svc
           - apigee-webhook-service.apigee-system.svc.cluster.local
           issuerRef:
             kind: Issuer
             name: apigee-selfsigned-issuer
           secretName: webhook-server-cert
         status:
           conditions:
           - lastTransitionTime: "2023-06-26T13:25:11Z"
             message: Certificate is up to date and has not expired
             observedGeneration: 1
             reason: Ready
             status: "True"
             type: Ready
           **notAfter : "2023-09-24T13:25:11Z"**
           **notBefore : "2023-06-26T13:25:11Z"**
           renewalTime: "2023-08-25T13:25:11Z"
           revision: 1




### Cause: cert-manager is not healthy

#### Diagnosis

  1. Check the health of the `cert-manager` pods in the `cert-manager` namespace: 
         
         kubectl -n cert-manager get pods

If `cert-manager` pods are healthy, all `cert-manager` pods should be ready `(1/1)` and in `Running` state, otherwise, that could be the reason for this issue: 
         
         NAME                                       READY   STATUS    RESTARTS   AGE
         cert-manager-59cf78f685-mlkvx              1/1     Running   0          15d
         cert-manager-cainjector-78cc865768-krjcp   1/1     Running   0          15d
         cert-manager-webhook-77c4fb46b6-7g9g6      1/1     Running   0          15d

  2. The `cert-manager` can fail for many reasons. Check the `cert-manager` logs and identify the reason for the failure and resolve them accordingly. 

One known reason is that the `cert-manager` will fail if it cannot communicate with the Kubernetes API. In this case, an error message similar to following is displayed:: 
         
         E0601 00:10:27.841516       1 leaderelection.go:330] error retrieving
         resource lock kube-system/cert-manager-controller: Get
         "https://192.168.0.1:443/api/v1/namespaces/kube-system/configmaps/cert-manager-controller":
         dial tcp 192.168.0.1:443: i/o timeout




#### Resolution

  1. Check the health of the Kubernetes cluster and fix any issues found. See [ Troubleshooting Clusters](https://kubernetes.io/docs/tasks/debug/debug-cluster/). 
  2. Refer to [ Troubleshooting](https://cert-manager.io/docs/troubleshooting) for additional `cert-manager` troubleshooting information. 



## Must gather diagnostic information

If the problem persists even after following the above instructions, gather the following diagnostic information, and then contact [Google Cloud Customer Care](https://cloud.google.com/support-hub/). 

  1. Google Cloud Project ID
  2. Apigee hybrid organization
  3. Apigee hybrid `overrides.yaml` file, masking any sensitive information. 
  4. Kubernetes pod status in all namespaces: 
         
         kubectl get pods -A > kubectl-pod-status`date +%Y.%m.%d_%H.%M.%S`.txt

  5. Kubernetes `cluster-info` dump: 
         
         # generate kubernetes cluster-info dump
         kubectl cluster-info dump -A --output-directory=/tmp/kubectl-cluster-info-dump
         # zip kubernetes cluster-info dump
         zip -r kubectl-cluster-info-dump`date +%Y.%m.%d_%H.%M.%S`.zip /tmp/kubectl-cluster-info-dump/*




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
