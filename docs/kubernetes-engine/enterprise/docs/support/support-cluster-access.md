---
url: https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/support/support-cluster-access/
title: Grant support read-only access to clusters \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:25:09.184074+00:00
---

# Grant support read-only access to clusters  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/support/support-cluster-access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)



Send feedback 

#  Grant support read-only access to clusters Stay organized with collections  Save and categorize content based on your preferences. 

If you have a problem with registered clusters outside Google Cloud that you can't resolve yourself, you may be asked to grant Google Cloud Support read-only access to your clusters to help them understand your issue and triage it faster. These clusters could be on bare metal, VMware, GDC connected, GKE on AWS, GKE on Azure, or GKE attached clusters.

This page tells you how to share this information with Google Cloud Support.

This page is for IT administrators and Operators who respond to alerts and pages when service level objectives (SLOs) aren't met or applications fail and debug to find root cause. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

In this support flow, a dedicated Google Cloud service account is set up for your support case and granted read-only access to your cluster. The support team can then run read-only commands using this service account to list pods, container image pull success/failure, inspect node status, and so on to help resolve your issue. The support team can't make any changes to your cluster.

For more information about support, see:

  * [Get support for clusters on bare metal](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support)
  * [Get support for clusters on VMware](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support)



## Before you begin

  * Ensure that you have the following command line tools installed: 
    * Google Cloud CLI with an earliest version of `486.0.0` for enabling access. If you need to install the Google Cloud CLI, see the [installation guide](https://docs.cloud.google.com/sdk/docs/install).
    * `kubectl` for running commands against Kubernetes clusters. If you need to install `kubectl`, see the [installation guide](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/before-you-begin#install-kubectl).
  * Ensure that you have [initialized](https://docs.cloud.google.com/sdk/docs/install-sdk#initializing_the) the gcloud CLI for use with your project.
  * Ensure that the clusters you need to troubleshoot are [registered to your project fleet](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-creation). You can verify that a cluster is registered by running `gcloud container fleet memberships list` (or `gcloud container fleet memberships describe MEMBERSHIP_NAME`, where MEMBERSHIP_NAME is the cluster's unique name).
  * Ensure that you have the `gkehub.rbacrolebindings.create` permission in your project. This permission is included in the `gkehub.editor` and `gkehub.admin` roles. You need this to enable Support access.
  * Ensure that you have enabled `connectgateway.googleapis.com` for your project. To do so, if you are not a project owner, you must be granted the `serviceusage.services.enable` permission.



## Manage Support access for the cluster

To enable Support access for the cluster, you run a `gcloud` command that propagates a set of read-only Kubernetes role-based access control (RBAC) policies to the target cluster. The support team won't be able to view your clusters until you successfully run this command. To see the RBAC policies that the command applies, see Review the RBAC policies in advance.

To enable support access for the cluster, run the following commands:
    
    
    # enable Connect Gateway API
    gcloud services enable connectgateway.googleapis.com --project=PROJECT_ID
    
    # generate RBAC to enable access
    gcloud container fleet memberships support-access enable MEMBERSHIP_NAME \
        --project=PROJECT_ID
    
    # verify the access is enabled
    gcloud container fleet memberships support-access describe MEMBERSHIP_NAME \
        --project=PROJECT_ID

Replace the following:

  * MEMBERSHIP_NAME: the name used to uniquely represent the cluster in its fleet. You can find out how to check your cluster's membership name in [Get fleet membership status](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/get-fleet-status).
  * PROJECT_ID: the project ID where the cluster is registered.



After the support case is closed, Google removes the support team's permission to access your cluster. You can also run the following command to manually remove Google's permission to access your cluster:
    
    
    gcloud container fleet memberships support-access disable MEMBERSHIP_NAME \
        --project=PROJECT_ID

## Review the RBAC policies in advance

You can also output the proposed RBAC policies to a file to preview, customize the list of resources in the policy rules, and apply them directly to the cluster with the following commands:
    
    
    # enable Connect Gateway API
    gcloud services enable connectgateway.googleapis.com --project=PROJECT_ID
    
    # display RBAC policies but don't apply them
    gcloud container fleet memberships support-access get-yaml MEMBERSHIP_NAME \
        --project=PROJECT_ID \
        --rbac-output-file=RBAC_OUTPUT_FILE
    
    # directly apply the modified policies to the cluster
    kubectl apply -f RBAC_OUTPUT_FILE

#### RBAC policies that the command applies

Your project ID and project number will appear in the output instead of `{PROJECT-NUMBER}`. 

### Google Distributed Cloud for VMware
    
    
          apiVersion: rbac.authorization.k8s.io/v1
          kind: ClusterRole
          metadata:
            creationTimestamp: null
            name: fleet-rrb-imp-actuation-gke-fleet-support-access
          rules:
          - apiGroups:
            - ""
            resourceNames:
            - service-{PROJECT-NUMBER}@gcp-sa-anthossupport.iam.gserviceaccount.com
            resources:
            - users
            verbs:
            - impersonate
          ---
          apiVersion: rbac.authorization.k8s.io/v1
          kind: ClusterRoleBinding
          metadata:
            creationTimestamp: null
            name: fleet-rrb-imp-actuation-gke-fleet-support-access
          roleRef:
            apiGroup: ""
            kind: ClusterRole
            name: fleet-rrb-imp-actuation-gke-fleet-support-access
          subjects:
          - kind: ServiceAccount
            name: connect-agent-sa
            namespace: gke-connect
          ---
          apiVersion: rbac.authorization.k8s.io/v1
          kind: ClusterRole
          metadata:
            creationTimestamp: null
            name: fleet-rrb-actuation-gke-fleet-support-access
          rules:
          - apiGroups:
            - acme.cert-manager.io
            resources: [challenges, orders]
            verbs: [get, list, watch]
          - apiGroups:
            - addons.gke.io
            resources:[metricsserver, monitoring, stackdrivers]
            verbs: [get, list, watch]
          - apiGroups:
            - admissionregistration.k8s.io
            resources: [mutatingwebhookconfigurations, validatingwebhookconfigurations]
            verbs: [get, list, watch]
          - apiGroups:
            - anthos.gke.io
            resources: [entitlements, healthcheckjobs, healthchecks]
            verbs: [get, list, watch]
          - apiGroups:
            - apiextensions.k8s.io
            resources: [customresourcedefinitions]
            verbs: [get, list, watch]
          - apiGroups:
            - apiregistration.k8s.io
            resources: [apiservices]
            verbs: [get, list, watch]
          - apiGroups:
            - apiserver.k8s.io
            resources: [flowschemas, prioritylevelconfigurations]
            verbs: [get, list, watch]
          - apiGroups:
            - apps
            resources: [controllerrevisions, daemonsets, deployments, replicasets, statefulset]
            verbs: [get, list, watch]
          - apiGroups:
            - apps.k8s.io
            resources: [applications]
            verbs: [get, list, watch]
          - apiGroups:
            - authentication.gke.io
            resources: [clientconfigs]
            verbs: [get, list, watch]
          - apiGroups:
            - batch
            resources: [cronjobs, jobs]
            verbs: [get, list, watch]
          - apiGroups:
            - bootstrap.cluster.x-k8s.io
            resources: [kubeadmconfigs, kubeadmconfigtemplates]
            verbs: [get, list, watch]
          - apiGroups:
            - bundle.gke.io
            resources: [bundlebuilders, bundles, clusterbundles, componentbuilders, componentlists, components, componentsets, gkeonprembundles, packagedeploymentclasses, packagedeployments, patchtemplatebuilders, patchtemplates, requirements]
            verbs: [get, list, watch]
          - apiGroups:
            - bundleext.gke.io
            resources: [nodeconfigs]
            verbs: [get, list, watch]
          - apiGroups:
            - certificates.k8s.io
            resources: [certificatesigningrequests]
            verbs: [get, list, watch]
          - apiGroups:
            - cert-manager.io
            resources: [certificaterequests, certificates, clusterissuers, issuers]
            verbs: [get, list, watch]
          - apiGroups:
            - cilium.io
            resources: [ciliumnodes, ciliumendpoints, ciliumidentities, ciliumegressnatpolicies, ciliumexternalworkloads]
            verbs: [get, list, watch]
          - apiGroups:
            - configmanagement.gke.io
            resources: [configmanagements]
            verbs: [get, list, watch]
          - apiGroups:
            - config.gatekeeper.sh
            resources: [configs]
            verbs: [get, list, watch]
          - apiGroups:
            - coordination.k8s.io
            resources: [leases]
            verbs: [get, list, watch]
          - apiGroups:
            - cluster.k8s.io
            resources: [clusters, controlplanes, machineclasses, machinedeployments, machines, machinesets]
            verbs: [get, list, watch]
          - apiGroups:
            - cluster.x-k8s.io
            resources: [clusters, controlplanes, machineclasses, machinedeployments, machinehealthchecks, machines, machinesets]
            verbs: [get, list, watch]
          - apiGroups:
            - clusterctl.cluster.x-k8s.io
            resources: [metadata, providers]
            verbs: [get, list, watch]
          - apiGroups:
            - crd.projectcalico.org
            resources: [bgpconfigurations, bgppeers, blockaffinities, clusterinformations, felixconfigurations, globalnetworkpolicies, globalnetworksets, hostendpoints, ipamblocks, ipamconfigs, ipamhandles, ippools, networkpolicies, networksets, vpntunnels]
            verbs: [get, list, watch]
          - apiGroups:
            - discovery.k8s.io
            resources: [endpointslices]
            verbs: [get, list, watch]
          - apiGroups:
            - expansion.gatekeeper.sh
            resources: [expansiontemplate]
            verbs: [get, list, watch]
          - apiGroups:
            - extensions.istio.io
            resources: [*]
            verbs: [get, list, watch]
          - apiGroups:
            - gateway.networking.k8s.io
            resources: [gatewayclasses, gateways, grpcroutes, httproutes, referencegrants, tcproutes, tlsroutes, udproutes]
            verbs: [get, list, watch]
          - apiGroups:
            - hub.gke.io
            resources: [memberships]
            verbs: [get, list, watch]
          - apiGroups:
            - install.istio.io
            resources: [*]
            verbs: [get, list, watch]
          - apiGroups:
            - k8s.cni.cncf.io
            resources: [network-attachment-definitions]
            verbs: [get, list, watch]
          - apiGroups:
            - mutations.gatekeeper.sh
            resources: [assign, assignimage, assignmetadata, modifyset, mutatorpodstatuses]
            verbs: [get, list, watch]
          - apiGroups:
            - networking.istio.io
            resources: [*]
            verbs: [get, list, watch]
          - apiGroups:
            - networking.k8s.io
            resources: [ingressclasses, ingresses, multiclusterconnectivityconfigs, networkgatewaygroups, networkgatewaynodes, networkinterfaces, networkloggings, networks, trafficsteerings]
            verbs: [get, list, watch]
          - apiGroups:
            - node.k8s.io
            resources: [runtimeclasses]
            verbs: [get, list, watch]
          - apiGroups:
            - policy
            resources: [poddisruptionbudgets, podsecuritypolicies]
            verbs: [get, list, watch]
          - apiGroups:
            - rbac.authorization.k8s.io
            resources: [clusterroles, clusterrolebindings, roles, rolebindings]
            verbs: [get, list, watch]
          - apiGroups:
            - security.istio.io
            resources: [*]
            verbs: [get, list, watch]
          - apiGroups:
            - storage.k8s.io
            resources: [csidrivers, csinodes, csistoragecapacities, storageclasses, volumeattachments]
            verbs: [get, list, watch]
          - apiGroups:
            - sriovnetwork.k8s.cni.cncf.io
            resources: [sriovnetworknodepolicies, sriovnetworknodestates, sriovoperatorconfigs]
            verbs: [get, list, watch]
          - apiGroups:
            - status.gatekeeper.sh
            resources: [constraintpodstatuses, constrainttemplatepodstatuses, expansiontemplatepodstatuses]
            verbs: [get, list, watch]
          - apiGroups:
            - telemetry.istio.io
            resources: [*]
            verbs: [get, list, watch]
          - apiGroups:
            - templates.gatekeeper.sh
            resources: [constrainttemplates]
            verbs: [get, list, watch]
          - apiGroups:
            - vm.cluster.gke.io
            resources: [gpuallocation, guestenvironmentdata, virtualmachineaccessrequest, virtualmachinedisk, virtualmachinepasswordresetrequest, virtualmachinetype, vmhighavailabilitypolicy, vmruntimes]
            verbs: [get, list, watch]
          - apiGroups:
            - '*'
            resources: [componentstatuses, configmaps, endpoints, events, horizontalpodautoscalers, limitranges, namespaces, nodes, persistentvolumeclaims, persistentvolumes, pods, pods/log, podtemplates, replicationcontrollers, resourcequotas, serviceaccounts, services]
            verbs: [get, list, watch]
          - apiGroups:
            - onprem.cluster.gke.io
            resources: [onpremadminclusters, onpremnodepools, onpremuserclusters, validations, onpremplatforms, onprembundles, clusterstates]
            verbs: [get, list, watch]
          - apiGroups:
            - vsphereproviderconfig.k8s.io
            resources: [vsphereclusterproviderconfigs, vspheremachineproviderconfigs]
            verbs: [get, list, watch]
          ---
          apiVersion: rbac.authorization.k8s.io/v1
          kind: ClusterRoleBinding
          metadata:
            creationTimestamp: null
            name: fleet-rrb-actuation-gke-fleet-support-access
          roleRef:
            apiGroup: ""
            kind: ClusterRole
            name: fleet-rrb-actuation-gke-fleet-support-access
          subjects:
          - kind: User
            name: service-{PROJECT-NUMBER}@gcp-sa-anthossupport.iam.gserviceaccount.com
          

### Google Distributed Cloud for Bare Metal
    
    
          apiVersion: rbac.authorization.k8s.io/v1
          kind: ClusterRole
          metadata:
            creationTimestamp: null
            name: fleet-rrb-imp-actuation-gke-fleet-support-access
          rules:
          - apiGroups:
            - ""
            resourceNames:
            - service-{PROJECT-NUMBER}@gcp-sa-anthossupport.iam.gserviceaccount.com
            resources:
            - users
            verbs:
            - impersonate
          ---
          apiVersion: rbac.authorization.k8s.io/v1
          kind: ClusterRoleBinding
          metadata:
            creationTimestamp: null
            name: fleet-rrb-imp-actuation-gke-fleet-support-access
          roleRef:
            apiGroup: ""
            kind: ClusterRole
            name: fleet-rrb-imp-actuation-gke-fleet-support-access
          subjects:
          - kind: ServiceAccount
            name: connect-agent-sa
            namespace: gke-connect
          ---
          apiVersion: rbac.authorization.k8s.io/v1
          kind: ClusterRole
          metadata:
            creationTimestamp: null
            name: fleet-rrb-actuation-gke-fleet-support-access
          rules:
          - apiGroups:
            - acme.cert-manager.io
            resources: [challenges, orders]
            verbs: [get, list, watch]
          - apiGroups:
            - addons.gke.io
            resources:[metricsserver, monitoring, stackdrivers]
            verbs: [get, list, watch]
          - apiGroups:
            - admissionregistration.k8s.io
            resources: [mutatingwebhookconfigurations, validatingwebhookconfigurations]
            verbs: [get, list, watch]
          - apiGroups:
            - anthos.gke.io
            resources: [entitlements, healthcheckjobs, healthchecks]
            verbs: [get, list, watch]
          - apiGroups:
            - apiextensions.k8s.io
            resources: [customresourcedefinitions]
            verbs: [get, list, watch]
          - apiGroups:
            - apiregistration.k8s.io
            resources: [apiservices]
            verbs: [get, list, watch]
          - apiGroups:
            - apiserver.k8s.io
            resources: [flowschemas, prioritylevelconfigurations]
            verbs: [get, list, watch]
          - apiGroups:
            - apps
            resources: [controllerrevisions, daemonsets, deployments, replicasets, statefulset]
            verbs: [get, list, watch]
          - apiGroups:
            - apps.k8s.io
            resources: [applications]
            verbs: [get, list, watch]
          - apiGroups:
            - authentication.gke.io
            resources: [clientconfigs]
            verbs: [get, list, watch]
          - apiGroups:
            - batch
            resources: [cronjobs, jobs]
            verbs: [get, list, watch]
          - apiGroups:
            - bootstrap.cluster.x-k8s.io
            resources: [kubeadmconfigs, kubeadmconfigtemplates]
            verbs: [get, list, watch]
          - apiGroups:
            - bundle.gke.io
            resources: [bundlebuilders, bundles, clusterbundles, componentbuilders, componentlists, components, componentsets, gkeonprembundles, packagedeploymentclasses, packagedeployments, patchtemplatebuilders, patchtemplates, requirements]
            verbs: [get, list, watch]
          - apiGroups:
            - bundleext.gke.io
            resources: [nodeconfigs]
            verbs: [get, list, watch]
          - apiGroups:
            - certificates.k8s.io
            resources: [certificatesigningrequests]
            verbs: [get, list, watch]
          - apiGroups:
            - cert-manager.io
            resources: [certificaterequests, certificates, clusterissuers, issuers]
            verbs: [get, list, watch]
          - apiGroups:
            - cilium.io
            resources: [ciliumnodes, ciliumendpoints, ciliumidentities, ciliumegressnatpolicies, ciliumexternalworkloads]
            verbs: [get, list, watch]
          - apiGroups:
            - configmanagement.gke.io
            resources: [configmanagements]
            verbs: [get, list, watch]
          - apiGroups:
            - config.gatekeeper.sh
            resources: [configs]
            verbs: [get, list, watch]
          - apiGroups:
            - coordination.k8s.io
            resources: [leases]
            verbs: [get, list, watch]
          - apiGroups:
            - cluster.k8s.io
            resources: [clusters, controlplanes, machineclasses, machinedeployments, machines, machinesets]
            verbs: [get, list, watch]
          - apiGroups:
            - cluster.x-k8s.io
            resources: [clusters, controlplanes, machineclasses, machinedeployments, machinehealthchecks, machines, machinesets]
            verbs: [get, list, watch]
          - apiGroups:
            - clusterctl.cluster.x-k8s.io
            resources: [metadata, providers]
            verbs: [get, list, watch]
          - apiGroups:
            - crd.projectcalico.org
            resources: [bgpconfigurations, bgppeers, blockaffinities, clusterinformations, felixconfigurations, globalnetworkpolicies, globalnetworksets, hostendpoints, ipamblocks, ipamconfigs, ipamhandles, ippools, networkpolicies, networksets, vpntunnels]
            verbs: [get, list, watch]
          - apiGroups:
            - discovery.k8s.io
            resources: [endpointslices]
            verbs: [get, list, watch]
          - apiGroups:
            - expansion.gatekeeper.sh
            resources: [expansiontemplate]
            verbs: [get, list, watch]
          - apiGroups:
            - extensions.istio.io
            resources: [*]
            verbs: [get, list, watch]
          - apiGroups:
            - gateway.networking.k8s.io
            resources: [gatewayclasses, gateways, grpcroutes, httproutes, referencegrants, tcproutes, tlsroutes, udproutes]
            verbs: [get, list, watch]
          - apiGroups:
            - hub.gke.io
            resources: [memberships]
            verbs: [get, list, watch]
          - apiGroups:
            - install.istio.io
            resources: [*]
            verbs: [get, list, watch]
          - apiGroups:
            - k8s.cni.cncf.io
            resources: [network-attachment-definitions]
            verbs: [get, list, watch]
          - apiGroups:
            - mutations.gatekeeper.sh
            resources: [assign, assignimage, assignmetadata, modifyset, mutatorpodstatuses]
            verbs: [get, list, watch]
          - apiGroups:
            - networking.istio.io
            resources: [*]
            verbs: [get, list, watch]
          - apiGroups:
            - networking.k8s.io
            resources: [ingressclasses, ingresses, multiclusterconnectivityconfigs, networkgatewaygroups, networkgatewaynodes, networkinterfaces, networkloggings, networks, trafficsteerings]
            verbs: [get, list, watch]
          - apiGroups:
            - node.k8s.io
            resources: [runtimeclasses]
            verbs: [get, list, watch]
          - apiGroups:
            - policy
            resources: [poddisruptionbudgets, podsecuritypolicies]
            verbs: [get, list, watch]
          - apiGroups:
            - rbac.authorization.k8s.io
            resources: [clusterroles, clusterrolebindings, roles, rolebindings]
            verbs: [get, list, watch]
          - apiGroups:
            - security.istio.io
            resources: [*]
            verbs: [get, list, watch]
          - apiGroups:
            - storage.k8s.io
            resources: [csidrivers, csinodes, csistoragecapacities, storageclasses, volumeattachments]
            verbs: [get, list, watch]
          - apiGroups:
            - sriovnetwork.k8s.cni.cncf.io
            resources: [sriovnetworknodepolicies, sriovnetworknodestates, sriovoperatorconfigs]
            verbs: [get, list, watch]
          - apiGroups:
            - status.gatekeeper.sh
            resources: [constraintpodstatuses, constrainttemplatepodstatuses, expansiontemplatepodstatuses]
            verbs: [get, list, watch]
          - apiGroups:
            - telemetry.istio.io
            resources: [*]
            verbs: [get, list, watch]
          - apiGroups:
            - templates.gatekeeper.sh
            resources: [constrainttemplates]
            verbs: [get, list, watch]
          - apiGroups:
            - vm.cluster.gke.io
            resources: [gpuallocation, guestenvironmentdata, virtualmachineaccessrequest, virtualmachinedisk, virtualmachinepasswordresetrequest, virtualmachinetype, vmhighavailabilitypolicy, vmruntimes]
            verbs: [get, list, watch]
          - apiGroups:
            - '*'
            resources: [componentstatuses, configmaps, endpoints, events, horizontalpodautoscalers, limitranges, namespaces, nodes, persistentvolumeclaims, persistentvolumes, pods, pods/log, podtemplates, replicationcontrollers, resourcequotas, serviceaccounts, services]
            verbs: [get, list, watch]
          - apiGroups:
            - addon.baremetal.cluster.gke.io
            resources: [addonmanifests, addonoverrides, addons, addonsets, addonsettemplates]
            verbs: [get, list, watch]
          - apiGroups:
            - baremetal.cluster.gke.io
            resources: [addonconfigurations, clustercidrconfigs, clustercredentials, clustermanifestdeployments, clusters, flatipmodes, healthchecks, inventorymachines, kubeletconfigs, machineclasses, machinecredentials, machines, nodepools, nodepoolclaims, nodeproblemdetectors, preflightchecks, secretforwarders]
            verbs: [get, list, watch]
          - apiGroups:
            - infrastructure.baremetal.cluster.gke.io
            resources:
            - baremetalclusters
            - baremetalmachines
            verbs: [get, list, watch]
          - apiGroups:
            - networking.baremetal.cluster.gke.io
            resources:
            - dpv2multinics
            verbs: [get, list, watch]
          ---
          apiVersion: rbac.authorization.k8s.io/v1
          kind: ClusterRoleBinding
          metadata:
            creationTimestamp: null
            name: fleet-rrb-actuation-gke-fleet-support-access
          roleRef:
            apiGroup: ""
            kind: ClusterRole
            name: fleet-rrb-actuation-gke-fleet-support-access
          subjects:
          - kind: User
            name: service-{PROJECT-NUMBER}@gcp-sa-anthossupport.iam.gserviceaccount.com
          

### GKE attached clusters
    
    
          apiVersion: rbac.authorization.k8s.io/v1
          kind: ClusterRole
          metadata:
            creationTimestamp: null
            name: fleet-rrb-imp-actuation-gke-fleet-support-access
          rules:
          - apiGroups:
            - ""
            resourceNames:
            - service-{PROJECT-NUMBER}@gcp-sa-anthossupport.iam.gserviceaccount.com
            resources:
            - users
            verbs:
            - impersonate
          ---
          apiVersion: rbac.authorization.k8s.io/v1
          kind: ClusterRoleBinding
          metadata:
            creationTimestamp: null
            name: fleet-rrb-imp-actuation-gke-fleet-support-access
          roleRef:
            apiGroup: ""
            kind: ClusterRole
            name: fleet-rrb-imp-actuation-gke-fleet-support-access
          subjects:
          - kind: ServiceAccount
            name: connect-agent-sa
            namespace: gke-connect
          ---
          apiVersion: rbac.authorization.k8s.io/v1
          kind: ClusterRole
          metadata:
            creationTimestamp: null
            name: fleet-rrb-actuation-gke-fleet-support-access
          rules:
          - apiGroups:
            - acme.cert-manager.io
            resources: [challenges, orders]
            verbs: [get, list, watch]
          - apiGroups:
            - addons.gke.io
            resources:[metricsserver, monitoring, stackdrivers]
            verbs: [get, list, watch]
          - apiGroups:
            - admissionregistration.k8s.io
            resources: [mutatingwebhookconfigurations, validatingwebhookconfigurations]
            verbs: [get, list, watch]
          - apiGroups:
            - anthos.gke.io
            resources: [entitlements, healthcheckjobs, healthchecks]
            verbs: [get, list, watch]
          - apiGroups:
            - apiextensions.k8s.io
            resources: [customresourcedefinitions]
            verbs: [get, list, watch]
          - apiGroups:
            - apiregistration.k8s.io
            resources: [apiservices]
            verbs: [get, list, watch]
          - apiGroups:
            - apiserver.k8s.io
            resources: [flowschemas, prioritylevelconfigurations]
            verbs: [get, list, watch]
          - apiGroups:
            - apps
            resources: [controllerrevisions, daemonsets, deployments, replicasets, statefulset]
            verbs: [get, list, watch]
          - apiGroups:
            - apps.k8s.io
            resources: [applications]
            verbs: [get, list, watch]
          - apiGroups:
            - authentication.gke.io
            resources: [clientconfigs]
            verbs: [get, list, watch]
          - apiGroups:
            - batch
            resources: [cronjobs, jobs]
            verbs: [get, list, watch]
          - apiGroups:
            - bootstrap.cluster.x-k8s.io
            resources: [kubeadmconfigs, kubeadmconfigtemplates]
            verbs: [get, list, watch]
          - apiGroups:
            - bundle.gke.io
            resources: [bundlebuilders, bundles, clusterbundles, componentbuilders, componentlists, components, componentsets, gkeonprembundles, packagedeploymentclasses, packagedeployments, patchtemplatebuilders, patchtemplates, requirements]
            verbs: [get, list, watch]
          - apiGroups:
            - bundleext.gke.io
            resources: [nodeconfigs]
            verbs: [get, list, watch]
          - apiGroups:
            - certificates.k8s.io
            resources: [certificatesigningrequests]
            verbs: [get, list, watch]
          - apiGroups:
            - cert-manager.io
            resources: [certificaterequests, certificates, clusterissuers, issuers]
            verbs: [get, list, watch]
          - apiGroups:
            - cilium.io
            resources: [ciliumnodes, ciliumendpoints, ciliumidentities, ciliumegressnatpolicies, ciliumexternalworkloads]
            verbs: [get, list, watch]
          - apiGroups:
            - configmanagement.gke.io
            resources: [configmanagements]
            verbs: [get, list, watch]
          - apiGroups:
            - config.gatekeeper.sh
            resources: [configs]
            verbs: [get, list, watch]
          - apiGroups:
            - coordination.k8s.io
            resources: [leases]
            verbs: [get, list, watch]
          - apiGroups:
            - cluster.k8s.io
            resources: [clusters, controlplanes, machineclasses, machinedeployments, machines, machinesets]
            verbs: [get, list, watch]
          - apiGroups:
            - cluster.x-k8s.io
            resources: [clusters, controlplanes, machineclasses, machinedeployments, machinehealthchecks, machines, machinesets]
            verbs: [get, list, watch]
          - apiGroups:
            - clusterctl.cluster.x-k8s.io
            resources: [metadata, providers]
            verbs: [get, list, watch]
          - apiGroups:
            - crd.projectcalico.org
            resources: [bgpconfigurations, bgppeers, blockaffinities, clusterinformations, felixconfigurations, globalnetworkpolicies, globalnetworksets, hostendpoints, ipamblocks, ipamconfigs, ipamhandles, ippools, networkpolicies, networksets, vpntunnels]
            verbs: [get, list, watch]
          - apiGroups:
            - discovery.k8s.io
            resources: [endpointslices]
            verbs: [get, list, watch]
          - apiGroups:
            - expansion.gatekeeper.sh
            resources: [expansiontemplate]
            verbs: [get, list, watch]
          - apiGroups:
            - extensions.istio.io
            resources: [*]
            verbs: [get, list, watch]
          - apiGroups:
            - gateway.networking.k8s.io
            resources: [gatewayclasses, gateways, grpcroutes, httproutes, referencegrants, tcproutes, tlsroutes, udproutes]
            verbs: [get, list, watch]
          - apiGroups:
            - hub.gke.io
            resources: [memberships]
            verbs: [get, list, watch]
          - apiGroups:
            - install.istio.io
            resources: [*]
            verbs: [get, list, watch]
          - apiGroups:
            - k8s.cni.cncf.io
            resources: [network-attachment-definitions]
            verbs: [get, list, watch]
          - apiGroups:
            - mutations.gatekeeper.sh
            resources: [assign, assignimage, assignmetadata, modifyset, mutatorpodstatuses]
            verbs: [get, list, watch]
          - apiGroups:
            - networking.istio.io
            resources: [*]
            verbs: [get, list, watch]
          - apiGroups:
            - networking.k8s.io
            resources: [ingressclasses, ingresses, multiclusterconnectivityconfigs, networkgatewaygroups, networkgatewaynodes, networkinterfaces, networkloggings, networks, trafficsteerings]
            verbs: [get, list, watch]
          - apiGroups:
            - node.k8s.io
            resources: [runtimeclasses]
            verbs: [get, list, watch]
          - apiGroups:
            - policy
            resources: [poddisruptionbudgets, podsecuritypolicies]
            verbs: [get, list, watch]
          - apiGroups:
            - rbac.authorization.k8s.io
            resources: [clusterroles, clusterrolebindings, roles, rolebindings]
            verbs: [get, list, watch]
          - apiGroups:
            - security.istio.io
            resources: [*]
            verbs: [get, list, watch]
          - apiGroups:
            - storage.k8s.io
            resources: [csidrivers, csinodes, csistoragecapacities, storageclasses, volumeattachments]
            verbs: [get, list, watch]
          - apiGroups:
            - sriovnetwork.k8s.cni.cncf.io
            resources: [sriovnetworknodepolicies, sriovnetworknodestates, sriovoperatorconfigs]
            verbs: [get, list, watch]
          - apiGroups:
            - status.gatekeeper.sh
            resources: [constraintpodstatuses, constrainttemplatepodstatuses, expansiontemplatepodstatuses]
            verbs: [get, list, watch]
          - apiGroups:
            - telemetry.istio.io
            resources: [*]
            verbs: [get, list, watch]
          - apiGroups:
            - templates.gatekeeper.sh
            resources: [constrainttemplates]
            verbs: [get, list, watch]
          - apiGroups:
            - vm.cluster.gke.io
            resources: [gpuallocation, guestenvironmentdata, virtualmachineaccessrequest, virtualmachinedisk, virtualmachinepasswordresetrequest, virtualmachinetype, vmhighavailabilitypolicy, vmruntimes]
            verbs: [get, list, watch]
          - apiGroups:
            - '*'
            resources: [componentstatuses, configmaps, endpoints, events, horizontalpodautoscalers, limitranges, namespaces, nodes, persistentvolumeclaims, persistentvolumes, pods, pods/log, podtemplates, replicationcontrollers, resourcequotas, serviceaccounts, services]
            verbs: [get, list, watch]
          ---
          apiVersion: rbac.authorization.k8s.io/v1
          kind: ClusterRoleBinding
          metadata:
            creationTimestamp: null
            name: fleet-rrb-actuation-gke-fleet-support-access
          roleRef:
            apiGroup: ""
            kind: ClusterRole
            name: fleet-rrb-actuation-gke-fleet-support-access
          subjects:
          - kind: User
            name: service-{PROJECT-NUMBER}@gcp-sa-anthossupport.iam.gserviceaccount.com
          

### GKE clusters
    
    
          apiVersion: rbac.authorization.k8s.io/v1
          kind: ClusterRole
          metadata:
            creationTimestamp: null
            name: fleet-rrb-imp-actuation-gke-fleet-support-access
          rules:
          - apiGroups:
            - ""
            resourceNames:
            - service-{PROJECT-NUMBER}@gcp-sa-anthossupport.iam.gserviceaccount.com
            resources:
            - users
            verbs:
            - impersonate
          ---
          apiVersion: rbac.authorization.k8s.io/v1
          kind: ClusterRoleBinding
          metadata:
            creationTimestamp: null
            name: fleet-rrb-imp-actuation-gke-fleet-support-access
          roleRef:
            apiGroup: ""
            kind: ClusterRole
            name: fleet-rrb-imp-actuation-gke-fleet-support-access
          subjects:
          - kind: ServiceAccount
            name: connect-agent-sa
            namespace: gke-connect
          ---
          apiVersion: rbac.authorization.k8s.io/v1
          kind: ClusterRole
          metadata:
            creationTimestamp: null
            name: fleet-rrb-actuation-gke-fleet-support-access
          rules:
          - apiGroups:
            - acme.cert-manager.io
            resources: [challenges, orders]
            verbs: [get, list, watch]
          - apiGroups:
            - addons.gke.io
            resources:[metricsserver, monitoring, stackdrivers]
            verbs: [get, list, watch]
          - apiGroups:
            - admissionregistration.k8s.io
            resources: [mutatingwebhookconfigurations, validatingwebhookconfigurations]
            verbs: [get, list, watch]
          - apiGroups:
            - anthos.gke.io
            resources: [entitlements, healthcheckjobs, healthchecks]
            verbs: [get, list, watch]
          - apiGroups:
            - apiextensions.k8s.io
            resources: [customresourcedefinitions]
            verbs: [get, list, watch]
          - apiGroups:
            - apiregistration.k8s.io
            resources: [apiservices]
            verbs: [get, list, watch]
          - apiGroups:
            - apiserver.k8s.io
            resources: [flowschemas, prioritylevelconfigurations]
            verbs: [get, list, watch]
          - apiGroups:
            - apps
            resources: [controllerrevisions, daemonsets, deployments, replicasets, statefulset]
            verbs: [get, list, watch]
          - apiGroups:
            - apps.k8s.io
            resources: [applications]
            verbs: [get, list, watch]
          - apiGroups:
            - authentication.gke.io
            resources: [clientconfigs]
            verbs: [get, list, watch]
          - apiGroups:
            - batch
            resources: [cronjobs, jobs]
            verbs: [get, list, watch]
          - apiGroups:
            - bootstrap.cluster.x-k8s.io
            resources: [kubeadmconfigs, kubeadmconfigtemplates]
            verbs: [get, list, watch]
          - apiGroups:
            - bundle.gke.io
            resources: [bundlebuilders, bundles, clusterbundles, componentbuilders, componentlists, components, componentsets, gkeonprembundles, packagedeploymentclasses, packagedeployments, patchtemplatebuilders, patchtemplates, requirements]
            verbs: [get, list, watch]
          - apiGroups:
            - bundleext.gke.io
            resources: [nodeconfigs]
            verbs: [get, list, watch]
          - apiGroups:
            - certificates.k8s.io
            resources: [certificatesigningrequests]
            verbs: [get, list, watch]
          - apiGroups:
            - cert-manager.io
            resources: [certificaterequests, certificates, clusterissuers, issuers]
            verbs: [get, list, watch]
          - apiGroups:
            - cilium.io
            resources: [ciliumnodes, ciliumendpoints, ciliumidentities, ciliumegressnatpolicies, ciliumexternalworkloads]
            verbs: [get, list, watch]
          - apiGroups:
            - configmanagement.gke.io
            resources: [configmanagements]
            verbs: [get, list, watch]
          - apiGroups:
            - config.gatekeeper.sh
            resources: [configs]
            verbs: [get, list, watch]
          - apiGroups:
            - coordination.k8s.io
            resources: [leases]
            verbs: [get, list, watch]
          - apiGroups:
            - cluster.k8s.io
            resources: [clusters, controlplanes, machineclasses, machinedeployments, machines, machinesets]
            verbs: [get, list, watch]
          - apiGroups:
            - cluster.x-k8s.io
            resources: [clusters, controlplanes, machineclasses, machinedeployments, machinehealthchecks, machines, machinesets]
            verbs: [get, list, watch]
          - apiGroups:
            - clusterctl.cluster.x-k8s.io
            resources: [metadata, providers]
            verbs: [get, list, watch]
          - apiGroups:
            - crd.projectcalico.org
            resources: [bgpconfigurations, bgppeers, blockaffinities, clusterinformations, felixconfigurations, globalnetworkpolicies, globalnetworksets, hostendpoints, ipamblocks, ipamconfigs, ipamhandles, ippools, networkpolicies, networksets, vpntunnels]
            verbs: [get, list, watch]
          - apiGroups:
            - discovery.k8s.io
            resources: [endpointslices]
            verbs: [get, list, watch]
          - apiGroups:
            - expansion.gatekeeper.sh
            resources: [expansiontemplate]
            verbs: [get, list, watch]
          - apiGroups:
            - extensions.istio.io
            resources: [*]
            verbs: [get, list, watch]
          - apiGroups:
            - gateway.networking.k8s.io
            resources: [gatewayclasses, gateways, grpcroutes, httproutes, referencegrants, tcproutes, tlsroutes, udproutes]
            verbs: [get, list, watch]
          - apiGroups:
            - hub.gke.io
            resources: [memberships]
            verbs: [get, list, watch]
          - apiGroups:
            - install.istio.io
            resources: [*]
            verbs: [get, list, watch]
          - apiGroups:
            - k8s.cni.cncf.io
            resources: [network-attachment-definitions]
            verbs: [get, list, watch]
          - apiGroups:
            - mutations.gatekeeper.sh
            resources: [assign, assignimage, assignmetadata, modifyset, mutatorpodstatuses]
            verbs: [get, list, watch]
          - apiGroups:
            - networking.istio.io
            resources: [*]
            verbs: [get, list, watch]
          - apiGroups:
            - networking.k8s.io
            resources: [ingressclasses, ingresses, multiclusterconnectivityconfigs, networkgatewaygroups, networkgatewaynodes, networkinterfaces, networkloggings, networks, trafficsteerings]
            verbs: [get, list, watch]
          - apiGroups:
            - node.k8s.io
            resources: [runtimeclasses]
            verbs: [get, list, watch]
          - apiGroups:
            - policy
            resources: [poddisruptionbudgets, podsecuritypolicies]
            verbs: [get, list, watch]
          - apiGroups:
            - rbac.authorization.k8s.io
            resources: [clusterroles, clusterrolebindings, roles, rolebindings]
            verbs: [get, list, watch]
          - apiGroups:
            - security.istio.io
            resources: [*]
            verbs: [get, list, watch]
          - apiGroups:
            - storage.k8s.io
            resources: [csidrivers, csinodes, csistoragecapacities, storageclasses, volumeattachments]
            verbs: [get, list, watch]
          - apiGroups:
            - sriovnetwork.k8s.cni.cncf.io
            resources: [sriovnetworknodepolicies, sriovnetworknodestates, sriovoperatorconfigs]
            verbs: [get, list, watch]
          - apiGroups:
            - status.gatekeeper.sh
            resources: [constraintpodstatuses, constrainttemplatepodstatuses, expansiontemplatepodstatuses]
            verbs: [get, list, watch]
          - apiGroups:
            - telemetry.istio.io
            resources: [*]
            verbs: [get, list, watch]
          - apiGroups:
            - templates.gatekeeper.sh
            resources: [constrainttemplates]
            verbs: [get, list, watch]
          - apiGroups:
            - vm.cluster.gke.io
            resources: [gpuallocation, guestenvironmentdata, virtualmachineaccessrequest, virtualmachinedisk, virtualmachinepasswordresetrequest, virtualmachinetype, vmhighavailabilitypolicy, vmruntimes]
            verbs: [get, list, watch]
          - apiGroups:
            - '*'
            resources: [componentstatuses, configmaps, endpoints, events, horizontalpodautoscalers, limitranges, namespaces, nodes, persistentvolumeclaims, persistentvolumes, pods, pods/log, podtemplates, replicationcontrollers, resourcequotas, serviceaccounts, services]
            verbs: [get, list, watch]
          ---
          apiVersion: rbac.authorization.k8s.io/v1
          kind: ClusterRoleBinding
          metadata:
            creationTimestamp: null
            name: fleet-rrb-actuation-gke-fleet-support-access
          roleRef:
            apiGroup: ""
            kind: ClusterRole
            name: fleet-rrb-actuation-gke-fleet-support-access
          subjects:
          - kind: User
            name: service-{PROJECT-NUMBER}@gcp-sa-anthossupport.iam.gserviceaccount.com
          

## Audit Google Cloud Support usage

The support team accesses your cluster using a per-project dedicated Google Cloud Service account through the connect gateway API. You can audit all support activities using [Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit).

To review the usage, [enable](https://docs.cloud.google.com/logging/docs/audit/configure-data-access#config-console-enable) Data Access audit logs and look for audit logs with the [caller identity](https://docs.cloud.google.com/logging/docs/audit#user-id) set to `service-PROJECT_NUMBER@gcp-sa-anthossupport.iam.gserviceaccount.com`. You will be able to see the resource accessed in the audit log's `labels.k8s-request-path` field.

For more information on how to view this audit log data, see [Viewing Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit#view-logs).

To view the available audit log operations for connect gateway, see [Audited Operations](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/connect-agent/audit-logging#audited_operations).

## FAQ

### What will Google be able to access?

This flow allows Google Cloud Support to have read-only access to non-PII resources. This means that Google won't have access to sensitive data for example to secrets, tokens, etc. Also, Google Cloud Support won't be able to run commands like `kubectl exec` to shell into pods/nodes to interact with underlying VM/machines directly. The list of resources that can be accessed are documented here.

### What changes will Google be able to make to my cluster?

This provides Google with read-only access, Google Cloud Support will not be able to make any modifications to the cluster. If Google Cloud Support has any suggested actions for resolving the issue, the customer will be asked to run mutation commands.

### How long will Google have this access for?

After the support case is closed, Google removes the support team's permission to access your cluster. You can also manually remove these permissions using the commands here.

### How is the cluster accessed?

Google Cloud Support will use the already enabled Connect Gateway service to access the cluster. No new softwares will be installed on the cluster. See [Connect Security Features](https://cloud.google.com/kubernetes-engine/fleet-management/docs/connect-agent/security-features) for details.

### Why does Google need this access?

This access allows Google Cloud Support to more easily understand the issue by having real-time read-only access to the cluster resources. Additionally, this reduces the back-and-forth communications so Google Cloud Support can triage and resolve issues much faster.

### Where can I see what resources were accessed in my cluster?

You can audit all Google Cloud Support activities on your cluster through Cloud Audit Logs. See here for instructions.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
