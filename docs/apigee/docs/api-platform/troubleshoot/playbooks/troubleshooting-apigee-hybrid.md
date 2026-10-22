---
url: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/troubleshooting-apigee-hybrid/
title: Troubleshooting Apigee hybrid stuck in creating or releasing state \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:27:43.462328+00:00
---

# Troubleshooting Apigee hybrid stuck in creating or releasing state  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/troubleshooting-apigee-hybrid/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Support ](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support)



Send feedback 

#  Troubleshooting Apigee hybrid stuck in creating or releasing state Stay organized with collections  Save and categorize content based on your preferences. 

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

**Note:** This document is applicable for Apigee hybrid users only. 

This document describes how to reset Apigee hybrid components when they are stuck in a `creating` or `releasing` state. 

Run the following command to list the Apigee hybrid installation main components: 
    
    
    kubectl get crd | grep apigee
    
    
    
    apigeeorganization (apigeeorganizations.apigee.cloud.google.com)
    apigeeenvironment (apigeeenvironments.apigee.cloud.google.com)
    apigeedatastore (apigeedatastores.apigee.cloud.google.com)
    apigeetelemetries (apigeetelemetries.apigee.cloud.google.com)
    apigeeredis (apigeeredis.apigee.cloud.google.com)

Run the following command to display the current state:
    
    
    kubectl get apigeedatastore -n NAMESPACE
    

When fully functional, each of these components will be in a `running` state. For example: 
    
    
    NAME      STATE     AGE
    default   running   5d6h

If the installation is not successful, components may be stuck in a `creating` (or `releasing`) state. For example: 
    
    
    NAME      STATE     AGE
    default   creating   5d6h

## Identify the problem

To identify the cause for the issue, begin by describing each component. The components are structured as follows: 

Each `ApigeeOrganization` custom resource is represented by the following hierarchy: 
    
    
    **ApigeeOrganization/HASHED_VALUE
    ├─ApigeeDeployment/apigee-connect-agent-HASHED_VALUE**
    │ ├─HorizontalPodAutoscaler/apigee-connect-agent-HASHED_VALUE-VER-xxxx
    │ ├─PodDisruptionBudget/apigee-connect-agent-HASHED_VALUE
    **│ ├─ReplicaSet/apigee-connect-agent-HASHED_VALUE-VER-xxxx
    │ │ └─Pod/apigee-connect-agent-HASHED_VALUE-VER-xxxx
    ├─ApigeeDeployment/apigee-mart-HASHED_VALUE**
    │ ├─HorizontalPodAutoscaler/apigee-mart-HASHED_VALUE-VER-xxxx
    │ ├─PodDisruptionBudget/apigee-mart-HASHED_VALUE
    **│ ├─ReplicaSet/apigee-mart-HASHED_VALUE-VER-xxxx
    │ │ └─Pod/apigee-mart-HASHED_VALUE-VER-xxxx
    ├─ApigeeDeployment/apigee-watcher-HASHED_VALUE**
    │ ├─HorizontalPodAutoscaler/apigee-watcher-HASHED_VALUE-VER-xxxx
    │ ├─PodDisruptionBudget/apigee-watcher-HASHED_VALUE
    **│ ├─ReplicaSet/apigee-watcher-HASHED_VALUE-VER-xxxx
    │ │ └─Pod/apigee-watcher-HASHED_VALUE-VER-xxxx**
    

Each `ApigeeEnvironment` custom resource is represented by the following hierarchy: 
    
    
    **ApigeeEnvironment/HASHED_VALUE
    ├─ApigeeDeployment/apigee-runtime-HASHED_VALUE**
    │ ├─HorizontalPodAutoscaler/apigee-runtime-HASHED_VALUE-VER-xxxx
    │ ├─PodDisruptionBudget/apigee-runtime-HASHED_VALUE
    **│ ├─ReplicaSet/apigee-runtime-HASHED_VALUE-VER-xxxx
    │ │ └─Pod/apigee-runtime-HASHED_VALUE-VER-xxxx
    ├─ApigeeDeployment/apigee-synchronizer-HASHED_VALUE**
    │ ├─HorizontalPodAutoscaler/apigee-synchronizer-HASHED_VALUE-VER-xxxx
    │ ├─PodDisruptionBudget/apigee-synchronizer-HASHED_VALUE
    **│ ├─ReplicaSet/apigee-synchronizer-HASHED_VALUE-VER-xxxx
    │ │ └─Pod/apigee-synchronizer-HASHED_VALUE-VER-xxxx
    ├─ApigeeDeployment/apigee-udca-HASHED_VALUE**
    │ ├─HorizontalPodAutoscaler/apigee-udca-HASHED_VALUE-VER-xxxx
    │ ├─PodDisruptionBudget/apigee-udca-HASHED_VALUE
    **│ ├─ReplicaSet/apigee-udca-HASHED_VALUE-VER-xxxx
    │ │ └─Pod/apigee-udca-HASHED_VALUE-VER-xxxx**
    

