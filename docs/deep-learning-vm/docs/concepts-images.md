---
url: https://docs.cloud.google.com/deep-learning-vm/docs/concepts-images/
title: Images, image families, and instances \u00a0|\u00a0 Deep Learning VM Images \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:40:50.576990+00:00
---

# Images, image families, and instances  |  Deep Learning VM Images  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deep-learning-vm/docs/concepts-images/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Deep Learning VM Images ](https://docs.cloud.google.com/deep-learning-vm/docs)
  * [ Guides ](https://docs.cloud.google.com/deep-learning-vm/docs/introduction)



Send feedback 

#  Images, image families, and instances Stay organized with collections  Save and categorize content based on your preferences. 

Deep Learning VM Images is a set of prepackaged virtual machine images with a deep learning framework that are ready to be run out of the box. The Deep Learning VM images take the hassle out of setting up an environment for training deep learning models by preconfiguring dependencies, preinstalling essential tools, and optimizing performance.

It is important to distinguish between _images_ , _image families_ , and _instances_.

## Image families

An image family is a set of images that are preconfigured for a specific purpose or using a specific architecture.

There are numerous Deep Learning VM image families. They are listed here, according to each one's main installed framework:

  * TensorFlow Enterprise family, with or without GPU
  * TensorFlow family, with or without GPU
  * PyTorch family, with or without GPU
  * R experimental family
  * A base, or "common" image family to which you can add your preferred framework, with or without GPU



[TensorFlow Enterprise](https://docs.cloud.google.com/tensorflow-enterprise/docs) is a distribution of [TensorFlow](https://www.tensorflow.org/) that has been optimized to run on Google Cloud and includes [Long Term Version Support](https://docs.cloud.google.com/tensorflow-enterprise/docs/overview#long_term_version_support).

If you know what framework you want to use and whether you want to enable one or more GPUs, you then choose whether to use the latest version of your framework or, if available, an older version. You can use Deep Learning VM images for some previous versions of frameworks. To find out more, see [Choosing an Image](https://docs.cloud.google.com/deep-learning-vm/docs/images).

## Images

An image is an individual virtual machine template. The Deep Learning VM images are preconfigured [public Compute Engine virtual machine images](https://docs.cloud.google.com/compute/docs/images#os-compute-support).

For more information about VM images, see the [Images](https://docs.cloud.google.com/compute/docs/images) conceptual topic in Compute Engine documentation.

For information about choosing a Deep Learning VM image, see [Choosing an Image](https://docs.cloud.google.com/deep-learning-vm/docs/images).

## Instances

An instance is a single virtual machine hosted on Google's infrastructure. A Deep Learning VM instance is based on one of the preconfigured Deep Learning VM images. You create an instance from an image using the Google Cloud console or the Google Cloud CLI.

For information about choosing a Deep Learning VM image, see [Choosing an Image](https://docs.cloud.google.com/deep-learning-vm/docs/images).

For information about creating instances of a Deep Learning VM image, see:

  * [Launching a Deep Learning VM Instance from the Command Line](https://docs.cloud.google.com/deep-learning-vm/docs/cli)

  * [Launching a Deep Learning VM Instance from the Cloud Marketplace](https://docs.cloud.google.com/deep-learning-vm/docs/cloud-marketplace)




For general information about creating instances in Compute Engine, see [Virtual Machine Instances](https://docs.cloud.google.com/compute/docs/instances).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
