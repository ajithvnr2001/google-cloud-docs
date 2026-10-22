---
url: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/no-network-connectivity/
title: No network connectivity between runtime plane and control plane \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:00:04.399594+00:00
---

# No network connectivity between runtime plane and control plane  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/no-network-connectivity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Support ](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support)



Send feedback 

#  No network connectivity between runtime plane and control plane Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** This document is applicable for Apigee hybrid users only. 

## Symptoms

  * API products, Developers, Apps do not get populated on the Apigee UI.
  * API proxy deployments do not complete.
  * Management API requests executed for reading and writing API products, Developers, and Apps fail.



## Error messages

This section describes the possible error messages displayed when there is no network connectivity. 

### ApigeeIssue

If this issue was reported as an ApigeeIssue, when the following command is run: 
    
    
    kubectl -n APIGEE_NAMESPACE get apigeeissues

where APIGEE_NAMESPACE is the name for a grouping of Kubernetes resources. 

the following error code is displayed: 
    
    
    NAME                               SEVERITY    AGE URL
    control-plane-connectivity-failure Error       1hr https://cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/no-network-connectivity

### API products, Developers, and Apps Apigee UI pages

The API products, Developers, and Apps Apigee UI pages display the following error: 
    
    
    Error: no connections available from the Apigee connect agent(s):
    refer to documentation to triage further.

### apigee-synchronizer logs

