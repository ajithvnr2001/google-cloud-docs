---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/kubernetes-auth-proxy/
title: Collect OAuth2 Proxy logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:46:20.610355+00:00
---

# Collect OAuth2 Proxy logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/kubernetes-auth-proxy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect OAuth2 Proxy logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest OAuth2 Proxy logs to Google Security Operations using Google Cloud Storage V2.

[OAuth2 Proxy](https://oauth2-proxy.github.io/oauth2-proxy/) is a CNCF Sandbox reverse proxy that provides authentication using OAuth2/OIDC providers (Google, GitHub, Keycloak, Azure AD, and others) to validate accounts by email, domain, or group. It generates authentication logs (login success/failure), request logs (proxied HTTP requests with user identity), and standard application logs. Because OAuth2 Proxy runs as a container in Kubernetes and writes all logs to stdout, a Kubernetes-native log collector (Fluentd) is used to forward logs to a GCS bucket for Google SecOps ingestion.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * A GCP project with Cloud Storage API enabled
  * Permissions to create and manage GCS buckets
  * Permissions to manage IAM policies on GCS buckets
  * A running Kubernetes cluster with OAuth2 Proxy deployed (via Helm chart or manual deployment)
  * `kubectl` access to the Kubernetes cluster with permissions to create DaemonSets, ConfigMaps, Secrets, and Namespaces
  * A GCP service account JSON key with `storage.objects.create` permission on the target GCS bucket



## Create Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `oauth2-proxy-logs-bucket`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




## Configure OAuth2 Proxy logging

OAuth2 Proxy writes three types of logs to stdout: standard logs, authentication logs, and request logs. All three are enabled by default. To ensure logs contain maximum security-relevant detail, configure OAuth2 Proxy with the following logging flags.

### Option 1: Configure via Helm chart values

  * If OAuth2 Proxy is deployed using the [official Helm chart](https://github.com/oauth2-proxy/manifests), add the following to your `values.yaml` file:
        
        config:
          configFile: |-
            standard_logging = true
            auth_logging = true
            request_logging = true
            silence_ping_logging = true
                standard_logging_format = "[{{.Timestamp}}] [{{.File}}] {{.Message}}"
            auth_logging_format = "{{.Client}} - {{.RequestID}} - {{.Username}} [{{.Timestamp}}] [{{.Status}}] {{.Message}}"
            request_logging_format = "{{.Client}} - {{.RequestID}} - {{.Username}} [{{.Timestamp}}] {{.Host}} {{.RequestMethod}} {{.Upstream}} {{.RequestURI}} {{.Protocol}} {{.UserAgent}} {{.StatusCode}} {{.ResponseSize}} {{.RequestDuration}}"
        

  * Apply the updated Helm values:
        
        helm upgrade oauth2-proxy oauth2-proxy/oauth2-proxy -f values.yaml -n <your-namespace>
        




### Option 2: Configure via command-line flags

  * If OAuth2 Proxy is deployed using a Kubernetes Deployment manifest, add the following arguments to the container spec:
        
        args:
          - --standard-logging=true
          - --auth-logging=true
          - --request-logging=true
          - --silence-ping-logging=true
        




### Option 3: Configure via environment variables

  * Set the following environment variables on the OAuth2 Proxy container:
        
        env:
          - name: OAUTH2_PROXY_STANDARD_LOGGING
            value: "true"
          - name: OAUTH2_PROXY_AUTH_LOGGING
            value: "true"
          - name: OAUTH2_PROXY_REQUEST_LOGGING
            value: "true"
          - name: OAUTH2_PROXY_SILENCE_PING_LOGGING
            value: "true"
        




### Verify OAuth2 Proxy logging

  * After applying the configuration, verify that OAuth2 Proxy is producing logs:
        
        kubectl logs -l app=oauth2-proxy -n <your-namespace> --tail=20
        

  * The output includes lines similar to the following:
        
        10.0.0.1 - abc123 - user@example.com [2024/01/15 10:30:00] [AuthSuccess] Authenticated via OAuth2
        10.0.0.1 - abc123 - user@example.com [2024/01/15 10:30:01] example.com GET 10.0.0.5:8080 "/dashboard" HTTP/1.1 "Mozilla/5.0" 200 1234 0.005
        




## Create GCP service account for Fluentd

Fluentd requires a GCP service account with write access to the GCS bucket.

  1. In the **GCP Console** , go to **IAM & Admin > Service Accounts**.
  2. Click **Create Service Account**.
  3. Provide the following configuration details: 
     * **Service account name** : Enter `fluentd-gcs-writer`
     * **Service account description** : Enter `Service account for Fluentd to write OAuth2 Proxy logs to GCS`
  4. Click **Create and Continue**.
  5. In the **Grant this service account access to project** section: 
     1. Click **Select a role**.
     2. Search for and select **Storage Object Admin**.
  6. Click **Continue**.
  7. Click **Done**.



### Create and download service account key

  1. In the **Service Accounts** list, click on the `fluentd-gcs-writer` service account.
  2. Go to the **Keys** tab.
  3. Click **Add Key > Create new key**.
  4. Select **JSON** as the key type.
  5. Click **Create**.
  6. Save the downloaded JSON key file securely. This file is used in the next step.



### Create Kubernetes secret for the service account key

  * Create a Kubernetes secret containing the GCP service account key in the namespace where Fluentd will be deployed:
        
        kubectl create namespace logging
        kubectl create secret generic fluentd-gcs-key \
          --from-file=service-account-key.json=<path-to-downloaded-key>.json \
          -n logging
        




## Deploy Fluentd DaemonSet to collect OAuth2 Proxy logs

Deploy Fluentd as a DaemonSet in the Kubernetes cluster to collect container logs from OAuth2 Proxy pods and forward them to the GCS bucket.

### Create Fluentd ConfigMap

  * Create a file named `fluentd-configmap.yaml` with the following content:
        
        apiVersion: v1
        kind: ConfigMap
        metadata:
          name: fluentd-gcs-config
          namespace: logging
        data:
          fluent.conf: |
            <source>
              @type tail
              read_from_head true
              tag kubernetes.*
              path /var/log/containers/*oauth2-proxy*.log
              pos_file /var/log/fluentd-oauth2-proxy.log.pos
              <parse>
                @type regexp
                expression /^(?<time>[^ ]+) (?<stream>stdout|stderr) [^ ]* (?<log>.*)$/
                time_format %Y-%m-%dT%H:%M:%S.%N%z
              </parse>
            </source>
        
            <filter kubernetes.**>
              @type kubernetes_metadata
              @id filter_kube_metadata
            </filter>
        
            <match kubernetes.**>
              @type gcs
              project YOUR_GCP_PROJECT_ID
              keyfile /etc/secrets/service-account-key.json
              bucket oauth2-proxy-logs-bucket
              path oauth2-proxy-logs/%Y/%m/%d/
              object_key_format %{path}%{time_slice}_%{hostname}_%{index}.%{file_extension}
              <buffer tag,time>
                @type file
                path /var/log/fluentd/gcs
                timekey 300
                timekey_wait 60
                timekey_use_utc true
                chunk_limit_size 10MB
              </buffer>
              <format>
                @type json
              </format>
            </match>
        




Replace the following values:

  * `YOUR_GCP_PROJECT_ID`: Your GCP project ID (for example, `my-project-123456`)
  * `oauth2-proxy-logs-bucket`: The name of the GCS bucket created earlier

  * Apply the ConfigMap:
        
        kubectl apply -f fluentd-configmap.yaml
        




### Create Fluentd DaemonSet

  * Create a file named `fluentd-daemonset.yaml` with the following content:
        
        apiVersion: apps/v1
        kind: DaemonSet
        metadata:
          name: fluentd-gcs
          namespace: logging
          labels:
            k8s-app: fluentd-gcs
        spec:
          selector:
            matchLabels:
              k8s-app: fluentd-gcs
          template:
            metadata:
              labels:
                k8s-app: fluentd-gcs
            spec:
              tolerations:
                - key: node-role.kubernetes.io/control-plane
                  effect: NoSchedule
                - key: node-role.kubernetes.io/master
                  effect: NoSchedule
              containers:
                - name: fluentd-gcs
                  image: fluent/fluentd-kubernetes-daemonset:v1-debian-gcs
                  resources:
                    limits:
                      memory: 512Mi
                    requests:
                      cpu: 100m
                      memory: 200Mi
                  volumeMounts:
                    - name: fluentd-gcs-config-volume
                      mountPath: /fluentd/etc/fluent.conf
                      subPath: fluent.conf
                      readOnly: true
                    - name: fluentd-gcs-secrets-volume
                      mountPath: /etc/secrets/service-account-key.json
                      subPath: service-account-key.json
                      readOnly: true
                    - name: varlog
                      mountPath: /var/log
                    - name: dockercontainerlogdirectory
                      mountPath: /var/log/pods
                      readOnly: true
                    - name: fluentd-buffer
                      mountPath: /var/log/fluentd
              terminationGracePeriodSeconds: 30
              volumes:
                - name: fluentd-gcs-config-volume
                  configMap:
                    name: fluentd-gcs-config
                - name: fluentd-gcs-secrets-volume
                  secret:
                    secretName: fluentd-gcs-key
                - name: varlog
                  hostPath:
                    path: /var/log
                - name: dockercontainerlogdirectory
                  hostPath:
                    path: /var/log/pods
                - name: fluentd-buffer
                  emptyDir: {}
        

  * Apply the DaemonSet:
        
        kubectl apply -f fluentd-daemonset.yaml
        




### Verify Fluentd deployment

  1. Verify that Fluentd pods are running on each node:
         
         kubectl get pods -n logging -l k8s-app=fluentd-gcs
         

  2. Check Fluentd logs for successful GCS writes:
         
         kubectl logs -l k8s-app=fluentd-gcs -n logging --tail=20
         

  3. Verify that log files appear in the GCS bucket:

     1. Go to **Cloud Storage > Buckets** in the GCP Console.
     2. Click on the bucket (for example, `oauth2-proxy-logs-bucket`).
     3. Navigate to the `oauth2-proxy-logs/` folder.
     4. Verify that `.json` files are present with recent timestamps.



## Retrieve the Google SecOps service account

Google SecOps uses a unique service account to read data from your GCS bucket. You must grant this service account access to your bucket.

### Get the service account email

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `OAuth2 Proxy Logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Kubernetes Auth Proxy** as the **Log type**.
  7. Click **Get Service Account**. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  8. Copy this email address for use in the next step.

**Note:** Each Google SecOps instance has a unique service account. Do not use service accounts from other documentation or examples.
  9. Click **Next**.

  10. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
           
           gs://oauth2-proxy-logs-bucket/oauth2-proxy-logs/
           

     * Replace `oauth2-proxy-logs-bucket` with your GCS bucket name.

**Note:** Always include the trailing slash (/) at the end of the URI.
     * **Source deletion option** : Select the deletion option according to your preference:

       * **Never** : Never deletes any files after transfers (recommended for testing).
       * **Delete transferred files** : Deletes files after successful transfer.
       * **Delete transferred files and empty directories** : Deletes files and empty directories after successful transfer.

**Note:** If you select a deletion option, the Google SecOps service account must have **Storage Object Admin** role instead of Storage Object Viewer. Update IAM permissions accordingly.
     * **Maximum File Age** : Include files modified in the last number of days (default is 180 days)

     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces)

     * **Ingestion labels** : The label to be applied to the events from this feed

  11. Click **Next**.

  12. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




## Grant IAM permissions to the Google SecOps service account

The Google SecOps service account needs **Storage Object Viewer** role on your GCS bucket.

  1. Go to **Cloud Storage > Buckets**.
  2. Click on your bucket name (for example, `oauth2-proxy-logs-bucket`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Paste the Google SecOps service account email (for example, `chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com`)
     * **Assign roles** : Select **Storage Object Viewer**
  6. Click **Save**.

**Note:** If you plan to use the deletion option "Delete transferred files" or "Delete transferred files and empty directories," grant **Storage Object Admin** role instead of Storage Object Viewer.

## OAuth2 Proxy log reference

The following table describes the log fields generated by OAuth2 Proxy and their security relevance:

### Authentication log fields

Field | Example | Description  
---|---|---  
Client | `10.0.0.1` | Client/remote IP address (uses `X-Real-IP` header if `--reverse-proxy=true`)  
RequestID | `00010203-0405-4607-8809-0a0b0c0d0e0f` | Request ID from the `X-Request-Id` header (random UUID if empty)  
Username | `user@example.com` | Email or username of the authentication request  
Timestamp | `2024/01/15 10:30:00` | Date and time of the authentication event  
Status | `AuthSuccess` | Authentication result: `AuthSuccess`, `AuthFailure`, or `AuthError`  
Message | `Authenticated via OAuth2` | Details of the authentication attempt  
  
### Request log fields

Field | Example | Description  
---|---|---  
Client | `10.0.0.1` | Client/remote IP address  
RequestID | `00010203-0405-4607-8809-0a0b0c0d0e0f` | Request ID  
Username | `user@example.com` | Authenticated user email  
Timestamp | `2024/01/15 10:30:01` | Date and time of the request  
Host | `app.example.com` | Value of the Host header  
RequestMethod | `GET` | HTTP request method  
Upstream | `10.0.0.5:8080` | Upstream server that handled the request  
RequestURI | `/dashboard` | URI path of the request  
Protocol | `HTTP/1.1` | Request protocol  
UserAgent | `Mozilla/5.0` | Full user agent string  
StatusCode | `200` | HTTP response status code  
ResponseSize | `1234` | Response size in bytes  
RequestDuration | `0.005` | Request processing time in seconds  
  
## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
about | about | Information about the event  
http_req_id_field | additional.fields | Additional fields not covered by standard UDM schema  
http_req_path_field | additional.fields |   
k8s_pod_app_field | additional.fields |   
k8s_pod_template_hash_field | additional.fields |   
k8s_pod_tls_mode_field | additional.fields |   
k8s_pod_canonical_revision_field | additional.fields |   
k8s_pod_canonical_name_field | additional.fields |   
pod_name | additional.fields |   
cntnr_name | additional.fields |   
destination_canonical_revision | additional.fields |   
requested_server | additional.fields |   
nodename_label | additional.fields |   
componentName_label | additional.fields |   
componentVersion_label | additional.fields |   
azureResourceID_label | additional.fields |   
producer_label | additional.fields |   
first_label | additional.fields |   
last_label | additional.fields |   
meta_name | additional.fields |   
resource_version_label | additional.fields |   
request_apiVersion | additional.fields |   
request_kind_label | additional.fields |   
request_type_label | additional.fields |   
response_apiVersion | additional.fields |   
response_kind_label | additional.fields |   
response_type_label | additional.fields |   
jsonPayload.message | metadata.description | Description of the event  
event_type | metadata.event_type | Type of event  
labels.request_id | metadata.product_log_id | Product-specific log identifier  
insertId | metadata.product_log_id |   
jsonPayload.chartVersion | metadata.product_version | Product version  
httpRequest.protocol | network.application_protocol | Application protocol used in the network connection  
network.direction | network.direction | Direction of network traffic  
httpRequest.requestMethod | network.http.method | HTTP method  
http_method | network.http.method |   
httpRequest.status | network.http.response_code | HTTP response code  
httpRequest.userAgent | network.http.user_agent | HTTP user agent  
requestMetadata.callerSuppliedUserAgent | network.http.user_agent |   
labels.protocol | network.ip_protocol | IP protocol  
httpRequest.responseSize | network.received_bytes | Number of bytes received  
labels.total_received_bytes | network.received_bytes |   
httpRequest.requestSize | network.sent_bytes | Number of bytes sent  
labels.total_sent_bytes | network.sent_bytes |   
jsonPayload.session | network.session_id | Session identifier  
labels.service_authentication_policy | network.tls.cipher | TLS cipher suite  
principal | principal | Principal entity involved in the event  
principal_hostname | principal.hostname | Hostname of the principal  
prin_userid | principal.user.userid | User ID of the principal  
security_result | security_result | Result of security evaluation  
target | target | Target entity involved in the event  
target_hostname | target.hostname | Hostname of the target  
resource_sub_type | target.resource.resource_subtype | Subtype of the target resource  
target_userid | target.user.userid | User ID of the target  
metadata.product_name | metadata.product_name | Product name  
metadata.vendor_name | metadata.vendor_name | Vendor name  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/kubernetes-auth-proxy-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
