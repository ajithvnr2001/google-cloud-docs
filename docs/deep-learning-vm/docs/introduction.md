---
url: https://docs.cloud.google.com/deep-learning-vm/docs/introduction/
title: Introduction to Deep Learning VM \u00a0|\u00a0 Deep Learning VM Images \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:33:16.840879+00:00
---

# Introduction to Deep Learning VM  |  Deep Learning VM Images  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deep-learning-vm/docs/introduction/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Deep Learning VM Images ](https://docs.cloud.google.com/deep-learning-vm/docs)
  * [ Guides ](https://docs.cloud.google.com/deep-learning-vm/docs/introduction)



Send feedback 

#  Introduction to Deep Learning VM Stay organized with collections  Save and categorize content based on your preferences. 

Deep Learning VM Images is a set of virtual machine images optimized for data science and machine learning tasks. All images come with key ML frameworks and tools pre-installed. You can use them out of the box on instances with GPUs to accelerate your data processing tasks.

Deep Learning VM images are available to support many combinations of framework and processor. There are currently images supporting [TensorFlow Enterprise](https://docs.cloud.google.com/tensorflow-enterprise/docs), TensorFlow, PyTorch, and generic high-performance computing, with versions for both CPU-only and GPU-enabled workflows.

To see a list of frameworks available, see [Choosing an image](https://docs.cloud.google.com/deep-learning-vm/docs/images).

## Pre-installed packages

Images are based on the Debian 11 and Ubuntu 22.04 operating systems, and these images can be configured to include the following:

  * Specific frameworks (for example, TensorFlow) and supporting packages.

  * Python 3.10 with the following packages:

    * numpy
    * scipy
    * matplotlib
    * pandas
    * nltk
    * pillow
    * scikit-image
    * opencv-python
    * scikit-learn
    * many more
  * JupyterLab notebook environments for quick prototyping

  * Nvidia packages with the latest Nvidia driver for GPU-enabled instances:

    * CUDA 11._x_ and 12._x_ (the version depends on the framework)
    * CuDNN 7._x_ and NCCL 2._x_ (the version depends on the CUDA version)



## Updates

Deep Learning VM images are updated regularly with bug fixes and package updates. Check the [release notes](https://docs.cloud.google.com/deep-learning-vm/docs/release-notes) for information about updates.

## Community support

Ask a question about Deep Learning VM on [Stack Overflow](https://stackoverflow.com/questions/tagged/google-dl-platform) or join the [google-dl-platform](https://groups.google.com/forum/#!forum/google-dl-platform) Google group to discuss Deep Learning VM.

[Learn more about getting support from the community](https://docs.cloud.google.com/deep-learning-vm/docs/getting-support#get_support_from_the_community).

## What's next

To get started using Deep Learning VM, create a new instance [using the Cloud Marketplace](https://docs.cloud.google.com/deep-learning-vm/docs/cloud-marketplace) or [using the command line](https://docs.cloud.google.com/deep-learning-vm/docs/cli).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
