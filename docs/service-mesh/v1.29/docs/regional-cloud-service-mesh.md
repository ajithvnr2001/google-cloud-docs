---
url: https://docs.cloud.google.com/service-mesh/v1.29/docs/regional-cloud-service-mesh/
title: Regional Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:52:24.372794+00:00
---

# Regional Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.29/docs/regional-cloud-service-mesh/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/v1.29/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/v1.29/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.29/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Regional Cloud Service Mesh

With regional isolation, clients connecting to a specific region of the Cloud Service Mesh control plane can only access resources within that region. Similarly, API resources within a specific region can only refer to other resources in that region.

Regional Cloud Service Mesh has the following Limitations:

  * The Istio API not supported. You cannot use Kubernetes with the Istio API using regional Traffic Director. Only Google Cloud APIs are supported in this preview.
  * The [existing considerations and limitations](https://docs.cloud.google.com/service-mesh/v1.29/docs//service-routing/service-routing-overview#considerations_and_limitations) of the global service routing APIs apply.
  * The minimum Envoy version to support xdSTP naming schemes is v1.31.1.
  * [Gateway for Mesh API](https://gateway-api.sigs.k8s.io/mesh/) is not supported.
  * The minimum gRPC version is v1.65.
  * Only the following regions are supported:
        
        africa-south1
        asia-east1
        asia-east2
        asia-northeast1
        asia-northeast2
        asia-northeast3
        asia-south1
        asia-south2
        asia-southeast1
        asia-southeast2
        australia-southeast1
        australia-southeast2
        europe-central2
        europe-north1
        europe-north2
        europe-southwest1
        europe-west10
        europe-west12
        europe-west1
        europe-west2
        europe-west3
        europe-west4
        europe-west6
        europe-west8
        europe-west9
        me-central1
        me-central2
        me-west1
        northamerica-northeast1
        northamerica-northeast2
        northamerica-south1
        southamerica-east1
        southamerica-west1
        us-central1
        us-east1
        us-east4
        us-east5
        us-south1
        us-west1
        us-west2
        us-west3
        us-west4
        




## Pricing

Each region in which regional Cloud Service Mesh is supported will have a regional SKU when this feature is Generally Available. For now, the pricing is the same as [global](https://docs.cloud.google.com/service-mesh/pricing).

## Prepare xDS client for Cloud Service Mesh

### Compute VM Envoy xDS

### Manual

The manual steps build on [Set up VMs using manual Envoy deployment](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/set-up-gce-vms). The main difference is that `ENVOY_CONTROL_PLANE_REGION` is set and injected into the bootstrap.

  1. Create the instance template:
         
         gcloud compute instance-templates create td-vm-templategcloud compute instance-templates create td-vm-template \
           --scopes=https://www.googleapis.com/auth/cloud-platform \
           --tags=http-td-tag,http-server,https-server \
           --image-family=debian-11 \
           --image-project=debian-cloud \
           --metadata=startup-script='#! /usr/bin/env bash
         
         # Set variables
         export ENVOY_CONTROL_PLANE_REGION="us-central1"
         export ENVOY_USER="envoy"
         export ENVOY_USER_UID="1337"
         export ENVOY_USER_GID="1337"
         export ENVOY_USER_HOME="/opt/envoy"
         export ENVOY_CONFIG="${ENVOY_USER_HOME}/config.yaml"
         export ENVOY_PORT="15001"
         export ENVOY_ADMIN_PORT="15000"
         export ENVOY_TRACING_ENABLED="false"
         export ENVOY_XDS_SERVER_CERT="/etc/ssl/certs/ca-certificates.crt"
         export ENVOY_ACCESS_LOG="/dev/stdout"
         export ENVOY_NODE_ID="$(cat /proc/sys/kernel/random/uuid)~$(hostname -i)"
         export BOOTSTRAP_TEMPLATE="${ENVOY_USER_HOME}/bootstrap_template.yaml"
         export GCE_METADATA_SERVER="169.254.169.254/32"
         export INTERCEPTED_CIDRS="*"
         export GCP_PROJECT_NUMBER=PROJECT_NUMBER
         export VPC_NETWORK_NAME=mesh:sidecar-mesh
         export GCE_ZONE=$(curl -sS -H "Metadata-Flavor: Google" http://metadata.google.internal/computeMetadata/v1/instance/zone | cut -d"/" -f4)
         
         # Create system user account for Envoy binary
         sudo groupadd ${ENVOY_USER} \
           --gid=${ENVOY_USER_GID} \
           --system
         sudo adduser ${ENVOY_USER} \
           --uid=${ENVOY_USER_UID} \
           --gid=${ENVOY_USER_GID} \
           --home=${ENVOY_USER_HOME} \
           --disabled-login \
           --system
         # Download and extract the Cloud Service Mesh tar.gz file
         cd ${ENVOY_USER_HOME}
         sudo curl -sL https://storage.googleapis.com/traffic-director/traffic-director-xdsv3.tar.gz -o traffic-director-xdsv3.tar.gz
         sudo tar -xvzf traffic-director-xdsv3.tar.gz traffic-director-xdsv3/bootstrap_template.yaml \
           -C bootstrap_template.yaml \
           --strip-components 1
         sudo tar -xvzf traffic-director-xdsv3.tar.gz traffic-director-xdsv3/iptables.sh \
           -C iptables.sh \
           --strip-components 1
         sudo rm traffic-director-xdsv3.tar.gz
         
         # Generate Envoy bootstrap configuration
         cat "${BOOTSTRAP_TEMPLATE}" \
           | sed -e "s|ENVOY_NODE_ID|${ENVOY_NODE_ID}|g" \
           | sed -e "s|ENVOY_ZONE|${GCE_ZONE}|g" \
           | sed -e "s|VPC_NETWORK_NAME|${VPC_NETWORK_NAME}|g" \
           | sed -e "s|CONFIG_PROJECT_NUMBER|${GCP_PROJECT_NUMBER}|g" \
           | sed -e "s|ENVOY_PORT|${ENVOY_PORT}|g" \
           | sed -e "s|ENVOY_ADMIN_PORT|${ENVOY_ADMIN_PORT}|g" \
           | sed -e "s|XDS_SERVER_CERT|${ENVOY_XDS_SERVER_CERT}|g" \
           | sed -e "s|TRACING_ENABLED|${ENVOY_TRACING_ENABLED}|g" \
           | sed -e "s|ACCESSLOG_PATH|${ENVOY_ACCESS_LOG}|g" \
           | sed -e "s|BACKEND_INBOUND_PORTS|${BACKEND_INBOUND_PORTS}|g" \
           | sed -e "s|trafficdirector.googleapis.com|trafficdirector.${ENVOY_CONTROL_PLANE_REGION}.rep.googleapis.com|g" \
           | sudo tee "${ENVOY_CONFIG}"
         
         # Install Envoy binary
         wget -O envoy_key https://apt.envoyproxy.io/signing.key
         cat envoy_key | sudo gpg --dearmor > $(pwd)/envoy-keyring.gpg
         echo "deb [arch=$(dpkg --print-architecture) signed-by=$(pwd)/envoy-keyring.gpg] https://apt.envoyproxy.io bullseye main" | sudo tee /etc/apt/sources.list.d/envoy.list
         sudo apt-get update
         sudo apt-get install envoy
         
         # Run Envoy as systemd service
         sudo systemd-run --uid=${ENVOY_USER_UID} --gid=${ENVOY_USER_GID} \
           --working-directory=${ENVOY_USER_HOME} --unit=envoy.service \
           bash -c "/usr/bin/envoy --config-path ${ENVOY_CONFIG} | tee"
         
         # Configure iptables for traffic interception and redirection
         sudo ${ENVOY_USER_HOME}/iptables.sh \
           -p "${ENVOY_PORT}" \
           -u "${ENVOY_USER_UID}" \
           -g "${ENVOY_USER_GID}" \
           -m "REDIRECT" \
           -i "${INTERCEPTED_CIDRS}" \
           -x "${GCE_METADATA_SERVER}"
         




### Compute VM gRPC xDS

Similar to global Cloud Service Mesh, gRPC clients need to configure a bootstrap in order to tell it how to connect to Regional Cloud Service Mesh.

You can use the [gRPC bootstrap generator](https://github.com/GoogleCloudPlatform/traffic-director-grpc-bootstrap) to generate this bootstrap. To set it to use regional Cloud Service Mesh, specify a new flag: `--xds-server-region`.

In this example, setting `xds-server-region` to `us-central1` automatically determines the regional Cloud Service Mesh endpoint: `trafficdirector.us-central1.rep.googleapis.com:443.`

### K8s Manual Envoy Injection

The manual steps build on [Set up Google Kubernetes Engine Pods using manual Envoy injection](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/set-up-gke-pods). However, you only need to modify the [section about manual pod injection](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/set-up-gke-pods#sidecar-injector).

  1. Change the control plane from global to regional:
         
         wget -q -O - https://storage.googleapis.com/traffic-director/demo/trafficdirector_client_new_api_sample_xdsv3.yaml
         
         sed -i "s/PROJECT_NUMBER/PROJECT_NUMBER/g" trafficdirector_client_new_api_sample_xdsv3.yaml
         
         sed -i "s/MESH_NAME/MESH_NAME/g" trafficdirector_client_new_api_sample_xdsv3.yaml
         
         sed -i "s|trafficdirector.googleapis.com|trafficdirector.${REGION}.rep.googleapis.com|g" trafficdirector_client_new_api_sample_xdsv3.yaml
         
         sed -i "s|gcr.io/google-containers/busybox|busybox:stable|g" trafficdirector_client_new_api_sample_xdsv3.yaml
         

     1. Apply the changes:
            
            kubectl apply -f trafficdirector_client_new_api_sample_xdsv3.yaml
            




## Setup guides

The section covers five independent configurations and deployment models. These are all regionalized versions of existing global service routing API setup guides.

  * Configuring Proxyless gRPC services with regional GRPCRoute and regional Cloud Service Mesh
  * Configuring Envoy sidecar proxy configuration with HTTP services with regional HTTPRoute and regional Cloud Service Mesh
  * Configuring TCP services with regional TCPRoute
  * Configuring published service backends for regional Cloud Service Mesh
  * Gateway TLS routing
  * Configuring cross-project references for regional Cloud Service Mesh and regional Route



### Configure Proxyless gRPC services with regional GRPCRoute and regional Cloud Service Mesh

This sections explains how to configure a proxyless gRPC service mesh with regional Cloud Service Mesh and regional GRPCRoute resources.

For your convenience, store the Google Cloud project number you perform configuration in, so that all examples in this guide can be copy-pasted in the command line:
    
    
    export PROJECT="PROJECT_NUMBER"
    export REGION="us-central1"
    export ZONE="us-central1-a"
    

Replace PROJECT_NUMBER with your project number.

Optionally, you can replace the following:

  * us-central1 with a different region you want to use.
  * us-central1-a with a different zone you want to use.
  * default with a different VPC_NAME.



#### Mesh configuration

When a proxyless gRPC application connects to an `xds://hostname`, the gRPC client library establishes a connection to the Cloud Service Mesh to get the routing configuration required to route requests for the hostname.

  1. Create a Mesh specification and store it in the mesh.yaml file:
         
         cat <<EOF > mesh.yaml
         name: grpc-mesh
         EOF
         

  2. Create a Mesh using the mesh.yaml specification:
         
         gcloud network-services meshes import grpc-mesh \
             --source=mesh.yaml \
             --location=${REGION}
         

After the regional mesh is created, Cloud Service Mesh is ready to serve the configuration. However, because no services are defined yet, the configuration is empty.




#### gRPC service configuration

For demonstration purposes you will create a regional backend service with auto-scaled VMs (using [Managed instance groups](https://docs.cloud.google.com/compute/docs/instance-groups#managed_instance_groups) \- MIG) that will serve `hello world` using the gRPC protocol on port 50051.

  1. Create the Compute Engine VM instance template with a `helloworld` gRPC service that is exposed on port 50051:
         
         gcloud compute instance-templates create grpc-td-vm-template \
           --scopes=https://www.googleapis.com/auth/cloud-platform \
           --tags=allow-health-checks \
           --image-family=debian-11 \
           --image-project=debian-cloud \
           --metadata-from-file=startup-script=<(echo '#! /bin/bash
         set -e
         cd /root
         sudo apt-get update -y
         sudo apt-get install -y openjdk-11-jdk-headless
         curl -L https://github.com/grpc/grpc-java/archive/v1.38.0.tar.gz | tar -xz
         cd grpc-java-1.38.0/examples/example-hostname
         ../gradlew --no-daemon installDist
         # Server listens on 50051
         sudo systemd-run ./build/install/hostname-server/bin/hostname-server')
         

  2. Create a MIG based on the template:
         
         gcloud compute instance-groups managed create grpc-td-mig-us-central1 \
           --zone=${ZONE} \
           --size=2 \
           --template=grpc-td-vm-template
         

  3. Configure a named port for the gRPC service. This is the port on which the gRPC service is configured to listen for requests.
         
         gcloud compute instance-groups set-named-ports grpc-td-mig-us-central1 \
           --named-ports=grpc-helloworld-port:50051 \
           --zone=${ZONE}
         

In this example, the port is 50051.

  4. Create gRPC health checks.
         
         gcloud compute health-checks create grpc grpc-helloworld-health-check \
           --use-serving-port --region=${REGION}
         

The services must implement the gRPC [health checking protocol](https://github.com/grpc/grpc/blob/master/doc/health-checking.md) for gRPC health checks to function properly. For more information, see [Creating health checks](https://docs.cloud.google.com/load-balancing/docs/health-checks). 

  5. Create a firewall rule to allow incoming health check connections to instances in your network:
         
         gcloud compute firewall-rules create grpc-vm-allow-health-checks \
           --network default --action allow --direction INGRESS \
           --source-ranges 35.191.0.0/16,209.85.152.0/22,209.85.204.0/22 \
           --target-tags allow-health-checks \
           --rules tcp:50051
         

  6. Create a regional [backend service](https://docs.cloud.google.com/load-balancing/docs/backend-service) with a load balancing scheme of `INTERNAL_SELF_MANAGED` and add the health check and a managed instance group created earlier to the Backend Service. The port in the port-name specified is used to connect to the VMs in the managed instance group.
         
         gcloud compute backend-services create grpc-helloworld-service \
             --load-balancing-scheme=INTERNAL_SELF_MANAGED \
             --protocol=GRPC \
             --port-name=grpc-helloworld-port \
           --health-checks="https://www.googleapis.com/compute/v1/projects/${PROJECT}/regions/${REGION}/healthChecks/grpc-helloworld-health-check" \
             --region=${REGION}
         

  7. Add the managed instance group to the `BackendService`:
         
         gcloud compute backend-services add-backend grpc-helloworld-service \
           --instance-group=grpc-td-mig-us-central1 \
           --instance-group-zone=${ZONE} \
           --region=${REGION}
         




#### Setup routing with regional GRPCRoute

At this point the regional mesh and gRPC server service are configured. Now you can set up the required routing. 

  1. Create regional GRPCRoute specification and store it in the grpc_route.yaml file:
         
         cat <<EOF > grpc_route.yaml
         name: helloworld-grpc-route
         hostnames:
         - helloworld-gce
         meshes:
         - projects/${PROJECT}/locations/${REGION}/meshes/grpc-mesh
         rules:
         - action:
             destinations:
             - serviceName: projects/${PROJECT}/locations/${REGION}/backendServices/grpc-helloworld-service
         EOF
         

  2. Create regional GRPCRoute using the grpc_route.yaml specification:
         
         gcloud network-services grpc-routes import helloworld-grpc-route \
             --source=grpc_route.yaml \
             --location=${REGION}
         

Cloud Service Mesh is now configured to load balance traffic for the services specified in the gRPC Route across backends in the managed instance group.




#### Create gRPC client service

To verify the configuration, instantiate a client application with a proxyless gRPC data plane. This application must specify (in its bootstrap file) the name of the mesh.

Once configured, this application can send a request to the instances or endpoints associated with the helloworld-gce using the `xds:///helloworld-gce` service URI.

In the following examples, use the `grpcurl` tool to test the gRPC service.

  1. Create a client VM:
         
         gcloud compute instances create grpc-client \
           --zone=${ZONE}\
           --scopes=https://www.googleapis.com/auth/cloud-platform \
           --image-family=debian-11 \
           --image-project=debian-cloud \
           --metadata-from-file=startup-script=<(echo '#! /bin/bash
         set -ex
         export PROJECT=PROJECT_NUMBER
         export REGION=us-central1
         export GRPC_XDS_BOOTSTRAP=/run/td-grpc-bootstrap.json
         echo export GRPC_XDS_BOOTSTRAP=$GRPC_XDS_BOOTSTRAP | sudo tee /etc/profile.d/grpc-xds-bootstrap.sh
         curl -L https://storage.googleapis.com/traffic-director/td-grpc-bootstrap-0.18.0.tar.gz | tar -xz
         ./td-grpc-bootstrap-0.18.0/td-grpc-bootstrap --config-mesh=grpc-mesh --xds-server-uri=trafficdirector.${REGION}.rep.googleapis.com:443 --gcp-project-number=${PROJECT} | sudo tee $GRPC_XDS_BOOTSTRAP
         sudo sed -i "s|\"authorities\": {|\"authorities\": {\n    \"traffic-director.${REGION}.xds.googleapis.com\": {\"xds_servers\":[{\"server_uri\": \"trafficdirector.${REGION}.rep.googleapis.com:443\", \"channel_creds\": [ { \"type\": \"google_default\" } ], \"server_features\": [ \"xds_v3\", \"ignore_resource_deletion\" ]}], \"client_listener_resource_name_template\": \"xdstp://traffic-director.${REGION}.xds.googleapis.com/envoy.config.listener.v3.Listener/${PROJECT}/mesh:grpc-mesh/%s\"},|g" $GRPC_XDS_BOOTSTRAP
         sudo sed -i "s|\"client_default_listener_resource_name_template\": \"xdstp://traffic-director-global.xds.googleapis.com|\"client_default_listener_resource_name_template\": \"xdstp://traffic-director.${REGION}.xds.googleapis.com|g" $GRPC_XDS_BOOTSTRAP')
         




#### Set up the environment variable and bootstrap file

The client application needs a bootstrap configuration file. The startup script in the previous section sets the `GRPC_XDS_BOOTSTRAP` environment variable and uses a helper script to generate the bootstrap file. The values for `TRAFFICDIRECTOR_GCP_PROJECT_NUMBER` and zone in the generated bootstrap file are obtained from the metadata server that knows these details about your Compute Engine VM instances.

You can provide these values to the helper script manually by using the `-gcp-project-number` option. You must provide a mesh name that matches the mesh resource using the `-config-mesh-experimental` option.

  1. To verify the configuration, sign in to the client:
         
         gcloud compute ssh grpc-client --zone=${ZONE}
         

  2. Download and install the `grpcurl` tool:
         
         curl -L https://github.com/fullstorydev/grpcurl/releases/download/v1.9.3/grpcurl_1.9.3_linux_x86_64.tar.gz | tar -xz
         

  3. Run the `grpcurl` tool with `xds:///helloworld-gce` as the service URI and `helloworld.Greeter/SayHello` as the service name and method to invoke.
         
         ./grpcurl --plaintext \
           -d '{"name": "world"}' \
           xds:///helloworld-gce helloworld.Greeter/SayHello
         

The parameters to the SayHello method are passed using the -d option.

You should see output similar to this, where `INSTANCE_NAME` is the name of the VM instance:
         
         Greeting: Hello world, from INSTANCE_HOSTNAME
         




This verifies that the proxyless gRPC client successfully connected to Cloud Service Mesh and learned about the backends for the helloworld-gce service using the xDS name resolver. The client sent a request to one of the service's backends without needing to know about the IP address or performing DNS resolution.

### Configuring Envoy sidecar proxy configuration with HTTP services with regional HTTPRoute and regional Mesh

This section explains how to configure an Envoy proxy-based service mesh with regional mesh and regional HTTPRoute resources.

For your convenience, store the Google Cloud project number you perform configuration in, so that all examples in this guide can be copy-pasted in the command line:
    
    
    export PROJECT_ID="PROJECT_ID"
    export PROJECT="PROJECT_NUMBER"
    export REGION="us-central1"
    export ZONE="us-central1-a"
    

Replace the following

  * PROJECT_ID with your project ID.
  * PROJECT_NUMBER with your project number.



Optionally, you can replace the following:

  * us-central1 with a different region you want to use.
  * us-central1-a with a different zone you want to use.



#### Mesh configuration

The sidecar Envoy proxy receives the service routing configuration from Cloud Service Mesh. The sidecar presents the name of the regional mesh resource to identify the specific service mesh configured. The routing configuration received from Cloud Service Mesh is used to direct the traffic going through the sidecar proxy to various regional Backend Services depending on request parameters, such as the hostname or headers, configured in the Route resource(s).

Note that the mesh name is the key that the sidecar proxy uses to request the configuration associated with this mesh.

  1. Create regional mesh specification and store it in the mesh.yaml file:
         
         cat <<EOF > mesh.yaml
         name: sidecar-mesh
         EOF
         

The interception port defaults to 15001 if unspecified.

  2. Create regional mesh using the mesh.yaml specification:
         
         gcloud network-services meshes import sidecar-mesh \
             --source=mesh.yaml \
             --location=${REGION}
         

After the regional mesh is created, Cloud Service Mesh is ready to serve the configuration. However, because no services are defined yet, the configuration will be empty.




#### HTTP server configuration

For demonstration purposes you will create a regional Backend Service with auto-scaled VMs (using [Managed instance groups](https://docs.cloud.google.com/compute/docs/instance-groups#managed_instance_groups) \- MIG) that will serve "hello world" using the gRPC protocol on port 80.

  1. Create the Compute Engine VM instance template with a `helloworld` HTTP service that is exposed on port 80:
         
         gcloud compute instance-templates create td-httpd-vm-template \
           --scopes=https://www.googleapis.com/auth/cloud-platform \
           --tags=http-td-server \
           --image-family=debian-11 \
           --image-project=debian-cloud \
           --metadata=startup-script="#! /bin/bash
         
         sudo apt-get update -y
         sudo apt-get install apache2 -y
         sudo service apache2 restart
         echo '<!doctype html><html><body><h1>'\`/bin/hostname\`'</h1></body></html>' | sudo tee /var/www/html/index.html"
         

  2. Create a MIG based on the template:
         
         gcloud compute instance-groups managed create http-td-mig-us-central1 \
           --zone=${ZONE} \
           --size=2 \
           --template=td-httpd-vm-template
         

  3. Create the health checks:
         
         gcloud compute health-checks create http http-helloworld-health-check --region=${REGION}
         

  4. Create a firewall rule to allow incoming health check connections to instances in your network:
         
         gcloud compute firewall-rules create http-vm-allow-health-checks \
           --network default --action allow --direction INGRESS \
           --source-ranges 35.191.0.0/16,209.85.152.0/22,209.85.204.0/22 \
           --target-tags http-td-server \
           --rules tcp:80
         

  5. Create a regional [backend service](https://docs.cloud.google.com/load-balancing/docs/backend-service) with a load balancing scheme of `INTERNAL_SELF_MANAGED`:
         
         gcloud compute backend-services create http-helloworld-service \
             --load-balancing-scheme=INTERNAL_SELF_MANAGED \
             --protocol=HTTP \
         --health-checks="https://www.googleapis.com/compute/v1/projects/${PROJECT}/regions/${REGION}/healthChecks/http-helloworld-health-check" \
             --region=${REGION}
         

  6. Add the health check and a managed or unmanaged instance group to the backend service:
         
         gcloud compute backend-services add-backend http-helloworld-service \
           --instance-group=http-td-mig-us-central1 \
           --instance-group-zone=${ZONE} \
           --region=${REGION}
         

This example uses the managed instance group with the Compute Engine VM template that runs the sample HTTP service we created earlier. 




#### Set up routing with regional HTTPRoute

The mesh resource and HTTP server are configured. You can now connect them using an HTTPRoute resource that associates a hostname with a Backend Service. 

  1. Create HTTPRoute specification and store as http_route.yaml:
         
         cat <<EOF > http_route.yaml
         name: helloworld-http-route
         hostnames:
         - helloworld-gce
         meshes:
         - projects/${PROJECT}/locations/${REGION}/meshes/sidecar-mesh
         rules:
         - action:
             destinations:
             - serviceName: projects/${PROJECT}/locations/${REGION}/backendServices/http-helloworld-service
         EOF
         

  2. Create the HTTPRoute using the http_route.yaml specification:
         
         gcloud network-services http-routes import helloworld-http-route \
             --source=http_route.yaml \
             --location=${REGION}
         

Cloud Service Mesh is now configured to load balance traffic for the services specified in the HTTPRoute across backends in the managed instance group.




#### Create HTTP client with Envoy sidecar

In this section you instantiate a client VM with Envoy sidecar proxy to request Cloud Service Mesh configuration created earlier. Note that the `mesh` parameter in the Google Cloud CLI command references the mesh resource created earlier.
    
    
    gcloud compute instance-templates create td-vm-template \
      --scopes=https://www.googleapis.com/auth/cloud-platform \
      --tags=http-td-tag,http-server,https-server \
      --image-family=debian-11 \
      --image-project=debian-cloud \
      --metadata=startup-script='#! /usr/bin/env bash
    
    # Set variables
    export ENVOY_CONTROL_PLANE_REGION="us-central1"
    export ENVOY_USER="envoy"
    export ENVOY_USER_UID="1337"
    export ENVOY_USER_GID="1337"
    export ENVOY_USER_HOME="/opt/envoy"
    export ENVOY_CONFIG="${ENVOY_USER_HOME}/config.yaml"
    export ENVOY_PORT="15001"
    export ENVOY_ADMIN_PORT="15000"
    export ENVOY_INBOUND_PORT="15006"
    export ENVOY_TRACING_ENABLED="false"
    export ENVOY_XDS_SERVER_CERT="/etc/ssl/certs/ca-certificates.crt"
    export ENVOY_ACCESS_LOG="/dev/stdout"
    export ENVOY_NODE_ID="$(cat /proc/sys/kernel/random/uuid)~$(hostname -i)"
    export BOOTSTRAP_TEMPLATE="${ENVOY_USER_HOME}/bootstrap_template.yaml"
    export GCE_METADATA_SERVER="169.254.169.254/32"
    export INTERCEPTED_CIDRS="*"
    export GCP_PROJECT_NUMBER=PROJECT_NUMBER
    export VPC_NETWORK_NAME=mesh:sidecar-mesh
    export GCE_ZONE=$(curl -sS -H "Metadata-Flavor: Google" http://metadata.google.internal/computeMetadata/v1/instance/zone | cut -d"/" -f4)
    
    # Create system user account for Envoy binary
    sudo groupadd ${ENVOY_USER} \
      --gid=${ENVOY_USER_GID} \
      --system
    sudo adduser ${ENVOY_USER} \
      --uid=${ENVOY_USER_UID} \
      --gid=${ENVOY_USER_GID} \
      --home=${ENVOY_USER_HOME} \
      --disabled-login \
      --system
    # Download and extract the Cloud Service Mesh tar.gz file
    cd ${ENVOY_USER_HOME}
    sudo curl -sL https://storage.googleapis.com/traffic-director/traffic-director-xdsv3.tar.gz -o traffic-director-xdsv3.tar.gz
    sudo tar -xvzf traffic-director-xdsv3.tar.gz traffic-director-xdsv3/bootstrap_template.yaml \
      -C bootstrap_template.yaml \
      --strip-components 1
    sudo tar -xvzf traffic-director-xdsv3.tar.gz traffic-director-xdsv3/iptables.sh \
      -C iptables.sh \
      --strip-components 1
    sudo rm traffic-director-xdsv3.tar.gz
    
    # Generate Envoy bootstrap configuration
    cat "${BOOTSTRAP_TEMPLATE}" \
      | sed -e "s|ENVOY_NODE_ID|${ENVOY_NODE_ID}|g" \
      | sed -e "s|ENVOY_ZONE|${GCE_ZONE}|g" \
      | sed -e "s|VPC_NETWORK_NAME|${VPC_NETWORK_NAME}|g" \
      | sed -e "s|CONFIG_PROJECT_NUMBER|${GCP_PROJECT_NUMBER}|g" \
      | sed -e "s|ENVOY_PORT|${ENVOY_PORT}|g" \
      | sed -e "s|ENVOY_ADMIN_PORT|${ENVOY_ADMIN_PORT}|g" \
      | sed -e "s|XDS_SERVER_CERT|${ENVOY_XDS_SERVER_CERT}|g" \
      | sed -e "s|TRACING_ENABLED|${ENVOY_TRACING_ENABLED}|g" \
      | sed -e "s|ACCESSLOG_PATH|${ENVOY_ACCESS_LOG}|g" \
      | sed -e "s|BACKEND_INBOUND_PORTS|${BACKEND_INBOUND_PORTS}|g" \
      | sed -e "s|ENVOY_INBOUND_PORT|${ENVOY_INBOUND_PORT}|g" \
      | sed -e "s|trafficdirector.googleapis.com|trafficdirector.${ENVOY_CONTROL_PLANE_REGION}.rep.googleapis.com|g" \
      | sudo tee "${ENVOY_CONFIG}"
    
    # Install Envoy binary
    wget -O envoy_key https://apt.envoyproxy.io/signing.key
    cat envoy_key | sudo gpg --dearmor > $(pwd)/envoy-keyring.gpg
    echo "deb [arch=$(dpkg --print-architecture) signed-by=$(pwd)/envoy-keyring.gpg] https://apt.envoyproxy.io bullseye main" | sudo tee /etc/apt/sources.list.d/envoy.list
    sudo apt-get update
    sudo apt-get install envoy
    
    # Run Envoy as systemd service
    sudo systemd-run --uid=${ENVOY_USER_UID} --gid=${ENVOY_USER_GID} \
      --working-directory=${ENVOY_USER_HOME} --unit=envoy.service \
      bash -c "/usr/bin/envoy --config-path ${ENVOY_CONFIG} | tee"
    
    # Configure iptables for traffic interception and redirection
    sudo ${ENVOY_USER_HOME}/iptables.sh \
      -p "${ENVOY_PORT}" \
     -u "${ENVOY_USER_UID}" \
      -g "${ENVOY_USER_GID}" \
      -m "REDIRECT" \
      -i "${INTERCEPTED_CIDRS}" \
      -x "${GCE_METADATA_SERVER}"
    '
    
    gcloud compute instances create td-vm-client \
      --zone=${ZONE} \
      --source-instance-template td-vm-template
    

  1. Login to the created VM:
         
         gcloud compute ssh td-vm-client --zone=${ZONE}
         

  2. Verify HTTP connectivity to the created test services:
         
         curl -H "Host: helloworld-gce" http://10.0.0.1/
         

The command returns a response from one of the VMs in the Managed Instance Group with its hostname printed to the console.




### Configuring TCP services with regional TCPRoute

This configuration flow is very similar to [Set up Envoy proxies with HTTP services](https://docs.cloud.google.com/service-mesh/v1.29/docs/service-routing/set-up-envoy-http-mesh) with an exception that Backend Service provides a TCP service and routing based on the TCP/IP parameters is used rather than based on the HTTP protocol.

For your convenience, store the Google Cloud project number you perform configuration in, so that all examples in this guide can be copy-pasted in the command line:
    
    
    export PROJECT_ID="PROJECT_ID"
    export PROJECT="PROJECT_NUMBER"
    export REGION="us-central1"
    export ZONE="us-central1-a"
    

Replace the following

  * PROJECT_ID with your project ID.
  * PROJECT_NUMBER with your project number.



Optionally, you can replace the following:

  * us-central1 with a different region you want to use.
  * us-central1-a with a different zone you want to use.



#### Mesh configuration

  1. Create regional mesh specification and store it in the mesh.yaml file:
         
         cat <<EOF > mesh.yaml
         name: sidecar-mesh
         EOF
         

  2. Create regional mesh using the mesh.yaml specification:
         
         gcloud network-services meshes import sidecar-mesh \
             --source=mesh.yaml \
             --location=${REGION}
         




#### TCP server configuration

For demonstration purposes you will create a regional Backend Service with auto-scaled VMs (using [Managed instance groups](https://docs.cloud.google.com/compute/docs/instance-groups#managed_instance_groups) \- MIG) that will serve "hello world" using the gRPC protocol on port 10000.

  1. Create the Compute Engine VM instance template with a test service on port 10000 using netcat utility:
         
         gcloud compute instance-templates create tcp-td-vm-template \
           --scopes=https://www.googleapis.com/auth/cloud-platform \
           --tags=allow-health-checks \
           --image-family=debian-11 \
           --image-project=debian-cloud \
           --metadata=startup-script="#! /bin/bash
         sudo apt-get update -y
         sudo apt-get install netcat -y
         while true;
           do echo 'Hello from TCP service' | nc -l -s 0.0.0.0 -p 10000;
         done &"
         

  2. Create a MIG based on the template:
         
         gcloud compute instance-groups managed create tcp-td-mig-us-central1 \
           --zone=${ZONE} \
           --size=1 \
           --template=tcp-td-vm-template
         

  3. Set the named ports on the created managed instance group to `port 10000`:
         
         gcloud compute instance-groups set-named-ports tcp-td-mig-us-central1 \
           --zone=${ZONE} --named-ports=tcp:10000
         

  4. Create a regional health check:
         
         gcloud compute health-checks create tcp tcp-helloworld-health-check --port 10000 --region=${REGION}
         

  5. Create a firewall rule to allow incoming health check connections to instances in your network:
         
         gcloud compute firewall-rules create tcp-vm-allow-health-checks \
           --network default --action allow --direction INGRESS \
           --source-ranges 35.191.0.0/16,209.85.152.0/22,209.85.204.0/22 \
           --target-tags allow-health-checks \
           --rules tcp:10000
         

  6. Create a regional backend service with a load balancing scheme of INTERNAL_SELF_MANAGED and add the health check and a managed or unmanaged instance group to the backend service.
         
         gcloud compute backend-services create tcp-helloworld-service \
             --region=${REGION} \
             --load-balancing-scheme=INTERNAL_SELF_MANAGED \
             --protocol=TCP \
             --port-name=tcp \
             --health-checks="https://www.googleapis.com/compute/v1/projects/${PROJECT}/regions/${REGION}/healthChecks/tcp-helloworld-health-check"
         

  7. Add the MIG to the BackendService:
         
         gcloud compute backend-services add-backend tcp-helloworld-service \
           --instance-group tcp-td-mig-us-central1 \
           --instance-group-zone=${ZONE} \
           --region=${REGION}
         




#### Set up routing with regional TCPRoute

  1. Create TCPRoute specification and store it in the tcp_route.yaml file:
         
         cat <<EOF > tcp_route.yaml
         name: helloworld-tcp-route
         meshes:
         - projects/${PROJECT}/locations/${REGION}/meshes/sidecar-mesh
         rules:
         - action:
             destinations:
             - serviceName: projects/${PROJECT}/locations/${REGION}/backendServices/tcp-helloworld-service
           matches:
           - address: '10.0.0.1/32'
             port: '10000'
         EOF
         

  2. Create TCPRoute using the tcp_route.yaml specification:
         
         gcloud network-services tcp-routes import helloworld-tcp-route \
             --source=tcp_route.yaml \
             --location=${REGION}
         




#### Create TCP client with Envoy sidecar

  1. Create a VM with Envoy connected to Cloud Service Mesh:
         
         gcloud compute instance-templates create td-vm-template \
           --scopes=https://www.googleapis.com/auth/cloud-platform \
           --tags=http-td-tag,http-server,https-server \
           --image-family=debian-11 \
           --image-project=debian-cloud \
           --metadata=startup-script='#! /usr/bin/env bash
         
         # Set variables
         export ENVOY_CONTROL_PLANE_REGION="us-central1"
         export ENVOY_USER="envoy"
         export ENVOY_USER_UID="1337"
         export ENVOY_USER_GID="1337"
         export ENVOY_USER_HOME="/opt/envoy"
         export ENVOY_CONFIG="${ENVOY_USER_HOME}/config.yaml"
         export ENVOY_PORT="15001"
         export ENVOY_ADMIN_PORT="15000"
         export ENVOY_TRACING_ENABLED="false"
         export ENVOY_XDS_SERVER_CERT="/etc/ssl/certs/ca-certificates.crt"
         export ENVOY_ACCESS_LOG="/dev/stdout"
         export ENVOY_NODE_ID="$(cat /proc/sys/kernel/random/uuid)~$(hostname -i)"
         export BOOTSTRAP_TEMPLATE="${ENVOY_USER_HOME}/bootstrap_template.yaml"
         export GCE_METADATA_SERVER="169.254.169.254/32"
         export INTERCEPTED_CIDRS="*"
         export GCP_PROJECT_NUMBER=PROJECT_NUMBER
         export VPC_NETWORK_NAME=mesh:sidecar-mesh
         
         export GCE_ZONE=$(curl -sS -H "Metadata-Flavor: Google" http://metadata.google.internal/computeMetadata/v1/instance/zone | cut -d"/" -f4)
         
         # Create system user account for Envoy binary
         sudo groupadd ${ENVOY_USER} \
           --gid=${ENVOY_USER_GID} \
           --system
         sudo adduser ${ENVOY_USER} \
           --uid=${ENVOY_USER_UID} \
           --gid=${ENVOY_USER_GID} \
           --home=${ENVOY_USER_HOME} \
           --disabled-login \
           --system
         # Download and extract the Cloud Service Mesh tar.gz file
         cd ${ENVOY_USER_HOME}
         sudo curl -sL https://storage.googleapis.com/traffic-director/traffic-director-xdsv3.tar.gz -o traffic-director-xdsv3.tar.gz
         sudo tar -xvzf traffic-director-xdsv3.tar.gz traffic-director-xdsv3/bootstrap_template.yaml \
           -C bootstrap_template.yaml \
           --strip-components 1
         sudo tar -xvzf traffic-director-xdsv3.tar.gz traffic-director-xdsv3/iptables.sh \
           -C iptables.sh \
           --strip-components 1
         sudo rm traffic-director-xdsv3.tar.gz
         
         # Generate Envoy bootstrap configuration
         cat "${BOOTSTRAP_TEMPLATE}" \
           | sed -e "s|ENVOY_NODE_ID|${ENVOY_NODE_ID}|g" \
           | sed -e "s|ENVOY_ZONE|${GCE_ZONE}|g" \
           | sed -e "s|VPC_NETWORK_NAME|${VPC_NETWORK_NAME}|g" \
           | sed -e "s|CONFIG_PROJECT_NUMBER|${GCP_PROJECT_NUMBER}|g" \
           | sed -e "s|ENVOY_PORT|${ENVOY_PORT}|g" \
           | sed -e "s|ENVOY_ADMIN_PORT|${ENVOY_ADMIN_PORT}|g" \
           | sed -e "s|XDS_SERVER_CERT|${ENVOY_XDS_SERVER_CERT}|g" \
           | sed -e "s|TRACING_ENABLED|${ENVOY_TRACING_ENABLED}|g" \
           | sed -e "s|ACCESSLOG_PATH|${ENVOY_ACCESS_LOG}|g" \
           | sed -e "s|BACKEND_INBOUND_PORTS|${BACKEND_INBOUND_PORTS}|g" \
           | sed -e "s|trafficdirector.googleapis.com|trafficdirector.${ENVOY_CONTROL_PLANE_REGION}.rep.googleapis.com|g" \
           | sudo tee "${ENVOY_CONFIG}"
         
         # Install Envoy binary
         wget -O envoy_key https://apt.envoyproxy.io/signing.key
         cat envoy_key | sudo gpg --dearmor > $(pwd)/envoy-keyring.gpg
         echo "deb [arch=$(dpkg --print-architecture) signed-by=$(pwd)/envoy-keyring.gpg] https://apt.envoyproxy.io bullseye main" | sudo tee /etc/apt/sources.list.d/envoy.list
         sudo apt-get update
         sudo apt-get install envoy
         
         # Run Envoy as systemd service
         sudo systemd-run --uid=${ENVOY_USER_UID} --gid=${ENVOY_USER_GID} \
           --working-directory=${ENVOY_USER_HOME} --unit=envoy.service \
           bash -c "/usr/bin/envoy --config-path ${ENVOY_CONFIG} | tee"
         
         # Configure iptables for traffic interception and redirection
         sudo ${ENVOY_USER_HOME}/iptables.sh \
           -p "${ENVOY_PORT}" \
         -u "${ENVOY_USER_UID}" \
           -g "${ENVOY_USER_GID}" \
           -m "REDIRECT" \
           -i "${INTERCEPTED_CIDRS}" \
           -x "${GCE_METADATA_SERVER}"
         '
         
         gcloud compute instances create td-vm-client \
           --zone=${ZONE} \
           --source-instance-template td-vm-template
         

  2. Login to the created VM:
         
         gcloud compute ssh td-vm-client --zone=${ZONE}
         

  3. Verify connectivity to the created test services:
         
         curl 10.0.0.1:10000 --http0.9 -v
         

You should see a text `Hello from TCP service` returned to you as well as be able to see any text you type returned back to you by the netcat service running on the remote VM.




### Regional mesh configuration in the host project

Designate a project as the host project. Any service account with permission to create/update/delete meshes in this project can control the routing configurations attached to regional meshes in this project.

  1. Define a variable that will be used throughout the example:
         
         export REGION="us-central1"
         

Optionally, you can replace us-central1 with a different region you want to use.

  2. Create mesh specification and store it in the mesh.yaml file:
         
         cat <<EOF > mesh.yaml
         name: shared-mesh
         EOF
         

  3. Define a mesh resource in this project with the required configuration:
         
         gcloud network-services meshes import shared-mesh \
             --source=mesh.yaml \
             --location=${REGION}
         

Note the full URI of this mesh resource. Service owners will need it in the future in to attach their routes to this Mesh.

  4. Grant the `networkservices.meshes.use` IAM permission to this mesh and to the cross-project service accounts that should be able to attach their services information to this mesh:
         
         gcloud projects add-iam-policy-binding HOST_PROJECT_NUMBER --member='HTTP_ROUTE_SERVICE_OWNER_ACCOUNT' --role='roles/compute.networkAdmin'
         

Now all service owners that have `networkservices.meshes.use` permission granted to them are able to add their routing rules to this mesh.




#### Route configuration in service projects

Each service owner needs to create regional Backend Service(s) and regional Route resources in their project similar to [Set up Envoy proxies with HTTP services](https://docs.cloud.google.com/service-mesh/v1.29/docs/service-routing/set-up-envoy-http-mesh). The only difference is that each HTTPRoute/GRPCRoute/TCPRoute would have the URI of the host project's mesh resource in the `meshes` field.

  1. Create a sharedvpc-http-route:
         
         echo "name: sharedvpc-http-route
         hostnames:
         - helloworld-gce
         meshes:
         - /projects/HOST_PROJECT_NUMBER/locations/${REGION}/meshes/shared-mesh
         rules:
         - action:
             destinations:
             - serviceName: \"SERVICE_URL\"" | \
         gcloud network-services http-routes import sharedvpc-http-route \
             --source=- \
             --location=${REGION}
         




#### Configuring client services in service projects

While configuring a Cloud Service Mesh client (Envoy proxy or proxyless) that is located in a service project needs to specify the project number where the mesh resource is located and the mesh name in its bootstrap configuration. `sh TRAFFICDIRECTOR_GCP_PROJECT_NUMBER=HOST_PROJECT_NUMBER TRAFFICDIRECTOR_MESH_NAME=MESH_NAME`

### Configuring published service backends for regional Cloud Service Mesh

Published service backends let you configure regional Cloud Service Mesh to route traffic to published services through Private Service Connect.

For more information about published service backends, see [published service backends](https://docs.cloud.google.com/vpc/docs/about-accessing-vpc-hosted-services-endpoints#service-bindings).

Before you complete the steps in the following sections, do the following:

  * Make sure that the producer and consumer VPC networks belong to the same organization.
  * [Identify the service attachment URI](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer#attachment-details) of the service that you want to access.
  * Identify the name of the VPC network that your Cloud Service Mesh clients will use. This is required for the `TRAFFICDIRECTOR_NETWORK_NAME` configuration.



#### Set up environment variables

For your convenience, store the following values so that all examples in this section can be copy-pasted in the command line:
    
    
    export PROJECT_NUMBER="PROJECT_NUMBER"
    export REGION="us-central1"
    export MESH_NAME="my-mesh"
    export NETWORK_NAME="default"
    export SUBNET_NAME="default"
    export SERVICE_ATTACHMENT_URI="SERVICE_ATTACHMENT_URI"
    export BACKEND_SERVICE_NAME="published-service-backend"
    

#### Client configuration

To ensure that the correct Private Service Connect endpoints are delivered to your Cloud Service Mesh clients (Envoy or proxyless gRPC), you must include the `TRAFFICDIRECTOR_NETWORK_NAME` variable in the node metadata.
    
    
    TRAFFICDIRECTOR_GCP_PROJECT_NUMBER=${PROJECT_NUMBER}
    TRAFFICDIRECTOR_MESH_NAME=${MESH_NAME}
    TRAFFICDIRECTOR_NETWORK_NAME=${NETWORK_NAME}
    

#### Create a regional Mesh
    
    
    gcloud network-services meshes import ${MESH_NAME} \
        --location=${REGION} \
        --source=- <<EOF
    name: ${MESH_NAME}
    EOF
    

#### Create a Private Service Connect endpoint

A Private Service Connect endpoint is required in the consumer network to connect to the service attachment.

  1. Reserve an internal IP address for the endpoint. If the subnet that you want to use doesn't exist, [create one](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#add-subnets).
         
         gcloud compute addresses create psc-endpoint-ip \
             --region=${REGION} \
             --subnet=${SUBNET_NAME} \
             --purpose=GCE_ENDPOINT
         

  2. Create the forwarding rule for the endpoint:
         
         gcloud compute forwarding-rules create psc-endpoint \
             --region=${REGION} \
             --network=${NETWORK_NAME} \
             --address=psc-endpoint-ip \
             --target=${SERVICE_ATTACHMENT_URI}
         




#### Create a backend service with a published service backend

To use published service backends, you add the service attachment URI as a backend to the regional backend service.

  1. Create the regional backend service:
         
         gcloud beta compute backend-services create published-service-backend \
             --load-balancing-scheme=INTERNAL_SELF_MANAGED \
             --protocol=HTTP \
             --region=${REGION}
         

  2. Associate the backend service with a service attachment (replace /regions with /locations in the service attachment URI):
         
         gcloud beta compute backend-services add-backend published-service-backend \
             --region=${REGION} \
             --service=${SERVICE_ATTACHMENT_URI}
         




#### Configure routing with an HTTPRoute

  * Create the HTTPRoute and attach it to the Mesh:
        
        gcloud network-services http-routes import published-service-backend-route \
            --location=${REGION} \
            --source=- <<EOF
        name: published-service-backend-route
        hostnames:
        - helloworld-gce
        meshes:
        - projects/${PROJECT_NUMBER}/locations/${REGION}/meshes/${MESH_NAME}
        rules:
        - action:
            destinations:
            - serviceName: projects/${PROJECT_NUMBER}/locations/${REGION}/backendServices/${BACKEND_SERVICE_NAME}
        EOF
        




Clients in the mesh can now reach the published service by using the hostname `helloworld-gce`.

### Gateway TLS routing

This section demonstrates how to set up an Envoy proxy-based ingress gateway with regional Gateway and regional TLSRoute resources.

A regional external passthrough Network Load Balancer directs traffic to Envoy proxies that act as an ingress gateway. The Envoy proxies use TLS passthrough routing and direct traffic to HTTPS servers running on the backend VM instances.

Define some variables that will be used throughout the example.
    
    
    export PROJECT_ID="PROJECT_ID"
    export PROJECT_NUMBER="PROJECT_NUMBER"
    export REGION="us-central1"
    export ZONE="us-central1-b"
    export NETWORK_NAME = "default"
    

Replace the following: default

  * PROJECT_ID with your project ID.
  * PROJECT_NUMBER with your project number.



Optionally, you can replace the following:

  * us-central1 with a different region you want to use.
  * us-central1-b with a different zone you want to use.
  * default with a different network name you want to use.



### Cross-referencing regional mesh and regional route resources in multi-project Shared VPC environment

There are scenarios where service mesh configuration consists of services that are owned by different projects. For example, in Shared VPC or peered VPC deployments it is possible for each project owner to define their own set of services with a purpose for these services to be available to all other projects.

This configuration is "cross-project" because multiple resources defined in different projects are combined together to form a single configuration that can be served to a proxy or proxyless client.

**Note:** References between regional resource must exist in the same region.

#### Configure firewall rules

  1. Configure firewall rules to allow traffic from any source. Edit the commands for your ports and source IP address ranges.
         
         gcloud compute firewall-rules create allow-gateway-health-checks \
         --network=${NETWORK_NAME} \
         --direction=INGRESS \
         --action=ALLOW \
         --rules=tcp \
         --source-ranges="35.191.0.0/16,209.85.152.0/22,209.85.204.0/22" \
         --target-tags=gateway-proxy
         




#### Configure IAM permissions

  1. Create a service account identity for the gateway proxies:
         
         gcloud iam service-accounts create gateway-proxy
         

  2. Assign the required IAM roles to the service account identity:
         
         gcloud projects add-iam-policy-binding ${PROJECT_ID} \
           --member="serviceAccount:gateway-proxy@${PROJECT_ID}.iam.gserviceaccount.com" \
           --role="roles/trafficdirector.client"
         
         
         gcloud projects add-iam-policy-binding ${PROJECT_ID} \
           --member="serviceAccount:gateway-proxy@${PROJECT_ID}.iam.gserviceaccount.com" \
           --role="roles/logging.logWriter"
         




#### Configure the regional Gateway:

  1. In a file called gateway8443.yaml, create the Gateway specification for HTTP traffic:
         
         cat <<EOF > gateway8443.yaml
         name: gateway8443
         scope: gateway-proxy-8443
         ports:
         - 8443
         type: OPEN_MESH
         EOF
         

  2. Create the regional Gateway resource using the gateway8443.yaml specification:
         
         gcloud network-services gateways import gateway8443 \
             --source=gateway8443.yaml \
             --location=${REGION}
         




#### Create a managed instance group with Envoy proxies

In this section you create an instance template for a VM running an automatically deployed Envoy service proxy. The Envoys have the scope set to `gateway-proxy`. Don't pass the serving port as a parameter of the `--service-proxy` flag.

  1. Create a managed instance group with Envoy proxies:
         
         gcloud beta compute instance-templates create gateway-proxy \
           --scopes=https://www.googleapis.com/auth/cloud-platform \
           --tags=gateway-proxy,http-td-tag,http-server,https-server \
           --image-family=debian-11 \
           --image-project=debian-cloud \
           --network-interface=network=${NETWORK_NAME} \
           --service-account="gateway-proxy@${PROJECT_ID}.iam.gserviceaccount.com" \
           --metadata=startup-script='#! /usr/bin/env bash
         
         # Set variables
         export ENVOY_CONTROL_PLANE_REGION="us-central1"
         export GCP_PROJECT_NUMBER=PROJECT_NUMBER
         export VPC_NETWORK_NAME=scope:gateway-proxy-8443
         export ENVOY_USER="envoy"
         export ENVOY_USER_UID="1337"
         export ENVOY_USER_GID="1337"
         export ENVOY_USER_HOME="/opt/envoy"
         export ENVOY_CONFIG="${ENVOY_USER_HOME}/config.yaml"
         export ENVOY_PORT="15001"
         export ENVOY_ADMIN_PORT="15000"
         export ENVOY_TRACING_ENABLED="false"
         export ENVOY_XDS_SERVER_CERT="/etc/ssl/certs/ca-certificates.crt"
         export ENVOY_ACCESS_LOG="/dev/stdout"
         export ENVOY_NODE_ID="$(cat /proc/sys/kernel/random/uuid)~$(hostname -i)"
         export BOOTSTRAP_TEMPLATE="${ENVOY_USER_HOME}/bootstrap_template.yaml"
         export GCE_METADATA_SERVER="169.254.169.254/32"
         export INTERCEPTED_CIDRS="*"
         
         export GCE_ZONE=$(curl -sS -H "Metadata-Flavor: Google" http://metadata.google.internal/computeMetadata/v1/instance/zone | cut -d"/" -f4)
         
         # Create system user account for Envoy binary
         sudo groupadd ${ENVOY_USER} \
           --gid=${ENVOY_USER_GID} \
           --system
         sudo adduser ${ENVOY_USER} \
           --uid=${ENVOY_USER_UID} \
           --gid=${ENVOY_USER_GID} \
           --home=${ENVOY_USER_HOME} \
           --disabled-login \
           --system
         # Download and extract the Cloud Service Mesh tar.gz file
         cd ${ENVOY_USER_HOME}
         sudo curl -sL https://storage.googleapis.com/traffic-director/traffic-director-xdsv3.tar.gz -o traffic-director-xdsv3.tar.gz
         sudo tar -xvzf traffic-director-xdsv3.tar.gz traffic-director-xdsv3/bootstrap_template.yaml \
           -C bootstrap_template.yaml \
           --strip-components 1
         sudo tar -xvzf traffic-director-xdsv3.tar.gz traffic-director-xdsv3/iptables.sh \
           -C iptables.sh \
           --strip-components 1
         sudo rm traffic-director-xdsv3.tar.gz
         
         # Generate Envoy bootstrap configuration
         cat "${BOOTSTRAP_TEMPLATE}" \
           | sed -e "s|ENVOY_NODE_ID|${ENVOY_NODE_ID}|g" \
           | sed -e "s|ENVOY_ZONE|${GCE_ZONE}|g" \
           | sed -e "s|VPC_NETWORK_NAME|${VPC_NETWORK_NAME}|g" \
           | sed -e "s|CONFIG_PROJECT_NUMBER|${GCP_PROJECT_NUMBER}|g" \
           | sed -e "s|ENVOY_PORT|${ENVOY_PORT}|g" \
           | sed -e "s|ENVOY_ADMIN_PORT|${ENVOY_ADMIN_PORT}|g" \
           | sed -e "s|XDS_SERVER_CERT|${ENVOY_XDS_SERVER_CERT}|g" \
           | sed -e "s|TRACING_ENABLED|${ENVOY_TRACING_ENABLED}|g" \
           | sed -e "s|ACCESSLOG_PATH|${ENVOY_ACCESS_LOG}|g" \
           | sed -e "s|BACKEND_INBOUND_PORTS|${BACKEND_INBOUND_PORTS}|g" \
           | sed -e "s|trafficdirector.googleapis.com|trafficdirector.${ENVOY_CONTROL_PLANE_REGION}.rep.googleapis.com|g" \
           | sudo tee "${ENVOY_CONFIG}"
         
         # Install Envoy binary
         wget -O envoy_key https://apt.envoyproxy.io/signing.key
         cat envoy_key | sudo gpg --dearmor > $(pwd)/envoy-keyring.gpg
         echo "deb [arch=$(dpkg --print-architecture) signed-by=$(pwd)/envoy-keyring.gpg] https://apt.envoyproxy.io bullseye main" | sudo tee /etc/apt/sources.list.d/envoy.list
         sudo apt-get update
         sudo apt-get install envoy
         
         # Run Envoy as systemd service
         sudo systemd-run --uid=${ENVOY_USER_UID} --gid=${ENVOY_USER_GID} \
           --working-directory=${ENVOY_USER_HOME} --unit=envoy.service \
           bash -c "/usr/bin/envoy --config-path ${ENVOY_CONFIG} | tee"
         
         # Configure iptables for traffic interception and redirection
         sudo ${ENVOY_USER_HOME}/iptables.sh \
           -p "${ENVOY_PORT}" \
         -u "${ENVOY_USER_UID}" \
           -g "${ENVOY_USER_GID}" \
           -m "REDIRECT" \
           -i "${INTERCEPTED_CIDRS}" \
           -x "${GCE_METADATA_SERVER}"
         '
         

  2. Create a regional managed instance group from the instance template:
         
         gcloud compute instance-groups managed create gateway-proxy \
           --region=${REGION} \
           --size=1 \
           --template=gateway-proxy
         

  3. Set the serving port name for the managed instance group:
         
         gcloud compute instance-groups managed set-named-ports gateway-proxy \
           --named-ports=https:8443 \
           --region=${REGION}
         




#### Set up the regional external passthrough network load balancer

  1. Create a static external regional IP address:
         
         gcloud compute addresses create xnlb-${REGION} \
           --region=${REGION}
         

  2. Obtain the IP address that is reserved for the external load balancer:
         
         gcloud compute addresses describe xnlb-${REGION} \
           --region=${REGION} --format='value(address)'
         

  3. Create a health check for the gateway proxies:
         
         gcloud compute health-checks create tcp xnlb-${REGION} \
           --region=${REGION} \
           --use-serving-port
         

  4. Create a backend service for the gateway proxies:
         
         gcloud compute backend-services create xnlb-${REGION} \
           --health-checks=xnlb-${REGION} \
           --health-checks-region=${REGION} \
           --load-balancing-scheme=EXTERNAL \
           --protocol=TCP \
           --region=${REGION} \
           --port-name=https
         

  5. Add the managed instance group as a backend:
         
         gcloud compute backend-services add-backend xnlb-${REGION} \
           --instance-group=gateway-proxy \
           --instance-group-region=${REGION} \
           --region=${REGION}
         

  6. Create a forwarding rule to route traffic to the gateway proxies:
         
         gcloud compute forwarding-rules create xnlb-${REGION} \
           --region=${REGION} \
           --load-balancing-scheme=EXTERNAL \
           --address=${IP_ADDRESS} \
           --ip-protocol=TCP \
           --ports=8443 \
           --backend-service=xnlb-${REGION} \
           --backend-service-region=${REGION}
         




#### Configure a managed instance group running an HTTPS service

  1. Create an instance template with an HTTPS service that is exposed on port 8443:
         
         gcloud compute instance-templates create td-https-vm-template \
           --scopes=https://www.googleapis.com/auth/cloud-platform \
           --tags=https-td-server \
           --image-family=debian-11 \
           --image-project=debian-cloud \
           --metadata=startup-script='#! /bin/bash
         
         sudo rm -rf /var/lib/apt/lists/*
         sudo apt-get -y clean
         sudo apt-get -y update
         sudo apt-get -y install apt-transport-https ca-certificates curl gnupg2 software-properties-common
         sudo curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -
         sudo add-apt-repository -y "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable"
         sudo apt-get -y update
         sudo apt-get -y install docker-ce
         sudo which docker
         echo "{ \"registry-mirrors\": [\"https://mirror.gcr.io\"] }" | sudo tee -a /etc/docker/daemon.json
         sudo service docker restart
         sudo docker run -e HTTPS_PORT=9999 -p 8443:9999 --rm -dt mendhak/http-https-echo:22'
         

  2. Create a managed instance group based on the instance template:
         
         gcloud compute instance-groups managed create https-td-mig-us-${REGION} \
           --zone=${ZONE} \
           --size=2 \
           --template=td-https-vm-template
         

  3. Set the name of the serving port for the managed instance group:
         
         gcloud compute instance-groups managed set-named-ports https-td-mig-us-${REGION} \
           --named-ports=https:8443 \
           --zone=${ZONE}
         

  4. Create a health check:
         
         gcloud compute health-checks create https https-helloworld-health-check \
           --port=8443 --region=${REGION}
         

  5. Create a firewall rule to allow incoming health check connections to instances in your network:
         
         gcloud compute firewall-rules create https-vm-allow-health-checks \
           --network ${NETWORK_NAME} --action allow --direction INGRESS \
           --source-ranges 35.191.0.0/16,130.211.0.0/22 \
           --target-tags https-td-server \
           --rules tcp:8443
         

  6. Create a regional backend service with a load balancing scheme of `INTERNAL_SELF_MANAGED` and add the health check:
         
         gcloud compute backend-services create https-helloworld-service \
           --region=${REGION} \
           --load-balancing-scheme=INTERNAL_SELF_MANAGED \
           --port-name=https \
           --health-checks="https://www.googleapis.com/compute/v1/projects/${PROJECT}/regions/${REGION}/healthChecks/https-helloworld-health-check"
         

  7. Add the managed instance group as a backend to the backend service:
         
         gcloud compute backend-services add-backend https-helloworld-service \
           --instance-group=https-td-mig-us-${REGION} \
           --instance-group-zone=${ZONE} \
           --region=${REGION}
         




#### Set up routing with a TLSRoute resource

  1. In a file called tls_route.yaml, create the TLSRoute specification:
         
         cat <<EOF > tls_route.yaml
         name: helloworld-tls-route
         gateways:
         - projects/${PROJECT_NUMBER}/locations/${REGION}/gateways/gateway8443
         rules:
         - matches:
           - sniHost:
             - example.com
             alpn:
             - h2
           action:
             destinations:
             - serviceName: projects/${PROJECT_NUMBER}/locations/${REGION}/backendServices/https-helloworld-service
         EOF
         

In the previous instruction, TLSRoute matches example.com as SNI and h2 as ALPN. If the matches are changed as follows, TLSRoute matches SNI or ALPN:
         
         - matches:
           - sniHost:
             - example.com
           - alpn:
             - h2
         

  2. Use the tls_route.yaml specification to create the TLSRoute resource:
         
         gcloud network-services tls-routes import helloworld-tls-route \
             --source=tls_route.yaml \
             --location=${REGION}
         




#### Validate the deployment

  1. Run the following curl command to verify HTTP connectivity to the test services that you created:
         
         curl https://example.com:8443 --resolve example.com:8443:${IP_ADDRESS} -k
         

  2. The command returns a response from one of the VMs in the managed instance group. The output is similar to the following:
         
         {
           "path": "/",
           "headers": {
             "host": "example.com:8443",
             "user-agent": "curl/8.16.0",
             "accept": "*/*"
           },
           "method": "GET",
           "body": "",
           "fresh": false,
           "hostname": "example.com",
           "ip": "::ffff:10.128.0.59",
           "ips": [],
           "protocol": "https",
           "query": {},
           "subdomains": [],
           "xhr": false,
           "os": {
             "hostname": "19cd7812e792"
           },
           "connection": {
             "servername": "example.com"
           }
         




#### Verify with a negative verification

  1. In the following command, the SNI does not match example.com, so the Gateway rejects the connection:
         
         curl https://invalid-server.com:8443 --resolve invalid-server.com:8443:${IP_ADDRESS} -k
         

  2. In the following command, the ALPN does not match h2 (HTTP2 protocol), so the Gateway rejects the connection:
         
         curl https://example.com:8443 --resolve example.com:8443:${IP_ADDRESS} -k --http1.1
         

The previous commands all return the following error:
         
         curl: (35) OpenSSL SSL_connect: Connection reset by peer in connection.
         

  3. In the following command, the client is creating a plain text (unencrypted) connection, so the Gateway rejects the connection with a 404 Not Found error:
         
         curl example.com:8443 --resolve example.com:8443:${IP_ADDRESS} -k
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
