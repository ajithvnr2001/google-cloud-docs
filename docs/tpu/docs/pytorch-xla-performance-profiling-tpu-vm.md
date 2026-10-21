---
url: https://docs.cloud.google.com/tpu/docs/pytorch-xla-performance-profiling-tpu-vm/
title: Profile PyTorch XLA workloads \u00a0|\u00a0 Cloud TPU \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:54:20.987035+00:00
---

# Profile PyTorch XLA workloads  |  Cloud TPU  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/pytorch-xla-performance-profiling-tpu-vm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Profile PyTorch XLA workloads

**Deprecated:** This page applies to PyTorch/XLA, which is deprecated and replaced by [TorchTPU](https://docs.cloud.google.com/tpu/docs/pytorch-on-tpu). The PyTorch/XLA repo will be archived on November 15, 2026. Start new PyTorch workloads with TorchTPU and migrate existing PyTorch/XLA workloads to TorchTPU. 

Performance optimization is a crucial part of building efficient machine learning models. You can use the [XProf](https://openxla.org/xprof) profiling tool to measure the performance of your machine learning workloads. XProf lets you capture detailed traces of your model's execution on XLA devices. These traces can help you to identify performance bottlenecks, understand device utilization, and optimize your code.

This guide describes the process of programmatically capturing a trace from your PyTorch XLA script and visualizing using XProf and Tensorboard.

## Capture a trace

You can capture a trace by adding a few lines of code to your existing training script. The primary tool for capturing a trace is the `torch_xla.debug.profiler` module, which is typically imported with the alias `xp`.

### 1\. Start the profiler server

Before you can capture a trace, you need to start the profiler server. This server runs in the background of your script and collects the trace data. You can start it by calling `xp.start_server()` near the beginning of your main execution block.

### 2\. Define the trace duration

Wrap the code you want to profile within `xp.start_trace()` and `xp.stop_trace()` calls. The `start_trace` function takes a path to a directory where the trace files are saved.

It's common practice to wrap the main training loop to capture the most relevant operations.
    
    
    # The directory where the trace files are stored.
    log_dir = '/root/logs/'
    
    # Start tracing
    xp.start_trace(log_dir)
    
    # ... your training loop or other code to be profiled ...
    train_mnist()
    
    # Stop tracing
    xp.stop_trace()
    

### 3\. Add custom trace labels

By default, the traces captured are low-level Pytorch XLA functions and can be hard to navigate. You can add custom labels to specific sections of your code using the `xp.Trace()` context manager. These labels will appear as named blocks in the profiler's timeline view, making it much easier to identify specific operations like data preparation, the forward pass, or the optimizer step.

The following example shows how you can add context to different parts of a training step.
    
    
    def forward(self, x):
        # This entire block will be labeled 'forward' in the trace
        with xp.Trace('forward'):
            x = F.relu(F.max_pool2d(self.conv1(x), 2))
            x = F.relu(F.max_pool2d(self.conv2(x), 2))
            x = x.view(-1, 7*7*64)
            x = F.relu(self.fc1(x))
            x = self.fc2(x)
            return F.log_softmax(x, dim=1)
    
    # You can also nest context managers for more granular detail
    for batch_idx, (data, target) in enumerate(train_loader):
        with torch_xla.step():
            with xp.Trace('train_step_data_prep_and_forward'):
                optimizer.zero_grad()
                data, target = data.to(device), target.to(device)
                output = model(data)
    
            with xp.Trace('train_step_loss_and_backward'):
                loss = loss_fn(output, target)
                loss.backward()
    
            with xp.Trace('train_step_optimizer_step_host'):
                optimizer.step()
    

## Complete example

The following example shows how to capture a trace from a PyTorch XLA script, based on the [mnist_xla.py](https://gist.github.com/vfdev-5/70f695e462443685a0922e79ce0ee899#file-mnist_xla-py) file.
    
    
    import torch
    import torch.optim as optim
    from torchvision import datasets, transforms
    
    # PyTorch/XLA specific imports
    import torch_xla
    import torch_xla.core.xla_model as xm
    import torch_xla.debug.profiler as xp
    
    def train_mnist():
        # ... (model definition and data loading code) ...
        print("Starting training...")
        # ... (training loop as defined in the previous section) ...
        print("Training finished!")
    
    if __name__ == '__main__':
        # 1. Start the profiler server
        server = xp.start_server(9012)
    
        # 2. Start capturing the trace and define the output directory
        xp.start_trace('/root/logs/')
    
        # Run the training function that contains custom trace labels
        train_mnist()
    
        # 3. Stop the trace
        xp.stop_trace()
    

## Visualize the trace

When your script has finished, the trace files are saved in the directory you specified (for example, `/root/logs/`). You can visualize this trace using [XProf and TensorBoard](https://github.com/openxla/xprof).

  1. **Install TensorBoard.**
         
         pip install tensorboard_plugin_profile tensorboard

  2. **Launch TensorBoard.** Point TensorBoard to the log directory you used in `xp.start_trace()`:
         
         tensorboard --logdir /root/logs/

  3. **View the Profile.** Open the URL provided by TensorBoard in your web browser (usually `http://localhost:6006`). Navigate to the **PyTorch XLA - Profile** tab to view the interactive trace. You will be able to see the custom labels you created and analyze the execution time of different parts of your model.




If you use Google Cloud to run your workloads, we recommend the [cloud-diagnostics-xprof tool](https://github.com/AI-Hypercomputer/cloud-diagnostics-xprof). It provides a streamlined profile collection and viewing experience using VMs running Tensorboard and XProf.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
