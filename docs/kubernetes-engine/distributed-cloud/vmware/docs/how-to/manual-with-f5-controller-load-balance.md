---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/manual-with-f5-controller-load-balance/
title: Load balancing with F5 and legacy Google-provided controllers \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:19:43.847240+00:00
---

# Load balancing with F5 and legacy Google-provided controllers  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/manual-with-f5-controller-load-balance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Load balancing with F5 and legacy Google-provided controllers Stay organized with collections  Save and categorize content based on your preferences. 

In version 1.29 and lower, user clusters created with the [loadBalancer.f5BigIP](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#loadbalancer-f5bigip-section) configuration deployed F5 controllers provided by Google. Because these controllers have [limitations](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/migrate-recommended-features#migrate_configuration_settings_for_your_f5_big-ip_load_balancer), in version 1.30 and higher, Google Distributed Cloud blocks creating clusters with the `loadBalancer.f5BigIP` configuration. Instead, new clusters must be configured for [manual load balancing](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/manual-load-balance), and you need to deploy F5 controllers yourself.

This page shows how to deploy the legacy Google-provided F5 controllers for a user cluster created with Google Distributed Cloud. Although deploying these controllers is supported, we recommend that you install the latest CIS controller from F5.

## Prerequisites:

  * You have a user cluster with the [manualLB](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#loadbalancer-manuallb-section) configuration.

  * You have a F5 server for the user cluster and you know its login information.

  * You want to automate the process to configure virtual servers in F5 for Kubernetes Services of type LoadBalancer in your user cluster.




## Step1. Prepare templates for the controllers

Get the F5 information and generate the templates.

### Get F5 information

  1. Set the following placeholder variables with the login information from the F5 server:

     * F5 UserName: `USERNAME`

     * F5 Password: `PASSWORD`

     * F5 Address: `ADDRESS`

     * F5 Partition: `PARTITION`

  2. Set the `SnatPoolName`. If you aren't using SNAT, leave the placeholder variable empty:
         
         SnatPoolName: SNAT_POOL_NAME
         




### Get the registry and version information

  1. Get the `onpremusercluster` custom resource:
         
         kubectl --kubeconfig USER_CLUSTER_KUBECONFIG get onpremusercluster -oyaml -n kube-system
         

  2. Copy the following fields from the `onpremusercluster` custom resource: 
         
         Registry: REGISTRY (onpremusercluster.spec.registry.address)
         ImageTag: IMAGE_TAG (onpremusercluster.spec.gkeOnPremVersion)
         




## Generate the templates
    
    
    cat > templates.yaml << EOF
    apiVersion: v1
    kind: Secret
    metadata:
      name: bigip-login
      namespace: kube-system
    stringData:
      password: "PASSWORD"
      username: "USERNAME"
      url: "ADDRESS"
      partition: "PARTITION"
    ---
    apiVersion: v1
    kind: ServiceAccount
    metadata:
      name: bigip-ctlr
      namespace: kube-system
    ---
    apiVersion: v1
    kind: ServiceAccount
    metadata:
      name: load-balancer-f5
      namespace: kube-system
    ---
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: k8s-bigip-ctlr-deployment
      namespace: kube-system
    spec:
      replicas: 1
      selector:
        matchLabels:
          app: k8s-bigip-ctlr
      template:
        metadata:
          name: k8s-bigip-ctlr
          labels:
            app: k8s-bigip-ctlr
        spec:
          serviceAccountName: bigip-ctlr
          volumes:
            - name: bigip-login
              secret:
                secretName: bigip-login
          containers:
            - name: k8s-bigip-ctlr
              image: "REGISTRY/k8s-bigip-ctlr:v1.14.0-gke.28"
              resources:
                requests:
                  cpu: 60m
                  memory: 90Mi
              volumeMounts:
                - name: bigip-login
                  readOnly: true
                  mountPath: "/etc/bigip-login"
              env:
                - name: BIGIP_PARTITION
                  valueFrom:
                    secretKeyRef:
                      name: bigip-login
                      key: partition
              command: ["/app/bin/k8s-bigip-ctlr"]
              args: [
                # See the k8s-bigip-ctlr documentation for information about
                # all config options
                # http://clouddocs.f5.com/products/connectors/k8s-bigip-ctlr/latest
                "--http-listen-address=:9097",
                "--credentials-directory=/etc/bigip-login",
                "--bigip-partition=\$(BIGIP_PARTITION)",
                "--log-level=ERROR",
                "--pool-member-type=nodeport",
                "--manage-ingress=false",
                "--vs-snat-pool-name=SNAT_POOL_NAME"
              ]
          dnsPolicy: Default
          imagePullSecrets:
            - name: private-registry-creds
          nodeSelector:
            kubernetes.io/os: linux
    ---
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: load-balancer-f5
      namespace: kube-system
      labels:
        app: load-balancer-f5
    spec:
      replicas: 1
      selector:
        matchLabels:
          app: load-balancer-f5
      template:
        metadata:
          name: load-balancer-f5
          labels:
            app: load-balancer-f5
        spec:
          serviceAccountName: load-balancer-f5
          containers:
            - name: load-balancer-f5
              image: "REGISTRY/load-balancer-f5:IMAGE_TAG"
              env:
                - name: BIGIP_PARTITION
                  valueFrom:
                    secretKeyRef:
                      name: bigip-login
                      key: partition
              command:
                - ./load-balancer-f5
              args:
                - "--bigip-partition=\$(BIGIP_PARTITION)"
              resources:
                requests:
                  cpu: 2m
                  memory: 13Mi
          imagePullSecrets:
            - name: private-registry-creds
          nodeSelector:
            kubernetes.io/os: linux
    ---
    kind: ClusterRoleBinding
    apiVersion: rbac.authorization.k8s.io/v1
    metadata:
      name: bigip-ctlr-clusterrole-binding
    roleRef:
      apiGroup: rbac.authorization.k8s.io
      kind: ClusterRole
      name: bigip-ctlr-clusterrole
    subjects:
      - kind: ServiceAccount
        name: bigip-ctlr
        namespace: kube-system
    ---
    kind: ClusterRoleBinding
    apiVersion: rbac.authorization.k8s.io/v1
    metadata:
      name: load-balancer-f5-clusterrole-binding
    roleRef:
      apiGroup: rbac.authorization.k8s.io
      kind: ClusterRole
      name: load-balancer-f5-clusterrole
    subjects:
      - kind: ServiceAccount
        name: load-balancer-f5
        namespace: kube-system
    ---
    kind: ClusterRole
    apiVersion: rbac.authorization.k8s.io/v1
    metadata:
      name:
        bigip-ctlr-clusterrole
    rules:
      - apiGroups: ["", "extensions"]
        resources: ["nodes", "services", "endpoints", "namespaces", "ingresses", "pods"]
        verbs: ["get", "list", "watch"]
      - apiGroups: ["", "extensions"]
        resources: ["configmaps", "events", "ingresses/status"]
        verbs: ["get", "list", "watch"]
      - apiGroups: ["", "extensions"]
        resources: ["secrets"]
        resourceNames: ["bigip-login"]
        verbs: ["get", "list", "watch"]
    ---
    kind: ClusterRole
    apiVersion: rbac.authorization.k8s.io/v1
    metadata:
      name:
        load-balancer-f5-clusterrole
    rules:
      - apiGroups: [""]
        resources: ["events", "nodes"]
        verbs: ["get", "list", "watch"]
      - apiGroups: [""]
        resources: ["services", "services/status"]
        verbs: ["get", "list", "watch", "patch", "update"]
      - apiGroups: [""]
        resources: ["configmaps"]
        verbs: ["get", "list", "watch",  "create", "patch", "delete"]
    EOF
    

## Step2. Apply the templates to user cluster
    
    
    kubectl --kubeconfig USER_CLUSTER_KUBECONFIG apply -f templates.yaml
    

**Note:** After every upgrade of the cluster's control plane, you have to make these changes.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
