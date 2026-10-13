---
url: https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/set-up-gke-pods/
title: Set up Google Kubernetes Engine Pods using manual Envoy injection \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:05:00.150193+00:00
---

# Set up Google Kubernetes Engine Pods using manual Envoy injection  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/set-up-gke-pods/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Set up Google Kubernetes Engine Pods using manual Envoy injection

This guide shows you how to configure Google Kubernetes Engine or Kubernetes Pod hosts and the load balancing components that Cloud Service Mesh requires.

**Note:** The configuration examples are for demonstration purposes. You might need to deploy additional components based on your environment and requirements.

Before you follow the instructions in this guide, complete the prerequisite tasks described in [Prepare to set up on service routing APIs with Envoy and proxyless workloads](https://docs.cloud.google.com/service-mesh/docs/onboarding/prepare-service-routing-envoy-proxyless).

You can configure Cloud Service Mesh using the Compute Engine load balancing SDK or REST APIs. See the [load balancing API and gcloud references](https://docs.cloud.google.com/load-balancing/docs/apis).

**Note:** This guide only supports Cloud Service Mesh with Google Cloud APIs and does not support Istio APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview).

## Configuring GKE/Kubernetes clusters for Cloud Service Mesh

This section describes the required steps to enable GKE/Kubernetes clusters to work with Cloud Service Mesh.

### Creating the GKE cluster

GKE clusters must meet the following requirements:

  * Network endpoint groups support must be enabled. For more information and examples, refer to [Standalone network endpoint groups](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/standalone-neg). The standalone NEGs feature is available in General Availability for Cloud Service Mesh.
  * The cluster nodes instances' service account must have permission to access the Cloud Service Mesh API. 
    * For information about the required permissions, see [Enable the service account to access the Traffic Director API](https://docs.cloud.google.com/service-mesh/docs/onboarding/prepare-service-routing-envoy-proxyless#enable-service-account).
    * For information about enabling the Cloud Service Mesh API, see [Enabling the Cloud Service Mesh API](https://docs.cloud.google.com/service-mesh/docs/service-routing/prepare-for-envoy-setup#enable-api).
  * The containers must have access to the Cloud Service Mesh API, protected by OAuth authentication. For more information, refer to [host configuration](https://docs.cloud.google.com/service-mesh/docs/service-routing/set-up-gce-vms#configure-vm-host).



The following example shows how to create a GKE cluster called `traffic-director-cluster` in the `us-central1-a` zone.

### Console

To create a cluster using Google Cloud console, perform the following steps:

  1. Go to the Kubernetes Engine menu in Google Cloud console.

[Go to the Google Kubernetes Engine menu](https://console.cloud.google.com/kubernetes/list)

  2. Click **Create cluster**.

  3. Complete the following fields:

     * **Name:** Enter `traffic-director-cluster`.
     * **Location type:** `Zonal`.
     * **Zone:** `us-central1-a`.
  4. From the navigation pane, under **Node Pools** , click **default-pool**.

  5. The **Size** field indicates the number of nodes to create in the cluster. You must have available [resource quota](https://docs.cloud.google.com/kubernetes-engine/quotas#resource_quota) for the nodes and their resources (such as firewall routes).

  6. From the navigation pane, under **default-pool** , click **Nodes**.

  7. The **Machine type** field indicates the Compute Engine [machine type](https://docs.cloud.google.com/compute/docs/machine-types) to use for the instances. Each machine type is billed differently. For machine type pricing information, refer to the [Compute Engine pricing page](https://cloud.google.com/compute/pricing#machinetype).

  8. From the navigation pane, under **default-pool** , click **Security**.

  9. Under **Access scopes** click **Allow full access to all Cloud APIs**.

  10. Customize your cluster as necessary.

  11. Click **Create**.




After you create a cluster in Google Cloud console, you need to configure `kubectl` to interact with the cluster. To learn more, refer to [Generating a `kubeconfig` entry](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl#generate_kubeconfig_entry).

### gcloud
    
    
    gcloud container clusters create traffic-director-cluster \
      --zone us-central1-a \
      --scopes=https://www.googleapis.com/auth/cloud-platform \
      --enable-ip-alias
    

#### Obtaining the required GKE cluster privileges

For GKE, switch to the cluster(2) you just created by issuing the following command. This points kubectl to the correct cluster.
    
    
    gcloud container clusters get-credentials traffic-director-cluster \
        --zone us-central1-a
    

## Configuring GKE/Kubernetes services

This section shows how to prepare Kubernetes deployment specifications to work with Cloud Service Mesh. This consists of configuring services with NEGs as well as injecting sidecar proxies into Pod s that require access to the services managed by Cloud Service Mesh.

### Configure the firewall rule

To verify that the backend Pods are running, you must configure a firewall rule allowing the health checker IP address ranges.

###  Console 

  1. Go to the **Firewall policies** page in the Google Cloud console.   
[Go to the Firewall policies page](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)
  2. Click **Create firewall rules**.
  3. On the **Create a firewall rule** page, supply the following information: 
     * **Name** : Provide a name for the rule. For this example, use `fw-allow-health-checks`.
     * **Network** : Choose a VPC network.
     * **Priority** : Enter a number for the priority. Lower numbers have higher priorities. Be sure that the firewall rule has a higher priority than other rules that might deny ingress traffic.
     * **Direction of traffic** : Choose **ingress**.
     * **Action on match** : Choose **allow**.
     * **Targets** : Choose **All instances in the network**.
     * **Source filter** : Choose the correct IP range type.
     * **Source IP ranges** : `35.191.0.0/16,130.211.0.0/22`
     * **Destination filter** : Select the IP type.
     * **Protocols and ports** : Click **Specified ports and protocols** , then check `tcp`. TCP is the underlying protocol for all health check protocols.
     * Click **Create**.



###  gcloud 

  1. Use the following `gcloud` command to create a firewall rule named `fw-allow-health-checks` that allows incoming connections to instances in your network with the `allow-health-checks` tag. Replace NETWORK_NAME with the name of your network.
         
         gcloud compute firewall-rules create fw-allow-health-checks \
             --network NETWORK_NAME \
             --action ALLOW \
             --direction INGRESS \
             --source-ranges 35.191.0.0/16,130.211.0.0/22 \
             --rules tcp




For more information, see [configure firewal rule for health checks](https://docs.cloud.google.com/load-balancing/docs/health-checks#firewall_rules).

### Configuring GKE / Kubernetes services with NEGs

GKE services must be exposed through network endpoint groups (NEGs) so that you can configure them as backends of a Cloud Service Mesh backend service. Add the NEG annotation to your Kubernetes service specification and choose a name (by replacing `NEG-NAME` in the sample below) so that you can find it easily later. You need the name when you attach the NEG to your Cloud Service Mesh backend service. For more information on annotating NEGs, see [Naming NEGs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/standalone-neg#naming_negs).

**Note:** The `trafficdirector_service_sample.yaml` package provided with this setup guide uses the NEG name `service-test-neg`.
    
    
    ...
    metadata:
      annotations:
        cloud.google.com/neg: '{"exposed_ports": {"80":{"name": "NEG-NAME"}}}'
    spec:
      ports:
      - port: 80
        name: service-test
        protocol: TCP
        targetPort: 8000
    

For each service, a standalone NEG is created, containing endpoints that are the pod's IP addresses and ports. For more information and examples, refer to [Standalone network endpoint groups](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/standalone-neg).

For demonstration purposes, you can deploy a sample service that serves its hostname over HTTP on port 80:
    
    
    wget -q -O - \
    https://storage.googleapis.com/traffic-director/demo/trafficdirector_service_sample.yaml \
    | kubectl apply -f -
    

Verify that the new service hostname is created and the application Pod is running:
    
    
    kubectl get svc
    

This returns: 
    
    
    NAME             TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
    service-test     ClusterIP   10.71.9.71   none          80/TCP    41m
    [..skip..]
    
    
    
    kubectl get pods
    

This returns: 
    
    
    NAME                        READY     STATUS    RESTARTS   AGE
    app1-6db459dcb9-zvfg2       1/1       Running   0          6m
    [..skip..]
    

#### Saving the NEG's name

Find the NEG created from the example above and record the NEG's name.

### Console

To view a list of network endpoint groups, go to the **Network Endpoint Groups** page in the Google Cloud console.   
[Go to the **Network Endpoint Groups** page](https://console.cloud.google.com/compute/networkendpointgroups/list)

### gcloud
    
    
    gcloud compute network-endpoint-groups list
    

This returns the following:
    
    
    NAME                 LOCATION          ENDPOINT_TYPE      SIZE
    NEG-NAME           us-central1-a     GCE_VM_IP_PORT      1
    

Save the NEG name in the `NEG_NAME` variable, for example:
    
    
    NEG_NAME=$(gcloud compute network-endpoint-groups list \
    | grep service-test | awk '{print $1}')
    

**Note:** If you named your NEG, as discussed in Configuring GKE services with NEGs you should see that the NEG name matches the one you supplied in the Kubernetes service specification. If you did not name your NEG, a name is auto-generated for you.

## Configuring Google Cloud load balancing components for Cloud Service Mesh

The instructions in this section ensure that GKE services are accessible on the service VIP load balanced by Cloud Service Mesh, using a load balancing configuration similar to other [Google Cloud Load Balancing](https://docs.cloud.google.com/load-balancing/docs) products.

You must configure the following components:

  * A health check. For more information on health checks, read [Health Check Concepts](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts) and [Creating Health Checks](https://docs.cloud.google.com/load-balancing/docs/health-checks).
  * A backend service. For more information on backend services, read [Backend Services](https://docs.cloud.google.com/load-balancing/docs/backend-service).
  * A route rule. This includes creating a forwarding rule and a URL map. For more information, read [Using forwarding rules](https://docs.cloud.google.com/load-balancing/docs/forwarding-rules) and [Using URL maps](https://docs.cloud.google.com/load-balancing/docs/https/url-map).



The Cloud Service Mesh configuration example that follows makes these assumptions:

  1. The NEGs and all other resources are created in `default` network, with auto mode, in the zone `us-central1-a`.
  2. The NEG name for the cluster is stored in the `${NEG_NAME}` variable.



### Creating the health check

Create the [health check](https://docs.cloud.google.com/load-balancing/docs/health-checks).

###  Console 

  1. Go to the Health checks page in the Google Cloud console.   
[Go to the Health checks page](https://console.cloud.google.com/compute/healthChecks)
  2. Click **Create Health Check**.
  3. For the name, enter `td-gke-health-check`.
  4. For the protocol, select **HTTP**.
  5. Click **Create**.



###  gcloud 
    
    
    gcloud compute health-checks create http td-gke-health-check \
      --use-serving-port
    

### Creating the backend service

Create a global [backend service](https://docs.cloud.google.com/load-balancing/docs/backend-service#create-backend-service) with a load balancing scheme of **INTERNAL_SELF_MANAGED**. In the Google Cloud console, the load balancing scheme is set implicitly. Add the health check to the backend service.

###  Console 

  1. Go to the Cloud Service Mesh page in the Google Cloud console. 

[Go to the Cloud Service Mesh page](https://console.cloud.google.com/net-services/trafficdirector/services/list)

  2. On the **Services** tab, click **Create Service**.

  3. Click **Continue**.

  4. For the service name, enter `td-gke-service`.

  5. Under **Backend type** , select **Network endpoint groups**.

  6. Select the network endpoint group you created.

  7. Set the **Maximum RPS** to `5`.

  8. Click **Done**.

  9. Under **Health check** , select `td-gke-health-check`, which is the health check you created.

  10. Click **Continue**.




###  gcloud 

  1. Create the backend service and associate the health check with the backend service.
         
         gcloud compute backend-services create td-gke-service \
          --global \
          --health-checks td-gke-health-check \
          --load-balancing-scheme INTERNAL_SELF_MANAGED
         

  2. Add the backend NEGs to the backend service.
         
         gcloud compute backend-services add-backend td-gke-service \
          --global \
          --network-endpoint-group ${NEG_NAME} \
          --network-endpoint-group-zone us-central1-a \
          --balancing-mode RATE \
          --max-rate-per-endpoint 5
         




### Creating the routing rule map

Use these instructions to create the route rule, forwarding rule, and internal IP address for your Cloud Service Mesh configuration.

Traffic sent to the internal IP address is intercepted by the Envoy proxy and sent to the appropriate service according to the host and path rules.

The forwarding rule is created as a global forwarding rule with the `load-balancing-scheme` set to `INTERNAL_SELF_MANAGED`.

You can set the address of your forwarding rule to `0.0.0.0`. If you do, traffic is routed based on the HTTP hostname and path information configured in the URL map, regardless of the actual IP address that the hostname resolves to. In this case, the URLs (hostname plus URL path) of your services, as configured in the host rules, must be unique within your service mesh configuration. That is, you cannot have two different services, with different set of backends, that both use the same hostname and path combination.

Alternatively, you can enable routing based on the actual destination VIP of the service. If you configure the VIP of your service as an `address` parameter of the forwarding rule, only requests destined to this IP address are routed based on the HTTP parameters specified in the URL map.

**Note:** Regardless of the method selected, traffic to the VIP address that your service hostname resolves to must be intercepted by the sidecar proxy on the client host that needs to access your service. Refer to Configuring a single Compute Engine VM for Cloud Service Mesh for full host configuration details.**Note:** Each forwarding rule in a VPC network must have a unique combination of IP address and port per VPC network, including the `0.0.0.0` address. If you create more than one forwarding rule with the same IP address and port in a particular VPC network, only the first forwarding rule is valid. The others are ignored.

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

  1. Create a URL map that uses the backend service.
         
         gcloud compute url-maps create td-gke-url-map \
            --default-service td-gke-service
         

  2. Create a URL map path matcher and a host rule to route traffic for your service based on hostname and a path. This example uses `service-test` as the service name and a default path matcher that matches all path requests for this host (`/*`). `service-test` is also the configured name of the Kubernetes service that is used in the sample configuration above.
         
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
         




At this point, Cloud Service Mesh is configured to load balance traffic for the services specified in the URL map across backends in the network endpoint group.

Depending on how your microservices are distributed on your network, you might need to add more forwarding rules or more host and path rules to the URL map.

## Verifying the configuration by deploying a sample client for tests

This section shows how to reach Cloud Service Mesh backends from a client application.

To demonstrate functionality, you can deploy a sample Pod running Busybox. The pod has access to `service-test`, which was created in the previous section and receives traffic that is load balanced by Cloud Service Mesh.

### Injecting a sidecar proxy into GKE / Kubernetes Pods

To access a service managed by Cloud Service Mesh, a Pod must have an xDS API-compatible sidecar proxy installed.

In this example, you deploy a Busybox client with an Istio-proxy sidecar and init containers added to the deployment using the reference specification.

If you are using the older APIs, replace the PROJECT_NUMBER and NETWORK_NAME variables with your project number and network name:
    
    
    wget -q -O - https://storage.googleapis.com/traffic-director/demo/trafficdirector_client_sample_xdsv3.yaml
    sed -i "s/PROJECT_NUMBER/PROJECT_NUMBER/g" trafficdirector_client_sample_xdsv3.yaml
    sed -i "s/NETWORK_NAME/NETWORK_NAME/g" trafficdirector_client_sample_xdsv3.yaml
    kubectl apply -f trafficdirector_client_sample_xdsv3.yaml
    

If you are using the new [service routing APIs](https://docs.cloud.google.com/service-mesh/docs/service-routing/service-routing-overview), which are currently in preview, replace the PROJECT_NUMBER and MESH_NAME variables with the project number and `Mesh` name:
    
    
    wget -q -O - https://storage.googleapis.com/traffic-director/demo/trafficdirector_client_new_api_sample_xdsv3.yaml
    sed -i "s/PROJECT_NUMBER/PROJECT_NUMBER/g" trafficdirector_client_new_api_sample_xdsv3.yaml
    sed -i "s/MESH_NAME/MESH_NAME/g" trafficdirector_client_new_api_sample_xdsv3.yaml
    kubectl apply -f trafficdirector_client_new_api_sample_xdsv3.yaml
    

The Busybox Pod has two containers running. The first container is the client based on the Busybox image and the second container is the Envoy proxy injected as a sidecar. You can get more information about the Pod by running the following command:
    
    
    kubectl describe pods -l run=client
    

### Reaching the backend service

Once configured, applications on Pods that have a sidecar proxy injected can access services managed by Cloud Service Mesh services. To verify the configuration, you can access a shell on one of the containers.

If you used the demo configuration provided in this guide, you can execute the following verification command to make sure that the hostname of the serving Pod is returned.
    
    
    # Get name of the Pod  with busybox.
    BUSYBOX_POD=$(kubectl get po -l run=client -o=jsonpath='{.items[0].metadata.name}')
    
    # Command to execute that tests connectivity to the service service-test.
    TEST_CMD="wget -q -O - service-test; echo"
    
    # Execute the test command on the Pod .
    kubectl exec -it $BUSYBOX_POD -c busybox -- /bin/sh -c "$TEST_CMD"
    

### Understanding traffic interception by the sidecar proxy

Note that, in this example, when the Busybox client makes requests to the backend service, each request is proxied by the sidecar proxy.

This demonstration application uses the Envoy proxy. Because of that, the client sees 'server: envoy' in the header of server responses.

To confirm this, use the following commands:
    
    
    # Get the name of the Pod  with Busybox.
    BUSYBOX_POD=$(kubectl get po -l run=client -o=jsonpath='{.items[0].metadata.name}')
    
    # Command to send a request to service-test and output server response headers.
    TEST_CMD="wget -S --spider service-test; echo"
    
    # Execute the test command on the Pod .
    kubectl exec -it $BUSYBOX_POD -c busybox -- /bin/sh -c "$TEST_CMD"
    

In this example, you created a forwarding rule using the VIP address 0.0.0.0. This means that Cloud Service Mesh forwards requests to the backend based on the `Host` header only. In this case, the destination IP address can be any address as long as the request host header matches the host defined in the URL map `service-test`.

To confirm that, run the following test commands:
    
    
    # Get name of the Pod  with Busybox.
    BUSYBOX_POD=$(kubectl get po -l run=client -o=jsonpath='{.items[0].metadata.name}')
    
    # Command to send a request to service-test setting the Host header and using a random IP address.
    TEST_CMD="wget -q --header 'Host: service-test' -O - 1.2.3.4; echo"
    
    # Execute the test command on the Pod .
    kubectl exec -it $BUSYBOX_POD -c busybox -- /bin/sh -c "$TEST_CMD"
    

## What's next

  * Learn about [advanced traffic management](https://docs.cloud.google.com/service-mesh/docs/service-routing/advanced-traffic-management).
  * Learn how to [troubleshoot Cloud Service Mesh deployments](https://docs.cloud.google.com/service-mesh/docs/service-routing/troubleshooting).
  * Learn how to set up [observability with Envoy](https://docs.cloud.google.com/service-mesh/docs/service-routing/observability-envoy).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
