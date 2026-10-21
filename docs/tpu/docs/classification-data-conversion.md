---
url: https://docs.cloud.google.com/tpu/docs/classification-data-conversion/
title: Convert an image classification dataset for use with Cloud TPU \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:26:16.439873+00:00
---

# Convert an image classification dataset for use with Cloud TPU  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/classification-data-conversion/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Convert an image classification dataset for use with Cloud TPU

This tutorial describes how to use the [image classification data converter sample](https://github.com/tensorflow/tpu/tree/master/tools/data_converter/image_classification) script to convert a raw image classification dataset into the [TFRecord](https://www.tensorflow.org/tutorials/load_data/tfrecord) format used to train Cloud TPU models.

[TFRecord](https://www.tensorflow.org/tutorials/load_data/tfrecord)s make reading large files from Cloud Storage more efficient than reading each image as an individual file. You can use TFRecord anywhere you are using a `tf.data.Dataset` pipeline.

See the following TensorFlow documents for more information on using TFRecord:

  * [TFRecord and tf.train.Example](https://www.tensorflow.org/tutorials/load_data/tfrecord)
  * [tf.data.Dataset](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)
  * [tf.data: Build TensorFlow input pipelines](https://www.tensorflow.org/guide/data)
  * [PyTorch TFRecord reader and writer](https://github.com/vahidk/tfrecord)



If you use the PyTorch or JAX framework, and are not using Cloud Storage for your dataset storage, you might not get the same advantage from TFRecords.

## Conversion overview

The [image classification folder within the data converter repository](https://github.com/tensorflow/tpu/tree/master/tools/data_converter) on GitHub contains the `converter` script, `image_classification_data.py`, and a sample implementation, `simple_example.py`, you can copy and modify to do your own data conversion.

The image classification data converter sample defines two classes, `ImageClassificationConfig` and `ImageClassificationBuilder`. These classes are defined in `tpu/tools/data_converter/image_classification_data.py`.

`ImageClassificationConfig` is an abstract base class. You subclass `ImageClassificationConfig` to define the configuration needed to instantiate an `ImageClassificationBuilder`.

`ImageClassificationBuilder` is a [TensorFlow dataset builder](https://www.tensorflow.org/datasets/api_docs/python/tfds/builder) for image classification datasets. It is a subclass of [`tdfs.core.GeneratorBasedBuilder`](https://www.tensorflow.org/datasets/api_docs/python/tfds/core/DatasetBuilder). It retrieves data examples from your dataset and converts them to TFRecords. The TFRecords are written to a path specified by the `data_dir` parameter to the `__init__` method of `ImageClassificationBuilder`.

In [simple_example.py](https://github.com/tensorflow/tpu/blob/master/tools/data_converter/image_classification/simple_example.py), `SimpleDatasetConfig` subclasses `ImageClassificationConfig`, implementing properties that define the supported modes, number of image classes, and an example generator that yields a dictionary containing image data and an image class for each example in the dataset.

The `main()` function creates a dataset of randomly generated image data and instantiates a `SimpleDatasetConfig` object specifying the number of classes and the path to the dataset on disk. Next, `main()` instantiates an `ImageClassificationBuilder` object, passing in the `SimpleDatasetConfig` instance. Finally, `main()` calls `download_and_prepare()`. When this method is called, the `ImageClassificationBuilder` instance uses the data example generator implemented by `SimpleDatasetConfig` to load each example and saves them to a series of TFRecord files.

For a more detailed explanation, see the [Classification Converter Notebook](https://github.com/tensorflow/tpu/blob/master/tools/colab/image_classification_converter.ipynb).

## Modify the data conversion sample to load your dataset

To convert your dataset into TFRecord format, subclass the `ImageClassificationConfig` class defining the following properties:

  * `num_labels`: returns the number of image classes
  * `supported_modes`: returns a list of modes supported by your dataset (for example: test, train, and validate)
  * `text_label_map`: returns a dictionary that models the mapping between a text class label and an integer class label (`SimpleDatasetConfig` does not use this property, because it does not require a mapping)
  * `download_path`: the path from which to download your dataset (`SimpleDatasetConfig` does not use this property, the `example_generator()` loads the data from disk)



Implement the `example_generator()` generator function. This method must yield a dictionary containing the image data and the image class name for each example. `ImageClassificationBuilder` uses the `example_generator()` function to retrieve each example and writes them to disk in TFRecord format.

## Run the data conversion sample

  1. Create a Cloud Storage bucket using the following command:

**Note:** In the following command, replace BUCKET_NAME with the name you want to assign to your bucket.
         
         gcloud storage buckets create gs://BUCKET_NAME --project=PROJECT_ID --location=LOCATION

Replace the following:

     * BUCKET_NAME: A name for the bucket.
     * PROJECT_ID: Your project ID.
     * LOCATION: The [location](https://docs.cloud.google.com/storage/docs/locations) where your bucket will be created. For example, `US-CENTRAL1`.
  2. Create a Cloud TPU using the [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create).
         
         $ gcloud compute instances create TPU_NAME \
             --machine-type=MACHINE_TYPE \
             --zone=ZONE \
             --image-family=IMAGE_FAMILY \
             --image-project=IMAGE_PROJECT \
             --maintenance-policy=TERMINATE

Replace the following:

     * TPU_NAME: A name for the TPU.
     * MACHINE_TYPE: The machine type to use for the TPU VM. For more information, see [TPU machine types](https://docs.cloud.google.com/compute/docs/tpus/tpu-machines#tpu_machine_types).
     * ZONE: The [zone](https://docs.cloud.google.com/tpu/docs/regions-zones) where the TPU will be created.
     * IMAGE_FAMILY: The image family of the OS image that you want to use. The latest non-deprecated image associated with that family will be used. To specify a specific image, replace the `--image-family` flag with the `--image` flag and set its value to a supported OS image. For a list of supported operating systems, see [TPU OS images](https://docs.cloud.google.com/tpu/docs/tpu-os-images).
     * IMAGE_PROJECT: The project ID of the OS image. For a list of project IDs associated with each public image, see [TPU OS images](https://docs.cloud.google.com/tpu/docs/tpu-os-images).
  3. Connect to the TPU using SSH:
         
         $ gcloud compute ssh TPU_NAME --zone=ZONE

When you connect to the TPU, your shell prompt changes from `username@projectname` to `username@vm-name`.

  4. Install required packages.
         
         (vm)$ pip3 install opencv-python-headless pillow
         (vm)$ pip3 install tensorflow-datasets

  5. Create the following environment variables used by the script.
         
         (vm)$ export STORAGE_BUCKET=gs://BUCKET_NAME
         (vm)$ export CONVERTED_DIR=$HOME/tfrecords
         (vm)$ export GENERATED_DATA=$HOME/data
         (vm)$ export GCS_CONVERTED=$STORAGE_BUCKET/data_converter/image_classification/tfrecords
         (vm)$ export GCS_RAW=$STORAGE_BUCKET/image_classification/raw
         (vm)$ export PYTHONPATH="$PYTHONPATH:/usr/share/tpu/models"

  6. Download the TensorFlow TPU repository.
         
         (vm)$ cd /usr/share/
         (vm)$ git clone https://github.com/tensorflow/tpu.git
         (vm)$ cd tpu/tools/data_converter




## Run the data converter on a fake dataset

The `simple_example.py` script is located in the `image_classification` folder of the data converter sample. Running the script with the following parameters generates a set of fake images and converts them into TFRecords.
    
    
    (vm)$ python3 image_classification/simple_example.py \
      --num_classes=1000 \
      --data_path=$GENERATED_DATA \
      --generate=True \
      --num_examples_per_class_low=10 \
      --num_examples_per_class_high=11 \
      --save_dir=$CONVERTED_DIR

## Run the data converter on one of our raw datasets

  1. Create an environment variable for the location of the raw data.
         
         (vm)$ export GCS_RAW=gs://cloud-tpu-test-datasets/data_converter/raw_image_classification

  2. Run the `simple_example.py` script.
         
         (vm)$ python3 image_classification/simple_example.py \
         --num_classes=1000 \
         --data_path=$GCS_RAW \
         --generate=False \
         --save_dir=$CONVERTED_DIR




The `simple_example.py` script takes the following parameters:

  * `num_classes` refers to the number of classes in the dataset. We're using 1000 here to match ImageNet format.
  * `generate` determines whether or not to generate the raw data.
  * `data_path` refers to the path where the data is generated if `generate=True` or the path where the raw data is stored if `generate=False`.
  * `num_examples_per_class_low` and `num_examples_per_class_high` determine how many examples per class to generate. The script generates a random number of examples in this range.
  * `save_dir` refers to where the saved TFRecords are saved. In order to train a model on Cloud TPU, the data must be stored on Cloud Storage. This can be on Cloud Storage or on the VM.



## Rename and move the TFRecords to Cloud Storage

The following example uses the converted data with the ResNet model.

  1. Rename the TFRecords to the same format as ImageNet TFRecords:
         
         (vm)$ cd $CONVERTED_DIR/image_classification_builder/Simple/0.1.0/
         (vm)$ sudo apt update
         (vm)$ sudo apt install rename
         
         (vm)$ rename -v 's/image_classification_builder-(\w+)\.tfrecord/$1/g' *

  2. Copy the TFRecords to Cloud Storage:
         
         (vm)$ gcloud storage cp train* $GCS_CONVERTED
         (vm)$ gcloud storage cp validation* $GCS_CONVERTED




## Clean up

  1. Disconnect from the Cloud TPU, if you have not already done so:
         
         (vm)$ exit

Your prompt should now be `user@projectname`, showing you are in the Cloud Shell.

  2. In your Cloud Shell, run the [`gcloud compute instances delete`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/delete) command to delete the TPU VM.
         
         $ gcloud compute instances delete TPU_NAME \
             --zone=ZONE

  3. Verify the VM has been deleted by running the [`gcloud compute instances list`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/list) command. The deletion might take several minutes.
         
         $ gcloud compute instances list --zone=ZONE

  4. Delete the bucket by running the following command, replacing BUCKET_NAME with the name of the bucket you created for this tutorial:
         
         $ gcloud storage rm gs://BUCKET_NAME --recursive




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
