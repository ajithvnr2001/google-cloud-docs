---
url: https://docs.cloud.google.com/distributed-cloud/sandbox/latest/services/speech-to-text/
title: Try out Speech-to-Text \u00a0|\u00a0 Google Distributed Cloud Sandbox \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:53:52.087633+00:00
---

# Try out Speech-to-Text  |  Google Distributed Cloud Sandbox  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/sandbox/latest/services/speech-to-text/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Sandbox ](https://docs.cloud.google.com/distributed-cloud/sandbox/latest)



Send feedback 

#  Try out Speech-to-Text Stay organized with collections  Save and categorize content based on your preferences. 

This guide walks you through the process of running a Speech-to-Text test using Google's Vertex AI Speech service.

Before trying this sample, follow the Python setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest).

  1. Create a python file `speech-to-text-test.py`. Replace the `image_uri_to_test` value with the URI of a source image, as shown:
         
         from google.cloud import speech
         
         def transcribe_gcs_audio(gcs_uri: str) -> speech.RecognizeResponse:
             client = speech.SpeechClient()
         
             audio = speech.RecognitionAudio(uri=gcs_uri)
             config = speech.RecognitionConfig(
                 encoding=speech.RecognitionConfig.AudioEncoding.FLAC,
                 sample_rate_hertz=16000,
                 language_code="en-US", # Specify the language code (e.g., "en-US" for US English)
                 # You can add more features here, e.g.:
                 # enable_automatic_punctuation=True,
                 # model="default" # or "latest_long", "phone_call", "video" (v2 API)
             )
         
             # Performs synchronous speech recognition on the audio file
             response = client.recognize(config=config, audio=audio)
         
             # Print the transcription
             for result in response.results:
                 print(f"Transcript: {result.alternatives[0].transcript}")
                 if result.alternatives[0].confidence:
                     print(f"Confidence: {result.alternatives[0].confidence:.2f}")
         
             return response
         
         if __name__ == "__main__":
             # Replace with the URI of your audio file in Google Cloud Storage
             audio_file_uri = "AUDIO_FILE_URI"
         
             print(f"Transcribing audio from: {audio_file_uri}")
             transcribe_gcs_audio(audio_file_uri)
         

Replace the following:

     * `AUDIO_FILE_URI`: the URI of an audio file "`gs://your-bucket/your-image.png`"
  2. Create a Dockerfile:
         
         ROM python:3.9-slim
         
         WORKDIR /app
         
         COPY speech-to-text-test.py /app/
         
         # Install 'requests' for HTTP calls
         RUN pip install --no-cache-dir requests
         
         CMD ["python", "speech-to-text-test.py"]
         

  3. Build the Docker image for the Speech-to-Text application:
         
         docker build -t speech-to-text-app .
         

  4. Follow instructions at [Configure Docker](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch/platform-application/deploy-container-workloads#configure-docker) to:

     1. Configure Docker,
     2. Create a secret, and
     3. Upload the image to HaaS.
  5. [Sign in to the user cluster](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch/clusters#kubernetes-clusters) and generate its kubeconfig file with a user identity. Make sure that you set the kubeconfig path as an environment variable:
         
         export KUBECONFIG=${CLUSTER_KUBECONFIG_PATH}
         

  6. Create a Kubernetes secret by running the following command in your terminal, pasting your API key:
         
         kubectl create secret generic gcp-api-key-secret \
           --from-literal=GCP_API_KEY='PASTE_YOUR_API_KEY_HERE'
         

This command creates a secret named `gcp-api-key-secret` with a key `GCP_API_KEY`.

  7. Apply the Kubernetes manifest:
         
         apiVersion: batch/v1
         kind: Job
         metadata:
           name: speech-to-text-test-job
         spec:
           template:
             spec:
               containers:
               - name: speech-to-text-test-container
                 image: HARBOR_INSTANCE_URL/HARBOR_PROJECT/speech-to-text-app:latest # Your image path
                 # Mount the API key from the secret into the container
                 # as an environment variable named GCP_API_KEY.
                 imagePullSecrets:
                 - name: SECRET
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
         
         kubectl get jobs/speech-to-text-test-job
         # It will show 0/1 completions, then 1/1 after it succeeds
         

  9. After the job has completed, you can view the output in the pod logs:
         
         kubectl logs -l job-name=speech-to-text-test-job
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
