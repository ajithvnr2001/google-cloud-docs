---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/custom-kube-dns/
title: Set up a custom kube-dns Deployment \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:22:48.247448+00:00
---

# Set up a custom kube-dns Deployment  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/custom-kube-dns/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Set up a custom kube-dns Deployment Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document explains how to customize the DNS setup in your Google Kubernetes Engine (GKE) Standard cluster by replacing the default, GKE-managed `kube-dns` with your own deployment. This gives you more control over your cluster's DNS provider. For example, you can:

  * Fine-tune CPU and memory resources for DNS components.
  * Use a specific `kube-dns` image version.
  * Deploy an alternative DNS provider, such as CoreDNS, that adheres to the Kubernetes DNS specification.



This document is only for Standard clusters; Google manages the DNS configuration in Autopilot clusters. For a deeper understanding of DNS providers in GKE, see [About service discovery](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-discovery) and [`kube-dns`](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kube-dns).

**Caution:** If you run a custom DNS deployment, you are responsible for its ongoing maintenance. This includes ensuring the `kube-dns` and autoscaler container images are up to date with the latest versions and security patches. To find the latest recommended images, inspect the default `kube-dns` deployment in the `kube-system` namespace of a GKE cluster.

This document is for GKE users, including Developers and Admins and architects. To learn more about common roles and example tasks in Google Cloud, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

