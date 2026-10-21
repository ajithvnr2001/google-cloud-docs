---
url: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/ingressgateway/api-calls-fail-timeout-errors/
title: API calls fail with timeout errors \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:22:22.567201+00:00
---

# API calls fail with timeout errors  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/ingressgateway/api-calls-fail-timeout-errors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Support ](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support)



Send feedback 

#  API calls fail with timeout errors Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/troubleshoot/404-support-d) documentation._

**Note:** This document is applicable for Apigee hybrid users only. 

## Symptom

You may observe one of the following symptoms: 

  1. The client applications get timeout errors as a response for API calls on Apigee hybrid.
  2. You observe errors such as `Error from server (invalid)` or `The Job "apigee-resources-install" is invalid` while applying configuration (`overrides.yaml`) to the cluster during hybrid installation.



## Error messages

You may observe one of the following errors: 

### Error response to API calls

The API requests on Apigee hybrid may fail with the following error message:  

    
    
    * Connection failed
    * connect to 34.84.67.39 port 443 failed: Operation timed out
    * Failed to connect to example.apis.com port 443: Operation timed out
    * Closing connection 0
    curl: (7) Failed to connect to example.apis.com port 443: Operation timed out

### Errors observed while applying configuration (overrides.yaml) to clusters

You may observe one of the following errors while applying configuration (`overrides.yaml` file) to clusters during the installation: 

### Error #1
    
    
    helm upgrade operator apigee-operator/ \
      --install \
      --create-namespace \
      --namespace APIGEE_NAMESPACE \
      --atomic \
      -f OVERRIDES_FILE
    
    
    ...
    ...
    Error from server (Invalid): error when applying patch:
    to:
    Resource: "batch/v1, Resource=jobs", GroupVersionKind: "batch/v1, Kind=Job"
    Name: "istio-init-crd-10-1.4.6", Namespace: "istio-system"
    to:
    Resource: "batch/v1, Resource=jobs", GroupVersionKind: "batch/v1, Kind=Job"
    Name: "istio-init-crd-11-1.4.6", Namespace: "istio-system"
    to:
    Resource: "batch/v1, Resource=jobs", GroupVersionKind: "batch/v1, Kind=Job"
    Name: "istio-init-crd-14-1.4.6", Namespace: "istio-system"

