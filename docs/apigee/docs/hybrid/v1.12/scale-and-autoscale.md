---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/scale-and-autoscale/
title: Scale and autoscale runtime services \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T02:08:02.846199+00:00
---

# Scale and autoscale runtime services  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/scale-and-autoscale/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Scale and autoscale runtime services Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.12 of the Apigee hybrid documentation. **This version is end of life.** You should upgrade to a newer version. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.12 keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/scale-and-autoscale.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/scale-and-autoscale.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/scale-and-autoscale.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/scale-and-autoscale.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/scale-and-autoscale.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/scale-and-autoscale.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/scale-and-autoscale.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/scale-and-autoscale.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/scale-and-autoscale.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/scale-and-autoscale.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/scale-and-autoscale.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/scale-and-autoscale.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/scale-and-autoscale.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/scale-and-autoscale.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/scale-and-autoscale.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/scale-and-autoscale.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/scale-and-autoscale.html)



You can scale most services running in Kubernetes from the command line or in a configuration override. You can set scaling parameters for Apigee hybrid runtime services in the [`overrides.yaml` file](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/customize-services).

Service | Implemented As | Scaling  
---|---|---  
**Cassandra** | ApigeeDatastore (CRD) | See [Scaling Cassandra](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/cassandra-scaling#scaling-cassandra).   
**Ingress/LoadBalancer** | [Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) | Cloud Service Mesh uses [Horizontal Pod Autoscaling](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/) (HPAs).  
**Logger** | [DaemonSet](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/) | DaemonSets manage replicas of a pod on all nodes, so they scale when you scale the pods themselves.   
**MART  
Apigee Connect  
Watcher** | ApigeeOrganization (CRD) | To scale via configuration, increase the value of the Deployment's `replicaCountMin` configuration property for the `mart`, `watcher`, and/or `connectAgent` stanzas. For example:
    
    
    mart:
     replicaCountMax: 2
     replicaCountMin: 1
    
    watcher:
     replicaCountMax: 2
     replicaCountMin: 1
    
    connectAgent:
     replicaCountMax: 2
     replicaCountMin: 1

These Deployments use a Horizontal Pod Autoscaler for autoscaling. Set the Deployment object's `targetCPUUtilizationPercentage` property to the threshold for scaling up; when this value is exceeded, Kubernetes adds pods up to the value of `replicaCountMax`. For more information on setting configuration properties, see [Manage runtime plane components](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/customize-services).  
**Runtime  
Synchronizer  
UDCA** | ApigeeEnvironment (CRD) | To scale via configuration, increase the value of the `replicaCountMin` property for the `udca`, `synchronizer`, and/or `runtime` stanzas in the overrides file. For example: 
    
    
    synchronizer:
     replicaCountMax: 10
     replicaCountMin: 1
    
    runtime:
     replicaCountMax: 10
     replicaCountMin: 1
    
    udca:
     replicaCountMax: 10
     replicaCountMin: 1

**Note:** These changes apply to ALL environments in the overrides file. If you wish to customize scaling for each environment see Advanced configurations below.  These deployments use a Horizontal Pod Autoscaler for autoscaling. Set the Deployment object's `targetCPUUtilizationPercentage` property to the threshold for scaling up; when this value is exceeded, Kubernetes adds pods up to the value of `replicaCountMax`. For more information on setting configuration properties, see [Manage runtime plane components](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/customize-services).  
  
##  Advanced configurations 

In some scenarios, you may need to use advanced scaling options. Example scenarios include: 

  * Setting different scaling options for each environment. For example, where env1 has a `minReplica` of 5 and env2 has a `minReplica` of 2. 
  * Setting different scaling options for each component within an environment. For example, where the `udca` component has a `maxReplica` of 5 and the `synchronizer` component has a `maxReplica` of 2.



The following example shows how to use the `kubernetes patch` command to change the `maxReplicas` property for the `runtime` component: 

  1. Create environment variables to use with the command: 
         
         export ENV=my-environment-name
         export NAMESPACE=apigee  #the namespace where apigee is deployed
         export COMPONENT=runtime #can be udca or synchronizer
         export MAX_REPLICAS=2
         export MIN_REPLICAS=1

  2. Apply the patch. Note that this example assumes that `kubectl` is in your `PATH`: 
         
         kubectl patch apigeeenvironment -n $NAMESPACE \
           $(kubectl get apigeeenvironments -n $NAMESPACE -o jsonpath='{.items[?(@.spec.name == "'$ENV'" )]..metadata.name}') \
           --patch "$(echo -e "spec:\n  components:\n    $COMPONENT:\n      autoScaler:\n        maxReplicas: $MAX_REPLICAS\n        minReplicas: $MIN_REPLICAS")" \
           --type merge

  3. Verify the change: 
         
         kubectl get hpa -n $NAMESPACE




## Environment-based scaling

By default, scaling is described at the organization level. You can override the default settings by specifying environment-specific scaling in the `overrides.yaml` file as shown in the following example: 
    
    
    envs:
      # Apigee environment name
      - name: test
        components:
        # Environment-specific scaling override
        # Otherwise, uses scaling defined at the respective root component
         runtime:
          replicaCountMin: 2
          replicaCountMax: 20
      

## Metrics-based scaling

With metrics-based scaling, the runtime can use CPU and application metrics to scale the `apigee-runtime` pods. The Kubernetes [Horizontal Pod Autoscaler (HPA) API](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/horizontal-pod-autoscaler-v2/#HorizontalPodAutoscalerSpec), uses the `hpaBehavior` field to configure the scale-up and scale-down behaviors of the target service. Metrics-based scaling is not available for any other components in a hybrid deployment. 

**Note:** The behavior and meaning of each of the individual fields in the YAML examples in this section are not unique to Apigee hybrid. These concepts come directly from [ Kubernetes scaling policies](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/#scaling-policies). **Note** : An internal connection between Prometheus and the Prometheus-Adapter on port 6443 must be open in order to receive metrics data and enable scaling. For more information on required ports, see [Internal connections](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/ports#internal).

Scaling can be adjusted based on the following metrics: 

Metric | Measure | Considerations  
---|---|---  
serverNioTaskWaitTime |  Average wait time (in picoseconds) of processing queue in runtime instances for proxy requests at the http layer.  | This metric measures the impact of the number and payload size of proxy requests and responses.  
serverMainTaskWaitTime | Average wait time (in picoseconds) of processing queue in runtime instances for proxy requests to process policies.  | This metric measures the impact of complexity in the policies attached to the proxy request flow.  
  
The following example from the `runtime` stanza in the `overrides.yaml` illustrates the standard parameters (and permitted ranges) for scaling `apigee-runtime` pods in a hybrid implementation: 
    
    
    hpaMetrics:
          serverMainTaskWaitTime: 400M (300M to 450M)
          serverNioTaskWaitTime: 400M (300M to 450M)
          targetCPUUtilizationPercentage: 75
        hpaBehavior:
          scaleDown:
            percent:
              periodSeconds: 60 (30 - 180)
              value: 20 (5 - 50)
            pods:
              periodSeconds: 60 (30 - 180)
              value: 2 (1 - 15)
            selectPolicy: Min
            stabilizationWindowSeconds: 120 (60 - 300)
          scaleUp:
            percent:
              periodSeconds: 60 (30 - 120)
              value: 20 (5 - 100)
            pods:
              periodSeconds: 60 (30 - 120)
              value: 4 (2 - 15)
            selectPolicy: Max
            stabilizationWindowSeconds: 30 (30 - 120)
      

### Configure more aggressive scaling

Increasing the `percent` and `pods` values of the scale-up policy will result in a more aggressive scale-up policy. Similarly, increasing the `percent` and `pods` values in `scaleDown` will result in an aggressive scale-down policy. For example: 
    
    
    hpaMetrics:
        serverMainTaskWaitTime: 400M
        serverNioTaskWaitTime: 400M
        targetCPUUtilizationPercentage: 75
      hpaBehavior:
        scaleDown:
          percent:
            periodSeconds: 60
            value: 20
          pods:
            periodSeconds: 60
            **value: 4**
          selectPolicy: Min
          stabilizationWindowSeconds: 120
        scaleUp:
          percent:
            periodSeconds: 60
            **value: 30**
          pods:
            periodSeconds: 60
            **value: 5**
          selectPolicy: Max
          stabilizationWindowSeconds: 30

In the above example, the `scaleDown.pods.value` is increased to **5** , the `scaleUp.percent.value ` is increased to **30** , and the `scaleUp.pods.value` is increased to **5**.

**Note** : The value of `periodSeconds` should not go below 30.

### Configure less aggressive scaling

The `hpaBehavior` configuration values can also be decreased to implement less aggressive scale-up and scale-down policies. For example: 
    
    
    hpaMetrics:
        serverMainTaskWaitTime: 400M
        serverNioTaskWaitTime: 400M
        targetCPUUtilizationPercentage: 75
      hpaBehavior:
        scaleDown:
          percent:
            periodSeconds: 60
            **value: 10**
          pods:
            periodSeconds: 60
            **value: 1**
          selectPolicy: Min
          **stabilizationWindowSeconds: 180**
        scaleUp:
          percent:
            periodSeconds: 60
            value: 20
          pods:
            periodSeconds: 60
            value: 4
          selectPolicy: Max
          stabilizationWindowSeconds: 30

In the above example, the `scaleDown.percent.value` is decreased to **10** , the `scaleDown.pods.value` is decreased to **1** , and the `scaleUp.stablizationWindowSeconds` is increased to **180**.

For more information about metrics-based scaling using the `hpaBehavior` field, see [ Scaling policies](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/#scaling-policies).

### Disable metrics-based scaling

While metrics-based scaling is enabled by default and cannot be completely disabled, you can configure the metrics thresholds at a level that metrics-based scaling will not be triggered. The resulting scaling behavior will be the same as CPU-based scaling. For example, you can use the following configuration to prevent triggering metrics-based scaling: 
    
    
    hpaMetrics:
          serverMainTaskWaitTime: 4000M
          serverNioTaskWaitTime: 4000M
          targetCPUUtilizationPercentage: 75
        hpaBehavior:
          scaleDown:
            percent:
              periodSeconds: 60
              value: 10
            pods:
              periodSeconds: 60
              value: 1
            selectPolicy: Min
            stabilizationWindowSeconds: 180
          scaleUp:
            percent:
              periodSeconds: 60
              value: 20
            pods:
              periodSeconds: 60
              value: 4
            selectPolicy: Max
            stabilizationWindowSeconds: 30

## Troubleshooting

This section describes troubleshooting methods for common errors you may encounter while configuring scaling and auto-scaling.

### HPA shows `unknown` for metrics values

If metrics-based scaling does not work and the HPA shows `unknown` for metrics values, use the following command to check the HPA output: 
    
    
    kubectl describe hpa HPA_NAME

When running the command, replace HPA_NAME with the name of the HPA you wish to view.

The output will show the CPU target and utilization of the service, indicating that CPU scaling will work in the absence of metrics-based scaling. For HPA behavior using multiple parameters, see [Scaling on multiple metrics](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/#scaling-on-multiple-metrics).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
