---
url: https://docs.cloud.google.com/tpu/docs/profile-tpu-vm/
title: Profile your model on Cloud TPU VMs \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:36:17.932364+00:00
---

# Profile your model on Cloud TPU VMs  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/profile-tpu-vm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Profile your model on Cloud TPU VMs

Profiling is one of the main tools for you to optimize performance of your models on Cloud TPU. The core profiling tool is called XProf, which is available from the [OpenXLA/XProf](https://github.com/openxla/xprof) GitHub repository. XProf supports profiling of all XLA-based frameworks including JAX, PyTorch, and Tensorflow/Keras.

## Capturing profiles

In order to use XProf, you need to first capture a profile of your model. There are two ways to capture profiles:

  1. Programmatic capture
  2. On-demand capture (aka manual capture)



With programmatic capture, you need to annotate your model code in order to specify where in your code you want to capture profiles. Typically, you capture a profile for a few training steps, or profile a specific block of code within your model. There are different ways to capture traces in the different frameworks JAX, PyTorch, and TensorFlow - either API-based start or stop trace or context manager based. In higher-level frameworks such as MaxText, you can enable profile capture by just enabling a flag `profiler=xplane` when running MaxText.

You can use on-demand profile capture when you want to capture profiles in an ad hoc manner, or when you didn't enable programmatic profile capture. This can be helpful when you see a problem with your model metrics during the run and want to capture profiles at that instant for some period in order to diagnose the problem.

To enable on-demand profile capture, you still need to start the XProf server within your code. Enabling `profiler.start_server` will start an XProf server on your ML workload which listens for the on-demand capture trigger to start capturing profiles. You can trigger on-demand profile capture either through the Tensorboard UI or through CLI with the XProfiler tool.

You can find out how to enable programmatic and on-demand capture for different frameworks at:

  * [JAX](https://docs.jax.dev/en/latest/profiling.html)
  * [PyTorch](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/)
  * [Tensorflow](https://www.tensorflow.org/guide/profiler)



For both programmatic and on-demand profile capture, you need to specify the location where you want to store the captured profiles. You can choose to store the profiles in a directory on your TPU VM with a path similar to `/profiles/run-name` or use Cloud Storage with a path similar to `gs://bucket-name/run-name/`.

With the aforementioned paths, your profiles will be captured under:

`/profiles/run-name/plugins/profile/session1/`

or

`gs://bucket-name/run-name/plugins/profile/session1/`.

A session represents one capture of profiles during a run of your model. For example, if you capture profiles in a training run from steps 1-3 and later capture profiles from steps 8-10, then these are profiles for the same run, but the first capture from steps 1-3 will be `session1` and second capture from steps 8-10 will be `session2`.

The different sessions will be denoted with different date stamps under each run. You can capture profiles in different sessions either programmatically or on-demand or a mix of both. This is useful when you want to compare profiles from different parts of your model training. For example, comparing profiles from the beginning of training with profiles from the end of training.

## Visualizing profiles with TensorBoard

To view XProf profiles in Tensorboard, you need to install the tensorboard-plugin-profile plugin.

In order to visualize your captured profiles on Google Cloud, we recommend you use TensorBoard either on a TPU VM or use the XProfiler tool to host TensorBoard on a VM or GKE pod.

If you captured your profiles on the TPU VM, you can view the captured profiles using TensorBoard on that TPU VM.

To install XProf and TensorBoard on a TPU VM, you can run these commands:
    
    
    pip install tensorboard_plugin_profile tensorboard
    pip install xprof

To view the profiles captured with TensorBoard, run:
    
    
    $ tensorboard --logdir=profiles/run-name

or
    
    
    $ tensorboard --logdir=profiles

To load multiple profiles from multiple runs, point TensorBoard to the root directory that contains all your runs and profiles rather than to the subdirectory that has profiles of a specific run.

### Cloud-Diagnostics-XProf library for visualizing Tensorboard profiles on Google Cloud

The `cloud-diagnostics-xprof` (aka XProfiler Library) makes it easier to host TensorBoard and visualize profiles on Google Cloud. For more information, see the cloud-diagnostics-xprof GitHub repository.

The cloud-diagnostics-xprof repository provides the following improvements over running XProf and TensorBoard locally:

  * Setup and packaging of XProf and TensorBoard dependencies
  * Store your profiles in Cloud Storage which can be useful for long-term retention and post-run analysis (local profiles captured will be deleted after researcher finishes run)
  * Fast loading of large profiles and multiple profiles by provisioning TensorBoard on Compute Engine VM or GKE pod, with option to change machine type based on user needs for loading speed and cost
  * Create a link for sharing of profiles and collaboration with team members and Google engineers
  * Easier on-demand profiling of workloads on GKE and Compute Engine to choose any host running your workload to capture profiles



Before using the XProfiler library, you need to capture profiles for your workload code either programmatically or by starting the profile server, so you can do on-demand profile capture later.

To set up the XProfiler library, you need to have setup Google Cloud CLI and a Python virtual environment, and then all you need to do is run:
    
    
    pip install cloud-diagnostics-xprof

This will install all the necessary XProf and TensorBoard dependencies.

Next, to create a VM or GKE pod to host TensorBoard, run the following command:
    
    
    xprofiler create -z $ZONE -l $GCS_PATH

or
    
    
    xprofiler create --GKE -z $ZONE -l $GCS_PATH

Replace $ZONE with any zone and $GCS_PATH with the path to your profile traces. You can specify the root directory that contains all of your profile traces for multiple runs, or a specific set of profile traces for one run.

For example, if you capture profiles in the following directories:
    
    
    gs://bucket-name/run1/plugins/profile/session1/<profile.xplane.pb>
    gs://bucket-name/run1/plugins/profile/session2/<profile.xplane.pb>
    gs://bucket-name/run2/plugins/profile/session1/<profile.xplane.pb>
    

You can set the Cloud Storage path to the root directory (`gs://bucket-name`):
    
    
    xprofiler create -z $ZONE -l gs://bucket-name/
    

In the TensorBoard UI, you will see all the profiles for all the runs and sessions as `run1/session1`, `run1/session2`, `run2/session1`.

By default, `xprofiler create` will create a Compute Engine VM, specifically a c4-highmem-8 VM. You can change the machine type with the `-m` flag. If you want to create a TensorBoard instance on GKE pod instead of a Compute Engine VM, you can pass the `–GKE` flag to `xprofiler create`. Hosting a TensorBoard instance on a GKE pod may make it easier to manage TensorBoard along with the rest of your workload deployed on GKE.

The VM or GKE pod that hosts TensorBoard makes loading of large profiles and multiple profiles much faster on Google Cloud than locally hosted TensorBoard. Based on our benchmarking, you will see profiles of the order of 1 GB load within a few minutes for the first load using the default c4-highmem-8 VM. Further, you can choose the right machine type based on your performance and cost needs.

After you run `xprofiler create`, you will see output similar to the following:
    
    
    Instance for gs://<bucket> has been created.
    You can access it via the following:
    1. https://<id>-dot-us-<region>.notebooks.googleusercontent.com.
    2. xprofiler connect -z <zone> -l gs://bucket-name -m ssh
    Instance is hosted at xprof-97db0ee6-93f6-46d4-b4c4-6d024b34a99f VM.
    

The first option is a link that you can click to view your XProf profiles on a TensorBoard. This link enables sharing of profiles with your team and also with Google engineers helping with performance optimization on Google Cloud.

You control who has access to the link based on permissions set for the Cloud Storage bucket that stores your profile data. In case the link doesn't work for some reason, we also provide a way to connect to the TensorBoard instance using SSH in order to view your profiles using `xprofiler connect` command.

If you enabled the Cloud Profiler server in your workload code (which is required for both programmatic and on-demand captures) and want to perform on-demand profiling, you can do this in two ways:

a. Click the **Capture profile** button on TensorBoard. You can now choose any device host that your workload is running on to be profiled. We support on-demand capture for workloads running on GKE or Compute Engine.

b. Use the XProfiler capture command, providing information such as zone, Cloud Storage bucket, framework, host VM/pod names, and duration of capture in milliseconds. This is the same information as what you need to enter in the TensorBoard UI.

For more details on how to use `cloud-diagnostics-xprof` library, check out [this GitHub page](https://github.com/AI-Hypercomputer/cloud-diagnostics-xprof).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
