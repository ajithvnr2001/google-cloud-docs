---
url: https://docs.cloud.google.com/tpu/docs/ml-diagnostics/maxtext/
title: Use ML Diagnostics with MaxText \u00a0|\u00a0 Cloud TPU \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:54:08.795233+00:00
---

# Use ML Diagnostics with MaxText  |  Cloud TPU  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/ml-diagnostics/maxtext/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Use ML Diagnostics with MaxText

[MaxText](https://maxtext.readthedocs.io/en/latest/index.html) is an open-source Large Language Model (LLM) library built to run on TPUs and GPUs for model training. ML Diagnostics SDK comes pre-integrated with MaxText. You can enable ML Diagnostics with MaxText by using the `managed-mldiagnostics` flag.

When enabled, you will be able to perform the following:

  * Create a managed `MachineLearning` run with all the MaxText configs.
  * Upload profiling traces, if the profiling is enabled by the `profiler="xplane"` flag.
  * Upload training metrics at a defined interval using the `log_period` flag.



Use the following flags when using ML Diagnostics with MaxText:
    
    
    managed_mldiagnostics: True  # Enable the managed diagnostics
    managed_mldiagnostics_run_group: GROUP_NAME  # Used to group multiple runs. (Optional)
    

To enable ML Diagnostics in MaxText, you can either change the configuration file of your run, or pass the flags from the command line. For example, pass the following flags with the `MaxText.train` command:
    
    
    python3 -m MaxText.train \
      src/MaxText/configs/base.yml \
      run_name="demo-mldiagnostics-run-2" \
      model_name="<your_chosen_model>" \
      base_output_directory=gs://<your_gcs_folder>/ \
      dataset_type=synthetic \
      steps=100 \
      log_period=10 \
      profiler=xplane \
      upload_all_profiler_results=True \
      managed_mldiagnostics=True \
      managed_mldiagnostics_run_group="demo-mldiagnostics-group"
    

In this example, setting the `upload_all_profiler_results=True` flag captures multi-host profiles from all hosts.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
