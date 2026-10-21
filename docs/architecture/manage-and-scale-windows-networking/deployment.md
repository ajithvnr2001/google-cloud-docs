---
url: https://docs.cloud.google.com/architecture/manage-and-scale-windows-networking/deployment/
title: Deploy Windows applications on managed Kubernetes \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:22:09.278352+00:00
---

# Deploy Windows applications on managed Kubernetes  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/manage-and-scale-windows-networking/deployment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Deploy Windows applications on managed Kubernetes Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2024-08-14 UTC

This document describes how you deploy the reference architecture in [Manage and scale networking for Windows applications that run on managed Kubernetes](https://docs.cloud.google.com/architecture/manage-and-scale-windows-networking).

These instructions are intended for cloud architects, network administrators, and IT professionals who are responsible for the design and management of Windows applications that run on [Google Kubernetes Engine (GKE)](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview) clusters.

## Architecture

The following diagram shows the reference architecture that you use when you deploy Windows applications that run on managed GKE clusters.

![Data flows through an internal Application Load Balancer and an Envoy gateway.](https://docs.cloud.google.com/static/architecture/images/manage-and-scale-windows-networking-archdiagram.svg)

As shown in the preceding diagram, an arrow represents the workflow for managing networking for Windows applications that run on GKE using Cloud Service Mesh and Envoy gateways. The regional GKE cluster includes both Windows and Linux node pools. [Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs) creates and manages traffic routes to the Windows Pods.

## Objectives

  * Create and set up a GKE cluster to run Windows applications and Envoy proxies.
  * Deploy and verify the Windows applications.
  * Configure Cloud Service Mesh as the control plane for the Envoy gateways.
  * Use the [Kubernetes Gateway API](https://gateway-api.sigs.k8s.io/) to provision the internal Application Load Balancer and expose the Envoy gateways.
  * Understand the continual deployment operations you created.



## Costs

Deployment of this architecture uses the following billable components of Google Cloud:

  * [Cloud Load Balancing](https://docs.cloud.google.com/vpc/network-pricing#lb)
  * [Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine/pricing)
  * [Cloud Service Mesh](https://cloud.google.com/service-mesh/pricing)



When you finish this deployment, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Before you begin

  1. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  3. Enable the Cloud Shell, and Cloud Service Mesh APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=cloudshell.googleapis.com,trafficdirector.googleapis.com,networkservices.googleapis.com)

  4. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)




If running in a shared Virtual Private Cloud (VPC) environment, you also need to follow the [instructions to manually create the proxy-only subnet and firewall rule](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress#shared_vpc) for the Cloud Load Balancing responsiveness checks.

## Create a GKE cluster

Use the following steps to create a GKE cluster. You use the GKE cluster to contain and run the Windows applications and Envoy proxies in this deployment.

  1. In Cloud Shell, run the following Google Cloud CLI command to create a regional GKE cluster with one node in each of the three [regions](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones):
         
         gcloud container clusters create my-cluster
             --enable-ip-alias \
             --num-nodes=1 \
             --release-channel stable \
             --enable-dataplane-v2 \
             --region us-central1 \
             --scopes=cloud-platform \
             --gateway-api=standard
         

  2. Add the Windows node pool to the GKE cluster:
         
         gcloud container node-pools create win-pool \
             --cluster=my-cluster \
             --image-type=windows_ltsc_containerd \
             --no-enable-autoupgrade \
             --region=us-central1 \
             --num-nodes=1 \
             --machine-type=n1-standard-2 \
             --windows-os-version=ltsc2019
         

This operation might take around 20 minutes to complete.

  3. Store your Google Cloud project ID in an environment variable:
         
         export PROJECT_ID=$(gcloud config get project)
         

  4. Connect to the GKE cluster:
         
         gcloud container clusters get-credentials my-cluster --region us-central1
         

  5. List all the nodes in the GKE cluster:
         
         kubectl get nodes
         

The output should display three Linux nodes and three Windows nodes.

After the GKE cluster is ready, you can deploy two Windows-based test applications.




## Deploy two test applications

In this section, you deploy two Windows-based test applications. Both test applications print the hostname that the application runs on. You also create a Kubernetes Service to expose the application through standalone network endpoint groups (NEGs).

When you deploy a Windows-based application and a Kubernetes Service on a regional cluster, it creates a NEG for each zone in which the application runs. Later, this deployment guide discusses how you can configure these NEGs as backends for Cloud Service Mesh services.

  1. In Cloud Shell, apply the following YAML file with [`kubectl`](https://kubernetes.io/docs/reference/kubectl/) to deploy the first test application. This command deploys three instances of the test application, one in each regional zone.
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           labels:
             app: win-webserver-1
           name: win-webserver-1
         spec:
           replicas: 3
           selector:
             matchLabels:
               app: win-webserver-1
           template:
             metadata:
               labels:
                 app: win-webserver-1
               name: win-webserver-1
             spec:
              containers:
               - name: windowswebserver
                 image: k8s.gcr.io/e2e-test-images/agnhost:2.36
                 command: ["/agnhost"]
                 args: ["netexec", "--http-port", "80"]
              topologySpreadConstraints:
               - maxSkew: 1
                 topologyKey: kubernetes.io/hostname
                 whenUnsatisfiable: DoNotSchedule
                 labelSelector:
                   matchLabels:
                     app: win-webserver-1
              nodeSelector:
               kubernetes.io/os: windows
         

  2. Apply the matching Kubernetes Service and expose it with a NEG:
         
         apiVersion: v1
         kind: Service
         metadata:
           name: win-webserver-1
           annotations:
             cloud.google.com/neg: '{"exposed_ports": {"80":{"name": "win-webserver-1"}}}'
         spec:
           type: ClusterIP
           selector:
             app: win-webserver-1
           ports:
           - name: http
             protocol: TCP
             port: 80
             targetPort: 80
         

  3. Verify the deployment:
         
         kubectl get pods
         

The output shows that the application has three running Windows Pods.
         
         NAME                               READY   STATUS    RESTARTS   AGE
         win-webserver-1-7bb4c57f6d-hnpgd   1/1     Running   0          5m58s
         win-webserver-1-7bb4c57f6d-rgqsb   1/1     Running   0          5m58s
         win-webserver-1-7bb4c57f6d-xp7ww   1/1     Running   0          5m58s
         

  4. Verify that the Kubernetes Service was created:
         
         $ kubectl get svc
         

The output resembles the following:
         
         NAME              TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
         kubernetes        ClusterIP   10.64.0.1            443/TCP   58m
         win-webserver-1   ClusterIP   10.64.6.20           80/TCP    3m35s
         

  5. Run the `describe` command for `kubectl` to verify that corresponding NEGs were created for the Kubernetes Service in each of the zones in which the application runs:
         
         $ kubectl describe service win-webserver-1
         

The output resembles the following:
         
         Name:              win-webserver-1
         Namespace:         default
         Labels:            
         Annotations:       cloud.google.com/neg: {"exposed_ports": {"80":{"name": "win-webserver-1"}}}
                            cloud.google.com/neg-status: {"network_endpoint_groups":{"80":"win-webserver-1"},"zones":["us-central1-a","us-central1-b","us-central1-c"]}
         Selector:          app=win-webserver-1
         Type:              ClusterIP
         IP Family Policy:  SingleStack
         IP Families:       IPv4
         IP:                10.64.6.20
         IPs:               10.64.6.20
         Port:              http  80/TCP
         TargetPort:        80/TCP
         Endpoints:         10.60.3.5:80,10.60.4.5:80,10.60.5.5:80
         Session Affinity:  None
         Events:
           Type    Reason  Age    From            Message
           ----    ------  ----   ----            -------
           Normal  Create  4m25s  neg-controller  Created NEG "win-webserver-1" for default/win-webserver-1-win-webserver-1-http/80-80-GCE_VM_IP_PORT-L7 in "us-central1-a".
           Normal  Create  4m18s  neg-controller  Created NEG "win-webserver-1" for default/win-webserver-1-win-webserver-1-http/80-80-GCE_VM_IP_PORT-L7 in "us-central1-b".
           Normal  Create  4m11s  neg-controller  Created NEG "win-webserver-1" for default/win-webserver-1-win-webserver-1-http/80-80-GCE_VM_IP_PORT-L7 in "us-central1-c".
           Normal  Attach  4m9s   neg-controller  Attach 1 network endpoint(s) (NEG "win-webserver-1" in zone "us-central1-a")
           Normal  Attach  4m8s   neg-controller  Attach 1 network endpoint(s) (NEG "win-webserver-1" in zone "us-central1-c")
           Normal  Attach  4m8s   neg-controller  Attach 1 network endpoint(s) (NEG "win-webserver-1" in zone "us-central1-b")
         

The output from the preceding command shows you that a NEG was created for each zone.

  6. Optional: Use gcloud CLI to verify that the NEGs were created:
         
         gcloud compute network-endpoint-groups list
         

The output is as follows:
         
         NAME                                                        LOCATION            ENDPOINT_TYPE     SIZE
         win-webserver-1                                us-central1-a  GCE_VM_IP_PORT  1
         win-webserver-1                                us-central1-b  GCE_VM_IP_PORT  1
         win-webserver-1                                us-central1-c  GCE_VM_IP_PORT  1
         

  7. To deploy the second test application, apply the following YAML file:
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           labels:
             app: win-webserver-2
           name: win-webserver-2
         spec:
           replicas: 3
           selector:
             matchLabels:
               app: win-webserver-2
           template:
             metadata:
               labels:
                 app: win-webserver-2
               name: win-webserver-2
             spec:
              containers:
               - name: windowswebserver
                 image: k8s.gcr.io/e2e-test-images/agnhost:2.36
                 command: ["/agnhost"]
                 args: ["netexec", "--http-port", "80"]
              topologySpreadConstraints:
               - maxSkew: 1
                 topologyKey: kubernetes.io/hostname
                 whenUnsatisfiable: DoNotSchedule
                 labelSelector:
                   matchLabels:
                     app: win-webserver-2
              nodeSelector:
               kubernetes.io/os: windows
         

  8. Create the corresponding Kubernetes Service:
         
         apiVersion: v1
         kind: Service
         metadata:
           name: win-webserver-2
           annotations:
             cloud.google.com/neg: '{"exposed_ports": {"80":{"name": "win-webserver-2"}}}'
         spec:
           type: ClusterIP
           selector:
             app: win-webserver-2
           ports:
           - name: http
             protocol: TCP
             port: 80
             targetPort: 80
         

  9. Verify the application deployment:
         
         kubectl get pods
         

Check the output and verify that there are three running Pods.

  10. Verify that the Kubernetes Service and three NEGs were created:
         
         kubectl describe service win-webserver-2
         




## Configure Cloud Service Mesh

In this section, Cloud Service Mesh is configured as the control plane for the Envoy gateways.

You map the Envoy gateways to the relevant Cloud Service Mesh routing configuration by specifying the `scope_name` parameter. The `scope_name` parameter lets you configure different routing rules for the different Envoy gateways.

  1. In Cloud Shell, create a firewall rule that allows incoming traffic from the Google services that are checking application responsiveness:
         
         gcloud compute firewall-rules create allow-health-checks \
           --network=default \
           --direction=INGRESS \
           --action=ALLOW \
           --rules=tcp \
           --source-ranges="35.191.0.0/16,130.211.0.0/22,209.85.152.0/22,209.85.204.0/22"
         

  2. Check the responsiveness of the first application:
         
         gcloud compute health-checks create http win-app-1-health-check \
           --enable-logging \
           --request-path="/healthz" \
           --use-serving-port
         

  3. Check the responsiveness of the second application:
         
         gcloud compute health-checks create http win-app-2-health-check \
           --enable-logging \
           --request-path="/healthz" \
           --use-serving-port
         

  4. Create a Cloud Service Mesh backend service for the first application:
         
         gcloud compute backend-services create win-app-1-service \
          --global \
          --load-balancing-scheme=INTERNAL_SELF_MANAGED \
          --port-name=http \
          --health-checks win-app-1-health-check
         

  5. Create a Cloud Service Mesh backend service for the second application:
         
         gcloud compute backend-services create win-app-2-service \
          --global \
          --load-balancing-scheme=INTERNAL_SELF_MANAGED \
          --port-name=http \
          --health-checks win-app-2-health-check
         

  6. Add the NEGs you created previously. These NEGs are associated with the first application you created as a backend to the Cloud Service Mesh backend service. This code sample adds one NEG for each zone in the regional cluster you created.
         
         BACKEND_SERVICE=win-app-1-service
         APP1_NEG_NAME=win-webserver-1
         MAX_RATE_PER_ENDPOINT=10
         
         gcloud compute backend-services add-backend $BACKEND_SERVICE \
           --global \
           --network-endpoint-group $APP1_NEG_NAME \
           --network-endpoint-group-zone us-central1-b \
           --balancing-mode RATE \
           --max-rate-per-endpoint $MAX_RATE_PER_ENDPOINT
         
         gcloud compute backend-services add-backend $BACKEND_SERVICE \
           --global \
           --network-endpoint-group $APP1_NEG_NAME \
           --network-endpoint-group-zone us-central1-a \
           --balancing-mode RATE \
           --max-rate-per-endpoint $MAX_RATE_PER_ENDPOINT
         
         gcloud compute backend-services add-backend $BACKEND_SERVICE \
           --global \
           --network-endpoint-group $APP1_NEG_NAME \
           --network-endpoint-group-zone us-central1-c \
           --balancing-mode RATE \
           --max-rate-per-endpoint $MAX_RATE_PER_ENDPOINT
         

  7. Add additional NEGs. These NEGs are associated with the second application you created as a backend to the Cloud Service Mesh backend service. This code sample adds one NEG for each zone in the regional cluster you created.
         
         BACKEND_SERVICE=win-app-2-service
         APP2_NEG_NAME=win-webserver-2
         
         gcloud compute backend-services add-backend $BACKEND_SERVICE \
           --global \
           --network-endpoint-group $APP2_NEG_NAME \
           --network-endpoint-group-zone us-central1-b \
           --balancing-mode RATE \
           --max-rate-per-endpoint $MAX_RATE_PER_ENDPOINT
         
         gcloud compute backend-services add-backend $BACKEND_SERVICE \
           --global \
           --network-endpoint-group $APP2_NEG_NAME \
           --network-endpoint-group-zone us-central1-a \
           --balancing-mode RATE \
           --max-rate-per-endpoint $MAX_RATE_PER_ENDPOINT
         
         gcloud compute backend-services add-backend $BACKEND_SERVICE \
           --global \
           --network-endpoint-group $APP2_NEG_NAME \
           --network-endpoint-group-zone us-central1-c \
           --balancing-mode RATE \
           --max-rate-per-endpoint $MAX_RATE_PER_ENDPOINT
         




### Configure additional Cloud Service Mesh resources

Now that you've configured the Cloud Service Mesh services, you need to configure two additional resources to complete your Cloud Service Mesh setup.

First, these steps show how to configure a [`Gateway`](https://docs.cloud.google.com/service-mesh/docs/service-routing-overview#gateway-resource) resource. A `Gateway` resource is a virtual resource that's used to generate Cloud Service Mesh routing rules. Cloud Service Mesh routing rules are used to configure Envoy proxies as gateways.

Next, the steps show how to configure an [`HTTPRoute`](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1/projects.locations.httpRoutes) resource for each of the backend services. The `HTTPRoute` resource maps HTTP requests to the relevant backend service.

  1. In Cloud Shell, create a YAML file called `gateway.yaml` that defines the `Gateway` resource:
         
         cat <<EOF> gateway.yaml
         name: gateway80
         scope: gateway-proxy
         ports:
         - 8080
         type: OPEN_MESH
         EOF
         

  2. Create the `Gateway` resource by invoking the `gateway.yaml` file:
         
         gcloud network-services gateways import gateway80 \
           --source=gateway.yaml \
           --location=global
         

The `Gateway` name will be `projects/$PROJECT_ID/locations/global/gateways/gateway80`.

You use this `Gateway` name when you create `HTTPRoutes` for each backend service.




### Create the `HTTPRoutes` for each backend service:

  1. In Cloud Shell, store your Google Cloud project ID in an environment variable:
         
         export PROJECT_ID=$(gcloud config get project)
         

  2. Create the `HTTPRoute` YAML file for the first application:
         
         cat <<EOF> win-app-1-route.yaml
         name: win-app-1-http-route
         hostnames:
         - win-app-1
         gateways:
         - projects/$PROJECT_ID/locations/global/gateways/gateway80
         rules:
         - action:
            destinations:
            - serviceName: "projects/$PROJECT_ID/locations/global/backendServices/win-app-1-service"
         EOF
         

  3. Create the `HTTPRoute` resource for the first application:
         
         gcloud network-services http-routes import win-app-1-http-route \
           --source=win-app-1-route.yaml \
           --location=global
         

  4. Create the `HTTPRoute` YAML file for the second application:
         
         cat <<EOF> win-app-2-route.yaml
         name: win-app-2-http-route
         hostnames:
         - win-app-2
         gateways:
         - projects/$PROJECT_ID/locations/global/gateways/gateway80
         rules:
         - action:
            destinations:
          - serviceName: "projects/$PROJECT_ID/locations/global/backendServices/win-app-2-service"
         EOF
         

  5. Create the `HTTPRoute` resource for the second application:
         
         gcloud network-services http-routes import win-app-2-http-route \
           --source=win-app-2-route.yaml \
           --location=global
         




## Deploy and expose the Envoy gateways

After you create the two Windows-based test applications and the Cloud Service Mesh, you deploy the Envoy gateways by creating a deployment YAML file. The deployment YAML file accomplishes the following tasks:

  * Bootstraps the Envoy gateways.
  * Configures the Envoy gateways to use Cloud Service Mesh as its control plane.
  * Configures the Envoy gateways to use `HTTPRoutes` for the gateway named `Gateway80`.



Deploy two replica Envoy gateways. This approach helps to make the gateways fault tolerant and provides redundancy. To automatically scale the Envoy gateways based on load, you can optionally configure a Horizontal Pod Autoscaler. If you decide to configure a Horizontal Pod Autoscaler, you must follow the instructions in [Configuring horizontal Pod autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/horizontal-pod-autoscaling).

  1. In Cloud Shell, create a YAML file:
         
         apiVersion: apps/v1
         kind: Deployment
             metadata:
           creationTimestamp: null
           labels:
             app: td-envoy-gateway
           name: td-envoy-gateway
         spec:
           replicas: 2
           selector:
             matchLabels:
               app: td-envoy-gateway
           template:
             metadata:
               creationTimestamp: null
               labels:
                 app: td-envoy-gateway
             spec:
               containers:
               - name: envoy
                 image: envoyproxy/envoy:v1.21.6
                 imagePullPolicy: Always
                 resources:
                   limits:
                     cpu: "2"
                     memory: 1Gi
                   requests:
                     cpu: 100m
                     memory: 128Mi
                 env:
                 - name: ENVOY_UID
                   value: "1337"
                 volumeMounts:
                   - mountPath: /etc/envoy
                     name: envoy-bootstrap
               initContainers:
               - name: td-bootstrap-writer
                 image: gcr.io/trafficdirector-prod/xds-client-bootstrap-generator
                 imagePullPolicy: Always
                 args:
                   - --project_number='my_project_number'
                   - --scope_name='gateway-proxy'
                   - --envoy_port=8080
                   - --bootstrap_file_output_path=/var/lib/data/envoy.yaml
                   - --traffic_director_url=trafficdirector.googleapis.com:443
                   - --expose_stats_port=15005
                 volumeMounts:
                   - mountPath: /var/lib/data
                     name: envoy-bootstrap
               volumes:
                 - name: envoy-bootstrap
                   emptyDir: {}
         

     * Replace my_project_number with your project number.

       * You can find your project number by running the following command:
    
    gcloud projects describe $(gcloud config get project)
     --format="value(projectNumber)"
    

Port `15005` is used to expose the Envoy Admin endpoint named `/stats`. It's also used for the following purposes:

     * As a responsiveness endpoint from the internal Application Load Balancer.
     * As a way to consume Google Cloud Managed Service for Prometheus metrics from Envoy.

When the two Envoy Gateway Pods are running, create a service of type `ClusterIP` to expose them. You must also create a YAML file called [`BackendConfig`](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ingress-configuration#create_backendconfig). `BackendConfig` defines a non-standard responsiveness check. That check is used to verify the responsiveness of the Envoy gateways.

  2. To create the backend configuration with a non-standard responsiveness check, create a YAML file called `envoy-backendconfig`:
         
         apiVersion: cloud.google.com/v1
         kind: BackendConfig
         metadata:
           name: envoy-backendconfig
         spec:
           healthCheck:
             checkIntervalSec: 5
             timeoutSec: 5
             healthyThreshold: 2
             unhealthyThreshold: 3
             type: HTTP
             requestPath: /stats
             port: 15005
         

The responsiveness check will use the `/stats` endpoint on port `15005` to continuously check the responsiveness of the Envoy gateways.

  3. Create the Envoy gateways service:
         
         apiVersion: v1
         kind: Service
         metadata:
           name: td-envoy-gateway
           annotations:
             cloud.google.com/backend-config: '{"default": "envoy-backendconfig"}'
         spec:
           type: ClusterIP
           selector:
             app: td-envoy-gateway
           ports:
           - name: http
             protocol: TCP
             port: 8080
             targetPort: 8080
           - name: stats
             protocol: TCP
             port: 15005
             targetPort: 15005
         

  4. View the Envoy gateways service you created:
         
         kubectl get svc td-envoy-gateway
         




## Create the Kubernetes Gateway resource

Creating the Kubernetes Gateway resource provisions the internal Application Load Balancer to expose the Envoy gateways.

Before creating that resource, you must create two sample self-signed certificates and then import them into the GKE cluster as Kubernetes Secrets. The certificates enable the following gateway architecture:

  * Each application is served over HTTPS.
  * Each application uses a dedicated certificate.



When using self-managed certificates, the internal Application Load Balancer can use up to the [maximum limit of certificates](https://docs.cloud.google.com/load-balancing/docs/quotas#target_proxies) to expose applications with different fully qualified domain names.

To create the certificates use `openssl`.

  1. In Cloud Shell, generate a configuration file for the first certificate:
         
         cat <<EOF >CONFIG_FILE
         [req]
         default_bits              = 2048
         req_extensions            = extension_requirements
         distinguished_name        = dn_requirements
         prompt                    = no
         [extension_requirements]
         basicConstraints          = CA:FALSE
         keyUsage                  = nonRepudiation, digitalSignature, keyEncipherment
         subjectAltName            = @sans_list
         [dn_requirements]
         0.organizationName        = example
         commonName                = win-webserver-1.example.com
         [sans_list]
         DNS.1                     = win-webserver-1.example.com
         EOF
         

  2. Generate a private key for the first certificate:
         
         openssl genrsa -out sample_private_key 2048
         

  3. Generate a certificate request:
         
         openssl req -new -key sample_private_key -out CSR_FILE -config CONFIG_FILE
         

  4. Sign and generate the first certificate:
         
         openssl x509 -req -signkey sample_private_key -in CSR_FILE -out sample.crt     -extfile CONFIG_FILE -extensions extension_requirements -days 90
         

  5. Generate a configuration file for the second certificate:
         
         cat <<EOF >CONFIG_FILE2
         [req]
         default_bits              = 2048
         req_extensions            = extension_requirements
         distinguished_name        = dn_requirements
         prompt                    = no
         [extension_requirements]
         basicConstraints          = CA:FALSE
         keyUsage                  = nonRepudiation, digitalSignature, keyEncipherment
         subjectAltName            = @sans_list
         [dn_requirements]
         0.organizationName        = example
         commonName                = win-webserver-2.example.com
         [sans_list]
         DNS.1                     = win-webserver-2.example.com
         EOF
         

  6. Generate a private key for the second certificate:
         
         openssl genrsa -out sample_private_key2 2048
         

  7. Generate a certificate request:
         
         openssl req -new -key sample_private_key2 -out CSR_FILE2 -config CONFIG_FILE2
         

  8. Sign and generate the second certificate:
         
         openssl x509 -req -signkey sample_private_key2 -in CSR_FILE2 -out sample2.crt     -extfile CONFIG_FILE2 -extensions extension_requirements -days 90
         




## Import certificates as Kubernetes Secrets

In this section, you accomplish the following tasks:

  * Import the self-signed certificates into the GKE cluster as Kubernetes Secrets.
  * Create a static IP address for an internal VPC.
  * Create the Kubernetes Gateway API resource.
  * Verify that the certificates work.


  1. In Cloud Shell, import the first certificate as a Kubernetes Secret:
         
         kubectl create secret tls sample-cert --cert sample.crt --key sample_private_key
         

  2. Import the second certificate as a Kubernetes Secret:
         
         kubectl create secret tls sample-cert-2 --cert sample2.crt --key sample_private_key2
         

  3. To enable internal Application Load Balancer, create a static IP address on the internal VPC:
         
         gcloud compute addresses create sample-ingress-ip --region us-central1 --subnet default
         

  4. Create the Kubernetes Gateway API resource YAML file:
         
         kind: Gateway
         apiVersion: gateway.networking.k8s.io/v1beta1
         metadata:
           name: internal-https
         spec:
           gatewayClassName: gke-l7-rilb
           addresses:
             - type: NamedAddress
               value: sample-ingress-ip
           listeners:
           - name: https
             protocol: HTTPS
             port: 443
             tls:
               mode: Terminate
               certificateRefs:
               - name: sample-cert
               - name: sample-cert-2
         

By default, a Kubernetes Gateway has no default routes. The gateway returns a page not found (404) error when requests are sent to it.

  5. Configure a default `route` YAML file for the Kubernetes Gateway that passes all incoming requests to the Envoy gateways:
         
         kind: HTTPRoute
           apiVersion: gateway.networking.k8s.io/v1beta1
           metadata:
             name: envoy-default-backend
           spec:
             parentRefs:
             - kind: Gateway
               name: internal-https
             rules:
             - backendRefs:
               - name: td-envoy-gateway
                 port: 8080
         

Verify the full flow by sending HTTP requests to both applications. To verify that the Envoy gateways route traffic to the correct application Pods, inspect the HTTP Host header.

  6. Find and store the Kubernetes Gateway IP address in an environment variable:
         
         export EXTERNAL_IP=$(kubectl get gateway internal-https -o json | jq .status.addresses[0].value -r)
         

  7. Send a request to the first application:
         
         curl --insecure -H "Host: win-app-1" https://$EXTERNAL_IP/hostName
         

  8. Send a request to the second application:
         
         curl --insecure -H "Host: win-app-2" https://$EXTERNAL_IP/hostName
         

  9. Verify that the hostname returned from the request matches the Pods running `win-app-1` and `win-app-2`:
         
         kubectl get pods
         

The output should display `win-app-1` and `win-app-2`.




## Monitor Envoy gateways

Monitor your Envoy gateways with [Google Cloud Managed Service for Prometheus](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus).

Google Cloud Managed Service for Prometheus should be enabled by default on the cluster that you created earlier.

  1. In Cloud Shell, create a `PodMonitoring` resource by applying the following YAML file:
         
         apiVersion: monitoring.googleapis.com/v1
         kind: PodMonitoring
         metadata:
           name: prom-envoy
         spec:
           selector:
             matchLabels:
               app: td-envoy-gateway
           endpoints:
           - port: 15005
             interval: 30s
             path: /stats/prometheus
         

After applying the YAML file, the system begins to collect Google Cloud Managed Service for Prometheus metrics in a dashboard.

  2. To create the Google Cloud Managed Service for Prometheus metrics dashboard, follow these instructions:

     1. Sign in to the Google Cloud console.
     2. Open the menu menu.
     3. Click **Operations > Monitoring > Dashboards**.
  3. To import the dashboard, follow these instructions:

     1. On the Dashboards screen, click **Sample Library**.
     2. Enter envoy in the filter box.
     3. Click **Istio Envoy Prometheus Overview**.
     4. Select the checkbox.
     5. Click **Import** and then click **Confirm** to import the dashboard.
  4. To view the dashboard, follow these instructions:

     1. Click **Dashboard List**.
     2. Select **Integrations**.
     3. Click **Istio Envoy Prometheus Overview** to view the dashboard.



You can now see the most important metrics of your Envoy gateways. You can also configure alerts based on your criteria. Before you clean up, send a few more test requests to the applications and see how the dashboard updates with the latest metrics.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this deployment, either delete the project that contains the resources, or keep the project and delete the individual resources.

### Delete the project

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



## What's next

  * Learn more about the Google Cloud products used in this deployment guide: 
    * [GKE networking best practices](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/networking)
    * [Best practices for running cost effective Kubernetes applications on GKE](https://docs.cloud.google.com/architecture/best-practices-for-running-cost-effective-kubernetes-applications-on-gke#observe_your_gke_clusters_and_watch_for_recommendations)
    * [Cloud Service Mesh control plane observability](https://docs.cloud.google.com/service-mesh/docs/control-plane-observability)
    * [Using self-managed SSL certificates with load balancers](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/self-managed-certs)
  * For more reference architectures, diagrams, and best practices, explore the [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



## Contributors

Author: [Eitan Eibschutz](https://www.linkedin.com/in/eitaneibschutz) | Staff Technical Solutions Consultant

Other contributors: 

  * [John Laham](https://www.linkedin.com/in/lahamjohn) | Solutions Architect
  * [Kaslin Fields](https://www.linkedin.com/in/kaslinfields) | Developer Advocate
  * [Maridi (Raju) Makaraju](https://www.linkedin.com/in/mmraju) | Supportability Tech Lead
  * [Valavan Rajakumar](https://www.linkedin.com/in/valavanr) | Key Enterprise Architect
  * [Victor Moreno](https://www.linkedin.com/in/vimoreno) | Product Manager, Cloud Networking



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-08-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-08-14 UTC."],[],[]] 