This document assumes you are familiar with the following:

  * [Kubernetes Service](https://kubernetes.io/docs/concepts/services-networking/service/).
  * [Multi-cluster Services](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-cluster-services).
  * [About service discovery](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-service-discovery).
  * [Service discovery and DNS in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-discovery).
  * [About Cloud DNS](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-cloud-dns).



## Set up a custom kube-dns deployment

This section explains how to replace the GKE-managed `kube-dns` with your own deployment.

### Create and deploy the custom manifest

  1. Save the following `Deployment` manifest as `custom-kube-dns.yaml`. This manifest uses `kube-dns`.
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: DNS_DEPLOYMENT_NAME
           namespace: kube-system
           labels:
             k8s-app: kube-dns
           annotations:
             deployment.kubernetes.io/revision: "1"
         spec:
           selector:
             matchLabels:
               k8s-app: kube-dns
           strategy:
             rollingUpdate:
               maxSurge: 10%
               maxUnavailable: 0
             type: RollingUpdate
           template:
             metadata:
               creationTimestamp: null
               labels:
                 k8s-app: kube-dns
             spec:
               containers:
               - name: kubedns
                 image: registry.k8s.io/dns/k8s-dns-kube-dns:1.22.28
                 resources:
                   limits:
                     memory: '170Mi'
                   requests:
                     cpu: 100m
                     memory: '70Mi'
                 livenessProbe:
                   httpGet:
                     path: /healthcheck/kubedns
                     port: 10054
                     scheme: HTTP
                   initialDelaySeconds: 60
                   timeoutSeconds: 5
                   successThreshold: 1
                   failureThreshold: 5
                 readinessProbe:
                   httpGet:
                     path: /readiness
                     port: 8081
                     scheme: HTTP
                   initialDelaySeconds: 3
                   timeoutSeconds: 5
                 args:
                 - --domain=cluster.local.
                 - --dns-port=10053
                 - --config-dir=/kube-dns-config
                 - --v=2
                 env:
                 - name: PROMETHEUS_PORT
                   value: "10055"
                 ports:
                 - containerPort: 10053
                   name: dns-local
                   protocol: UDP
                 - containerPort: 10053
                   name: dns-tcp-local
                   protocol: TCP
                 - containerPort: 10055
                   name: metrics
                   protocol: TCP
                 volumeMounts:
                 - name: kube-dns-config
                   mountPath: /kube-dns-config
                 securityContext:
                   allowPrivilegeEscalation: false
                   readOnlyRootFilesystem: true
                   runAsUser: 1001
                   runAsGroup: 1001
               - name: dnsmasq
                 image: registry.k8s.io/dns/k8s-dns-dnsmasq-nanny:1.22.28
                 livenessProbe:
                   httpGet:
                     path: /healthcheck/dnsmasq
                     port: 10054
                     scheme: HTTP
                   initialDelaySeconds: 60
                   timeoutSeconds: 5
                   successThreshold: 1
                   failureThreshold: 5
                 args:
                 - -v=2
                 - -logtostderr
                 - -configDir=/etc/k8s/dns/dnsmasq-nanny
                 - -restartDnsmasq=true
                 - --
                 - -k
                 - --cache-size=1000
                 - --no-negcache
                 - --dns-forward-max=1500
                 - --log-facility=-
                 - --server=/cluster.local/127.0.0.1#10053
                 - --server=/in-addr.arpa/127.0.0.1#10053
                 - --server=/ip6.arpa/127.0.0.1#10053
                 ports:
                 - containerPort: 53
                   name: dns
                   protocol: UDP
                 - containerPort: 53
                   name: dns-tcp
                   protocol: TCP
                 resources:
                   requests:
                     cpu: 150m
                     memory: 20Mi
                 volumeMounts:
                 - name: kube-dns-config
                   mountPath: /etc/k8s/dns/dnsmasq-nanny
                 securityContext:
                   capabilities:
                     drop:
                     - all
                     add:
                     - NET_BIND_SERVICE
                     - SETGID
               - name: sidecar
                 image: registry.k8s.io/dns/k8s-dns-sidecar:1.22.28
                 livenessProbe:
                   httpGet:
                     path: /metrics
                     port: 10054
                     scheme: HTTP
                   initialDelaySeconds: 60
                   timeoutSeconds: 5
                   successThreshold: 1
                   failureThreshold: 5
                 args:
                 - --v=2
                 - --logtostderr
                 - --probe=kubedns,127.0.0.1:10053,kubernetes.default.svc.cluster.local,5,SRV
                 - --probe=dnsmasq,127.0.0.1:53,kubernetes.default.svc.cluster.local,5,SRV
                 ports:
                 - containerPort: 10054
                   name: metrics
                   protocol: TCP
                 resources:
                   requests:
                     memory: 20Mi
                     cpu: 10m
                 securityContext:
                   allowPrivilegeEscalation: false
                   readOnlyRootFilesystem: true
                   runAsUser: 1001
                   runAsGroup: 1001
               dnsPolicy: Default
               restartPolicy: Always
               schedulerName: default-scheduler
               securityContext: {}
               serviceAccount: kube-dns
               serviceAccountName: kube-dns
               terminationGracePeriodSeconds: 30
               tolerations:
               - key: CriticalAddonsOnly
                 operator: Exists
               volumes:
               - configMap:
                   defaultMode: 420
                   name: kube-dns
                   optional: true
                 name: kube-dns-config
         

Replace `DNS_DEPLOYMENT_NAME` with the name of your custom DNS Deployment.

  2. Apply the manifest to the cluster:
         
         kubectl create -f custom-kube-dns.yaml
         




### Scale down the GKE-managed `kube-dns`

To avoid conflicts, disable the GKE-managed `kube-dns` and `kube-dns-autoscaler` Deployments by scaling them to zero replicas:
    
    
    kubectl scale deployment --replicas=0 kube-dns-autoscaler kube-dns --namespace=kube-system
    

### Configure a custom autoscaler

The default `kube-dns-autoscaler` only scales the GKE-managed `kube-dns` Deployment. If your custom DNS provider requires autoscaling, you must deploy a separate autoscaler and grant it permissions to modify your custom DNS Deployment.

  1. Create the following manifest and save it as `custom-dns-autoscaler.yaml`.
         
         apiVersion: v1
         kind: ConfigMap
         metadata:
           name: custom-dns-autoscaler
           namespace: kube-system
         data:
           linear: |-
             {
               "coresPerReplica": 256,
               "nodesPerReplica": 16,
               "preventSinglePointFailure": true
             }
         ---
         apiVersion: rbac.authorization.k8s.io/v1
         kind: ClusterRoleBinding
         metadata:
           name: system:custom-dns-autoscaler
         roleRef:
           apiGroup: rbac.authorization.k8s.io
           kind: ClusterRole
           name: system:custom-dns-autoscaler
         subjects:
         - kind: ServiceAccount
           name: kube-dns-autoscaler
           namespace: kube-system
         ---
         apiVersion: rbac.authorization.k8s.io/v1
         kind: ClusterRole
         metadata:
           name: system:custom-dns-autoscaler
         rules:
         - apiGroups:
           - ""
           resources:
           - nodes
           verbs:
           - list
           - watch
         - apiGroups:
           - apps
           resourceNames:
           - DNS_DEPLOYMENT_NAME
           resources:
           - deployments/scale
           verbs:
           - get
           - update
         - apiGroups:
           - ""
           resources:
           - configmaps
           verbs:
           - get
           - create
         ---
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: custom-dns-autoscaler
           namespace: kube-system
           labels:
             k8s-app: custom-dns-autoscaler
         spec:
           selector:
             matchLabels:
               k8s-app: custom-dns-autoscaler
           template:
             metadata:
               labels:
                 k8s-app: custom-dns-autoscaler
             spec:
               priorityClassName: system-cluster-critical
               securityContext:
                 seccompProfile:
                   type: RuntimeDefault
                 supplementalGroups: [ 65534 ]
                 fsGroup: 65534
               nodeSelector:
                 kubernetes.io/os: linux
               containers:
               - name: autoscaler
                 image: registry.k8s.io/autoscaling/cluster-proportional-autoscaler:1.8.9
                 resources:
                   requests:
                     cpu: "20m"
                     memory: "10Mi"
                 command:
                 - /cluster-proportional-autoscaler
                 - --namespace=kube-system
                 - --configmap=custom-dns-autoscaler
                 - --target=Deployment/DNS_DEPLOYMENT_NAME
                 - --default-params={"linear":{"coresPerReplica":256,"nodesPerReplica":16,"preventSinglePointFailure":true}}
                 - --logtostderr=true
                 - --v=2
               tolerations:
               - key: "CriticalAddonsOnly"
                 operator: "Exists"
               serviceAccountName: kube-dns-autoscaler
         

Replace `DNS_DEPLOYMENT_NAME` in the `resourceNames` field and in the `command` field with the name of your custom DNS Deployment.

  2. Apply the manifest to the cluster:
         
         kubectl create -f custom-dns-autoscaler.yaml
         




## Verify the deployment

Verify that your custom DNS Pods are running:
    
    
    kubectl get pods -n kube-system -l k8s-app=kube-dns
    

Because you scaled the GKE-managed `kube-dns` deployment to zero replicas, only Pods from your custom Deployment appear in the output. Verify that their status is `Running`.

## Restore the GKE-managed kube-dns

If you deployed a custom `kube-dns` configuration and need to revert to the default GKE-managed setup, you must delete your custom resources and re-enable the managed `kube-dns` deployment.

Follow these steps to restore the GKE-managed `kube-dns`:

  1. Delete the custom `kube-dns` deployment and its autoscaler. If you saved the manifests as `custom-kube-dns.yaml` and `custom-dns-autoscaler.yaml`, run the following commands to delete the resources:
         
         kubectl delete -f custom-dns-autoscaler.yaml
         kubectl delete -f custom-kube-dns.yaml
         

If you did not save the manifests, manually delete the Deployment, ClusterRole, and ClusterRoleBinding that you created for your custom deployment.

  2. Restore the GKE-managed `kube-dns-autoscaler`. Run the following command to scale the `kube-dns-autoscaler` deployment back to one replica:
         
         kubectl scale deployment --replicas=1 kube-dns-autoscaler --namespace=kube-system
         

This command re-enables the managed `kube-dns-autoscaler`, which then automatically scales the managed `kube-dns` deployment to the appropriate number of replicas for your cluster's size.

  3. Verify the restoration.

Check the `kube-dns` and `kube-dns-autoscaler` Pods to ensure they are running correctly:
         
         kubectl get pods -n kube-system -l k8s-app=kube-dns
         

The output should show that the GKE-managed `kube-dns` Pods are in the `Running` state.




## What's next

  * Read an overview of how GKE provides [managed DNS](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-discovery).
  * Read [DNS for Services and Pods](https://kubernetes.io/docs/concepts/services-networking/dns-pod-service) for a general overview of how DNS is used in Kubernetes clusters.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
