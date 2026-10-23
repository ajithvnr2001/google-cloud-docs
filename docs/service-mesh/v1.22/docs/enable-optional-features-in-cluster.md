---
url: https://docs.cloud.google.com/service-mesh/v1.22/docs/enable-optional-features-in-cluster/
title: Enable optional features on an in-cluster control plane \u00a0|\u00a0 Cloud Service Mesh v1.22 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:34:11.821571+00:00
---

# Enable optional features on an in-cluster control plane  |  Cloud Service Mesh v1.22  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.22/docs/enable-optional-features-in-cluster/

You are viewing archived v1.22 Service Mesh documentation.

Available versions

[Cloud Service Mesh latest](https://docs.cloud.google.com/service-mesh/docs)  
[Cloud Service Mesh 1.28 archive](https://docs.cloud.google.com/service-mesh/v1.28/docs)  
[Cloud Service Mesh 1.27 archive](https://docs.cloud.google.com/service-mesh/v1.27/docs)  
[Cloud Service Mesh 1.26 archive](https://docs.cloud.google.com/service-mesh/v1.26/docs)  
[Cloud Service Mesh 1.25 archive](https://docs.cloud.google.com/service-mesh/v1.25/docs)  
[Cloud Service Mesh 1.24 archive](https://docs.cloud.google.com/service-mesh/v1.24/docs)  
[Cloud Service Mesh 1.23 archive](https://docs.cloud.google.com/service-mesh/v1.23/docs)  
[Cloud Service Mesh 1.22 archive](https://docs.cloud.google.com/service-mesh/v1.22/docs)  
[Cloud Service Mesh 1.21 archive](https://docs.cloud.google.com/service-mesh/v1.21/docs)  
[Cloud Service Mesh 1.20 archive](https://docs.cloud.google.com/service-mesh/v1.20/docs)  
[Anthos Service Mesh 1.19 archive](https://docs.cloud.google.com/service-mesh/v1.19/docs)  


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ v1.22 ](https://docs.cloud.google.com/service-mesh/v1.22/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.22/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Enable optional features on an in-cluster control plane

This page describes how to enable optional features on Cloud Service Mesh with an in-cluster control plane.

When you install in-cluster Cloud Service Mesh, the [features that are enabled by default differ by platform](https://docs.cloud.google.com/service-mesh/v1.22/docs/supported-features-in-cluster). You can override the default configuration and enable an optional feature by including an _overlay_ file when you install (or upgrade) Cloud Service Mesh. An overlay file is a YAML file containing an [`IstioOperator`](https://docs.cloud.google.com/service-mesh/v1.22/docs/glossary#istio_operator) custom resource (CR) that you use to configure the control plane. Specify one feature per overlay file. You can layer on more overlays, and each overlay file overrides the configuration on the previous layers.

**Caution:** Using `asmcli install` overwrites the existing control plane configuration. When you enable optional features to an existing installation, make sure to specify all files that you want to keep in the original configuration, as well as the overlay files for the features that you want to enable. We recommended that you store the overlay files that you use for installation in source control so that you can apply the same configurations to your control plane with upgrades or when enabling additional optional features. This ensures no downtime when enabling optional features.

## About the overlay files

The overlay files on this page are in the [`anthos-service-mesh`](https://github.com/GoogleCloudPlatform/anthos-service-mesh-packages/tree/release-1.22/asm/istio/options) package in GitHub. These files contain common customizations to the default configuration. You can use these files as they are, or you can make additional changes to them as needed.

When you install Cloud Service Mesh using `asmcli` script, you can specify one or more overlay files with the `--option` or the `--custom_overlay` options. If you don't need to make any changes to the files in the `anthos-service-mesh` repository, you can use `--option`, and the script fetches the file from GitHub for you. Otherwise, you can make changes to the overlay file, and then use the `--custom_overlay` option to pass it to the `asmcli`.

**Important:** Don't specify more than one `IstioOperator` CR in an overlay file because `istioctl install` only applies the first CR that it finds in the file.Don't include multiple CRs in one overlay file | Create separate overlay files for each CR  
---|---  
![multiple CRs in one yaml](https://docs.cloud.google.com/static/service-mesh/v1.22/docs/images/multiple-configs-one-yaml.png) | ![separate yaml files for each CR](https://docs.cloud.google.com/static/service-mesh/v1.22/docs/images/separate-yaml-files.png)  
  
## How to enable optional features

The following examples are simplified to show only using the custom overlays to enable optional features. Replace `OTHER_FLAGS` with the [required installation flags](https://docs.cloud.google.com/service-mesh/v1.22/docs/unified-install/install-anthos-service-mesh#install_anthos_service_mesh).

**Important:** The order of the files on the command line matters. Be sure to specify the configuration required for the default features first, and then the overlay files after that.

The `asmcli install` command provides two ways to enable an optional feature. The method that you use depends on whether you need to make changes to the overlay file.

  * Use [`--option`](https://docs.cloud.google.com/service-mesh/v1.22/docs/unified-install/reference#options) when you don't need to make any changes to the overlay file. With `--option`, `asmcli` fetches the file from the GitHub repository for you, so you must have an internet connection.
        
        ./asmcli install \
          OTHER_FLAGS \
          --option OPTION_NAME
        

Replace `OPTION_NAME` with the option you want to enable. Be sure to omit the .yaml extension and only include the name of the overlay file, such as `iap-operator` and `attached-cluster`. For a list of options refer to the [`anthos-service-mesh`](https://github.com/GoogleCloudPlatform/anthos-service-mesh-packages/tree/release-1.22/asm/istio/options) package.

  * Use [`--custom_overlay`](https://docs.cloud.google.com/service-mesh/v1.22/docs/unified-install/reference#options) when you need to customize the overlay file.
        
        ./asmcli install \
          OTHER_FLAGS \
          --custom_overlay PATH_TO_FILE
        

Replace `PATH_TO_FILE` with the path to the overlay file you want to use.




## YAML for optional features

The following sections provide the YAML to enable optional and supported features.

## mTLS `STRICT` mode

The `global.mtls.enabled` configuration was removed from the `IstioOperator` CR to avoid issues with upgrades and to provide a more flexible installation. To enable `STRICT` mTLS, configure a [peer authentication policy](https://docs.cloud.google.com/service-mesh/v1.22/docs/security/configuring-mtls) instead.

## Distroless proxy image

As a best practice, you should restrict the contents of a container runtime to only the necessary packages. This approach improves security and the signal-to-noise ratio of Common Vulnerabilities and Exposures (CVE) scanners. Istio provides proxy images based on [distroless base images](https://github.com/GoogleContainerTools/distroless).

The following configuration enables distroless images for the entire Cloud Service Mesh. An image type change requires each pod to restart and get re-injected to take effect.
    
    
    apiVersion: install.istio.io/v1alpha1
    kind: IstioOperator
    spec:
      meshConfig:
        defaultConfig:
          image:
            imageType: distroless
    

The distroless image does not contain any binaries other than the proxy. It is therefore not possible to `exec` a shell or use `curl`, `ping`, or other debug utilities inside the container.

If you run a curl command, you see the following error:
    
    
    error: Internal error occurred: error executing command in container: failed to exec in container: failed to start exec  "<container-id>"
    OCI runtime exec failed: exec failed: unable to start container process: exec: "curl": executable file not found in $PATH: unknown
    

If you run a shell command, you see the following error:
    
    
    error: Internal error occurred: error executing command in container: failed to exec in container: failed to start exec "<container-id>"
    OCI runtime exec failed: exec failed: container_linux.go:380: starting container process caused: exec: "sh": executable file not found in $PATH: unknown
    

If you need access to these tools for specific pods, you may override the `imageType` by using the following pod annotation.
    
    
    sidecar.istio.io/proxyImageType: debug
    

After changing the image type of a deployment via the annotation, the deployment should be restarted.
    
    
    kubectl rollout restart deployment -n NAMESPACE DEPLOYMENT_NAME

For most types of proxy debugging, [`istioctl proxy-cmd`](https://istio.io/latest/docs/ops/diagnostic-tools/proxy-cmd) should be used which does not require a debug base image.

## Use a custom overlay for custom registry

You can use a custom overlay for custom registries, such as if you need to install Cloud Service Mesh from a custom container registry. For example:
    
    
    apiVersion: install.istio.io/v1alpha1
    kind: IstioOperator
    spec:
      hub: {private_registry_url}
    

The following is a list of images for Cloud Service Mesh that you need to mirror to the custom container registry:

  * Install-cni - `gke.gcr.io/asm/install-cni:1.22.8-asm.5`
  * Managed Data Plane - `gke.gcr.io/asm/mdp:1.22.8-asm.5`
  * Pilot - `gke.gcr.io/asm/pilot:1.22.8-asm.5`
  * Proxyv2 - `gke.gcr.io/asm/proxyv2:1.22.8-asm.5`

**Note:** If you use a [Canonical Service](https://docs.cloud.google.com/service-mesh/v1.22/docs/canonical-service), then you also need to mirror the custom container registries `gcr.io/kubebuilder/kube-rbac-proxy:v0.13.1` and `gke.gcr.io/asm/canonical-service-controller:1.10.3-asm.16`.

### Add images to a private registry

To push Cloud Service Mesh images to a private registry, complete the following steps.

**Note:** Use a client from which you can pull from `gcr.io` and push to your private registry.

  1. Pull the Cloud Service Mesh images: 
         
         docker pull gke.gcr.io/asm/install-cni:1.22.8-asm.5
         docker pull gke.gcr.io/asm/mdp:1.22.8-asm.5
         docker pull gke.gcr.io/asm/pilot:1.22.8-asm.5
         docker pull gke.gcr.io/asm/proxyv2:1.22.8-asm.5
         

  2. Create a variable for your private registry URL: 
         
         export PRIVATE_REGISTRY_URL=PRIVATE_REGISTRY_URL
         

Replace `PRIVATE_REGISTRY_URL` with your private registry URL. 
  3. Tag the images with your private registry URL: 
         
         docker tag gke.gcr.io/asm/install-cni:1.22.8-asm.5 \
          ${PRIVATE_REGISTRY_URL}/gke.gcr.io/asm/install-cni:1.22.8-asm.5
         docker tag gke.gcr.io/asm/mdp:1.22.8-asm.5 \
          ${PRIVATE_REGISTRY_URL}/gke.gcr.io/asm/mdp:1.22.8-asm.5
         docker tag gke.gcr.io/asm/pilot:1.22.8-asm.5 \
          ${PRIVATE_REGISTRY_URL}/gke.gcr.io/asm/pilot:1.22.8-asm.5
         docker tag gke.gcr.io/asm/proxyv2:1.22.8-asm.5 \
          ${PRIVATE_REGISTRY_URL}/gke.gcr.io/asm/proxyv2:1.22.8-asm.5
         

  4. Push the tagged images to your private registry: 
         
         docker push ${PRIVATE_REGISTRY_URL}/gke.gcr.io/asm/install-cni:1.22.8-asm.5
         docker push ${PRIVATE_REGISTRY_URL}/gke.gcr.io/asm/mdp:1.22.8-asm.5
         docker push ${PRIVATE_REGISTRY_URL}/gke.gcr.io/asm/pilot:1.22.8-asm.5
         docker push ${PRIVATE_REGISTRY_URL}/gke.gcr.io/asm/proxyv2:1.22.8-asm.5
         

  5. (Optional) If you use a [canonical service](https://docs.cloud.google.com/service-mesh/v1.22/docs/canonical-service), then add the canonical service images to your private registry. 
     1. Pull the Cloud Service Mesh canonical service images: 
            
            docker pull gcr.io/kubebuilder/kube-rbac-proxy:v0.13.1
                    docker pull gke.gcr.io/asm/canonical-service-controller:1.10.3-asm.16
                    

     2. Tag the images with your private registry URL: 
            
            docker tag gcr.io/kubebuilder/kube-rbac-proxy:v0.13.1 \
                    ${PRIVATE_REGISTRY_URL}/gcr.io/kubebuilder/kube-rbac-proxy:v0.13.1
                    docker tag gke.gcr.io/asm/canonical-service-controller:1.10.3-asm.16 \
                    ${PRIVATE_REGISTRY_URL}/gke.gcr.io/asm/canonical-service-controller:1.10.3-asm.16
                    

     3. Push the tagged images to your private registry: 
            
            docker push ${PRIVATE_REGISTRY_URL}/gke.gcr.io/asm/kube-rbac-proxy:v0.13.1
                    docker push ${PRIVATE_REGISTRY_URL}/gke.gcr.io/asm/canonical-service-controller:1.10.3-asm.16
                    




If you can pull the tagged images from your private registry, then the procedure was successful. 

## Increase termination drain duration

By default Envoy will wait five seconds (`5s`) for existing connections to complete when a pod is terminating.

Pod `terminationGracePeriodSeconds` must be greater than `terminationDrainDuration` value.

For more information see [Global Mesh Options](https://istio.io/v1.22/docs/reference/config/istio.mesh.v1alpha1/#ProxyConfig).
    
    
    ---
    apiVersion: install.istio.io/v1alpha1
    kind: IstioOperator
    spec:
      meshConfig:
        defaultConfig:
          terminationDrainDuration: 30s
    

## Enable Access logs
    
    
    ---
    apiVersion: install.istio.io/v1alpha1
    kind: IstioOperator
    spec:
      meshConfig:
        accessLogFile: "/dev/stdout"

For more information, see [Enable Envoy's access logging](https://istio.io/v1.22/docs/tasks/observability/logs/access-log/#enable-envoy-s-access-logging).

## Cloud Trace

Cloud Trace is available with Cloud Service Mesh installations on the following platforms:

  * GKE on Google Cloud
  * GKE Enterprise clusters on-premises if you install with Cloud Service Mesh certificate authority


    
    
    ---
    apiVersion: install.istio.io/v1alpha1
    kind: IstioOperator
    spec:
      meshConfig:
        enableTracing: true
      values:
        global:
          proxy:
            tracer: stackdriver

For more information, see [Accessing traces](https://docs.cloud.google.com/service-mesh/v1.22/docs/observability/accessing-traces).

## Egress via egress gateways

We recommend that you install an [injected gateway](https://docs.cloud.google.com/service-mesh/v1.22/docs/glossary#injection) as described in [Install and upgrade gateways](https://docs.cloud.google.com/service-mesh/v1.22/docs/operate-and-maintain/gateways).

## Istio Container Network Interface

How you enable the Istio Container Network Interface (CNI) depends on the environment that Cloud Service Mesh is installed on.

  1. [Enable a network policy](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy).

  2. Choose the overlay file that matches your platform.




### Enable CNI on GKE
    
    
    ---
    apiVersion: install.istio.io/v1alpha1
    kind: IstioOperator
    spec:
      components:
        cni:
          enabled: true
          namespace: kube-system
      values:
        cni:
          cniBinDir: /home/kubernetes/bin
          excludeNamespaces:
            - istio-system
            - kube-system

### Enable CNI on-premises
    
    
    ---
    apiVersion: install.istio.io/v1alpha1
    kind: IstioOperator
    spec:
      components:
        cni:
          enabled: true
          namespace: kube-system
      values:
        cni:
          cniBinDir: /opt/cni/bin
          excludeNamespaces:
            - istio-system
            - kube-system
            - gke-system

## Enable Traffic logs for off-Google Cloud

Installing Cloud Service Mesh with Istio CA outside of Google Cloud reports metrics to Prometheus by default. Use this option to enable reporting Traffic logs instead, or both Prometheus and Stackdriver, so you can use the Cloud Service Mesh dashboards.

### Only Stackdriver
    
    
    ---
    apiVersion: install.istio.io/v1alpha1
    kind: IstioOperator
    spec:
      values:
        telemetry:
          enabled: true
          v2:
            enabled: true
            prometheus:
              enabled: false
            stackdriver:
              enabled: true

### Stackdriver and Prometheus
    
    
    ---
    apiVersion: install.istio.io/v1alpha1
    kind: IstioOperator
    spec:
      values:
        telemetry:
          enabled: true
          v2:
            enabled: true
            prometheus:
              enabled: true
            stackdriver:
              enabled: true

## Enable an internal load balancer

We recommend that you install an [injected gateway](https://docs.cloud.google.com/service-mesh/v1.22/docs/glossary#injection) as described in [Install and upgrade gateways](https://docs.cloud.google.com/service-mesh/v1.22/docs/operate-and-maintain/gateways) to set up an internal load balancer on GKE. When configuring the gateway Service, you include the annotation: `networking.gke.io/load-balancer-type: "Internal"`

## External certificate management on the ingress gateway

For information on enabling external certificate management on the ingress gateway using Envoy SDS, see [Secure Gateways](https://istio.io/v1.22/docs/tasks/traffic-management/ingress/secure-ingress/).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