### Error #2
    
    
    helm upgrade operator apigee-operator/ \
    --install \
    --create-namespace \
    --namespace APIGEE_NAMESPACE \
    --atomic \
    -f OVERRIDES_FILE
    
    
    ...
    ...
    The Job "apigee-resources-install" is invalid: spec.template: Invalid value:
    core.PodTemplateSpec{ObjectMeta:v1.ObjectMeta{Name:"apigee-resources-install",
    GenerateName:"", Namespace:"", SelfLink:"", UID:"", ResourceVersion:"",
    Generation:0,

## Possible causes

These errors can happen if the `istio-ingressgateway` service is in a `pending` state and unable to bind to an external IP address as shown below: 
    
    
    kubectl get services -n istio-system
    NAME                      TYPE         CLUSTER-IP   EXTERNAL-IP  PORT(S)             AGE
    istio-ingressgateway      LoadBalancer 10.198.5.104 **< pending>**    15020:31927/TCP,    12h
                                                                     80:31381/TCP,
                                                                     443:31391/TCP,
                                                                     31400:31401/TCP,
                                                                     15443:32623/TCP
    

The possible causes for the `istio-ingressgateway` service to be in a `pending` state are as follows: 

Cause | Description  
---|---  
Jobs in erroneous/pending state in istio-system namespace | The `incomplete/erroneous` jobs in the `istio-system` namespace could cause the `istio-ingressgateway` service to be in `pending` state forever and unable to bind to an external IP address.   
Incorrect IP address range assigned to external load balancer | An incorrect IP address range may be configured in the `istio-operator.yaml` file causing the `istio-ingressgateway` service to get into `pending` state forever and unable to bind to an external IP address during the installation.   
  
## Cause: Jobs in istio-system namespace in erroneous/pending state

### Diagnosis

  1. Check the status of the jobs in the `istio-system` namespace using the following command: 
         
         kubectl get jobs -n istio-system
         

  2. The status of the jobs must be `complete`. If the status of the jobs is in an `erroneous/pending` state, then that's the cause of this problem. 



### Resolution

  1. If any of the jobs are in the `pending` or `erroneous` state, delete them using the following command: 
         
         kubectl -n istio-system delete job JOB_NAME_FROM_STEP_1
         

  2. Re-run the installation by applying the `overrides.yaml` file: 

Update the `apigee-serving-cert` using [Helm](https://docs.cloud.google.com/apigee/docs/hybrid/latest/helm-reference):
         
         helm install operator apigee-operator/
         --namespace APIGEE_NAMESPACE \
         --atomic \
         -f OVERRIDES_FILE \
         --dry-run=server

Make sure to include all of the settings shown, including `--atomic` so that the action rolls back on failure.

Install the chart:
         
         helm upgrade operator apigee-operator/
         --namespace APIGEE_NAMESPACE \
         --atomic \
         -f OVERRIDES_FILE




## Cause: Incorrect IP address range assigned to external load balancer

### Diagnosis

  1. Check the IP address configured for the load balancer in the `istio- operator.yaml` file. For example, the following snippet shows the location in the `istio-operator.yaml` file where the IP address is configured: 
         
         -name: istio-ingressgateway
           enabled: true
           k8s:
             service:
               type: LoadBalancer
              loadBalancerIP: 10.195.24.23

  2. The `istio-ingressgateway` service is configured as a load balancer (indicated by type) in the `istio-operator.yaml` file. During the ASM installation, a load balancer is created with the configured IP address and wired to communicate with the `istio- ingressgateway` service. Therefore, the IP address configured should be correct and reserved for the load balancer. 
  3. Engage your network team and verify that the IP address configured for `loadBalancerIP` is correct. If it is incorrect, then the load balancer service will not be able to bind to the IP address. This causes the `istio-ingressgateway` service to be in the `pending` state forever. 



### Resolution

  1. Work with your network team and configure the correct IP address in the `istio- operator.yaml` file. 
  2. Re-run the installation for the [ Apigee ingress gateway](https://docs.cloud.google.com/apigee/docs/hybrid/latest/managing-ingress) and apply the `overrides.yaml` file: 
         
         helm upgrade $ORG_NAME apigee-org/ \
           --install \
           --namespace APIGEE_NAMESPACE \
           --atomic \
           -f OVERRIDES_FILE




## Must gather diagnostic information

If the problem persists even after following the above instructions, gather the following diagnostic information and then contact [Google Cloud Customer Care](https://cloud.google.com/support-hub/): 

  1. The Google Cloud Project ID
  2. The name of the Apigee hybrid organization
  3. Kubernetes Cluster name
  4. Google Cloud project name if kubernetes cluster resides in different Google Cloud project
  5. The `overrides.yaml` file
  6. The `Istio-operator .yaml` file used during the ASM installation.
  7. Collect the logs from each `istio-ingressgateway` pod in the `istio-system` namespace: 
         
         kubectl logs NAME_OF_ISTIO_INGRESSGATEWAY_POD -n istio-system > /tmp/NAME_OF_ISTIO_INGRESSGATEWAY_POD.log
         

  8. Collect the description of the each pod in the `istio-system` namespace: 
         
         kubectl describe pod NAME_OF_ISTIO_INGRESSGATEWAY_POD -n istio-system > /tmp/NAME_OF_ISTIO_INGRESSGATEWAY_POD.yaml
         

  9. Collect the list of services in the `istio-system` namespace: 
         
         kubectl get svc -n istio-system
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
