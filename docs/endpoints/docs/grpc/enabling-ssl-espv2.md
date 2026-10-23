---
url: https://docs.cloud.google.com/endpoints/docs/grpc/enabling-ssl-espv2/
title: Enabling SSL for Cloud Endpoints with ESPv2 \u00a0|\u00a0 Cloud Endpoints with gRPC \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:01:46.843217+00:00
---

# Enabling SSL for Cloud Endpoints with ESPv2  |  Cloud Endpoints with gRPC  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/grpc/enabling-ssl-espv2/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ gRPC ](https://docs.cloud.google.com/endpoints/docs/grpc/about-grpc)



Send feedback 

#  Enabling SSL for Cloud Endpoints with ESPv2 Stay organized with collections  Save and categorize content based on your preferences. 

[OpenAPI](https://docs.cloud.google.com/endpoints/docs/openapi/enabling-ssl-espv2 "View this page for the Cloud Endpoints OpenAPI docs") | gRPC

This page explains how to enable a Secure Sockets Layer (SSL) port when deploying Extensible Service Proxy V2 (ESPv2) with Google Kubernetes Engine, Kubernetes, or Compute Engine. You may want to enable an SSL port for your deployed Endpoints service for some use cases.

Before you begin, make sure that you have already reviewed the [tutorials](https://docs.cloud.google.com/endpoints/docs/grpc/tutorials) for your chosen service type and environment, and know how to deploy ESPv2 without SSL.

**Note:** This tutorial describes how to use _self-managed SSL certificates_ with ESPv2. Google-managed SSL certificates aren't currently supported by ESPv2. 

## Configuring your SSL keys and certificates

To configure your SSL port to serve HTTPS requests, follow the steps below:

  1. Check to ensure that your SSL key file is named `server.key` and your certificate file is named `server.crt`. For testing, you can generate a self-signed `server.key` and `server.crt` using OpenSSL with the following command:
         
         openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
         -keyout ./server.key -out ./server.crt

  2. Specify both `CN` and `subjectAltName` in your server certificate. The value of these attributes should match the DNS or IP used by clients to call your service; otherwise, the SSL handshake will fail.




## Enabling SSL for ESPv2 on Kubernetes

To enable the SSL port for ESPv2 on Kubernetes:

  1. Create a Kubernetes secret with your SSL key and certificate:
         
         kubectl create secret generic esp-ssl \
           --from-file=./server.crt --from-file=./server.key

  2. Edit the Kubernetes configuration files, for example, `echo-ssl.yaml`, as shown in the following snippet:
         
         template:
           metadata:
             labels:
               app: esp-echo
           spec:
             volumes:
             - name: esp-ssl
               secret:
                 secretName: esp-ssl
             containers:
             - name: esp
               image: gcr.io/endpoints-release/endpoints-runtime:2
               args: [
                 "--listener_port", "9000",
                 "--backend", "127.0.0.1:8081",
                 "--service", "SERVICE_NAME",
                 "--rollout_strategy", "managed",
                 "--ssl_server_cert_path", "/etc/esp/ssl",
               ]
               ports:
                 - containerPort: 9000
               volumeMounts:
               - mountPath: /etc/esp/ssl
                 name: esp-ssl
                 readOnly: true
             - name: echo
               image: gcr.io/endpoints-release/echo:latest
               ports:
                 - containerPort: 8081

**Note** : The configuration sample displays the lines that need to be edited. To deploy the file to Cloud Endpoints, the complete configuration file is required.

**Note:** The ESPv2 container cannot bind to privileged ports, including port 443. Instead, use a Kubernetes Service resource to map 443 to a non-privileged `--listener_port`, such as `9000`.
  3. Mount the Kubernetes secrets you created as volumes, following the directions in the [Kubernetes volumes page](https://kubernetes.io/docs/concepts/storage/volumes/).

  4. Start up ESPv2 as described in [Specifying startup options for ESPv2](https://docs.cloud.google.com/endpoints/docs/grpc/specify-esp-v2-startup-options), but make sure you add the startup flag `--ssl_server_cert_path` to specify the path for the mounted certificate files.

  5. Start the service with the updated Kubernetes configuration file by using `kubectl`.
         
         kubectl apply -f echo-ssl.yaml

**Note:** If you already have an existing [Kubernetes deployment](http://kubernetes.io/docs/user-guide/deployments/), you can [update the deployment](http://kubernetes.io/docs/user-guide/deployments/#updating-a-deployment) directly.
  6. Generate the root certificate for the client by using the following OpenSSL command:
         
         openssl x509 -in ./server.crt -out ./client.pem -outform PEM
          

If the client is using `curl`, the file `client.pem` can be used in the `--caroot` flag. For gRPC, the `client.pem` is used as the root certificate file of the SSL credential for gRPC channel.




### Update SSL certificates

It is important to update your SSL certificates periodically. To update your SSL certificates, you must perform the following steps:

  * Create new certificates, as described in Step 1 above.
  * Mount the new certificates to the Kubernetes secrets, as described in Step 3 above.
  * Update the ESPv2 Kubernetes deployment, as described in Step 5 above.
  * Regenerate the client root certificate file, as described in Step 6 above.



## Enabling SSL for ESPv2 on Compute Engine

To enable SSL on Compute Engine, first copy the `server.key` and `server.crt` files to your Compute Engine instance's `/etc/nginx/ssl` folder, using the following steps:

  1. Run the following command and replace INSTANCE_NAME with the name of your Compute Engine instance:
         
         gcloud compute scp server.* INSTANCE-NAME
         

  2. Connect to the instance using `ssh`.
         
         gcloud compute ssh INSTANCE-NAME
         

  3. In the instance VM box, make the directory and copy in the files:
         
         sudo mkdir -p /etc/esp/ssl
           sudo cp server.* /etc/esp/ssl/

  4. Follow the instructions for your service type to deploy with Docker. When you run the ESPv2 Docker container, use this command:
         
         sudo docker run --name=esp \
          --detach \
          --publish=443:9000 \
          --net=esp_net \
          --volume=/etc/esp/ssl:/etc/esp/ssl \
           gcr.io/endpoints-release/endpoints-runtime:2 \
          --service=SERVICE_NAME \
          --rollout_strategy=managed \
          --backend=echo:8080 \
          --ssl_server_cert_path=/etc/esp/ssl \
          --listener_port=9000

As compared to the non-SSL `docker run` command, the SSL version of the command creates a different configuration. For example, the SSL command:

     * Mounts the folder with the key and CRT files to the container by using `--volume`.
     * Uses `--ssl_server_cert_path=/etc/esp/ssl` to tell ESPv2 to find the server certificate files `server.key` and `server.crt` in the `/etc/esp/ssl` folder.
     * Changes the port mapping flag `--publish`. Incoming requests to HTTPS port 443 are mapped to ESPv2 port 9000.

**Note:** The ESPv2 container cannot bind to privileged ports, including port 443. Instead, use the `--publish` flag to map 443 to a non-privileged `--listener_port`, such as `9000`.



### Update SSL certificates

It is important to update your SSL certificates periodically. To update your SSL certificates, you must perform the following steps:

  * Create new certificates and copy them into VM instances, as described in Step 1 above.
  * Copy the new certificates into the `/etc/esp/ssl` directory, as described in Step 3 above.
  * Stop and restart the ESPv2 container using the `sudo docker run` command, as described in Step 4 above.



## Testing the SSL port

To make the testing the SSL port easier, set the following environment variables:

  1. Set IP_ADDRESS to the IP address of the Compute Engine instance with the new SSL certificate.

**Note:** The example test commands below assume that the server does not yet have a fully qualified domain name (FQDN) and that IP_ADDRESS has been used as the FQDN when generating the self-signed certificate. When the server does get an FQDN, use the FQDN to generate the certificate. Then, replace IP_ADDRESS with the FQDN in the example commands below.
  2. Set ENDPOINTS_KEY to a valid [API key](https://console.cloud.google.com/apis/credentials).




Once the SSL port is enabled, you can use HTTPS to send requests to the Extensible Service Proxy. If your certificate is self-signed, use `-k` to turn on the insecure option in `curl`:
    
    
    curl -k -d '{"message":"hello world"}' -H "content-type:application/json" \
    https://IP_ADDRESS:443/echo?key=ENDPOINTS_KEY
    

Alternatively, generate the certificate in `pem` format and use the `--cacert` option to use the self-signed certificate in `curl`, as shown below:
    
    
      openssl x509 -in server.crt -out client.pem -outform PEM
      curl --cacert "./client.pem" -d '{"message":"hello world"}' -H "content-type:application/json" \
      https://IP_ADDRESS:443/echo?key=ENDPOINTS_KEY
      

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
