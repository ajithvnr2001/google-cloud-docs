---
url: https://docs.cloud.google.com/tpu/docs/coco-setup/
title: Downloading, preprocessing, and uploading the COCO dataset \u00a0|\u00a0 Cloud TPU \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:54:09.916722+00:00
---

# Downloading, preprocessing, and uploading the COCO dataset  |  Cloud TPU  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/coco-setup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Downloading, preprocessing, and uploading the COCO dataset

COCO is a large-scale object detection, segmentation, and captioning dataset. Machine learning models that use the COCO dataset include:

  * Mask-RCNN
  * Retinanet
  * ShapeMask



Before you can train a model on a Cloud TPU, you must prepare the training data.

This document describes how to prepare the [COCO](http://cocodataset.org) dataset for models that run on Cloud TPU. The COCO dataset can only be prepared after you have created a Compute Engine VM. The script used to prepare the data, `download_and_preprocess_coco.sh`, is installed on the VM and must be run on the VM.

After preparing the data by running the `download_and_preprocess_coco.sh` script, you can bring up the Cloud TPU and run the training.

To fully download and preprocess and upload the COCO dataset to a Cloud Storage bucket takes approximately 2 hours.

  1. In your [Cloud Shell](https://console.cloud.google.com/), configure `gcloud` with your project ID.
         
         export PROJECT_ID=project-id
         gcloud config set project ${PROJECT_ID}

  2. In your [Cloud Shell](https://console.cloud.google.com/), create a Cloud Storage bucket using the following command:

**Note:** In the following command, replace bucket-name with the name you want to assign to your bucket.
         
         gcloud storage buckets create gs://bucket-name --project=${PROJECT_ID} --location=us-central2

  3. Create a Compute Engine VM to download and preprocess the dataset. For more information, see [Create and start a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance).
         
         $ gcloud compute instances create vm-name \
             --zone=us-central2-b \
             --image-family=ubuntu-2204-lts \
             --image-project=ubuntu-os-cloud \
             --machine-type=n1-standard-16 \
             --boot-disk-size=300GB \
             --scopes=https://www.googleapis.com/auth/cloud-platform

  4. Connect to the Compute Engine VM using SSH:
         
         $ gcloud compute ssh vm-name --zone=us-central2-b

When you connect to the VM, your shell prompt changes from `username@projectname` to `username@vm-name`.

  5. Set up two variables, one for the storage bucket you created earlier and one for the directory that holds the training data (`DATA_DIR`) on the storage bucket.
         
         (vm)$ export STORAGE_BUCKET=gs://bucket-name
         
         (vm)$ export DATA_DIR=${STORAGE_BUCKET}/coco

  6. Install the packages needed to pre-process the data.
         
         (vm)$ sudo apt-get update && \
           sudo apt-get install python3-pip && \
           sudo apt-get install -y python3-tk && \
           pip3 install --user Cython matplotlib opencv-python-headless pyyaml Pillow numpy absl-py tensorflow && \
           pip3 install --user "git+https://github.com/cocodataset/cocoapi#egg=pycocotools&subdirectory=PythonAPI" && \
           pip3 install protobuf==3.19.0 tensorflow==2.11.0 numpy==1.26.4

  7. Run the `download_and_preprocess_coco.sh` script to convert the COCO dataset into a set of TFRecord files (`*.tfrecord`) that the training application expects.
         
         (vm)$ git clone https://github.com/tensorflow/tpu.git
         (vm)$ sudo -E bash tpu/tools/datasets/download_and_preprocess_coco.sh ./data/dir/coco

This installs the required libraries and then runs the preprocessing script. It outputs `*.tfrecord` files in your local data directory. The COCO download and conversion script takes approximately one hour to complete.

  8. Copy the data to your Cloud Storage bucket.

After you convert the data into the TFRecord format, copy the data from local storage to your Cloud Storage bucket using the gcloud CLI. You must also copy the annotation files. These files help validate the model's performance.
         
         (vm)$ gcloud storage cp ./data/dir/coco/*.tfrecord ${DATA_DIR}
         (vm)$ gcloud storage cp ./data/dir/coco/raw-data/annotations/*.json ${DATA_DIR}




## Clean up

Follow these steps to clean up your Compute Engine and Cloud Storage resources.

  1. Disconnect from the Compute Engine VM:
         
         (vm)$ exit

  2. Delete your Compute Engine VM:
         
         $ gcloud compute instances delete vm-name \
             --zone=us-central2-b

  3. Delete your Cloud Storage bucket and its contents:
         
         $ gcloud storage rm -r gs://bucket-name
         $ gcloud storage buckets delete gs://bucket-name




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
