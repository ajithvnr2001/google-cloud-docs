---
url: https://docs.cloud.google.com/tpu/docs/imagenet-setup/
title: Download, pre-process, and upload the ImageNet dataset \u00a0|\u00a0 Cloud TPU \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:26:26.393253+00:00
---

# Download, pre-process, and upload the ImageNet dataset  |  Cloud TPU  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/imagenet-setup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Download, pre-process, and upload the ImageNet dataset

This document describes how to download, pre-process, and upload the ImageNet dataset to use with Cloud TPU VM architecture.

ImageNet is an image database. The images in the database are organized into a hierarchy, with each node of the hierarchy depicted by hundreds and thousands of images.

The size of the ImageNet database means it can take a considerable amount of time to train a model. An alternative is to use a demonstration version of the dataset, referred to as _fake_imagenet_. This demonstration version lets you test the model, while reducing the storage and time requirements associated with using the full ImageNet database.

## Pre-process the full ImageNet dataset

The ImageNet dataset consists of three parts, training data, validation data, and image labels.

The training data contains 1000 categories and 1.2 million images, packaged for downloading. The validation and test data are not contained in the ImageNet training data (duplicates have been removed).

The validation and test data consists of 150,000 photographs, collected from [Flickr](https://www.flickr.com/) and other search engines, hand labeled with the presence or absence of 1000 object categories. The 1000 object categories contain both internal nodes and leaf nodes of ImageNet, but don't overlap with each other. A random subset of 50,000 of the images with labels has been released as validation data along with a list of the 1000 categories. The remaining images are used for evaluation and have been released without labels.

### Steps to pre-process the full ImageNet dataset

There are five steps to preparing the full ImageNet dataset for use by a machine learning model:

  1. Verify that you have space on the download target.
  2. Set up the target directories.
  3. Register on the ImageNet site and request download permission.
  4. Download the dataset to local disk or VM instance.

**Note:** Downloading the Imagenet dataset to a VM instance takes considerably longer than downloading to your local machine (approximately 40 hours versus 7 hours). If you download the dataset to your local machine, you must copy the files to a VM instance to pre-process them. You must then upload the files to Cloud Storage before using them to train your model. Copying the training and validation files from your local machine to the VM instance takes about 13 hours. The recommended approach is to download the dataset to a VM instance.
  5. Run the pre-processing and upload script.




### Verify space requirements

Whether you download the dataset to your local machine or to a VM instance, you need about 300 GiB of space available on the download target.

The default disk allocation for a TPU VM is 10 GB. Since the download to your TPU VM requires 300 GiB, if you are going to download to your TPU VM instance, you either need to add a [durable block storage volume](https://docs.cloud.google.com/tpu/docs/attach-durable-block-storage-compute) with additional space to complete the download or increase the size of the boot disk on the TPU. On a TPU VM, you can check your available storage with the `df -ha` command. For more information about resizing disks, see [Modify the size and provisioned performance of a Hyperdisk volume](https://docs.cloud.google.com/compute/docs/disks/modify-hyperdisks) and [Modify the size of a Persistent Disk volume](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk).

When adding durable block storage, be sure to make a note of the directory where you mounted the disk. For example: `/mnt/disks/mnt-dir`.

### Set up the target directories

On your local machine or VM instance, set up the directory structure to store the downloaded data.

  1. Change to a directory where you want to download the data. If you're using a persistent disk, replace DATASET_ROOT_DIR with the directory where your disk is mounted, for example, `/mnt/disks/mnt-dir`:
         
         cd DATASET_ROOT_DIR

  2. Create a directory, for example, `imagenet`, on your download target (local machine or TPU VM).
         
         mkdir imagenet
         

  3. Under this directory, create two sub directories: `train` and `validation`.
         
         mkdir imagenet/train
         mkdir imagenet/validation
         

  4. Export the `imagenet` directory as `IMAGENET_HOME`.
         
         export IMAGENET_HOME=DATASET_ROOT_DIR/imagenet
         sudo chown ${USER} ${IMAGENET_HOME}




### Register and request permission to download the dataset

Register on the [Imagenet website](http://image-net.org/). You cannot download the dataset until ImageNet confirms your registration and sends you a confirmation email. If you don't get the confirmation email within a couple of days, contact [ImageNet support](mailto:imagenet.help.desk@gmail.com) to see why your registration has not been confirmed. Once your registration is confirmed, you can download the dataset. The Cloud TPU tutorials that use the ImageNet dataset use the images from the ImageNet Large Scale Visual Recognition Challenge 2012 (ILSVRC2012).

### Download the ImageNet dataset

  1. From the [LSRVC 2012 download site](https://image-net.org/challenges/LSVRC/2012/2012-downloads.php), go to the Images section on the page and right-click "Training images (Task 1 & 2)". The URL to download the largest part of the training set. Save the URL.

Right-click "Training images (Task 3)" to get the URL for the second training set. Save the URL.

Right-click "Validation images (all tasks)" to get the URL for the validation dataset. Save the URL.

If you download the ImageNet files to your local machine, you need to copy the directories on your local machine to the corresponding `$IMAGENET_HOME` directory on your VM instance. Copying the ImageNet dataset from local host to your VM instance takes approximately 13 hours.

Before copying the ImageNet dataset to your TPU VM, you need to identify the name of your TPU VM instance. To do that, connect to your TPU VM using SSH. The VM instance name is shown in the command prompt following the `@` symbol.

Use the following command to copy the files under ~/imagenet on your local machine to `$IMAGENET_HOME` on your VM.
         
         gcloud compute scp --recurse $IMAGENET_HOME USERNAME@VM_INSTANCE_NAME:~/imagenet

  2. From `$IMAGENET_HOME`, download the "Training images (Task 1 & 2)" files using the saved URL.

The "Training images (Task 1 & 2)" file is the large training set. It is 138 GiB, and if you are downloading to your TPU VM using the Cloud Shell, the download takes approximately 40 hours. If the Cloud Shell loses its connection to the VM, you can prepend `nohup` to the command or use [screen](https://linuxize.com/post/how-to-use-linux-screen/).
         
         cd $IMAGENET_HOME
         nohup wget https://image-net.org/data/ILSVRC/2012/ILSVRC2012_img_train.tar

Replace the URL with the URL you previously saved for "Training images (Task 1 & 2)", as the URL might have changed.

  3. Extract the individual training directories into the `$IMAGENET_HOME/train` directory using the following command. The extraction takes between 1 - 3 hours.
         
         tar xf $IMAGENET_HOME/ILSVRC2012_img_train.tar -C $IMAGENET_HOME/train

Extract the individual training tar files located in the `$IMAGENET_HOME/train` directory, as shown in the following script:
         
         cd $IMAGENET_HOME/train
         for f in *.tar; do
             d=basename $f .tar
             mkdir $d
             tar xf $f -C $d
         done

Delete the tar files after you have extracted them to free up disk space.

  4. From `$IMAGENET_HOME`, download the "Training images (Task 3)" files using the saved URL.

The "Training images (Task 3)" file is 728 MB and takes just a few minutes to download, so you don't need to take precautions against losing the Cloud Shell connection.
         
         wget https://image-net.org/data/ILSVRC/2012/ILSVRC2012_img_train_t3.tar

Replace the URL with the URL you previously saved for "Training images (Task 3)", as the URL might have changed.

  5. Extract the individual training directories into the `$IMAGENET_HOME/train` directory using the following command.
         
         tar xf $IMAGENET_HOME/ILSVRC2012_img_train_t3.tar -C $IMAGENET_HOME/train

Extract the individual training tar files located in the `$IMAGENET_HOME/train` directory, as shown in the following script:
         
         cd ${IMAGENET_HOME}/train
         
         for f in *.tar; do
             d=`basename $f .tar`
             mkdir $d
             tar xf $f -C $d
         done

Delete the tar files after you have extracted them to free up disk space.

  6. From `$IMAGENET_HOME`, download the "Validation images (all tasks)" files using the saved URL.

When downloading the "Validation images (all tasks)" file, your Cloud Shell may disconnect. You can use `nohup` or [screen](https://linuxize.com/post/how-to-use-linux-screen/) to prevent Cloud Shell from disconnecting.
         
         wget https://image-net.org/data/ILSVRC/2012/ILSVRC2012_img_val.tar

Replace the URL with the URL you previously saved for "Validation images (all tasks)", as the URL might have changed.

This download takes about 30 minutes.

  7. Extract the individual validation files into the `$IMAGENET_HOME/validation` directory using the following command.
         
         tar xf $IMAGENET_HOME/ILSVRC2012_img_val.tar -C $IMAGENET_HOME/validation

If you downloaded the validation files to your local machine, you need to copy the `$IMAGENET_HOME/validation` directory on your local machine to the `$IMAGENET_HOME/validation` directory on your VM instance. This copy operation takes about 30 minutes.

  8. Download the labels file.
         
         wget -O $IMAGENET_HOME/synset_labels.txt \
         https://raw.githubusercontent.com/tensorflow/models/master/research/slim/datasets/imagenet_2012_validation_synset_labels.txt

If you downloaded the labels file to your local machine, you need to copy it to the `$IMAGENET_HOME` directory on your local machine to `$IMAGENET_HOME` on your VM instance. This copy operation takes a few seconds.

The training subdirectory names (for example, n03062245) are "WordNet IDs" (wnid). The [ImageNet API](https://image-net.org/download-attributes.php) shows the mapping of WordNet IDs to their associated validation labels in the `synset_labels.txt` file. A synset in this context is a visually similar group of images.




### Process the Imagenet dataset and, optionally, upload to Cloud Storage

  1. Download the `imagenet_to_gcs.py` script from GitHub:
         
         wget https://raw.githubusercontent.com/tensorflow/tpu/master/tools/datasets/imagenet_to_gcs.py

  2. If you are uploading the dataset to Cloud Storage:

     1. Use an existing bucket or create a new one by following the instructions in [Create buckets](https://docs.cloud.google.com/storage/docs/creating-buckets).

     2. Specify the storage bucket location to upload the ImageNet dataset:
            
            export STORAGE_BUCKET=gs://BUCKET_NAME

  3. If you are uploading the dataset to your local machine or VM, specify a data directory to hold the dataset:
         
         (vm)$ export DATA_DIR=$IMAGENET_HOME/DATASET_DIRECTORY

  4. Install the following libraries on your machine or in a virtual environment:
         
         pip3 install google-cloud-storage
         pip3 install tensorflow
         

  5. Run the script to pre-process the raw dataset as TFRecords and upload it to Cloud Storage using the following command:

**Note:** If you don't want to upload to Cloud Storage, specify `--nogcs_upload` as another parameter and leave off the `--project` and `--gcs_output_path` parameters.
         
         python3 imagenet_to_gcs.py \
           --project=$PROJECT \
           --gcs_output_path=$STORAGE_BUCKET  \
           --raw_data_dir=$IMAGENET_HOME \
           --local_scratch_dir=$IMAGENET_HOME/tf_records


**Note:** Downloading and preprocessing the data can take 10 or more hours, depending on your network and computer speed. Don't interrupt the script.

The script generates a set of directories (for both training and validation) of the form:
    
    
    ${DATA_DIR}/train-00000-of-01024
    ${DATA_DIR}/train-00001-of-01024
    ...
    ${DATA_DIR}/train-01023-of-01024
    

and
    
    
    ${DATA_DIR}/validation-00000-of-00128
    ${DATA_DIR}/validation-00001-of-00128
    ...
    ${DATA_DIR}/validation-00127-of-00128
    

After the data has been uploaded to your Cloud bucket, run your model and set `--data_dir=${DATA_DIR}`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
