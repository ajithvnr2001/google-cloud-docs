---
url: https://docs.cloud.google.com/distributed-cloud/sandbox/latest/services/ocr/
title: Try out Optical Character Recognition (OCR) \u00a0|\u00a0 Google Distributed Cloud Sandbox \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:06:47.974180+00:00
---

# Try out Optical Character Recognition (OCR)  |  Google Distributed Cloud Sandbox  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/sandbox/latest/services/ocr/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Sandbox ](https://docs.cloud.google.com/distributed-cloud/sandbox/latest)



Send feedback 

#  Try out Optical Character Recognition (OCR) Stay organized with collections  Save and categorize content based on your preferences. 

This guide walks you through the process of running an Optical Character Recognition (OCR) test using Google's Vertex AI Vision service.

Before trying this sample, follow the Python setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest).

  1. Create a python file `ocr_test.py`. Replace the `image_uri_to_test` value with the URI of a source image, as shown:
         
         import os
         import requests
         import json
         
         def detect_text_rest(image_uri):
             """Performs Optical Character Recognition (OCR) on an image by invoking the Vertex AI REST API."""
         
             # Securely fetch the API key from environment variables
             api_key = os.environ.get("GCP_API_KEY")
             if not api_key:
                 raise ValueError("GCP_API_KEY environment variable must be defined.")
         
             # Construct the Vision API endpoint URL
             vision_api_url = f"https://vision.googleapis.com/v1/images:annotate?key={api_key}"
         
             print(f"Initiating OCR process for image: {image_uri}")
         
             # Define the request payload for text detection
             request_payload = {
                 "requests": [
                     {
                         "image": {
                             "source": {
                                 "imageUri": image_uri
                             }
                         },
                         "features": [
                             {
                                 "type": "TEXT_DETECTION"
                             }
                         ]
                     }
                 ]
             }
         
             # Send a POST request to the Vision API
             response = requests.post(vision_api_url, json=request_payload)
             response.raise_for_status()  # Check for HTTP errors
         
             response_json = response.json()
         
             print("\n--- OCR Results ---")
         
             # Extract and print the detected text
             if "textAnnotations" in response_json["responses"]:
                 full_text = response_json["responses"]["textAnnotations"]["description"]
                 print(f"Detected Text:\n{full_text}")
             else:
                 print("No text was detected in the image.")
         
             print("--- End of Results ---\n")
         
         if __name__ == "__main__":
             # URI of a publicly available image, or a storage bucket
             image_uri_to_test = "IMAGE_URI"
         
             detect_text_rest(image_uri_to_test)
         

Replace the following:

     * `IMAGE_URI` with the URI of a publicly available image that contains text, for example, "`https://cloud.google.com/vision/docs/images/sign.jpg`". Alternatively, you can specify a Cloud Storage URI, for example, "`gs://your-bucket/your-image.png`"
  2. Create a Dockerfile:
         
         ROM python:3.9-slim
         
         WORKDIR /app
         
         COPY ocr_test.py /app/
         
         # Install 'requests' for HTTP calls
         RUN pip install --no-cache-dir requests
         
         CMD ["python", "ocr_test.py"]
         

  3. Build the Docker image for the translation application:
         
         docker build -t ocr-app .
         

  4. Follow instructions at [Configure Docker](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch/platform-application/deploy-container-workloads#configure-docker) to:

     1. Configure Docker,
     2. Create a secret, and
     3. Upload the image to HaaS.
  5. [Sign in to the user cluster](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch/clusters#kubernetes-clusters) and generate its kubeconfig file with a user identity. Make sure you set the kubeconfig path as an environment variable:
         
         export KUBECONFIG=${CLUSTER_KUBECONFIG_PATH}
         

  6. Create a Kubernetes secret by running the following command in your terminal, pasting your API key:
         
         kubectl create secret generic gcp-api-key-secret \
           --from-literal=GCP_API_KEY='PASTE_YOUR_API_KEY_HERE'
         

This command creates a secret named `gcp-api-key-secret` with a key `GCP_API_KEY`.

  7. Apply the kubernetes manifest:
         
         apiVersion: batch/v1
         kind: Job
         metadata:
           name: ocr-test-job-apikey
         spec:
           template:
             spec:
               containers:
               - name: ocr-test-container
                 image: HARBOR_INSTANCE_URL/HARBOR_PROJECT/ocr-app:latest # Your image path
                 # Mount the API key from the secret into the container
                 # as an environment variable named GCP_API_KEY.
                 imagePullSecrets:
                 - name: ${SECRET}
                 envFrom:
                 - secretRef:
                     name: gcp-api-key-secret
               restartPolicy: Never
           backoffLimit: 4
         
         

Replace the following:

     * `HARBOR_INSTANCE_URL`: the Harbor instance URL.
     * `HARBOR_PROJECT`: the Harbor project.
     * `SECRET`: the name of the secret created to store docker credentials.
  8. Check the job status:
         
         kubectl get jobs/ocr-test-job-apikey
         # It will show 0/1 completions, then 1/1 after it succeeds
         

  9. After the job has completed, you can view the OCR output in the pod logs:
         
         kubectl logs -l job-name=ocr-test-job-apikey
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
