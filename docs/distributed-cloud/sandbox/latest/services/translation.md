---
url: https://docs.cloud.google.com/distributed-cloud/sandbox/latest/services/translation/
title: Try out machine translation \u00a0|\u00a0 Google Distributed Cloud Sandbox \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:13:53.376557+00:00
---

# Try out machine translation  |  Google Distributed Cloud Sandbox  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/sandbox/latest/services/translation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Sandbox ](https://docs.cloud.google.com/distributed-cloud/sandbox/latest)



Send feedback 

#  Try out machine translation Stay organized with collections  Save and categorize content based on your preferences. 

This page walks through an example of using the Vertex AI API to translate text from one language to another.

In this example, you deploy the workloads without using GPUs. To deploy using GPUs, follow the steps in [Deploy GPU container workloads](https://docs.cloud.google.com/distributed-cloud/sandbox/latest/services/gpu#deploy_gpu).

## Translation API

The following sample demonstrates the use of Vertex AI for text translation.

  1. Make sure you set up Vertex AI access as described in [Using Vertex AI](https://docs.cloud.google.com/distributed-cloud/sandbox/latest/services/vertex-ai).
  2. Set up the Python Vertex AI API, by following the instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest).

  3. Create a python file `main.py`. This script leverages the Google Cloud Translation API, accessed using a container endpoint, to perform translations.
         
         import os
         import requests # Use requests for HTTP calls
         from flask import Flask, request, jsonify
         
         app = Flask(__name__)
         
         TRANSLATE_API_URL = 'https://translation.googleapis.com/language/translate/v2'
         
         @app.route('/translate', methods=['POST'])
         def translate_text():
         
             try:
                 data = request.get_json()
                 text_to_translate = data.get('text')
                 target_language = data.get('target_language', 'en') # Default to English
         
                 if not text_to_translate:
                     return jsonify({'error': 'Missing "text" in request body'}), 400
         
                 params = {
                     'key': '${API_KEY}', // insert API key
                     'q': text_to_translate,
                     'target': target_language
                 }
         
                 response = requests.post(TRANSLATE_API_URL, params=params)
                 response.raise_for_status() # Raise an exception for bad status codes (4xx or 5xx)
         
                 result = response.json()
         
                 # The structure of the response from the REST API is slightly different
                 # It's usually: {'data': {'translations': [{'translatedText': '...', 'detectedSourceLanguage': '...'}]}}
                 if 'data' in result and 'translations' in result['data'] and len(result['data']['translations']) > 0:
                     translation_info = result['data']['translations'][0]
                     return jsonify({
                         'original_text': text_to_translate,
                         'translated_text': translation_info['translatedText'],
                         'detected_source_language': translation_info.get('detectedSourceLanguage')
                     })
                 else:
                     return jsonify({'error': 'Unexpected response format from Translation API', 'details': result}), 500
         
             except requests.exceptions.HTTPError as http_err:
                 print(f"HTTP error occurred: {http_err} - {response.text}")
                 return jsonify({'error': f"Translation API request failed: {http_err}", 'details': response.text}), response.status_code
             except Exception as e:
                 print(f"Error during translation: {e}")
                 return jsonify({'error': str(e)}), 500
         
         if __name__ == '__main__':
             port = int(os.environ.get('PORT', 8080))
             app.run(debug=True, host='0.0.0.0', port=port)
         

  4. Create a docker file that contains the python script:
         
         FROM python:3.9-slim
         
         WORKDIR /app
         
         COPY . /app
         
         RUN pip install --no-cache-dir -r requirements.txt
         
         EXPOSE 8080
         ENV PORT 8080
         
         CMD ["python", "main.py"]
         

  5. Build the Docker image for the translation application:
         
         docker build -t translation-app .
         

  6. Follow instructions at [Configure Docker](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch/platform-application/deploy-container-workloads#configure-docker) to:

     1. Configure docker,
     2. Create a secret, and
     3. Upload the image to HaaS (Harbor as a Service).
  7. [Sign in to the user cluster](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch/clusters#kubernetes-clusters) and generate its kubeconfig file with a user identity. Make sure you set the kubeconfig path as an environment variable:
         
         export KUBECONFIG=${CLUSTER_KUBECONFIG_PATH}
         

  8. Create and deploy the Kubernetes Deployment and Service custom resources. To enable container egress, make sure to include the label `egress.networking.gke.io/enabled: "true"`, as shown in this example.
         
         kubectl --kubeconfig ${KUBECONFIG} -n TENANT_PROJECT \
         create -f - <<EOF
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: translation-deployment-apikey
         spec:
           replicas: 2
           selector:
             matchLabels:
               app: translation-apikey
           template:
             metadata:
               labels:
                 app: translation-apikey
                 egress.networking.gke.io/enabled: "true"
             spec:
               dnsConfig:
                 nameservers:
                 - 8.8.8.8
               containers:
               - name: translation-app
                 image: HARBOR_INSTANCE_URL/HARBOR_PROJECT/translation-app:latest
                 ports:
                 - containerPort: 8080
               imagePullSecrets:
                 - name: SECRET
         
         ---
         apiVersion: v1
         kind: Service
         metadata:
           name: translation-service-apikey
         spec:
           type: LoadBalancer
           selector:
             app: translation-apikey
           ports:
           - protocol: TCP
             port: 80
             targetPort: 8080
         EOF
         

Replace the following:

     * `HARBOR_INSTANCE_URL`: the Harbor instance URL.
     * `HARBOR_PROJECT`: the Harbor project.
     * `SECRET`: the name of the secret created to store docker credentials.
  9. Verify the pods were created by the deployment:
         
         kubectl --kubeconfig ${KUBECONFIG} get pods -n TENANT_PROJECT
         

  10. Create a network policy to allow all network traffic to the tenant project:
         
         kubectl --kubeconfig ${KUBECONFIG} -n TENANT_PROJECT \
         create -f - <<EOF
         apiVersion: networking.k8s.io/v1
         kind: NetworkPolicy
         metadata:
           annotations:
           name: allow-all
         spec:
           ingress:
           - from:
             - ipBlock:
                 cidr: 0.0.0.0/0
           podSelector: {}
           policyTypes:
           - Ingress
         EOF
         

**Note:** This network policy is unsecure, and is not safe outside the GDC Sandbox environment. In a real production environment, you are responsible for creating a more secure network policy.
  11. Export the IP address for the service:
         
         export IP=`kubectl --kubeconfig=${KUBECONFIG} get service nginx-service \
               -n TENANT_PROJECT -o jsonpath='{.status.loadBalancer.ingress[*].ip}'`
         

  12. Create an SSH tunnel session to the workload that you deployed.
         
         sshuttle -r zone1-org-1-data@GDC_SANDBOX_INSTANCE_NAME --no-latency-control \
           --ssh-cmd 'gcloud compute ssh --project PROJECT_NAME --zone ZONE --tunnel-through-iap' \
           10.200.0.0/16 --dns
         

  13. Test the service by sending a JSON payload with the text and the target language to `http://${IP}:8080/translate`, using a POST request with the `Content-Type` header set to `application/json`. The following curl command will translate "Hello, world!" to Spanish (`es`):
         
         curl -X POST -H "Content-Type: application/json" -d '{"text": "Hello, world\\!", "target\_language": "es"}' http://${IP}:8080/translate
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
