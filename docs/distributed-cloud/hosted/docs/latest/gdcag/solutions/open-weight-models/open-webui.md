---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/solutions/open-weight-models/open-webui/
title: Open WebUI for Open Weight Models user guide on GDC air-gapped \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T19:26:33.615053+00:00
---

# Open WebUI for Open Weight Models user guide on GDC air-gapped  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/solutions/open-weight-models/open-webui/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Open WebUI for Open Weight Models user guide on GDC air-gapped Stay organized with collections  Save and categorize content based on your preferences. 

This document provides step-by-step instructions for deploying [Open WebUI](https://github.com/open-webui/open-webui), a self-hosted, browser-based chat interface, on Google Distributed Cloud (GDC) air-gapped environments. Open WebUI connects to the inference backends deployed with the Ollama and vLLM user guides through their Ollama and OpenAI-compatible APIs, so developers and end users can interact with the open weight models without writing API calls.

## Architecture

Open WebUI runs as a single-replica `Deployment` in its own namespace of the standard cluster. Its state (user accounts, chats, settings) is stored on a `ReadWriteOnce` `PersistentVolumeClaim`. A `ConfigMap` holds the connection settings for the inference backends, which are reached through their in-cluster `Service` names, and a `Secret` holds the session signing key. A Kubernetes `Service` of type `LoadBalancer` exposes the web interface, and `NetworkPolicy` / `ProjectNetworkPolicy` objects secure access to it.

**Note:** Limitation: Without a ReadOnlyMany StorageClass, this solution can only deploy one replica. Open WebUI runs in offline mode: features that download models or content from the internet (retrieval-augmented generation with the default embedding model, web search, community sharing, image generation) are disabled.

## Before you begin

**Note:** This guide requires GDC air-gapped 1.16.2-hf1 (1.16.2-gdch.1353-1) or later, and a standard cluster.

Ensure that at least one inference backend has been deployed with the [Gemma models with Ollama user guide](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/solutions/open-weight-models/ollama/gemma), the [Gemma models with vLLM user guide](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/solutions/open-weight-models/vllm/gemma), or the [Mistral models with vLLM user guide](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/solutions/open-weight-models/vllm/mistral), and that you have access to the `${HOME}/gdcag-solutions` directory of the corresponding reference implementation on the workstation.

### Identity and Access Management

Ensure that the necessary IAM accounts, roles, and permissions are properly configured.

**GDC User** roles on **organization** :

  * Optional: Standard Cluster Admin (View clusters from the console)



**GDC User** roles on **project** :

  * Standard Cluster Admin (`standard-cluster-admin`)



**GDC User** role on the **standard cluster** :

  * `StandardClusterRoleBinding` to the `StandardClusterRole` `cluster-admin` (created by a Project IAM Admin, see the _Identity and Access Management_ section of the reference implementation)



### Workstation

Run all commands in this guide from a workstation with the required tools and connectivity to the environment and internet, unless a step states otherwise.

  1. Create the user guide directory structure:
         
         mkdir -p ${HOME}/gdcag-solutions/open-weight-models/open-webui/env.d
         mkdir -p ${HOME}/gdcag-solutions/open-weight-models/open-webui/secrets
         
         chmod u=rwx,go= ${HOME}/gdcag-solutions/open-weight-models/open-webui/secrets
         

  2. Create the session signing key:
         
         openssl rand -hex 32 > ${HOME}/gdcag-solutions/open-weight-models/open-webui/secrets/open_webui_secret_key
         
         chmod u=rw,go= ${HOME}/gdcag-solutions/open-weight-models/open-webui/secrets/open_webui_secret_key
         

  3. Create the user guide environment configuration file:
         
         cat << 'EOF' > ${HOME}/gdcag-solutions/open-weight-models/open-webui/env.d/open-webui.sh && echo "Successfully created." || echo "Failed to create!"
         # Open WebUI
         export GDCS_OPEN_WEBUI_IMAGE_TAG="v0.11.3"
         export GDCS_OPEN_WEBUI_NAME="open-webui"
         export GDCS_OPEN_WEBUI_PVC_SIZE="20Gi"
         export GDCS_OPEN_WEBUI_SECRET_KEY="$(cat ${GDCS_USER_GUIDE_HOME}/secrets/open_webui_secret_key)"
         
         # Inference backends (in-cluster Service addresses, several backends separated by ';').
         # The user guides name the Service after the model: Ollama uses GDCS_OLLAMA_MODEL_KUBERNETES
         # (gemma4:e4b -> gemma4-e4b) and vLLM uses GDCS_HF_MODEL_KUBERNETES (such as vllm-gemma or vllm-mistral)
         # (mistralai/Mistral-7B-Instruct-v0.2 -> mistralai-mistral-7b-instruct-v0-2); kubectl get service
         # in the workload namespace (ollama-gemma, vllm-gemma or vllm-mistral) lists them.
         export GDCS_OPEN_WEBUI_ENABLE_OLLAMA_API="OPEN_WEBUI_ENABLE_OLLAMA_API"
         export GDCS_OPEN_WEBUI_OLLAMA_BASE_URLS="OPEN_WEBUI_OLLAMA_BASE_URLS"
         export GDCS_OPEN_WEBUI_ENABLE_OPENAI_API="OPEN_WEBUI_ENABLE_OPENAI_API"
         export GDCS_OPEN_WEBUI_OPENAI_API_BASE_URLS="OPEN_WEBUI_OPENAI_API_BASE_URLS"
         export GDCS_OPEN_WEBUI_OPENAI_API_KEYS="none"         # vLLM does not check API keys unless started with --api-key
         
         # Workload
         export GDCS_WORKLOAD_NAMESPACE="open-webui"
         
         # CPU resources
         export GDCS_WORKLOAD_CPU_LIMIT="2"
         export GDCS_WORKLOAD_CPU_REQUEST="1"
         
         # Memory resources
         export GDCS_WORKLOAD_MEMORY_LIMIT="4Gi"
         export GDCS_WORKLOAD_MEMORY_REQUEST="2Gi"
         
         EOF
         

Replace the following:

     * `OPEN_WEBUI_ENABLE_OLLAMA_API`: `true` if you deployed an Ollama backend, otherwise `false`.
     * `OPEN_WEBUI_OLLAMA_BASE_URLS`: the in-cluster URLs of the Ollama Services, separated by `;`, for example `http://gemma4-e4b.ollama-gemma.svc.cluster.local`. Leave it empty if you deployed no Ollama backend.
     * `OPEN_WEBUI_ENABLE_OPENAI_API`: `true` if you deployed a vLLM backend, otherwise `false`.
     * `OPEN_WEBUI_OPENAI_API_BASE_URLS`: the in-cluster URLs of the vLLM Services with the `/v1` path, separated by `;`, for example `http://mistralai-mistral-7b-instruct-v0-2.vllm-mistral.svc.cluster.local/v1` or `http://google-gemma-4-e2b-it.vllm-gemma.svc.cluster.local/v1`. Leave it empty if you deployed no vLLM backend.
  4. Create the user guide environment loader file:
         
         cat << 'EOF' > ${HOME}/gdcag-solutions/open-weight-models/open-webui/env.sh && echo "Successfully created." || echo "Failed to create!"
         source "${HOME}/gdcag-solutions/open-weight-models/IMPLEMENTATION/env.sh"
         
         export GDCS_USER_GUIDE_HOME="${HOME}/gdcag-solutions/open-weight-models/open-webui"
         echo "GDCS_USER_GUIDE_HOME=${GDCS_USER_GUIDE_HOME}"
         
         # Sourced in dependency order
         source "${GDCS_USER_GUIDE_HOME}/env.d/open-webui.sh"
         EOF
         

Replace the following:

     * `IMPLEMENTATION`: `ollama` or `vllm`, the reference implementation that you completed on this workstation.
  5. Edit and review the environment file with your preferred editor:
         
         ${EDITOR:-vi} ${HOME}/gdcag-solutions/open-weight-models/open-webui/env.d/open-webui.sh
         

  6. Source the environment file:
         
         source ${HOME}/gdcag-solutions/open-weight-models/open-webui/env.sh
         

The output is similar to the following:
         
         GDCS_ROOT_HOME=HOME_DIRECTORY_PATH/gdcag-solutions
         GDCS_IMPLEMENTATION_HOME=HOME_DIRECTORY_PATH/gdcag-solutions/open-weight-models/IMPLEMENTATION
         GDCS_USER_GUIDE_HOME=HOME_DIRECTORY_PATH/gdcag-solutions/open-weight-models/open-webui
         


**Note:** Any time a new terminal or shell is started, the environment file needs to be sourced.

### Cluster

  1. Configure `gdcloud`:
         
         gdcloud config set core/account "default-user"
         gdcloud config set core/organization_console_url "${GDC_ZONAL_CONSOLE_URL}"
         gdcloud config set core/project "${GDC_PROJECT}"
         gdcloud config set core/zone "${GDC_ZONE}"
         

  2. Authenticate to the GDC environment:
         
         gdcloud auth login
         

  3. Retrieve cluster credentials:
         
         gdcloud clusters get-credentials "${GDC_STANDARD_CLUSTER_NAME}" \
         --project="${GDC_PROJECT}" \
         --standard \
         --zone="${GDC_ZONE}"
         

  4. Verify that the inference backend `Service`s referenced in the environment file exist:
         
         for url in $(echo "${GDCS_OPEN_WEBUI_OLLAMA_BASE_URLS};${GDCS_OPEN_WEBUI_OPENAI_API_BASE_URLS}" | tr ';' ' '); do
           host=$(echo "${url}" | sed -E 's#https?://([^/:]+).*#\1#')
           kubectl get service "${host%%.*}" --namespace="$(echo "${host}" | cut -d. -f2)" --output=wide
         done
         




## Implementation

### Artifact migration

  1. Define the list of required container images for the solution:
         
         declare -a GDCS_REGISTRY_IMAGES=(
           "ghcr.io/open-webui/open-webui:${GDCS_OPEN_WEBUI_IMAGE_TAG}"
         )
         export SERIALIZED_IMAGES=$(declare -p GDCS_REGISTRY_IMAGES)
         

  2. Seed the required container images to the artifact registry with the reference implementation's script:
         
         ${GDCS_IMPLEMENTATION_HOME}/seed_registry.sh
         




### Namespace

  1. Create the namespace:
         
         kubectl create namespace "${GDCS_WORKLOAD_NAMESPACE}"
         

  2. Add the `imagePullSecret`:
         
         kubectl create secret docker-registry "${GDCS_HARBOR_K8S_PULL_SECRET}" \
         --dry-run=client \
         --from-file=.dockerconfigjson=${GDCS_HARBOR_K8S_DOCKER_CONFIG}/config.json \
         --namespace="${GDCS_WORKLOAD_NAMESPACE}" \
         --output=yaml | kubectl apply -f -
         

  3. Create the `Secret` with the session signing key:
         
         kubectl create secret generic "${GDCS_OPEN_WEBUI_NAME}" \
         --dry-run=client \
         --from-literal=WEBUI_SECRET_KEY="${GDCS_OPEN_WEBUI_SECRET_KEY}" \
         --namespace="${GDCS_WORKLOAD_NAMESPACE}" \
         --output=yaml | kubectl apply -f -
         




### Storage

  1. Create the manifest for the `PersistentVolumeClaim` for the Open WebUI data:
         
         cat <<EOF > "${GDCS_USER_GUIDE_HOME}/${GDCS_OPEN_WEBUI_NAME}-rwo-pvc.yaml" && echo "Successfully created." || echo "Failed to create!"
         apiVersion: v1
         kind: PersistentVolumeClaim
         metadata:
           name: ${GDCS_OPEN_WEBUI_NAME}-rwo
         spec:
           accessModes:
             - ReadWriteOnce
           resources:
             requests:
               storage: ${GDCS_OPEN_WEBUI_PVC_SIZE}
           storageClassName: standard-rwo
           volumeMode: Filesystem
         EOF
         

  2. Apply the manifest for the `PersistentVolumeClaim`:
         
         kubectl apply \
         --filename="${GDCS_USER_GUIDE_HOME}/${GDCS_OPEN_WEBUI_NAME}-rwo-pvc.yaml" \
         --namespace="${GDCS_WORKLOAD_NAMESPACE}"
         




### Web interface

  1. Create the manifest for the Open WebUI `ConfigMap`, `Deployment` and `Service`. Open WebUI runs in offline mode (`OFFLINE_MODE`), keeps this `ConfigMap` as the source of truth (`ENABLE_PERSISTENT_CONFIG=false`) and disables the features that need internet access:
         
         cat <<EOF > "${GDCS_USER_GUIDE_HOME}/${GDCS_OPEN_WEBUI_NAME}-deployment.yaml" && echo "Successfully created." || echo "Failed to create!"
         apiVersion: v1
         kind: ConfigMap
         metadata:
           name: ${GDCS_OPEN_WEBUI_NAME}
         data:
           DATA_DIR: "/app/backend/data"
           ENABLE_COMMUNITY_SHARING: "false"
           ENABLE_IMAGE_GENERATION: "false"
           ENABLE_OLLAMA_API: "${GDCS_OPEN_WEBUI_ENABLE_OLLAMA_API}"
           ENABLE_OPENAI_API: "${GDCS_OPEN_WEBUI_ENABLE_OPENAI_API}"
           ENABLE_PERSISTENT_CONFIG: "false"
           ENABLE_SIGNUP: "true"
           ENABLE_VERSION_UPDATE_CHECK: "false"
           ENABLE_WEB_SEARCH: "false"
           OFFLINE_MODE: "true"
           OLLAMA_BASE_URLS: "${GDCS_OPEN_WEBUI_OLLAMA_BASE_URLS}"
           OPENAI_API_BASE_URLS: "${GDCS_OPEN_WEBUI_OPENAI_API_BASE_URLS}"
           OPENAI_API_KEYS: "${GDCS_OPEN_WEBUI_OPENAI_API_KEYS}"
           PORT: "8080"
         ---
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           labels:
             app: ${GDCS_OPEN_WEBUI_NAME}
           name: ${GDCS_OPEN_WEBUI_NAME}
         spec:
           replicas: 1
           selector:
             matchLabels:
               app: ${GDCS_OPEN_WEBUI_NAME}
           strategy:
             type: Recreate
           template:
             metadata:
               labels:
                 app: ${GDCS_OPEN_WEBUI_NAME}
             spec:
               containers:
                 - envFrom:
                     - configMapRef:
                         name: ${GDCS_OPEN_WEBUI_NAME}
                     - secretRef:
                         name: ${GDCS_OPEN_WEBUI_NAME}
                   image: ${GDCS_HARBOR_PROJECT_URI}/open-webui/open-webui:${GDCS_OPEN_WEBUI_IMAGE_TAG}
                   imagePullPolicy: IfNotPresent
                   livenessProbe:
                     failureThreshold: 3
                     httpGet:
                       path: /health
                       port: 8080
                     periodSeconds: 30
                     timeoutSeconds: 10
                   name: open-webui
                   ports:
                     - containerPort: 8080
                       name: http
                   readinessProbe:
                     failureThreshold: 3
                     httpGet:
                       path: /health
                       port: 8080
                     periodSeconds: 10
                     successThreshold: 1
                     timeoutSeconds: 5
                   resources:
                     limits:
                       cpu: "${GDCS_WORKLOAD_CPU_LIMIT}"
                       memory: "${GDCS_WORKLOAD_MEMORY_LIMIT}"
                     requests:
                       cpu: "${GDCS_WORKLOAD_CPU_REQUEST}"
                       memory: "${GDCS_WORKLOAD_MEMORY_REQUEST}"
                   securityContext:
                     allowPrivilegeEscalation: false
                   startupProbe:
                     failureThreshold: 60
                     httpGet:
                       path: /health
                       port: 8080
                     periodSeconds: 10
                     timeoutSeconds: 5
                   volumeMounts:
                     - mountPath: /app/backend/data
                       name: data
               imagePullSecrets:
                 - name: ${GDCS_HARBOR_K8S_PULL_SECRET}
               volumes:
                 - name: data
                   persistentVolumeClaim:
                     claimName: ${GDCS_OPEN_WEBUI_NAME}-rwo
         ---
         apiVersion: v1
         kind: Service
         metadata:
           name: ${GDCS_OPEN_WEBUI_NAME}
         spec:
           ports:
             - name: http
               port: 80
               protocol: TCP
               targetPort: 8080
           selector:
             app: ${GDCS_OPEN_WEBUI_NAME}
           type: LoadBalancer
         EOF
         

  2. Apply the manifest for the Open WebUI `ConfigMap`, `Deployment` and `Service`:
         
         kubectl apply \
         --filename="${GDCS_USER_GUIDE_HOME}/${GDCS_OPEN_WEBUI_NAME}-deployment.yaml" \
         --namespace="${GDCS_WORKLOAD_NAMESPACE}"
         

  3. Create the manifest for the Open WebUI `NetworkPolicy`:
         
         cat <<EOF > "${GDCS_USER_GUIDE_HOME}/${GDCS_OPEN_WEBUI_NAME}-netpol.yaml" && echo "Successfully created." || echo "Failed to create!"
         apiVersion: networking.k8s.io/v1
         kind: NetworkPolicy
         metadata:
           name: allow-${GDCS_OPEN_WEBUI_NAME}-ingress
           namespace: ${GDCS_WORKLOAD_NAMESPACE}
         spec:
           ingress:
             - from:
                 - ipBlock:
                     cidr: 0.0.0.0/0
                 - namespaceSelector: {}
               ports:
                 - port: 8080
                   protocol: TCP
           podSelector: {}
           policyTypes:
             - Ingress
         EOF
         

  4. Apply the manifest for the Open WebUI `NetworkPolicy`:
         
         kubectl apply \
         --filename="${GDCS_USER_GUIDE_HOME}/${GDCS_OPEN_WEBUI_NAME}-netpol.yaml"
         


**Note:** The `NetworkPolicy` admits traffic from any source to the workload port inside the cluster. Access to the LoadBalancer IP address from outside the project additionally requires a `ProjectNetworkPolicy` (`networking.gdc.goog/v1`) created in the project namespace by a Project NetworkPolicy Admin, see [Configure project network policies](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pnp/pnp-overview).

  1. Wait for the `Pod` to be Running:
         
         watch --color --interval 5 --no-title \
         "kubectl get pods --selector=app=${GDCS_OPEN_WEBUI_NAME} \
         --namespace=${GDCS_WORKLOAD_NAMESPACE} | GREP_COLORS='mt=01;92' grep -E --color=always -e '^' -e 'Running'"
         

  2. Wait for the `Deployment` to be Ready:
         
         watch --color --interval 5 --no-title \
         "kubectl get deployment/${GDCS_OPEN_WEBUI_NAME} \
         --namespace=${GDCS_WORKLOAD_NAMESPACE} | GREP_COLORS='mt=01;92' grep -E --color=always -e '^' -e '1/1     1            1'"
         

  3. Optional: Stream the container logs to monitor startup progress:
         
         kubectl logs deployment/${GDCS_OPEN_WEBUI_NAME} \
         --follow \
         --namespace="${GDCS_WORKLOAD_NAMESPACE}"
         




## Validation

  1. Retrieve the LoadBalancer IP address for Open WebUI:
         
         export OPEN_WEBUI_LB_IP=$(kubectl get service/${GDCS_OPEN_WEBUI_NAME} --namespace="${GDCS_WORKLOAD_NAMESPACE}" --output=jsonpath='{.status.loadBalancer.ingress[*].ip}')
         echo "OPEN_WEBUI_LB_IP=${OPEN_WEBUI_LB_IP}"
         

  2. Check the health and version endpoints using the load balancer:
         
         curl --show-error --silent http://${OPEN_WEBUI_LB_IP}/health && echo
         
         curl --show-error --silent http://${OPEN_WEBUI_LB_IP}/api/version && echo
         

The output is similar to the following:
         
         {"status":true}
         {"version":"0.11.3"}
         

  3. Check the health and version endpoints using port forwarding:
         
         kubectl port-forward service/${GDCS_OPEN_WEBUI_NAME} \
         --namespace="${GDCS_WORKLOAD_NAMESPACE}" 8080:80 &
         PF_PID=$!
         
         sleep 2
         
         curl --show-error --silent http://127.0.0.1:8080/health && echo
         curl --show-error --silent http://127.0.0.1:8080/api/version && echo
         
         kill ${PF_PID}
         

  4. Verify that Open WebUI can reach the inference backends:
         
         kubectl exec deployment/${GDCS_OPEN_WEBUI_NAME} \
         --namespace="${GDCS_WORKLOAD_NAMESPACE}" \
         -- sh -c 'for url in $(echo "${OLLAMA_BASE_URLS};${OPENAI_API_BASE_URLS}" | tr ";" " "); do case "${url}" in *"/v1") echo "${url}/models"; curl --max-time 10 --show-error --silent "${url}/models" | head -c 300; echo;; *) echo "${url}/api/tags"; curl --max-time 10 --show-error --silent "${url}/api/tags" | head -c 300; echo;; esac; done'
         

  5. Open `http://${OPEN_WEBUI_LB_IP}` in a browser and create the first account; the first account created becomes the administrator. Select a model in the chat view and send a prompt.

**Note:** When the LoadBalancer IP address isn't reachable from your workstation, run `kubectl port-forward service/${GDCS_OPEN_WEBUI_NAME} --namespace="${GDCS_WORKLOAD_NAMESPACE}" 8080:80` and open `http://127.0.0.1:8080` instead.



## Operations

### Add or change inference backends

  1. Update `GDCS_OPEN_WEBUI_OLLAMA_BASE_URLS` or `GDCS_OPEN_WEBUI_OPENAI_API_BASE_URLS` in `env.d/open-webui.sh`, source the environment file, and run the manifest step in Web interface again. Then apply the manifest and restart Open WebUI, which reads the `ConfigMap` on every start because persistent configuration is disabled:
         
         kubectl apply \
         --filename="${GDCS_USER_GUIDE_HOME}/${GDCS_OPEN_WEBUI_NAME}-deployment.yaml" \
         --namespace="${GDCS_WORKLOAD_NAMESPACE}"
         
         kubectl rollout restart deployment/${GDCS_OPEN_WEBUI_NAME} \
         --namespace="${GDCS_WORKLOAD_NAMESPACE}"
         




### Upgrade

  1. Set the new `GDCS_OPEN_WEBUI_IMAGE_TAG` in the environment file, source it, seed the new image and roll the `Deployment`:
         
         source ${HOME}/gdcag-solutions/open-weight-models/open-webui/env.sh
         
         declare -a GDCS_REGISTRY_IMAGES=(
           "ghcr.io/open-webui/open-webui:${GDCS_OPEN_WEBUI_IMAGE_TAG}"
         )
         export SERIALIZED_IMAGES=$(declare -p GDCS_REGISTRY_IMAGES)
         ${GDCS_IMPLEMENTATION_HOME}/seed_registry.sh
         
         kubectl set image deployment/${GDCS_OPEN_WEBUI_NAME} \
         open-webui="${GDCS_HARBOR_PROJECT_URI}/open-webui/open-webui:${GDCS_OPEN_WEBUI_IMAGE_TAG}" \
         --namespace="${GDCS_WORKLOAD_NAMESPACE}"
         




### Backup

  1. Create a `VolumeSnapshot` of the data volume (the `standard` `VolumeSnapshotClass` is available on GDC standard clusters):
         
         cat <<EOF | kubectl apply --namespace="${GDCS_WORKLOAD_NAMESPACE}" -f -
         apiVersion: snapshot.storage.k8s.io/v1
         kind: VolumeSnapshot
         metadata:
           name: ${GDCS_OPEN_WEBUI_NAME}-$(date +%Y%m%d-%H%M)
         spec:
           source:
             persistentVolumeClaimName: ${GDCS_OPEN_WEBUI_NAME}-rwo
           volumeSnapshotClassName: standard
         EOF
         




## Troubleshooting

Symptom | Likely cause | Action  
---|---|---  
No model is offered in the chat view | Backend `Service` address wrong, backend not Ready, or the backend `NetworkPolicy` doesn't admit the Open WebUI namespace | Run the backend verification step in _Validation_ ; check the backend `Deployment` and its `NetworkPolicy`  
`Pod` restarts during start-up | Slow first start on the `PersistentVolume` | Check `kubectl describe pod`; the `startupProbe` allows 10 minutes  
Document upload (RAG) fails | Offline mode blocks the download of the default embedding model | Configure `RAG_EMBEDDING_ENGINE=ollama` with an embedding model served by Ollama, or keep RAG disabled  
LoadBalancer IP stays `<pending>` or isn't reachable | Load balancer not available in the environment, or missing `ProjectNetworkPolicy` | Use the port forwarding validation step; ask the Project NetworkPolicy Admin for a `ProjectNetworkPolicy`  
Session invalid after a `Pod` restart | `WEBUI_SECRET_KEY` changed | Keep the `Secret` stable; restore it from `secrets/open_webui_secret_key`  
  
## Clean up

  1. Delete the Open WebUI resources:
         
         kubectl delete namespace "${GDCS_WORKLOAD_NAMESPACE}"
         

  2. Delete the local files:
         
         rm -rf ${HOME}/gdcag-solutions/open-weight-models/open-webui
         




## Additional materials

  * [Open WebUI documentation](https://docs.openwebui.com/)
  * [Open WebUI environment variable reference](https://docs.openwebui.com/reference/env-configuration)
  * [Ollama OpenAI compatibility](https://github.com/ollama/ollama/blob/main/docs/openai.md)
  * [vLLM OpenAI-compatible server](https://docs.vllm.ai/en/latest/serving/openai_compatible_server.html)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
