---
url: https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/set-up-gke-pods-auto/
title: Set up Google Kubernetes Engine Pods using automatic Envoy injection \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:32:27.169280+00:00
---

# Set up Google Kubernetes Engine Pods using automatic Envoy injection  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/set-up-gke-pods-auto/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Set up Google Kubernetes Engine Pods using automatic Envoy injection

## Overview

**Note:** This guide only supports Cloud Service Mesh with Google Cloud APIs and does not support Istio APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview).

In a service mesh, your application code doesn't need to know about your networking configuration. Instead, your applications communicate over a data plane, which is configured by a control plane that handles service networking. In this guide, Cloud Service Mesh is your control plane and the Envoy sidecar proxies are your data plane.

The Google managed Envoy sidecar injector adds Envoy sidecar proxies to your Google Kubernetes Engine Pods. When the Envoy sidecar injector adds a proxy, it also sets that proxy up to handle application traffic and connect to Cloud Service Mesh for configuration.

The guide walks you through a simple setup of Cloud Service Mesh with Google Kubernetes Engine. These steps provide the foundation that you can extend to advanced use cases, such as a service mesh that extends across multiple Google Kubernetes Engine clusters and, potentially, Compute Engine VMs. You can also use these instructions if you are configuring Cloud Service Mesh with Shared VPC.

The setup process involves:

  1. Creating a GKE cluster for your workloads.
  2. Installing the Envoy sidecar injector and enabling injection.
  3. Deploying a sample client and verifying injection.
  4. Deploying a Kubernetes service for testing.
  5. Configuring Cloud Service Mesh with Cloud Load Balancing components to route traffic to the test service.
  6. Verifying the configuration by sending a request from the sample client to the test service.