The following error message can be seen on `apigee-synchronizer` logs: 
    
    
    {"level":"SEVERE","thread":"Apigee-Timer-3","mdc":{"action":"SYNC","env":"dev",
      "org":"example-hybrid-dev"},"className":"com.apigee.httpclient.adaptor.RequestAdaptor",
      "method":"doSend","severity":"SEVERE","message":"request failed
      [CONTEXT ratelimit_period\u003d\"1 MINUTES [skipped: 1]\" ]",
      "formattedDate":"2023-02-01T06:27:48.700Z","logger":"SERVICES.HTTPCLIENTSERVICE",
      "exceptionStackTrace":"java.net.SocketTimeoutException: connect timed out
    ... com.apigee.httpclient.adaptor.RequestAdaptor.send(RequestAdaptor.java:251)
    at com.apigee.hybrid.runtime.contract.sync.context.HttpContractDownloader.download(HttpContractDownloader.java:84)
    at com.apigee.hybrid.runtime.contract.sync.context.ControlPlaneReplicationContext.getContract(ControlPlaneReplicationContext.java:66)

### apigee-watcher logs

The following error message can be seen on `apigee-watcher` logs: 
    
    
    {"level":"error","ts":1675232549.5093117,"caller":"watcher/watcher.go:60",
    "msg":"error during watch","name":"mpstatus","error":"INTERNAL: error sending
      mp status to mgmt: INTERNAL: failed to send runtime status
      Post \"https://apigee.googleapis.com/v1/organizations/example-hybrid-dev/instances/apigee-hybrid-australia-southeast1:reportStatus\":
      dial tcp 172.217.24.42:443: i/o timeout","stacktrace":
      "edge-internal.git.corp.google.com/apigee-watcher.git/watcher.
      (*Watcher).Start.func1.1\n\t/go/src/edge-internal/apigee-watcher/watcher/watcher.go:60"}

## Possible Causes

Platform | Cause | Description  
---|---|---  
All |  No network route available to the internet | If no network route is available to the internet, the Apigee runtime plane components will not be able to communicate with Apigee control plane APIs.   
All |  Apigee API endpoints are not allow-listed | If there is a firewall in place, Apigee API endpoints may have not been allow-listed.   
GKE |  Private Google Access is not enabled | If the deployment is on GKE, Private Google Access may have not been enabled in the subnet.   
All |  Unknown network failure |  If there is an unknown failure in the cluster network on connecting to the internet, this issue could occur.   
  
### Cause: No network route available to the internet

#### Diagnosis

  1. Depending on the platform used, verify whether there is a network route available from the cluster network to the internet. For example, for more information on networking on GKE, see [ Network overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-overview). 
  2. Check with your infrastructure and networking team to see if the cluster network uses a forward proxy server for connecting to the internet. 



#### Resolution

  1. Check with the network administrator and add a network route to the internet if possible. 
  2. If there is a forward proxy server used for communicating between the cluster network and internet, [ configure forward proxy server settings](https://docs.cloud.google.com/apigee/docs/hybrid/latest/config-prop-ref#httpproxy) in Apigee using the `overrides.yaml` file and apply that change to the runtime plane using the [Helm command](https://docs.cloud.google.com/apigee/docs/hybrid/latest/helm-reference): 

Dry run:
         
         helm upgrade ENV_GROUP_RELEASE_NAME apigee-virtualhost/ \
         --namespace APIGEE_NAMESPACE \
         --atomic \
         --set envgroup=ENV_GROUP \
         -f OVERRIDES_FILE \
         --dry-run=server
         

Make sure to include all of the settings shown, including `--atomic` so that the action rolls back on failure.

Your installation may or may not have been set up using an ENV_GROUP_RELEASE_NAME that differs from ENV_GROUP. For information on the settings, see [Install Apigee hybrid using Helm](https://docs.cloud.google.com/apigee/docs/hybrid/latest/install-helm-charts).

Install the chart:
         
         helm upgrade ENV_GROUP_RELEASE_NAME apigee-virtualhost/ \
         --namespace APIGEE_NAMESPACE \
         --atomic \
         --set envgroup=ENV_GROUP \
         -f OVERRIDES_FILE
         




### Cause: Apigee API endpoints are not allow-listed

#### Diagnosis

Check with the network administrator and verify whether [ the list of Apigee API endpoints](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/how-to/firewall-rules) are allow-listed in the firewall on the platform where Apigee is installed. For GKE, this could be [ Cloud Next Generation Firewall](https://console.cloud.google.com/networking/firewalls/list). 

#### Resolution

If the above list of Apigee API endpoints are not allow-listed, contact the network administrator and complete that requirement. 

### Cause: Private Google Access is not enabled

#### Diagnosis

  1. If Apigee is deployed on a [ private GKE cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/private-clusters) that does not have access to the internet, [ Private Google Access](https://cloud.google.com/vpc/docs/private-google-access) needs to be enabled to allow the Apigee runtime plane components access to Google APIs internally. 
  2. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  3. Click the name of a network. 
  4. On the **Subnets** tab, In the **Private Google Access** column, verify that the relevant subnet is enabled. If it is not, that's the reason for this failure. 



#### Resolution

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Click the name of a network.
  3. Click the name of a subnet.
  4. Click edit **Edit**.
  5. Select **Private Google Access On**.
  6. Click **Save**. Once enabled, this issue will be resolved.



### Cause: Unknown network failure

#### Diagnosis

Contact your network administrator and verify whether there are any unknown failures in the cluster network. 

#### Resolution

Work with your network administrator and resolve the issues in the cluster network. Once the network issues are fixed this problem will get resolved. 

## Must gather diagnostic information

If the problem persists even after following the above instructions, gather the following diagnostic information and then contact [Google Cloud Customer Care](https://cloud.google.com/support-hub/): 

  1. The Google Cloud Project ID.
  2. The name of the Apigee hybrid organization.
  3. The outputs of the following commands executed on all Kubernetes cluster nodes: 
         
         ping apigee.googleapis.com
         
         traceroute apigee.googleapis.com
         
         telnet apigee.googleapis.com 443

  4. The `overrides.yaml` file, masking any sensitive information.
  5. The Kubernetes pod status in all namespaces: 
         
         kubectl get pods -A > kubectl-pod-status`date +%Y.%m.%d_%H.%M.%S`.txt

  6. The Kubernetes cluster-info dump: 

Generate Kubernetes cluster-info dump:
         
         kubectl cluster-info dump -A --output-directory=/tmp/kubectl-cluster-info-dump

Zip Kubernetes cluster-info dump:
         
         zip -r kubectl-cluster-info-dump`date +%Y.%m.%d_%H.%M.%S`.zip /tmp/kubectl-cluster-info-dump/*




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
