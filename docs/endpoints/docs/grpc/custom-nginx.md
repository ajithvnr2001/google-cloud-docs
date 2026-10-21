---
url: https://docs.cloud.google.com/endpoints/docs/grpc/custom-nginx/
title: Using a custom nginx.conf on GKE \u00a0|\u00a0 Cloud Endpoints with gRPC \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:36:11.272176+00:00
---

# Using a custom nginx.conf on GKE  |  Cloud Endpoints with gRPC  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/grpc/custom-nginx/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ gRPC ](https://docs.cloud.google.com/endpoints/docs/grpc/about-grpc)



Send feedback 

#  Using a custom nginx.conf on GKE Stay organized with collections  Save and categorize content based on your preferences. 

[OpenAPI](https://docs.cloud.google.com/endpoints/docs/openapi/custom-nginx "View this page for the Cloud Endpoints OpenAPI docs") | gRPC

**Warning** : Using this flag is not recommended as it may break many features. Normally, ESP uses the nginx config generated from its start up flags. If a custom nginx config is provided with flag `-n`, the generated nginx config is not be used and ESP will not function properly. 

The preferred method for generating a custom nginx config is: 

  * Deploy an ESP container with the proper start up flags
  * Copy the generated nginx config from `/etc/nginx/endpoints/nginx.conf`
  * Apply your changes to the copy of the generated nginx.config



The steps above must be repeated whenever a new ESP version is used or any start up flags are changed.

If you want to use a custom `nginx.conf` on Google Kubernetes Engine, prepare one by extending this [sample nginx.conf](https://github.com/GoogleCloudPlatform/endpoints-samples/blob/master/k8s/nginx.conf). Here is a snippet of the configuration required by Cloud Endpoints:
    
    
    http {
      include /etc/nginx/mime.types;
      server_tokens off;
      client_max_body_size 32m;
    
      upstream app_server {
        server localhost:8081;
        keepalive 128;
      }
    
      endpoints {
        metadata_server;
      }
    
      server {
        # Running port
        listen 8080;
    
        # Running ssl port
        listen 443 ssl;
        ssl_certificate /etc/nginx/ssl/nginx.crt;
        ssl_certificate_key /etc/nginx/ssl/nginx.key;
    
        # Logging to stdout enables better integration with Docker and GKE/Kubernetes.
        access_log /dev/stdout;
    
        location / {
          # Begin Endpoints v2 Support
          endpoints {
            on;
            # After ESP 1.7.0, "server_config" field is required.
            # It has to be /etc/nginx/server_config.pb.txt exactly.
            # If not present, some new features will not work.
            server_config /etc/nginx/server_config.pb.txt;
    
            # After ESP 1.7.0, "api" field is not required.
            # If added, it has to be /etc/nginx/endpoints/service.json exactly.
            # api /etc/nginx/endpoints/service.json;
    
            # Uncomment the line below if you are not using Google Container Engine.
            # The path should be set to the “-k” path specified in the ESP container’s                 
            # args section in the Kubernetes yaml config.
            # google_authentication_secret /etc/nginx/creds/service-account-creds.json;
          }
          # End Endpoints v2 Support
    
          proxy_pass http://app_server;
          proxy_redirect off;
          proxy_set_header Host $host;
          proxy_set_header X-Real-IP $remote_addr;
          proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
          proxy_set_header X-Forwarded-Host $server_name;
          proxy_set_header X-Google-Real-IP $remote_addr;
    
          # 86400 seconds (24 hours) is the maximum a server is allowed.
          proxy_send_timeout 86400s;
          proxy_read_timeout 86400s;
        }
    
        include /var/lib/nginx/extra/*.conf;
      }
    
      server {
        # expose /nginx_status but on a different port to avoid
        # external visibility / conflicts with the app.
        listen 8090;
        location /nginx_status {
          stub_status on;
          access_log off;
        }
        location / {
          root /dev/null;
        }
      }
    }

Now create a Kubernetes Configmap with your custom `nginx.conf` using `kubectl`:
    
    
    kubectl create configmap nginx-config --from-file=nginx.conf

Edit the Kubernetes configuration file such as [`esp_echo_custom_config_gke.yaml`](https://github.com/GoogleCloudPlatform/endpoints-samples/blob/master/k8s/esp_echo_custom_config_gke.yaml) and replace `SERVICE_NAME` with the name of your Endpoints service.
    
    
    template:
      metadata:
        labels:
          app: esp-echo
      spec:
        volumes:
        - name: nginx-config
          configMap:
            name: nginx-config
        - name: nginx-ssl
          secret:
            secretName: nginx-ssl
        containers:
        - name: esp
          image: gcr.io/endpoints-release/endpoints-runtime:1
          args: [
            "-n", "/etc/nginx/custom/nginx.conf",
            "-s", "SERVICE_NAME",
            "--rollout_strategy", "managed",
          ]
          ports:
            - containerPort: 8080
            - containerPort: 443
          volumeMounts:
          - mountPath: /etc/nginx/ssl
            name: nginx-ssl
            readOnly: true
          - mountPath: /etc/nginx/custom
            name: nginx-config
            readOnly: true
        - name: echo 
          image: gcr.io/endpoints-release/echo:latest
          ports:
            - containerPort: 8081

Finally, start the service with the updated Kubernetes configuration file using `kubectl`.
    
    
    kubectl create -f esp_echo_custom_config_gke.yaml
    

For more information on getting the Endpoints service name, see the following topics:

  * For OpenAPI: [Getting the service name](https://docs.cloud.google.com/endpoints/docs/openapi/get-service-name-config-id#gcloud).
  * For gRPC: [Getting the service name](https://docs.cloud.google.com/endpoints/docs/grpc/get-service-name-config-id#gcloud).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