[ ![Overview of components deployed as part of this setup guide \(click to enlarge\)](https://docs.cloud.google.com/static/service-mesh/docs/images/td-auto-injector.png)](https://docs.cloud.google.com/static/service-mesh/docs/images/td-auto-injector.png) Overview of components deployed as part of this setup guide (click to enlarge)

## Prerequisites

Before you follow the instructions in this guide, complete the prerequisite tasks described in [Prepare to set up on service routing APIs with Envoy and proxyless workloads](https://docs.cloud.google.com/service-mesh/docs/onboarding/prepare-service-routing-envoy-proxyless).

For information about the Envoy version that is supported, see the [Cloud Service Mesh release notes](https://docs.cloud.google.com/service-mesh/docs/service-routing/release-notes).

**Note:** The sidecar injector and injected proxy are based on Istio's sidecar injector. Don't install the Envoy sidecar injector if you've already deployed Istio to your GKE cluster because this might cause conflicts in injection behavior.

### Additional prerequisites with Shared VPC

If you are setting up Cloud Service Mesh in a Shared VPC environment, make sure of the following.

  * You have the correct permissions and roles for Shared VPC.
  * You have set up the correct projects and billing.
  * You have enabled billing in the projects.
  * You have enabled the Cloud Service Mesh and GKE APIs in each project, including the host project.
  * You have set up the correct service accounts for each project.
  * You have created a VPC network and subnets.
  * You have enabled Shared VPC.



For more information, see [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc).

#### Configure IAM roles

This example of IAM role configuration assumes that the host project for Shared VPC has two subnets and there are two service projects in the Shared VPC.

  1. In Cloud Shell, create a working folder (`WORKDIR)` where you create the files associated with this section:
         
         mkdir -p ~/td-shared-vpc
         cd ~/td-shared-vpc
         export WORKDIR=$(pwd)
         

  2. Configure IAM permissions in the host project so that service projects can use the resources in the shared VPC.

In this step, you configure the IAM permissions so that `subnet-1` is accessible by service project 1 and `subnet-2` is accessible by service project 2. You assign the [Compute Network User IAM role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute) (`roles/compute.networkUser`) to both the Compute Engine compute default service account and the Google Cloud API service account in each service project for each subnet.

     1. For service project 1, configure IAM permissions for `subnet-1`:
            
            export SUBNET_1_ETAG=$(gcloud beta compute networks subnets get-iam-policy subnet-1 --project ${HOST_PROJECT} --region ${REGION_1} --format=json | jq -r '.etag')
            
            cat > subnet-1-policy.yaml <<EOF
            bindings:
            - members:
              - serviceAccount:${SVC_PROJECT_1_API_SA}
              - serviceAccount:${SVC_PROJECT_1_GKE_SA}
              role: roles/compute.networkUser
            etag: ${SUBNET_1_ETAG}
            EOF
            
            gcloud beta compute networks subnets set-iam-policy subnet-1 \
            subnet-1-policy.yaml \
                --project ${HOST_PROJECT} \
                --region ${REGION_1}
            

     2. For service project 2, configure IAM permissions for `subnet-2`:
            
            export SUBNET_2_ETAG=$(gcloud beta compute networks subnets get-iam-policy subnet-2 --project ${HOST_PROJECT} --region ${REGION_2} --format=json | jq -r '.etag')
            
            cat > subnet-2-policy.yaml <<EOF
            bindings:
            - members:
              - serviceAccount:${SVC_PROJECT_2_API_SA}
              - serviceAccount:${SVC_PROJECT_2_GKE_SA}
              role: roles/compute.networkUser
            etag: ${SUBNET_2_ETAG}
            EOF
            
            gcloud beta compute networks subnets set-iam-policy subnet-2 \
            subnet-2-policy.yaml \
                --project ${HOST_PROJECT} \
                --region ${REGION_2}
            

  3. For each service project, you must grant the [Kubernetes Engine Host Service Agent User IAM role](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/iam#host_service_agent_user) (`roles/container.hostServiceAgentUser`) to the GKE service account in the host project:
         
         gcloud projects add-iam-policy-binding ${HOST_PROJECT} \
             --member serviceAccount:${SVC_PROJECT_1_GKE_SA} \
             --role roles/container.hostServiceAgentUser
         
         gcloud projects add-iam-policy-binding ${HOST_PROJECT} \
             --member serviceAccount:${SVC_PROJECT_2_GKE_SA} \
             --role roles/container.hostServiceAgentUser
         

This role lets the GKE service account of the service project use the GKE service account of the host project to configure shared network resources.

  4. For each service project, grant the Compute Engine default service account the [Compute Network Viewer IAM role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute) (`roles/compute.networkViewer`) in the host project.
         
         gcloud projects add-iam-policy-binding ${SVC_PROJECT_1} \
             --member serviceAccount:${SVC_PROJECT_1_COMPUTE_SA} \
             --role roles/compute.networkViewer
         
         gcloud projects add-iam-policy-binding ${SVC_PROJECT_2} \
             --member serviceAccount:${SVC_PROJECT_2_COMPUTE_SA} \
             --role roles/compute.networkViewer
         

When the Envoy sidecar proxy connects to the [xDS](https://www.envoyproxy.io/docs/envoy/latest/api-docs/xds_protocol) service (Traffic Director API), the proxy uses the service account of the Compute Engine virtual machine (VM) host or of the GKE node instance. The service account must have the `compute.globalForwardingRules.get` project-level IAM permission. The Compute Network Viewer role is sufficient for this step.




## Configure project information

If you haven't created Google Cloud Project or installed Google Cloud CLI yet, follow these [instructions](https://docs.cloud.google.com/sdk/docs/install-sdk#before-you-begin). If you haven't installed kubectl yet, follow these [instructions](https://docs.cloud.google.com/kubernetes-engine/%0Adocs/how-to/cluster-access-for-kubectl#install_kubectl).
    
    
    # The project that contains your GKE cluster.
    export CLUSTER_PROJECT_ID=YOUR_CLUSTER_PROJECT_ID_HERE
    # The name of your GKE cluster.
    export CLUSTER=YOUR_CLUSTER_NAME
    # The channel of your GKE cluster. Eg: rapid, regular, stable. This channel
    # should correspond to the channel for your GKE cluster. If your GKE cluster
    # does not have a specified channel, please use unspecified in this field.
    export CHANNEL=YOUR_CLUSTER_CHANNEL
    # The location of your GKE cluster, Eg: us-central1 for regional GKE cluster,
    # us-central1-a for zonal GKE cluster
    export LOCATION=ZONE
    
    # The network name of the traffic director load balancing API.
    export MESH_NAME=default
    # The project that holds the mesh resources.
    export MESH_PROJECT_NUMBER=YOUR_MESH_PROJECT_NUMBER_HERE
    
    export TARGET=projects/${MESH_PROJECT_NUMBER}/global/networks/${MESH_NAME}
    
    gcloud config set project ${CLUSTER_PROJECT_ID}
    

If you are using the new [service routing APIs](https://docs.cloud.google.com/service-mesh/docs/service-routing/service-routing-overview), for [mesh resource](https://docs.cloud.google.com/service-mesh/docs/service-routing/service-routing-overview#mesh-resource), use the following instructions to set `MESH_NAME`, `MESH_PROJECT_NUMBER` and `TARGET`:
    
    
    # The mesh name of the traffic director load balancing API.
    export MESH_NAME=YOUR_MESH_NAME
    # The project that holds the mesh resources.
    export MESH_PROJECT_NUMBER=YOUR_MESH_PROJECT_NUMBER_HERE
    
    export TARGET=projects/${MESH_PROJECT_NUMBER}/locations/global/meshes/${MESH_NAME}
    

For [gateway resource](https://docs.cloud.google.com/service-mesh/docs/service-routing/service-routing-overview#gateway-resource), use the following instructions to set `SCOPE_NAME`, `SCOPE_PROJECT_NUMBER` and `TARGET`:
    
    
    # The gateway scope name of the traffic director load balancing API.
    export SCOPE_NAME=YOUR_SCOPE_NAME
    # The project that holds the gateway resources.
    export SCOPE_PROJECT_NUMBER=YOUR_GATEWAY_PROJECT_NUMBER_HERE
    
    export TARGET=projects/${SCOPE_PROJECT_NUMBER}/locations/global/gatewayScopes/${SCOPE_NAME}
    

In most scenarios, `CLUSTER_PROJECT_ID` and `MESH_PROJECT_NUMBER` refer to the same project. However, if you set up the different project, such as when using a Shared VPC, the `CLUSTER_PROJECT_ID` refers to the project ID that contains your GKE cluster, and the `MESH_PROJECT_NUMBER` refers to the project number that contains the resources. Ensure that you have configured the appropriate permissions to allow injected envoy to retrieve configurations from the

## Enable Mesh Config API

Enable the following API to get started with Google managed sidecar injector.
    
    
    gcloud services enable --project=${CLUSTER_PROJECT_ID} meshconfig.googleapis.com
    

## Creating a GKE cluster for your workloads

GKE clusters must meet the following requirements to support Cloud Service Mesh:

  * Network endpoint groups support must be enabled. For more information and examples, refer to [Standalone network endpoint groups](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/standalone-neg#requirements).
  * The service account for your GKE nodes/pods must have permission to access the Traffic Director API. For more information about the required permissions, see [Enable the service account to access the Traffic Director API](https://docs.cloud.google.com/service-mesh/docs/onboarding/prepare-service-routing-envoy-proxyless#enable-service-account).



### Creating the GKE cluster

Create a GKE cluster in your preferred zone, for example, `us-central1-a`.
    
    
    gcloud container clusters create YOUR_CLUSTER_NAME \
      --zone ZONE \
      --scopes=https://www.googleapis.com/auth/cloud-platform \
      --enable-ip-alias
    

### Pointing kubectl to the newly created cluster

Change the current context for `kubectl` to the newly created cluster by issuing the following command:
    
    
    gcloud container clusters get-credentials traffic-director-cluster \
        --zone ZONE
    

## Apply the configurations for Mutating Webhook

The following sections provide instructions apply the [MutatingWebhookConfiguration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.30/#mutatingwebhookconfiguration-v1-admissionregistration-k8s-io) to the cluster. When a pod is created, the in-cluster admission controller is invoked. The admission controller, talks to the managed sidecar injector to add the Envoy container to the pod.

Apply the following mutating webhook configurations to your cluster.
    
    
    cat <<EOF | kubectl apply -f -
    apiVersion: admissionregistration.k8s.io/v1
    kind: MutatingWebhookConfiguration
    metadata:
      labels:
        app: sidecar-injector
      name: td-mutating-webhook
    webhooks:
    - admissionReviewVersions:
      - v1beta1
      - v1
      clientConfig:
        url: https://meshconfig.googleapis.com/v1internal/projects/${CLUSTER_PROJECT_ID}/locations/${LOCATION}/clusters/${CLUSTER}/channels/${CHANNEL}/targets/${TARGET}:tdInject
      failurePolicy: Fail
      matchPolicy: Exact
      name: namespace.sidecar-injector.csm.io
      namespaceSelector:
        matchExpressions:
        - key: td-injection
          operator: Exists
      reinvocationPolicy: Never
      rules:
      - apiGroups:
        - ""
        apiVersions:
        - v1
        operations:
        - CREATE
        resources:
        - pods
        scope: '*'
      sideEffects: None
      timeoutSeconds: 30
    EOF
    

### Enabling sidecar injection

The following command enables injection for the `default` namespace. The sidecar injector injects sidecar containers to pods created under this namespace:
    
    
    kubectl label namespace default td-injection=enabled
    

You can verify that the `default` namespace is properly enabled by running the following command:
    
    
    kubectl get namespace -L td-injection
    

This should return:
    
    
    NAME              STATUS   AGE     TD-INJECTION
    default           Active   7d16h   enabled
    

If you are configuring service security for Cloud Service Mesh with Envoy, return to the section [Setting up a test service](https://docs.cloud.google.com/service-mesh/docs/service-routing/security-envoy-setup#set-up-test-service) in the that setup guide.

## Deploying a sample client and verifying injection

This section shows how to deploy a sample pod running Busybox, which provides a simple interface for reaching a test service. In a real deployment, you would deploy your own client application instead.
    
    
    cat <<EOF | kubectl apply -f -
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      labels:
        run: client
      name: busybox
    spec:
      replicas: 1
      selector:
        matchLabels:
          run: client
      template:
        metadata:
          labels:
            run: client
        spec:
          containers:
          - name: busybox
            image: busybox
            command:
            - sh
            - -c
            - while true; do sleep 1; done
    EOF
    

The Busybox pod consists of two containers. The first container is the client based on the Busybox image and the second container is the Envoy proxy injected by the sidecar injector. You can get more information about the pod by running the following command:
    
    
    kubectl describe pods -l run=client
    

This should return:
    
    
    …
    Init Containers:
    # Istio-init sets up traffic interception for the pod.
      Istio-init:
    …
    Containers:
    # busybox is the client container that runs application code.
      busybox:
    …
    # Envoy is the container that runs the injected Envoy proxy.
      envoy:
    …
    

## Cloud Service Mesh Proxy

The managed sidecar injector will use Cloud Service Mesh Proxy image as the proxy. The Cloud Service Mesh Proxy is a sidecar container responsible for starting an envoy proxy for mesh-enabled instances. The proxy image uses the OSS envoy image along with a proxy agent responsible for starting the envoy, providing bootstrap configuration, and healthchecking of the envoy. The Cloud Service Mesh Proxy image versions align with the OSS Envoy version. You can track the available proxy images here: <https://gcr.io/gke-release/csm/csm-mesh-proxy>. It is recommended to use the latest version of the proxy.

### Cloud Service Mesh Proxy upgrade

Upgrading to the latest version is highly recommended. Although the service mesh is fine when the control plane and proxies are at different versions, we recommend that you update the proxies so that they are configured with the new Cloud Service Mesh version.

The managed sidecar injector takes care of Envoy's version which always injects the latest Envoy version qualified by Google. If the Cloud Service Mesh Proxy version is newer than the proxy version, restart the proxies for your services.
    
    
    kubectl rollout restart deployment -n YOUR_NAMESPACE_HERE
    

## Deploying a Kubernetes service for testing

The following sections provide instructions for setting up a test service that you use later in this guide to provide end-to-end verification of your setup.

### Configuring GKE services with NEGs

GKE services must be exposed through network endpoint groups (NEGs) so that you can configure them as backends of a Cloud Service Mesh backend service. Add the NEG annotation to your Kubernetes service specification and choose a name (by replacing `NEG-NAME` in the sample below) so that you can find it easily later. You need the name when you attach the NEG to your Cloud Service Mesh backend service. For more information on annotating NEGs, see [Naming NEGs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/standalone-neg#naming_negs).

**Note:** The `trafficdirector_service_sample.yaml` package provided with this setup guide uses the NEG name `service-test-neg`.
    
    
    ...
    metadata:
      annotations:
        cloud.google.com/neg: '{"exposed_ports": {"80":{"name": "service-test-neg"}}}'
    spec:
      ports:
      - port: 80
        name: service-test
        protocol: TCP
        targetPort: 8000
    

This annotation creates a standalone NEG containing endpoints corresponding with the IP addresses and ports of the service's pods. For more information and examples, refer to [Standalone network endpoint groups](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/standalone-neg).

The following sample service includes the NEG annotation. The service serves the hostname over HTTP on port `80`. Use the following command to get the service and deploy it to your GKE cluster.
    
    
    wget -q -O - \
    https://storage.googleapis.com/traffic-director/demo/trafficdirector_service_sample.yaml \
    | kubectl apply -f -
    

Verify that the new service is created and the application pod is running:
    
    
    kubectl get svc
    

The output should be similar to the following:
    
    
    NAME             TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
    service-test     ClusterIP   10.71.9.71   none          80/TCP    41m
    [..skip..]
    

Verify that the application pod associated with this service is running:
    
    
    kubectl get pods
    

This returns: 
    
    
    NAME                        READY     STATUS    RESTARTS   AGE
    app1-6db459dcb9-zvfg2       2/2       Running   0          6m
    busybox-5dcf86f4c7-jvvdd    2/2       Running   0          10m
    [..skip..]
    

**Note:** Because the sidecar injector is enabled on the default namespace, sidecar proxies are also injected to the test service pod when it is created. The sidecar injector only configures interception for outbound traffic, so the test service's sidecar proxy is not involved in handling inbound traffic from the sample client.

### Saving the NEG's name

Find the NEG created from the example above and record its name for Cloud Service Mesh configuration in the next section.
    
    
    gcloud compute network-endpoint-groups list
    

This returns the following:
    
    
    NAME                       LOCATION            ENDPOINT_TYPE       SIZE
    service-test-neg           ZONE     GCE_VM_IP_PORT      1
    

Save the NEG's name in the NEG_NAME variable:
    
    
    NEG_NAME=$(gcloud compute network-endpoint-groups list \
    | grep service-test | awk '{print $1}')
    

**Note:** If you named your NEG, as discussed in Configuring GKE services with NEGs you should see that the NEG name matches the one you supplied in the Kubernetes service specification. If you did not name your NEG, a name is auto-generated for you.

## Configuring Cloud Service Mesh with Cloud Load Balancing components

This section configures Cloud Service Mesh using Compute Engine load balancing resources. This enables the sample client's sidecar proxy to receive configuration from Cloud Service Mesh. Outbound requests from the sample client are handled by the sidecar proxy and routed to the test service.

You must configure the following components:

  * A health check. For more information on health checks, read [Health Check Concepts](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts) and [Creating Health Checks](https://docs.cloud.google.com/load-balancing/docs/health-checks).
  * A backend service. For more information on backend services, read [Backend Services](https://docs.cloud.google.com/load-balancing/docs/backend-service).
  * A routing rule map. This includes creating a forwarding rule, a target HTTP proxy and a URL map. For more information, read [Using forwarding rules for Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/service-routing/forwarding-rules), [Using target proxies for Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/service-routing/target-proxies), and [Using URL maps](https://docs.cloud.google.com/load-balancing/docs/https/url-map).



### Creating the health check and firewall rule

Use the following instructions to create a health check and the firewall rule that is required for the health check probes. For more information, see [Firewall rules for health checks](https://docs.cloud.google.com/load-balancing/docs/health-checks#fw-rule).

###  Console 

  1. Go to the Health checks page in the Google Cloud console.   
[Go to the Health checks page](https://console.cloud.google.com/compute/healthChecks)
  2. Click **Create Health Check**.
  3. For the name, enter `td-gke-health-check`.
  4. For the protocol, select **HTTP**.
  5. Click **Create**.

  6. Go to the **Firewall policies** page in the Google Cloud console.   
[Go to the Firewall policies page](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  7. Click **Create firewall rules**.

  8. On the **Create a firewall rule** page, supply the following information:

     * **Name** : Provide a name for the rule. For this example, use `fw-allow-health-checks`.
     * **Network** : Choose a VPC network.
     * **Priority** : Enter a number for the priority. Lower numbers have higher priorities. Be sure that the firewall rule has a higher priority than other rules that might deny ingress traffic.
     * **Direction of traffic** : Choose **Ingress**.
     * **Action on match** : Choose **Allow**.
     * **Targets** : Choose **All instances in the network**.
     * **Source filter** : Choose the correct IP range type.
     * **Source IP ranges** : `35.191.0.0/16,130.211.0.0/22`
     * **Destination filter** : Select the IP type.
     * **Protocols and ports** : Click **Specified ports and protocols** , then check `tcp`. TCP is the underlying protocol for all health check protocols.
     * Click **Create**.



###  gcloud 

  1. Create the [health check](https://docs.cloud.google.com/load-balancing/docs/health-checks).
         
         gcloud compute health-checks create http td-gke-health-check \
           --use-serving-port
         

  2. Create the firewall rule to allow the health checker IP address ranges.
         
         gcloud compute firewall-rules create fw-allow-health-checks \
           --action ALLOW \
           --direction INGRESS \
           --source-ranges 35.191.0.0/16,130.211.0.0/22 \
           --rules tcp
         




### Creating the backend service

Create a global [backend service](https://docs.cloud.google.com/load-balancing/docs/backend-service) with a load balancing scheme of `INTERNAL_SELF_MANAGED`. In the Google Cloud console, the load balancing scheme is set implicitly. Add the health check to the backend service.

###  Console 

  1. Go to the Cloud Service Mesh page in the Google Cloud console. 

[Go to the Cloud Service Mesh page](https://console.cloud.google.com/net-services/trafficdirector/services/list)

  2. On the **Services** tab, click **Create Service**.

  3. Click **Continue**.

  4. For the service name, enter `td-gke-service`.

  5. Select **Network** , which you configured in the Cloud Service Mesh ConfigMap.

  6. Under **Backend type** , select **Network endpoint groups**.

  7. Select the network endpoint group you created.

  8. Set the **Maximum RPS** to `5`.

  9. Set the **Balancing mode** to **Rate**.

  10. Click **Done**.

  11. Under **Health check** , select `td-gke-health-check`, which is the health check you created.

  12. Click **Continue**.




###  gcloud 

  1. Create the backend service and associate the health check with the backend service.
         
         gcloud compute backend-services create td-gke-service \
          --global \
          --health-checks td-gke-health-check \
          --load-balancing-scheme INTERNAL_SELF_MANAGED
         

  2. Add the previously created NEG as a backend to the backend service. If you are configuring Cloud Service Mesh with a target TCP proxy, you must use `UTILIZATION` balancing mode. If you are using an HTTP or HTTPS target proxy, you can use `RATE` mode.
         
         gcloud compute backend-services add-backend td-gke-service \
          --global \
          --network-endpoint-group ${NEG_NAME} \
          --network-endpoint-group-zone ZONE \
          --balancing-mode [RATE | UTILIZATION] \
          --max-rate-per-endpoint 5
         




### Creating the routing rule map

The routing rule map defines how Cloud Service Mesh routes traffic in your mesh. As part of the routing rule map, you configure a virtual IP (VIP) address and a set of associated traffic management rules, such as host-based routing. When an application sends a request to the VIP, the attached Envoy sidecar proxy does the following:

  1. Intercepts the request.
  2. Evaluates it according to the traffic management rules in the URL map.
  3. Selects a backend service based on the hostname in the request.
  4. Chooses a backend or endpoint associated with the selected backend service.
  5. Sends traffic to that backend or endpoint.



###  Console 

In the console, the target proxy is combined with the forwarding rule. When you create the forwarding rule, Google Cloud automatically creates a target HTTP proxy and attaches it to the URL map.

The route rule consist of the forwarding rule and the host and path rules (also known as the URL map).

  1. Go to the Cloud Service Mesh page in the Google Cloud console. 

[Go to the Cloud Service Mesh page](https://console.cloud.google.com/net-services/trafficdirector/services/list)

  2. Click **Routing rule maps**

  3. Click **Create Routing Rule**.

  4. Enter `td-gke-url-map` as the **Name** of the URL map.

  5. Click **Add forwarding rule**.

  6. For the forwarding rule name, enter `td-gke-forwarding-rule`.

  7. Select your network.

  8. Select your **Internal IP**.

  9. Click **Save**.

  10. Optionally, add custom host and path rules or leave the path rules as the defaults.

  11. Set the host to `service-test`.

  12. Click **Save**.




###  gcloud 

  1. Create a URL map that uses `td-gke-service` as the default backend service.
         
         gcloud compute url-maps create td-gke-url-map \
            --default-service td-gke-service
         

  2. Create a URL map path matcher and a host rule to route traffic for your service based on hostname and a path. This example uses `service-test` as the service name and a default path matcher that matches all path requests for this host (`/*`).
         
         gcloud compute url-maps add-path-matcher td-gke-url-map \
            --default-service td-gke-service \
            --path-matcher-name td-gke-path-matcher
         
         gcloud compute url-maps add-host-rule td-gke-url-map \
            --hosts service-test \
            --path-matcher-name td-gke-path-matcher
         

  3. Create the target HTTP proxy.
         
         gcloud compute target-http-proxies create td-gke-proxy \
            --url-map td-gke-url-map
         

  4. Create the forwarding rule.
         
         gcloud compute forwarding-rules create td-gke-forwarding-rule \
           --global \
           --load-balancing-scheme=INTERNAL_SELF_MANAGED \
           --address=0.0.0.0 \
           --target-http-proxy=td-gke-proxy \
           --ports 80 --network default
         




At this point, Cloud Service Mesh configures your sidecar proxies to route requests that specify the `service-test` hostname to backends of `td-gke-service`. In this case, those backends are endpoints in the network endpoint group associated with the Kubernetes test service that you deployed earlier.

**Note:** Because you configured a default service (`td-gke-service`) for the URL map, any outbound request that is handled by a sidecar proxy is routed to the backends associated with this default service.

## Verifying the configuration

This section shows how to verify that traffic sent from the sample Busybox client is routed to your `service-test` Kubernetes service. To send a test request, you can access a shell on one of the containers and execute the following verification command. A `service-test` Pod should return the hostname of the serving pod.
    
    
    # Get the name of the pod running Busybox.
    BUSYBOX_POD=$(kubectl get po -l run=client -o=jsonpath='{.items[0].metadata.name}')
    
    # Command to execute that tests connectivity to the service service-test at
    # the VIP 10.0.0.1. Because 0.0.0.0 is configured in the forwarding rule, this
    # can be any VIP.
    TEST_CMD="wget -q -O - 10.0.0.1; echo"
    
    # Execute the test command on the pod.
    kubectl exec -it $BUSYBOX_POD -c busybox -- /bin/sh -c "$TEST_CMD"
    

Here's how the configuration is verified:

  * The sample client sent a request that specified the `service-test` hostname.
  * The sample client has an Envoy sidecar proxy that was injected by the Envoy sidecar injector.
  * The sidecar proxy intercepted the request.
  * Using the URL map, the Envoy matched the `service-test` hostname to the `td-gke-service` Cloud Service Mesh service.
  * The Envoy chose an endpoint from the network endpoint group associated with `td-gke-service`.
  * The Envoy sent the request to a pod associated with the `service-test` Kubernetes service.



## How to Migrate to Managed Sidecar Injector

This tutorial guides you through migrating an application from the legacy Traffic Director sidecar injector on GKE (with an in-cluster sidecar injector) to one using a managed sidecar injector.

### Disabling in-cluster sidecar injection

The following commands disable the legacy in-cluster sidecar injector for the default namespace
    
    
    kubectl label namespace default istio-injection-
    

### Cleanup in-cluster sidecar injector

Download and extract the legacy Envoy sidecar injector.
    
    
    wget https://storage.googleapis.com/traffic-director/td-sidecar-injector-xdsv3.tgz
    tar -xzvf td-sidecar-injector-xdsv3.tgz
    cd td-sidecar-injector-xdsv3
    

Delete in-cluster sidecar injector resources
    
    
    kubectl delete -f specs/
    

## What's next

  * Learn about [advanced traffic management](https://docs.cloud.google.com/service-mesh/docs/service-routing/advanced-traffic-management)
  * Learn about [Cloud Service Mesh service security](https://docs.cloud.google.com/service-mesh/docs/service-routing/security-overview).
  * Learn how to set up [observability with Envoy](https://docs.cloud.google.com/service-mesh/docs/service-routing/observability-envoy).
  * Learn how to [troubleshoot Cloud Service Mesh deployments](https://docs.cloud.google.com/service-mesh/docs/service-routing/troubleshooting).
  * Learn about [options for Google Kubernetes Engine Pod setup with automatic Envoy injection](https://docs.cloud.google.com/service-mesh/docs/service-routing/auto-gke-options).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