Begin problem identification by describing the root component. For example:
    
    
    kubectl describe apigeeorganization -n NAMESPACE COMPONENT_NAME
    

Check to see if the `State` of the component is `running`:
    
    
          Replicas:
            Available:  1
            Ready:      1
            Total:      1
            Updated:    1
          **State:        running
      State:            running**
    Events:             <none>
    

If there are no events logged at this level, repeat the process with `apigeedeployments` followed by `ReplicaSet`. For example: 
    
    
    kubectl get apigeedeployment -n NAMESPACE AD_NAME>
    

If `apigeedeployments` and `ReplicaSet` do not show any errors, focus on the pods that are not ready: 
    
    
    kubectl get pods -n NAMESPACE
    
    
    
    NAME                                                              READY   STATUS
    apigee-cassandra-default-0                                        1/1     Running
    apigee-connect-agent-apigee-b56a362-150rc2-42gax-dbrrn            1/1     Running
    apigee-logger-apigee-telemetry-s48kb                              1/1     Running
    apigee-mart-apigee-b56a362-150rc2-bcizm-7jv6w                     **0**/2     Running
    apigee-runtime-apigee-test-0d59273-150rc2-a5mov-dfb29             **0**/1     Running
    

In this example, `mart` and `runtime` are not ready. Inspect the pod logs to determine errors:
    
    
    kubectl logs -n NAMESPACE POD_NAME
    

### Deleting components

If you've made a mistake with any of these components, delete the component and recreate the environment using [Helm](https://docs.cloud.google.com/apigee/docs/hybrid/latest/helm-reference): 
    
    
    kubectl delete -n apigee apigeeenv HASHED_ENV_NAME
    

Follow this up with creating the environment (after making the necessary corrections): 
    
    
    helm upgrade ENV_NAME apigee-env/ \
    --install \
    --namespace APIGEE_NAMESPACE \
    --set env=ENV_NAME \
    --atomic \
    -f OVERRIDES_FILE \
    --dry-run=server

Make sure to include all of the settings shown, including `--atomic` so that the action rolls back on failure.

Install the chart:
    
    
    helm upgrade ENV_NAME apigee-env/ \
      --install \
      --namespace APIGEE_NAMESPACE \
      --set env=ENV_NAME \
      --atomic \
      -f OVERRIDES_FILE

## Inspect the controller

If there are no obvious error messages in the pod, but the component has not transitioned to the `running` state, inspect the `apigee-controller` for error messages. 
    
    
    kubectl logs -n NAMESPACE $(k get pods -n NAMESPACE | sed -n '2p' | awk '{print $1}') | grep -i error
    

This allows the user to see why the controller was unable to process the request (of `create`/`delete`/`update`, etc.). 

## Apigee datastore

Apache Cassandra is implemented as a `StatefulSet`. Each Cassandra instance contains: 
    
    
    **ApigeeDatastore/default**
    ├─Certificate/apigee-cassandra-default
    │ └─CertificateRequest/apigee-cassandra-default-wnd7s
    ├─Secret/config-cassandra-default
    ├─Service/apigee-cassandra-default
    │ ├─EndpointSlice/apigee-cassandra-default-7m9kx
    │ └─EndpointSlice/apigee-cassandra-default-gzqpr
    **└─StatefulSet/apigee-cassandra-default**
      ├─ControllerRevision/apigee-cassandra-default-6976b77bd
      ├─ControllerRevision/apigee-cassandra-default-7fc76588cb
      **└─Pod/apigee-cassandra-default-0**
      

This example shows one pod; however, typical production installs contain three or more pods. 

