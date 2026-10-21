---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/solutions/l7-lb-haproxy-impl/
title: HAProxy Layer 7 load balancing reference implementation \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T12:31:05.684063+00:00
---

# HAProxy Layer 7 load balancing reference implementation  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/solutions/l7-lb-haproxy-impl/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  HAProxy Layer 7 load balancing reference implementation Stay organized with collections  Save and categorize content based on your preferences. 

Google Distributed Cloud (GDC) air-gapped provides a built-in managed Layer 4 (L4) load balancer, but many enterprise applications require advanced Layer 7 (L7) capabilities, such as host-based routing, centralized TLS management, and complex traffic splitting. Historically, this is accomplished using the Ingress API, which is now considered feature-frozen in the Kubernetes community.

This reference architecture provides a self-managed Layer 7 load balancing solution. By deploying the popular HAProxy open source controller on a GDC standard cluster, customers can seamlessly route L7 traffic to hybrid environments. This architecture uses TLS Termination (HTTPRoute) to route traffic based on Server Name Indication (SNI) to both built-in containerized pods and applications hosted on external Virtual Machines.

## Architecture

![Architecture diagram for HAProxy Layer 7 load balancing on GDC air-gapped.](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/gdcag/solutions/images/l7-lb-haproxy-arch.png)

The key components of the solution include:

  * **Client:** An entity initiating HTTPS requests to interact with the applications.
  * **GDC standard cluster:** GDC provides a built-in way to create Kubernetes Vanilla Clusters. In this solution, the cluster will host the L7 LB and its controllers, along with the workloads and healess service for external VMs
  * **GDC L4 Load Balancer:** The built-in L4 load balancer serving as the entry point, distributing TCP/443 traffic directly to the Kubernetes Pods running the controllers.
  * **Ingress Controllers:** HAProxy operators running in the standard cluster. They monitor the `Ingress` resources and dynamically update the underlying proxies. [HAProxy Ingress Controller](https://www.haproxy.com/documentation/kubernetes-ingress/) will be used in the following implementation
  * **Ingress:** Standardized Kubernetes resources defining the physical listening port (443) and the SNI-based host routing rules with TLS Termination.
  * **Containerized Workload (Pods):** A standard Kubernetes Deployment exposed internally with a regular Kubernetes `Service`.
  * **VM-based Workload (External):** A workload hosted on an external VM on the project network, exposed to the proxy using a headless Kubernetes `Service` and a custom endpoint containing the VM's direct IP.
  * **Harbor Registry:** A private container registry used to store and serve the proxy and application images in the air-gapped environment.



In the standard cluster, you create three namespaces:

  * The `load-balancer` namespace hosts the HAProxy Ingress Controller and the HAProxy load balancer workload:

![The load-balancer namespace resources.](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/gdcag/solutions/images/l7-lb-haproxy-controller-ns.png)

  * The `hello-app` namespace hosts the `Deployment`, a `Service`, and an `Ingress` for the demo container workload:

![The hello-app namespace resources.](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/gdcag/solutions/images/l7-lb-haproxy-hello-app-ns.png)

  * The `vm-app` namespace hosts a headless service that exposes the external VM IP, an `EndpointSlice` that points at the external IP, and an `Ingress`:

![The vm-app namespace resources.](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/gdcag/solutions/images/l7-lb-haproxy-vm-app-ns.png)




## Before you begin

Before deploying this solution, ensure you have the following prerequisites in place:

  * **Software needed:** helm, docker, kubectl
  * **CLI login and local setup:** Download gdcloud CLI from the GDC console and set up your environment locally:
        
        export USER_NAME="USER_NAME"
        export PROJECT_ID="PROJECT_ID"
        export ZONE="ZONE"
        export ORG_NAME="ORG_NAME"
        export GDC_URL="GDC_URL"
        
        gdcloud components install gdcloud-k8s-auth-plugin
        
        gdcloud config set core/organization_console_url \
          https://console.$ORG_NAME.$ZONE.$GDC_URL
        gdcloud config set core/zone $ZONE
        gdcloud config set core/project ${PROJECT_ID}
        
        gdcloud auth login # use --login-config-cert option in case of TLS error
        

  * **Project Setup:** Create a [project](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/create-a-project) in your GDC air-gapped environment to hold the resources:
        
        gdcloud projects create $PROJECT_ID
        

  * **IAM Roles:** Grant your user the **Cluster Admin** and **Standard Cluster Admin** roles to manage Kubernetes resources, and the **Harbor Instance Admin** role to push images:
        
        # Grant standard cluster and cluster admin roles
        gdcloud projects add-iam-policy-binding ${PROJECT_ID} \
          --member="user:${USER_NAME}" \
          --role=cluster-admin
        
        gdcloud projects add-iam-policy-binding ${PROJECT_ID} \
          --member="user:${USER_NAME}" \
          --role=standard-cluster-admin
        
        # Grant Harbor instance admin role
        gdcloud projects add-iam-policy-binding ${PROJECT_ID} \
          --member="user:${USER_NAME}" \
          --role=harbor-instance-admin
        




## Create a standard cluster

This section guides you through the process of setting up a standard Kubernetes cluster within your GDC air-gapped environment. A standard cluster provides a flexible and robust foundation for deploying various workloads, including the HAProxy Ingress Controller, and your custom applications. The following steps will ensure your cluster is properly configured and accessible for subsequent deployments.

  1. Identify the available virtual machine image types by running:
         
         gdcloud compute machine-types list
         

  2. Select an appropriate machine type for your cluster worker nodes. For this tutorial, a machine type with _at least 4 vCPUs_ is recommended.
         
         export MACHINE_TYPE="MACHINE_TYPE"
         

  3. Get the management API server kubeconfig and set an alias:
         
         export CLUSTER_NAME="CLUSTER_NAME"
         
         KUBECONFIG=kubeconfig-admin.yaml gdcloud clusters \
           get-credentials ${ORG_NAME}-admin
         
         alias km="kubectl --kubeconfig kubeconfig-admin.yaml"
         

  4. Create a standard cluster with two worker nodes:
         
         km create -f - <<EOF
         apiVersion: cluster.gdc.goog/v1
         kind: Cluster
         metadata:
           name: ${CLUSTER_NAME}
           namespace: ${PROJECT_ID}
         spec:
           nodePools:
           - machineTypeName: ${MACHINE_TYPE}
             nodeCount: 2
             name: ${CLUSTER_NAME}-node-pool
         EOF
         

For more details on available options, refer to the [documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/create-standard-cluster).

Standard cluster creation can take up to 60 minutes to complete. To check the status, use the following command:
         
         km get clusters/${CLUSTER_NAME} \
           -n ${PROJECT_ID} \
           --watch
         

After the cluster is ready, the output should show a state of Running, like this:
         
         NAME         STATE     K8S VERSION
         my-cluster   Running   1.30.12-gke.300
         

  5. After the cluster is ready, retrieve its credentials:
         
         KUBECONFIG=kubeconfig-${CLUSTER_NAME}.yaml gdcloud clusters \
           get-credentials ${CLUSTER_NAME} \
           --standard \
           --project ${PROJECT_ID} \
           --zone ${ZONE}
         

  6. Create an alias to keep `kubectl` commands more concise in the rest of this guide. This alias will be used to interact with the standard cluster:
         
         alias kk="kubectl --kubeconfig kubeconfig-${CLUSTER_NAME}.yaml"
         

  7. Create namespaces for the controller, the "hello-app" demo containerized app, and the VM-based demo app:
         
         kk create namespace load-balancer
         kk create namespace hello-app
         kk create namespace vm-app
         




## Create and integrate Harbor Registry

Harbor is a container image registry with built-in support in GDC air-gapped. This section guides you through the steps to integrate a Harbor Registry with your standard cluster, including configuring credentials and secrets to enable secure pulling and pushing of images.

  1. Create a [Harbor instance](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/create-harbor-instances) in your project.
  2. Create a [Harbor project](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/create-harbor-projects) in your Harbor instance.
  3. Set environment variables:
         
         export HARBOR_INSTANCE_NAME="HARBOR_INSTANCE_NAME"
         export HARBOR_INSTANCE_URL="HARBOR_INSTANCE_URL"
         export HARBOR_PROJECT="HARBOR_PROJECT"
         export IMAGE_PULL_SECRET_NAME="harbor-secret"
         

  4. Sign in to the Harbor instance using a [robot account](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/deploy-container-workloads#create-image-pull-secret):
         
         docker --config=./docker login ${HARBOR_INSTANCE_URL}
         

  5. Create the secrets in the standard cluster:
         
         kk create secret docker-registry ${IMAGE_PULL_SECRET_NAME} \
           --from-file=.dockerconfigjson=./docker/config.json \
           -n load-balancer
         
         kk create secret docker-registry ${IMAGE_PULL_SECRET_NAME} \
           --from-file=.dockerconfigjson=./docker/config.json \
           -n hello-app
         




## Deploy demo containerized app

This section details the deployment of a demo containerized application (`hello-app`) within your GDC air-gapped Kubernetes cluster. You will create the necessary Kubernetes Deployment and Service resources to run the `hello-app` and expose it internally within the cluster, preparing it for access using the L7 load balancer.

  1. Upload a sample image for the demo containerized app into Harbor:
         
         docker pull gcr.io/google-samples/hello-app:1.0 \
           --platform linux/amd64
         docker tag gcr.io/google-samples/hello-app:1.0 \
           ${HARBOR_INSTANCE_URL}/${HARBOR_PROJECT}/hello-app:1.0
         docker --config=./docker push \
           ${HARBOR_INSTANCE_URL}/${HARBOR_PROJECT}/hello-app:1.0
         

  2. Deploy the following manifest in the standard cluster:
         
         cat << EOF > hello-app.yaml
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: hello-app
           namespace: hello-app
         spec:
           replicas: 2
           selector:
             matchLabels:
               app: hello-app
           template:
             metadata:
               labels:
                 app: hello-app
             spec:
               containers:
               - name: hello-server
                 image: ${HARBOR_INSTANCE_URL}/${HARBOR_PROJECT}/hello-app:1.0
                 ports:
                 - containerPort: 8080
               imagePullSecrets:
               - name: ${IMAGE_PULL_SECRET_NAME}
         ---
         apiVersion: v1
         kind: Service
         metadata:
           name: hello-app
           namespace: hello-app
         spec:
           type: ClusterIP
           selector:
             app: hello-app
           ports:
             - protocol: TCP
               port: 80
               targetPort: 8080
         EOF
         
         kk apply -f hello-app.yaml
         




Then verify that the deployment and the service are there
    
    
    kk get svc,deploy -n hello-app
    

## Deploy demo app in a VM

This section details the deployment of a demo application within a virtual machine (VM) outside your Kubernetes cluster. By setting up an HTTP server on a VM, you'll simulate an external application that the load balancer can expose, demonstrating its capability to manage traffic to resources both inside and outside the cluster.

First, create a VM for the demo app:

  1. Open the GDC console in your web browser.
  2. Select the same project as where you created your standard Kubernetes cluster.
  3. Open the menu then click **Virtual machines**.
  4. Click **Create Instance**.
  5. Give the VM the name `vm-workload`. A 2 vCPU image is enough for the example.
  6. For the boot disk image, select an Ubuntu 22.04 distribution, which comes with Python pre-installed.
  7. Click **Create**.
  8. Wait a few minutes until the VM becomes ready.
  9. Establish an SSH connection to VM: 
     1. In the GDC console, click the VM.
     2. Click **Connect with SSH**.



After you're connected to the SSH console, run the following:
    
    
    mkdir ~/simple-server
    cd ~/simple-server
    echo 'Welcome to my VM!' > index.html
    python3 -m http.server --bind 0.0.0.0 8080 &
    

To route traffic to a VM, create a headless Service (without selectors). This will be manually mapped to the VM's internal IP address using an `EndpointSlice` resource.
    
    
    kk apply -f - <<EOF
    apiVersion: v1
    kind: Service
    metadata:
      name: vm-app-svc
      namespace: vm-app
    spec:
      ports:
      - protocol: TCP
        port: 443
        targetPort: 443
    EOF
    

Get the IP address of `vm-workload` VM by running
    
    
    gdcloud compute instances list --project ${PROJECT_ID} \
      | grep workload-vm | awk '{print $3}'
    

The output will be the IP address of the VM that will be needed to set up the EndpointSlice resource.

Create the resource `EndpointSlice` that will connect to the VM-app selector-less Service and address the IP of the VM to which the traffic should be routed.
    
    
    apiVersion: discovery.k8s.io/v1
    kind: EndpointSlice
    metadata:
      name: vm-app-endpoints
      namespace: vm-app
      labels:
        kubernetes.io/service-name: vm-app-svc
    addressType: IPv4
    ports:
      - port: 8080
    endpoints:
      - addresses:
        - "VM_IP"
        conditions:
          ready: true
    

## Create self-signed certificates

This section guides you through the process of creating TLS certificates and Kubernetes secrets to secure communication for your container-based and VM-based applications. This guide uses self-signed certificates for convenience, but in production environments, you must use production-grade certificates, as described in Optional: Use production-ready certificates. Choose arbitrary sample domain names for these apps. By establishing secure connections, you ensure data integrity and confidentiality for clients accessing your application through the HAProxy Ingress Controller.

For the containerized app, we create a self-signed certificate and save it as a secret on the load-balancer namespace. This will be used for the TLS when requesting k8s-app.example.com
    
    
    openssl req -x509 -newkey rsa:2048 -nodes \
      -keyout tls-containerized.key \
      -out tls-containerized.crt \
      -subj "/CN=k8s-app.example.com" \
      -days 365
    
    kk create secret tls tls-containerized \
      --namespace load-balancer \
      --key tls-containerized.key \
      --cert tls-containerized.crt
    
    kk create secret tls tls-containerized \
      --namespace hello-app \
      --key tls-containerized.key \
      --cert tls-containerized.crt
    

For the VM app, a similar self-signed certificate is issued and saved. This will be used for the TLS when requesting vm-app.example.com
    
    
    openssl req -x509 -newkey rsa:2048 -nodes \
      -keyout tls-vm.key \
      -out tls-vm.crt \
      -subj "/CN=vm-app.example.com" \
      -days 365
    
    kk create secret tls tls-vm \
      --namespace load-balancer \
      --key tls-vm.key \
      --cert tls-vm.crt
    
    kk create secret tls tls-vm \
      --namespace vm-app \
      --key tls-vm.key \
      --cert tls-vm.crt
    

## Deploy HAProxy

### Install HAProxy Ingress controller and L4 LB
    
    
    export HAPROXY_VERSION=3.1.14
    
    # pull the HAProxy Ingress Controller image and push it to Harbor
    docker pull haproxytech/kubernetes-ingress:${HAPROXY_VERSION} \
      --platform linux/amd64
    docker tag haproxytech/kubernetes-ingress:${HAPROXY_VERSION} \
      ${HARBOR_INSTANCE_URL}/${HARBOR_PROJECT}/haproxy-ingress:${HAPROXY_VERSION}
    docker --config=./docker push \
      ${HARBOR_INSTANCE_URL}/${HARBOR_PROJECT}/haproxy-ingress:${HAPROXY_VERSION}
    
    # Get Helm repo
    helm repo add haproxytech https://haproxytech.github.io/helm-charts
    helm repo update
    
    # Install the Ingress Controller with helm
    helm upgrade --install haproxy-kubernetes-ingress \
      haproxytech/kubernetes-ingress \
      --kubeconfig kubeconfig-${CLUSTER_NAME}.yaml \
      --namespace load-balancer \
      --set controller.image.repository=${HARBOR_INSTANCE_URL}/${HARBOR_PROJECT}/haproxy-ingress \
      --set controller.image.tag=${HAPROXY_VERSION} \
      --set controller.existingImagePullSecret=${IMAGE_PULL_SECRET_NAME} \
      --set controller.service.type=LoadBalancer \
      --set-json \
      controller.service.annotations='{"networking.gke.io/load-balancer-type": "internal"}'
    

The HAProxy Ingress Controller gains a unique virtual IP address for client access using a `LoadBalancer` type service. This service sets up a fully-managed Layer 4 load balancer. For this guide's simplicity, an internal load balancer is created by setting the `load-balancer-type` annotation to `internal`. Omitting this annotation would result in an external load balancer. The Kubernetes deployment securely pulls images from Harbor using the provided secret (`${IMAGE_PULL_SECRET_NAME}`), which contains the Harbor robot account's credentials.

### Validate HAProxy Ingress controller installation

Check that the HAProxy Ingress Controller's pods are running and ready:
    
    
    kk get pods -n load-balancer
    

The output should look like the following:
    
    
    NAME                                          READY   STATUS      RESTARTS   AGE
    haproxy-kubernetes-ingress-78dc9c8676-f8fcb   1/1     Running     0          35s
    haproxy-kubernetes-ingress-78dc9c8676-lfnr2   1/1     Running     0          65s
    haproxy-kubernetes-ingress-crdjob-3-tgj2h     0/1     Completed   0          65s
    

Check that the HAProxy Ingress Controller's service is created and configured:
    
    
    kk get services -n load-balancer
    

The output looks similar to the following:
    
    
    NAME                         TYPE           CLUSTER-IP     EXTERNAL-IP   PORT(S)                                                                  AGE
    haproxy-kubernetes-ingress   LoadBalancer   10.252.27.46   10.252.4.17   80:32023/TCP,443:31103/TCP,443:31103/UDP,1024:30146/TCP,6060:30718/TCP   10m
    

### Define Ingress resources for the demo apps

Create the Ingress resource that will connect the HAProxy to the containerized app Service
    
    
    cat << EOF > hello-app-ingress.yaml
    apiVersion: networking.k8s.io/v1
    kind: Ingress
    metadata:
      name: hello-app-ingress
      namespace: hello-app
      annotations:
        haproxy.org/ssl-redirect: "true"
        haproxy.org/ssl-redirect-port: "443"
        haproxy.org/ssl-redirect-code: "308"
    spec:
      ingressClassName: haproxy
      tls:
      - hosts:
        - "k8s-app.example.com"
        secretName: tls-containerized
      rules:
      - host: "k8s-app.example.com"
        http:
          paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: hello-app
                port:
                  number: 80
    EOF
    
    kk apply -f hello-app-ingress.yaml
    

Create the Ingress resource that will connect to the VM-app selector-less Service and address the IP of the VM to which the traffic should be routed.
    
    
    cat << EOF > vm-ingress.yaml
    apiVersion: networking.k8s.io/v1
    kind: Ingress
    metadata:
      name: vm-app-ingress
      namespace: vm-app
      annotations:
        haproxy.org/ssl-redirect: "true"
        haproxy.org/ssl-redirect-port: "443"
        haproxy.org/ssl-redirect-code: "308"
    spec:
      ingressClassName: haproxy
      tls:
      - hosts:
        - "vm-app.example.com"
        secretName: tls-vm
      rules:
      - host: "vm-app.example.com"
        http:
          paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: vm-app-svc
                port:
                  number: 443
    EOF
    
    kk apply -f vm-ingress.yaml
    

### Retrieve load balancer IP address

Run the command to get the IP address of the load balancer.
    
    
    kk get services/haproxy-kubernetes-ingress \
      -n load-balancer \
      -o jsonpath='{.status.loadBalancer.ingress[0].ip}'
    

This will be needed when verifying the access to the apps. This will be referred to as `LOAD_BALANCER_IP`.

## Create a client VM

Follow the steps to create a client VM:

  1. Open the GDC console in your web browser.
  2. Open the menu and click **Virtual machines**.
  3. Click **Create Instance**.
  4. Create a VM named `client`, select a small machine type and select either Rocky Linux or Ubuntu, which come with `curl` preinstalled.
  5. Click **Create**.
  6. Wait a few minutes until the VM becomes ready.
  7. After the VM is ready, establish an SSH connection with the VM: 
     1. In the GDC console, click the VM.
     2. Click **Connect with SSH**.



## Verify access and routing

To test the routing, execute `curl` commands from your client VM. You can connect to both applications using their defined hostnames with the load balancer's IP address.

By passing the `--resolve` flag in curl, you can force the domain names to resolve to your GDC air-gapped L4 Load Balancer's IP. Note that we pass the `-k` flag to trust the self-signed certificates.

Test the Kubernetes containerized app:
    
    
    curl -k --resolve k8s-app.example.com:443:$LOAD_BALANCER_IP https://k8s-app.example.com -v
    

Test the external VM app:
    
    
    curl -k --resolve vm-app.example.com:443:$LOAD_BALANCER_IP https://vm-app.example.com -v
    

If configured correctly, the Ingress controller will seamlessly act as TLS terminator and pass-through the traffic to the destination.

## Optional: Use production-ready certificates

This section covers how to leverage the GDC air-gapped CA Service to create a private Root Certificate Authority (CA), issue signed certificates for your workloads, and securely update your GDC air-gapped standard cluster and client VMs.

This section outlines how to use the GDC air-gapped [CA Service](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/ca-service/cas-overview) to create a private Root Certificate Authority (CA) and issue valid certificates for your applications. By installing this Root CA on your client VM, you can verify that TLS termination works seamlessly with trusted certificates, without needing to bypass SSL warnings (for example, using `curl -k`).

### Grant necessary permissions and get credentials

To manage the CA Service and issue certificates, your user needs the appropriate IAM roles in the project.

  1. Grant the `certificate-authority-service-admin` and `certificate-requester` roles:
         
         gdcloud projects add-iam-policy-binding ${PROJECT_ID} \
           --member=user:${USER_NAME} \
           --role=certificate-authority-service-admin
         
         gdcloud projects add-iam-policy-binding ${PROJECT_ID} \
           --member=user:${USER_NAME} \
           --role=certificate-requester
         

  2. Get the credentials of the management API server:
         
         gdcloud clusters get-credentials ${ORG_NAME}-admin
         




### Create the root CA

You will create a Certificate Authority in the management API server within your project namespace.

  1. Apply the `CertificateAuthority` resource:
         
         km apply -f - <<EOF
         apiVersion: pki.security.gdc.goog/v1
         kind: CertificateAuthority
         metadata:
           name: my-root-ca
           namespace: ${PROJECT_ID}
         spec:
           caProfile:
             commonName: "My Root CA"
             duration: 87600h # 10 years
             keyAlgorithm: RSA_2048
             maxChainLength: 1
           caType: ROOT
           keyLocation: HSM
           rotationPolicy:
             cronTime: 0 0 1 1 *
         EOF
         

**Note:** Root CA creation can take up to 40 minutes to complete. You can monitor the status using the following command. Wait until it returns `True` before proceeding.
         
         km -n ${PROJECT_ID} get \
         certificateauthority.pki.security.gdc.goog/my-root-ca -ojson \
         | jq -r '
         .status.conditions[] | select( .type as $id | "Ready" | index($id)) .status'
         




### Issue and deploy certificates

After the CA is ready, you will request certificates for both the containerized app and the VM-based app. These requests happen in the management API server, and the resulting keys must be moved to your standard cluster.

Create requests for both domains:
    
    
    km apply -f - <<EOF
    apiVersion: pki.security.gdc.goog/v1
    kind: CertificateRequest
    metadata:
      name: tls-containerized-req
      namespace: ${PROJECT_ID}
    spec:
      certificateAuthorityRef:
        name: my-root-ca
        namespace: ${PROJECT_ID}
      certificateConfig:
        subjectConfig:
          commonName: "k8s-app.example.com"
          dnsNames:
          - "k8s-app.example.com"
      signedCertificateSecret: tls-containerized-signed
    ---
    apiVersion: pki.security.gdc.goog/v1
    kind: CertificateRequest
    metadata:
      name: tls-vm-req
      namespace: ${PROJECT_ID}
    spec:
      certificateAuthorityRef:
        name: my-root-ca
        namespace: ${PROJECT_ID}
      certificateConfig:
        subjectConfig:
          commonName: "vm-app.example.com"
          dnsNames:
          - "vm-app.example.com"
      signedCertificateSecret: tls-vm-signed
    EOF
    

Wait a few moments for the certificates to be issued. You can verify they are ready when the Ready condition is True:
    
    
    km get certificaterequests -n ${PROJECT_ID}
    

### Update the standard cluster

If you followed the previous sections of this guide, you have self-signed secrets in your standard cluster. You must delete them before creating the new, signed versions:
    
    
    kk delete secret tls-containerized -n load-balancer
    kk delete secret tls-vm -n load-balancer
    
    kk delete secret tls-containerized -n hello-app
    kk delete secret tls-vm -n vm-app
    

Now, extract the signed certificates from the management API server and create the new secrets in the standard cluster.
    
    
    km get secret -n ${PROJECT_ID} tls-containerized-signed \
      -o jsonpath='{.data.tls\.crt}' \
      | base64 -d > tls-containerized.crt
    
    km get secret -n ${PROJECT_ID} tls-containerized-signed \
      -o jsonpath='{.data.tls\.key}' \
      | base64 -d > tls-containerized.key
    
    kk create secret tls tls-containerized \
      --namespace load-balancer \
      --key tls-containerized.key \
      --cert tls-containerized.crt
    
    kk create secret tls tls-containerized \
      --namespace hello-app \
      --key tls-containerized.key \
      --cert tls-containerized.crt
    
    km get secret -n ${PROJECT_ID} tls-vm-signed \
      -o jsonpath='{.data.tls\.crt}' \
      | base64 -d > tls-vm.crt
    
    km get secret -n ${PROJECT_ID} tls-vm-signed \
      -o jsonpath='{.data.tls\.key}' \
      | base64 -d > tls-vm.key
    
    kk create secret tls tls-vm \
      --namespace load-balancer \
      --key tls-vm.key \
      --cert tls-vm.crt
    
    kk create secret tls tls-vm \
      --namespace vm-app \
      --key tls-vm.key \
      --cert tls-vm.crt
    

The new secrets will be obtained automatically and refreshed by load balancers.

### Configure client trust

To verify the setup, you need to tell your client VM to trust your new root CA.

Extract the root CA certificate to a file:
    
    
    km get secret -n ${PROJECT_ID} my-root-ca-secret \
      -o jsonpath='{.data.tls\.crt}' \
      | base64 -d > my-root-ca.crt
    

Transfer the certificate to your client VM. (You can copy the content of my-root-ca.crt and paste it into a file on the client VM).

On the client VM, update the trust store.

If `client` VM is Ubuntu:
    
    
    sudo cp my-root-ca.crt /usr/local/share/ca-certificates/
    sudo chmod 644 /usr/local/share/ca-certificates/my-root-ca.crt
    sudo update-ca-certificates
    

If `client` VM is Rocky Linux:
    
    
    sudo cp my-root-ca.crt /etc/pki/ca-trust/source/anchors/
    sudo update-ca-trust
    

### Verify access

You can now access your applications using curl without the `-k` flag. The connection will be fully trusted.

Test the k8s containerized App:
    
    
    curl -v --resolve k8s-app.example.com:443:LOAD_BALANDER_IP https://k8s-app.example.com
    

Test the VM App:
    
    
    curl -v --resolve vm.example.com:443:LOAD_BALANDER_IP https://vm-app.example.com
    

If successful, you will see the application output immediately without any SSL certificate warnings.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