If the state for Cassandra is `creating` or `releasing`, the state MUST be reset. Certain problems (like Cassandra password changes) and problems not related to networking may require that you delete components. It is quite possible that in such cases, you cannot delete the instance (i.e., `kubectl delete apigeedatastore -n NAMESPACE default`). Using `--force` or `--grace-period=0` also does not help. 

The objective of `reset` is to change the state of the component (`apigeedatastore`) from `creating` or `releasing` back to `running`. Changing the state in this way typically **will not** solve the underlying problem. In most cases, the component should be deleted after a reset. 

**Warning:** Deleting the `apigeedatastore` also deletes the persistent volumes. All data in Cassandra will be lost. It is recommended that you back up the Cassandra data. 

  1. Attempt a delete (this won't be successful):
         
         kubectl delete -n NAMESPACE apigeedatastore default
         

It is common for this command to not complete. Use `Ctrl+C` and terminate the call. 

  2. Reset the state:

On Window 1:
         
         kubectl proxy
         

On Window 2:
         
         curl -X PATCH -H "Accept: application/json" -H "Content-Type: application/json-patch+json" --data '[{"op": "replace", "path": "/status/nestedState", "value": ""},{"op": "replace", "path": "/status/state", "value": "running"}]' 'http://127.0.0.1:8001/apis/apigee.cloud.google.com/v1alpha1/namespaces/apigee/apigeedatastores/default/status'
         

Remove the finalizer (Window 2):
         
         kubectl edit -n NAMESPACE apigeedatastore default
         

Look for the following two lines and delete them:
         
         finalizers:
         - apigeedatastore.apigee.cloud.google.com




## Common error scenarios

### Proxy configuration not available with runtime

This error can manifest in one of two ways: 

  * The `runtime` is not in the `ready` state.
  * The `runtime` has not received the latest version of the API.


  1. Start with the `synchronizer` pods.

Inspect the logs for the `synchronizer`. Common errors are as follows:

     * Lack of network connectivity (to `*.googleapi.com`)
     * Incorrect IAM access (service account not available or not provided by the Synchronizer Manager permission)
     * The [ setSyncAuthorization](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations/setSyncAuthorization) API was not invoked
  2. Inspect the `runtime` pods.

Inspecting the logs from the `runtime` pods will show why the `runtime` did not load the configuration. The control plane attempts to prevent most configuration mistakes from even going to the data plane. In cases where a validation is either impossible or not correctly implemented, the `runtime` will fail to load it.




### "No runtime pods" in the control plane

  1. Start with the `synchronizer` pods.

Inspect the logs for the `synchronizer`. Common errors are as follows:

     * Lack of network connectivity (to `*.googleapi.com`)
     * Incorrect IAM access (service account not available or not provided by the Synchronizer Manager permission)
     * The [ setSyncAuthorization](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations/setSyncAuthorization) API was not invoked. Perhaps the configuration never made it to the data plane.
  2. Inspect the `runtime` pods.

Inspecting the logs from the `runtime` pods will show why the `runtime` did not load the configuration.

  3. Inspect the `watcher` pods.

It is the `watcher` component that configures the ingress (routing) and reports proxy and ingress deployment status to the control plane. Inspect these logs to find out why the `watcher` is not reporting the status. Common reasons include a mismatch between the names in the `overrides.yaml` file and the control plane for environment name and/or environment group name.




### Debug session is not appearing in the control plane

  1. Start with the `synchronizer` pods.

Inspect the logs for the `synchronizer`. Common errors are as follows:

     * Lack of network connectivity (to `*.googleapi.com`)
     * Incorrect IAM access (service account not available or not provided by the Synchronizer Manager permission)
     * The [ setSyncAuthorization](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations/setSyncAuthorization) API was not invoked.
  2. Inspect the `runtime` pods.   
Inspecting the logs from the `runtime` pods will show why the `runtime` is not sending debug logs to UDCA.
  3. Inspect the UDCA pods.   
Inspecting the logs from the UDCA will show why UDCA is not sending debug session information to control plane.



### Cassandra returning large cache responses

The following warning message indicates that Cassandra is receiving read or write requests with a larger payload and can be safely ignored as this warning threshold is set to a lower value to indicate the response payload sizes.
    
    
    Batch for [cache_ahg_gap_prod_hybrid.cache_map_keys_descriptor, cache_ahg_gap_prod_hybrid.cache_map_entry] is of size 79.465KiB, exceeding specified threshold of 50.000KiB by 29.465KiB

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
