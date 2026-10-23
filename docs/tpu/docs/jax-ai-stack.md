---
url: https://docs.cloud.google.com/tpu/docs/jax-ai-stack/
title: Building production AI on Cloud TPUs with JAX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:36:21.456456+00:00
---

# Building production AI on Cloud TPUs with JAX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/jax-ai-stack/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Building production AI on Cloud TPUs with JAX

The [JAX AI stack](https://jaxstack.ai/) extends the JAX numerical core with a collection of Google-backed composable libraries, evolving it into a robust, end-to-end, open-source platform for Machine Learning at extreme scales. As such, the JAX AI stack consists of a comprehensive and robust ecosystem that addresses the entire ML lifecycle:

  * **Industrial scale foundation:** The JAX AI stack is architected for massive scale, leveraging ML Pathways for orchestrating training across tens of thousands of chips and [Orbax](https://orbax.readthedocs.io/en/latest/index.html) for resilient, high-throughput asynchronous checkpointing, enabling production-grade training of state-of-the-art models.

  * **Complete, production ready toolkit:** JAX AI stack provides a comprehensive set of libraries for the entire development process: [Flax](https://flax.readthedocs.io/en/stable/) for flexible model authoring, [Optax](https://optax.readthedocs.io/en/latest/) for composable optimization strategies, and [Grain](https://google-grain.readthedocs.io/en/latest/) for the deterministic data pipelines essential for reproducible large-scale runs.

  * **Peak, specialized performance:** To achieve maximum hardware utilization, the JAX AI stack offers specialized libraries including [Tokamax](https://github.com/openxla/tokamax) for state-of-the-art custom kernels, [Qwix](https://qwix.readthedocs.io/en/latest/) for non-intrusive quantization that boosts training and inference speed, and XProf for deep, hardware-integrated performance profiling.

  * **Full path to production:** The JAX AI stack provides a seamless transition from research to deployment. This includes [MaxText](https://maxtext.readthedocs.io/en/latest/) as a scalable reference for foundation model training, [Tunix](https://tunix.readthedocs.io/en/latest/) for state-of-the-art reinforcement learning (RL) and alignment, and a unified inference solution with [vLLM-JAX](https://github.com/vllm-project/vllm-jax) and the JAX serving runtime.




The JAX AI stack philosophy is one of loosely coupled components, each of which does one thing well. Rather than being a monolithic ML framework, JAX itself is narrowly-scoped and focuses on efficient array operations and program transformations. The ecosystem is built upon this core framework to provide a wide array of functionalities, related to both the training of ML models and other types of workloads such as scientific computing.

This system of loosely coupled components lets you select and combine libraries in the best way to suit your requirements. From a software engineering perspective, this architecture also lets you update functionality that would traditionally be considered core framework components (for example, data pipelines and checkpointing) iteratively without the risk of destabilizing the core framework or being caught up in release cycles. Given that most functionality is implemented in libraries rather than changes to a monolithic framework, this makes the core numerics library more durable and adaptable to future shifts in the technology landscape.

The following sections provide a technical overview of the JAX AI stack, its key features, the design decisions behind them, and how they combine to build a durable platform for modern ML workloads.

**The JAX AI stack and other ecosystem components**

**Component** | **Function / Description**  
---|---  
**JAX AI stack core and components** 1  
[JAX](https://docs.jax.dev/en/latest/) | Accelerator-oriented array computation and program transformation (JIT, grad, vmap, pmap).  
[Flax](https://flax.readthedocs.io/en/stable/) | Flexible neural network authoring library for intuitive model creation and modification.  
[Optax](https://optax.readthedocs.io/en/latest/) | A library of composable gradient processing and optimization transformations.  
[Orbax](https://orbax.readthedocs.io/en/latest/) | "Any-scale" distributed checkpointing library for hero-scale training resilience.  
[Grain](https://google-grain.readthedocs.io/en/latest/) | A scalable, deterministic, and checkpointable input data pipeline library.  
**JAX AI stack - Infrastructure**  
[XLA](https://openxla.org/) | Open-source machine learning compiler for TPUs, CPUs, and GPUs.  
[Pathways](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/pathways-intro) | Distributed runtime for orchestrating computation across tens of thousands of chips.  
**JAX AI stack - Adv. Development**  
[Pallas](https://docs.jax.dev/en/latest/pallas/index.html) | A JAX extension for writing low-level, high-performance custom kernels implemented in Python.  
[Tokamax](https://github.com/openxla/tokamax) | A curated library of state-of-the-art, high-performance custom kernels (for example, Attention).  
[Qwix](https://qwix.readthedocs.io/en/latest/) | A comprehensive, non-intrusive library for quantization (PTQ, QAT, QLoRA).  
**JAX AI stack - Application**  
[MaxText / MaxDiffusion](https://maxtext.readthedocs.io/en/latest/) | Flagship, scalable reference frameworks for training foundation models (for example, LLM and Diffusion).  
[Tunix](https://tunix.readthedocs.io/en/latest/index.html) | A framework for state-of-the-art post-training and alignment (RLHF, DPO).  
[vLLM-JAX](https://github.com/vllm-project/vllm-jax) | A high-performance LLM inference solution using built-in integration of the vLLM framework.  
[XProf](https://openxla.org/xprof) | A deep, hardware-integrated profiler for system-wide performance analysis.  
  
* * *

1Included in the `jax-ai-stack` Python package.

**Figure 1: The JAX AI stack and ecosystem components**

![JAX AI stack](https://docs.cloud.google.com/static/tpu/docs/images/JAX_ecosystem.png)

## The architectural imperative: performance beyond frameworks

As model architectures converge — for example, on multimodal Mixture-of-Experts (MoE) Transformers — the pursuit of peak performance is leading to the emergence of _Megakernels_. A Megakernel is effectively the entire forward pass (or a large portion) of one specific model, hand-coded using a lower-level API like the CUDA SDK on NVIDIA GPUs. This approach achieves maximum hardware utilization by aggressively overlapping compute, memory, and communication. Recent work from the research community has demonstrated that this approach can yield significant throughput gains, over 22% in some cases, for inference on GPUs. This trend is not limited to inference; evidence suggests that some large-scale training efforts have involved low-level hardware control to achieve substantial efficiency gains.

If this trend accelerates, all high-level frameworks as they exist today risk becoming less relevant, as low-level access to the hardware is what ultimately matters for performance on mature, stable architectures. This presents a challenge for all modern ML stacks: how to provide expert-level hardware control without sacrificing the productivity and flexibility of a high-level framework.

For TPUs to provide a clear path to this level of performance, the ecosystem must expose an API layer that is closer to the hardware, enabling the development of these highly specialized kernels. The JAX stack is designed to solve this by offering a continuum of abstraction (See Figure 2), from the automated, high-level optimizations of the XLA compiler to the fine-grained, manual control of the Pallas kernel-authoring library.

**Figure 2: The JAX continuum of abstraction**

![JAX continuum of abstraction](https://docs.cloud.google.com/static/tpu/docs/images/programming_TPUS.png)

## The core JAX AI stack

The core JAX AI Stack consists of five key libraries that provide the foundation for model development:

  * [JAX](https://docs.jax.dev/en/latest/)
  * [Flax](https://flax.readthedocs.io/en/stable/)
  * [Optax](https://optax.readthedocs.io/en/latest/)
  * [Orbax](https://orbax.readthedocs.io/en/latest/)
  * [Grain](https://google-grain.readthedocs.io/en/latest/).



### JAX: A foundation for composable, high performance program transformation

[JAX](https://docs.jax.dev/en/latest/) is a Python library for accelerator-oriented array computation and program transformation, designed for high-performance numerical computing and large-scale Machine Learning. With its functional programming model and NumPy-like API, JAX provides a solid foundation for higher-level libraries.

With its compiler-first design, JAX inherently promotes scalability by leveraging [XLA](https://openxla.org/xla) (see the XLA section) for aggressive, whole-program analysis, optimization, and hardware targeting. The JAX emphasis on functional programming (for example, pure functions) makes its core program transformations more tractable and, crucially, composable.

These core transformations can be mixed and matched to achieve high performance and scaling of workloads across model size, cluster size, and hardware types:

  * **jit** : Just-in-time compilation of Python functions into optimized, fused XLA executables.
  * **grad** : Automatic differentiation, supporting forward- and reverse-mode, as well as higher-order derivatives.
  * **vmap** : Automatic vectorization, enabling seamless batching and data parallelism without modifying function logic.
  * **pmap / shard_map** : Automatic parallelization across multiple devices (for example, TPU cores), forming the basis for distributed training.



The seamless integration with XLA's GSPMD (General-purpose SPMD) model allows JAX to automatically parallelize computations across large TPU Pods with minimal code changes. In most cases, scaling only requires high-level sharding annotations.

### Flax: Flexible neural network authoring

[Flax](https://flax.readthedocs.io/en/stable/) simplifies the creation, debugging, and analysis of neural networks in JAX by providing an intuitive, object-oriented approach to model building. While JAX's functional API is powerful, offers a more familiar layer-based abstraction for developers accustomed to frameworks like PyTorch, without any performance penalty.

This design simplifies modifying or combining trained model components. Techniques such as LoRA and quantization require manipulable model definitions, which Flax's `NNX` API provides through a Pythonic interface. `NNX` encapsulates model state, reducing user cognitive load, and allows for programmatic traversal and modification of the model hierarchy.

#### Key strengths:

  * Intuitive Object-Oriented API: Simplifies model construction and enables advanced use cases like submodule replacement and partial initialization.
  * Consistent with Core JAX: Flax provides lifted transformations that are fully compatible with JAX's functional paradigm, offering the full performance of JAX with enhanced developer friendliness.



### Optax: Composable gradient processing and optimization strategies

[Optax](https://optax.readthedocs.io/en/latest/index.html) is a gradient processing and optimization library for JAX. It is designed to provide model builders with building blocks that can be recombined in custom ways in order to train deep learning models amongst other applications. It builds on the capabilities of the core JAX library to provide a well tested high performance library of loss and optimizer functions and associated techniques that can be used to train ML models.

#### Motivation

The calculation and minimization of losses is at the core of what enables the training of ML models. With its support for automatic differentiation the core JAX library provides the numeric capabilities to train models, but it does not provide standard implementations of popular optimizers (for example, `RMSProp` or `Adam`) or losses (for example, `CrossEntropy` or `MSE`). While you could implement these functions (and some advanced developers will choose to do so), a bug in an optimizer implementation would introduce hard to diagnose model quality issues. Rather than having the user implement such critical pieces, Optax provides implementations of these algorithms that are tested for correctness and performance.

The field of optimization theory lies squarely in the realm of research, however its central role in training also makes it an indispensable part of training production ML models. A library that serves this role needs to be both flexible enough to accommodate rapid research iterations and also robust and performant enough to be dependable for production model training. It should also provide well tested implementations of state of the art algorithms which match the standard equations. The Optax library, through its modular composable architecture and emphasis on correct readable code is designed to achieve this.

#### Design

[Optax](https://optax.readthedocs.io/en/latest/) is designed to both enhance research velocity and the transition from research to production by providing readable, well-tested, and efficient implementations of core algorithms. Optax has uses beyond the context of deep learning, however in this context it can be viewed as a collection of well known loss functions, optimization algorithms and gradient transformations implemented in a pure functional fashion in line with the JAX philosophy. The collection of well known [losses](https://optax.readthedocs.io/en/latest/api/losses.html) and [optimizers](https://optax.readthedocs.io/en/latest/api/optimizers.html) enable users to get started with ease and confidence.

The modular approach taken by Optax lets you [chain multiple optimizers](https://optax.readthedocs.io/en/latest/api/combining_optimizers.html#chain) together followed by other common [transformations](https://optax.readthedocs.io/en/latest/api/transformations.html) (for example, gradient clipping) and [wrap](https://optax.readthedocs.io/en/latest/api/optimizer_wrappers.html) them using common techniques like MultiStep or Lookahead to achieve powerful optimization strategies with a few lines of code. The flexible interface lets you research new optimization algorithms and lets you use powerful second order optimization techniques like shampoo or muon.
    
    
    # Optax implementation of a RMSProp optimizer with a custom learning rate
    #  schedule, gradient clipping and gradient accumulation.
    optimizer = optax.chain(
      optax.clip_by_global_norm(GRADIENT_CLIP_VALUE),
      optax.rmsprop(learning_rate=optax.cosine_decay_schedule(init_value=lr,decay_steps=decay)),
      optax.apply_every(k=ACCUMULATION_STEPS)
    )
    
    # The same thing, in PyTorch
    optimizer = optim.RMSprop(model_params, lr=LEARNING_RATE)
    scheduler = optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=TOTAL_STEPS)
    for i, (inputs, targets) in enumerate(data_loader):
        # ... Training loop body ...
        if (i + 1) % ACCUMULATION_STEPS == 0:
            torch.nn.utils.clip_grad_norm_(model.parameters(), GRADIENT_CLIP_VALUE)
            optimizer.step()
            scheduler.step()
     optimizer.zero_grad()
    

The previous code snippet shows how to set up an optimizer with a custom learning rate, gradient clipping and gradient accumulation.

#### Key strengths

  * **Robust Library:** Provides a comprehensive library of losses, optimizers, and algorithms with a focus on correctness and readability.
  * **Modular Chainable Transformations:** This flexible API lets you craft powerful, complex optimization strategies declaratively, without modifying the training loop.
  * **Functional and Scalable:** The pure functional implementations integrate seamlessly with JAX's parallelization mechanisms (for example, pmap), letting you use the same code to scale from a single host to large clusters.



### Orbax / TensorStore - Large scale distributed checkpointing

[Orbax](https://orbax.readthedocs.io/en/latest/) is a checkpointing library for JAX designed for any scale, from single-device to large-scale distributed training. It aims to unify fragmented checkpointing implementations and deliver critical performance features, such as asynchronous and multi-tier checkpointing, to a wider audience. Orbax enables the resilience required for massive training jobs and provides a flexible format for publishing checkpoints.

Unlike generalized checkpoint and restore systems that snapshot the entire system state, ML checkpointing with Orbax selectively persists only the information essential for resuming training model weights, optimizer state, and data loader state. This targeted approach minimizes accelerator downtime. Orbax achieves this by overlapping I/O operations with computation, a critical feature for large workloads. The time accelerators are idle is reduced to the duration of the device to host data transfer, which can be further overlapped with the next training step, making checkpointing nearly free from a performance perspective.

At its core, Orbax uses [TensorStore](https://google.github.io/tensorstore/) for efficient, parallel reading and writing of array data. The Orbax API abstracts this complexity, offering a user-friendly interface for handling [PyTrees](https://docs.jax.dev/en/latest/pytrees.html), which are the standard representation of models in JAX.

#### Key strengths:

  * [Widespread adoption](https://orbax.readthedocs.io/en/latest/guides/checkpoint/async_checkpointing.html): With millions of monthly downloads, Orbax serves as a common medium for sharing ML artifacts.
  * Simplifies complexities: Orbax abstracts away the complexities of distributed checkpointing, including asynchronous saving, atomicity, and file system details.
  * Flexible: While offering APIs for common use cases, Orbax lets you customize your workflow to handle specialized requirements.
  * Performant and Scalable: Features like asynchronous checkpointing, an efficient storage format ([OCDBT](https://orbax.readthedocs.io/en/latest/guides/checkpoint/optimized_checkpointing.html)), and intelligent data loading strategies ensure that Orbax scales to training runs involving tens of thousands of nodes.



### Grain: Deterministic and scalable input data pipelines

[Grain](https://google-grain.readthedocs.io/en/latest/) is a Python library for reading and processing data for training and evaluating JAX models. It is flexible, fast and deterministic and supports advanced features like checkpointing which are essential to successfully training large workloads. It supports popular data formats and storage backends and also provides a flexible API to extend support to user specific formats and backends that are not natively supported. While Grain is primarily designed to work with JAX, it is framework independent, does not require JAX to run and can be used with other frameworks as well.

#### Motivation

Data pipelines form a critical part of the training infrastructure - they need to be flexible so that common transformations can be expressed efficiently, and performant enough that they are able to keep the accelerators busy at all times. They also need to be able to accommodate multiple storage formats and backends. Due to their higher step times, training large models at scale poses additional requirements on the data pipeline beyond those that are required by regular training workloads, primarily focused around determinism and reproducibility2. The Grain library is designed with a flexible architecture that addresses these needs.

* * *

2In the Section 5.1 of the [PaLM paper](https://dl.acm.org/doi/10.5555/3648699.3648939), the authors note that they observed very large loss spikes despite having gradient clipping enabled. The solution was to remove the offending data batches and restart training from a checkpoint before the loss spike. This is only possible with a fully deterministic and reproducible training setup.

#### Design

At the highest level, there are two ways to structure an input pipeline, as a separate cluster of data workers or by co-locating the data workers on the hosts that drive the accelerators. Grain chooses the latter for a variety of reasons.

Accelerators are combined with powerful hosts that typically sit idle during training steps, which makes it a natural choice to run the input data pipeline. There are additional advantages to this implementation - it simplifies your view of data sharding by providing a consistent view of sharding across input and compute. It could be argued that putting the data worker on the accelerator host risks saturating the host CPU, however this does not preclude offloading compute intensive transformations to another cluster using RPCs3.

On the API front, with a pure Python implementation that supports multiple processes and a flexible API, Grain lets you implement arbitrarily complex data transformations by composing pipeline stages together based on well understood [transformation](https://google-grain.readthedocs.io/en/latest/data_loader/transformations.html) paradigms.

Out of the box, Grain supports efficient random access data formats like `ArrayRecord` and `Bagz` alongside other popular data formats such as [Parquet](https://parquet.apache.org/) and `TFDS`. Grain includes support for reading from local file systems as well as reading from Cloud Storage by default. Along with supporting popular storage formats and backends, a clean abstraction to the storage layer lets you add support for or wrap your existing data sources to be compatible with the Grain library.

* * *

3This is how multimodal data pipelines need to operate - image and audio tokenizers, for example, are models themselves which run in their own clusters on their own accelerators and the input pipelines would make RPC calls to convert data examples into streams of tokens.

#### Key strengths

  * **Deterministic data feeding:** Colocating the data worker with the accelerator and coupling it with a stable global shuffle and [checkpointable iterators](https://google-grain.readthedocs.io/en/latest/tutorials/data_loader_tutorial.html#checkpointing) allows the model state and data pipeline state to be checkpointed together in a consistent snapshot using Orbax, enhancing the determinism of the training process.
  * **Flexible APIs to enable powerful data transformations:** A flexible, pure Python [transformations](https://google-grain.readthedocs.io/en/latest/data_loader/transformations.html) API lets you perform extensive data transformations within the input processing pipeline.
  * **Extensible support for multiple formats and backends:** An extensible [data sources](https://google-grain.readthedocs.io/en/latest/tutorials/data_sources/index.html) API supports popular storage formats and backends and lets you add support for new formats and backends.
  * **Powerful debugging interface:** Data pipeline [visualization tools](https://google-grain.readthedocs.io/en/latest/tutorials/dataset_debugging_tutorial.html) and a debug mode lets you introspect, debug and optimize the performance of your data pipelines.



## The extended JAX AI stack

Beyond the core stack, a rich ecosystem of specialized libraries provides the infrastructure, advanced tools, and application-layer solutions needed for end-to-end ML development.

### Foundational infrastructure: compilers and runtimes

#### XLA: The hardware independent, compiler centric engine

##### Motivation

XLA or Accelerated Linear Algebra is Google's domain specific compiler, which is well integrated into JAX and supports TPU, CPU and GPU hardware devices. XLA was designed to be a hardware independent code generator targeting TPUs, GPUs, and CPUs.

The XLA compiler's compiler-first design is a fundamental architectural choice that creates a durable advantage in a rapidly evolving research landscape. In contrast, the prevailing kernel-centric approach in other ecosystems relies on hand-optimized libraries for performance. While this is highly effective for stable, well-established model architectures, it creates a bottleneck for innovation. When new research introduces novel architectures, the ecosystem must wait for new kernels to be written and optimized. Our compiler-centric design, however, can often generalize to new patterns, providing a high-performance path for cutting-edge research from day one.

##### Design

XLA works by Just-In-Time (JIT) compiling the computation graphs that JAX generates during its tracing process (for example, when a function is decorated with `@jax.jit`).

This compilation follows a multi-stage pipeline:

  1. JAX Computation Graph
  2. High-Level Optimizer (HLO)
  3. Low-Level Optimizer (LLO)
  4. Hardware Code


  * **From JAX Graph to HLO** : The JAX computation graph is converted into XLA's HLO representation. At this high level, powerful, hardware-agnostic optimizations like operator fusion and efficient memory management are applied. The **StableHLO** dialect serves as a durable, versioned interface for this stage.
  * **From HLO to LLO:** After high-level optimizations, hardware-specific backends take over, lowering the HLO representation into a machine-oriented LLO.
  * **From LLO to Hardware Code:** The LLO is finally compiled into highly-efficient machine code. For TPUs, this code is bundled as **Very Long Instruction Word (VLIW)** packets that are sent directly to the hardware.



For scaling, XLA's design is built around parallelism. It employs algorithms to maximally use the matrix multiplication units (MXUs) on a chip. Between chips, XLA uses **SPMD (Single Program Multiple Data)** , a compiler-based parallelization technique that uses a single program across all devices. This powerful model is exposed through JAX APIs, letting you manage data, model, or pipeline parallelism with high-level sharding annotations.

For more complex parallelism patterns, **Multiple Program Multiple Data (MPMD)** is also possible, and libraries like `PartIR:MPMD` allow JAX users to provide MPMD annotations as well.

##### Key strengths

  * **Compilation** : just in time compilation of the computation graph enables optimizations to memory layout, buffer allocation, and memory management. Alternatives such as kernel based methodologies put that burden on the developer. In most cases, XLA can achieve excellent performance without compromising developer velocity.
  * **Parallelism:** XLA implements several forms of parallelism with SPMD, and this is exposed at the JAX level. This lets you express sharding strategies, allowing experimentation and scalability of models across thousands of chips.



#### Pathways: A unified runtime for massive scale distributed computation

[Pathways](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/pathways-intro) offers abstractions for distributed training and inference with built in fault tolerance and recovery, allowing ML researchers to code as if they are using a single, powerful machine.

##### Motivation

To be able to train and deploy large models, hundreds to thousands of chips are necessary. These chips are spread across numerous racks and host machines. A training job is a large-scale synchronous program that requires all of these chips, and their respective hosts to be working in tandem on XLA computations that have been parallelized (sharded). In the case of large language models, which may need more than tens of thousands of chips, this service must be capable of spanning multiple Pods across a data center fabric in addition to using interchip interconnect (ICI) and on-chip interconnect (OCI) fabrics within a Pod.

##### Design

ML Pathways is the system we use for coordinating distributed computations across hosts and TPU chips. It is designed for scalability and efficiency across hundreds of thousands of accelerators. For large-scale training, it provides a single Python client for multiple Pod jobs, [Megascale XLA](https://openxla.org/xprof/megascale_stats) integration, compilation service, and remote Python. It also supports cross-slice parallelism and preemption tolerance, enabling automatic recovery from resource preemptions.

Pathways incorporates optimized cross host collectives which enable XLA computation graphs to extend beyond a single TPU Pod. It expands XLA's support for data, model, and pipeline parallelism to work across TPU slice boundaries using the data center network (DCN) by means of integrating a distributed runtime that manages DCN communication with XLA communication primitives.

##### Key strengths

The single-controller architecture, integrated with JAX, is a key abstraction. It lets researchers explore various sharding and parallelism strategies for training and deployment while scaling to tens of thousands of chips with ease.

### Advanced development: performance, data, and efficiency

#### Pallas: Writing high performance custom kernels in JAX

While JAX is compiler first, there are situations where you might want fine grained control over the hardware to achieve maximum performance. Pallas is an extension to JAX that enables writing custom kernels for GPUs and TPUs. It aims to provide precise control over the generated code, combined with the high-level ergonomics of JAX tracing and the `jax.numpy` API.

Pallas exposes a grid-based parallelism model where a user-defined kernel function is launched across a multi-dimensional grid of parallel work-groups. It enables explicit management of the memory hierarchy by letting you define how tensors are tiled and transferred between slower, larger memory (for example, HBM) and faster, smaller on-chip memory (for example, VMEM on TPU, Shared Memory on GPU), using index maps to associate grid locations with specific data blocks. Pallas can lower the same kernel definition to execute efficiently on both Google's TPUs and various GPUs by compiling kernels into an intermediate representation suitable for the target architecture – Mosaic for TPUs, or utilizing technologies like Triton for GPUs. With Pallas, you can write high performance kernels that specialize blocks like attention to achieve the best model performance on the target hardware without needing to rely on vendor specific toolkits.

#### Tokamax: A curated library of state of the art kernels

If Pallas is a _tool_ for authoring kernels, [Tokamax](https://github.com/openxla/tokamax) is a _library_ of state-of-the-art custom accelerator kernels supporting both TPUs and GPUs. Tokamax is built on top of JAX and Pallas and lets you use the full power of your hardware. It also provides tooling for you to build and autotune custom kernels.

##### Motivation

JAX, with its roots in XLA, is a compiler-first framework, however, a narrow set of cases exists where you may need to take direct control of the hardware to achieve maximum performance4. Custom kernels are critical to getting the best performance from expensive ML accelerator resources such as TPUs and GPUs. While they are widely employed to enable performant execution of key operators such as Attention, implementing them requires a deep understanding of both the model and the target hardware architecture. Tokamax provides one authoritative source of curated, well-tested, high-performance kernels, in conjunction with robust shared infrastructure for their development, maintenance, and lifecycle management. Such a library can also act as a reference implementation for you to build on and customize as necessary. This lets you focus on your modeling efforts without needing to worry about infrastructure.

* * *

4This is a well established paradigm and has precedent in the CPU world, where compiled code forms the bulk of the program with developers dropping down to intrinsics or inline assembly to optimize performance critical sections.

##### Design

For any given kernel, Tokamax provides a common API that may be backed by multiple implementations. For example, TPU kernels may be implemented either by standard XLA lowering, or explicitly with Pallas/Mosaic-TPU. GPU kernels may be implemented by standard XLA lowering, with Mosaic-GPU, or Triton. By default, the Tokamax API picks the best-known implementation for a given configuration, determined by cached results from periodic autotuning and benchmarking runs, though you may choose specific implementations if needed. New implementations may be added over time to better exploit specific features in new hardware generations for even better performance.

A key component of the Tokamax library, beyond the kernels themselves, is the supporting infrastructure that lets you write custom kernels. For example, the autotuning infrastructure lets you define a set of configurable parameters (for example, tile sizes) that Tokamax can perform an exhaustive sweep on, to determine and cache the best possible tuned settings. Nightly regressions protect you from unexpected performance and numerics issues caused by changes to underlying compiler infrastructure or other dependencies.

##### Key strengths

  * **Seamless developer experience:** A unified, curated, library provides known good, high performance implementations of key kernels, with clear expressions of supported hardware generations and expected performance, both programmatically and in documentation. This minimizes fragmentation and churn.
  * **Flexibility and lifecycle management:** You may choose different implementations, even changing them over time if appropriate. For example, if the XLA compiler enhances support for certain operations no longer requires custom kernels, there is a path to deprecation and migration.
  * **Extensibility:** You can implement your own kernels, while leveraging well supported shared infrastructure, allowing you to focus on value added capabilities and optimizations. Clearly authored standard implementations serve as a starting point for users to learn from and extend.



#### Qwix: Non-intrusive, comprehensive quantization

[Qwix](https://qwix.readthedocs.io/en/latest/) is a comprehensive quantization library for the JAX AI stack, supporting both LLMs and other model types across all stages, including training (Quantization Aware Training (QAT), Quantization Technique (QT), Quantized Low-Rank Adaptation (QLoRA)) and inference Post Training Quantization (PTQ), targeting both XLA and on-device runtimes.

##### Motivation

Existing quantization libraries, particularly in the PyTorch ecosystem, often serve limited purposes (for example, only PTQ or only QLoRA). This fragmented landscape forces you to switch tools, impeding consistent code usage and precise numerical matching between training and inference. Furthermore, many solutions require substantial model modifications, tightly coupling the model logic to the quantization logic.

##### Design

Qwix's design philosophy emphasizes a comprehensive solution and, critically, **non-intrusive model integration**. It is architected with a hierarchical, extensible design built on reusable functional APIs.

This non-intrusive integration is achieved through a meticulously designed **interception mechanism** that redirects JAX functions to their quantized counterparts. This lets you integrate your models without any modifications, completely decoupling quantization code from model definitions.

The following example demonstrates applying `w4a4` (a 4-bit weight, 4-bit activation) quantization to an LLM's MLP layers and `w8` (a 8-bit weight) quantization to the embedder. To change the quantization recipe, you only need to update the rules list.
    
    
    fp_model = ModelWithoutQuantization(...)
    rules = [
        qwix.QuantizationRule(
            module_path=r'embedder',
            weight_qtype='int8',
        ),
        qwix.QuantizationRule(
            module_path=r'layers_\d+/mlp',
            weight_qtype='int4',
            act_qtype='int4',
            tile_size=128,
            weight_calibration_method='rms,7',
        ),
    ]
    quantized_model = qwix.quantize_model(fp_model, qwix.PtqProvider(rules))
    

##### Key strengths

  * **Comprehensive Solution:** Qwix is broadly applicable across numerous quantization scenarios, ensuring consistent code usage between training and inference.
  * **Non-Intrusive Model Integration:** As the example shows, you can integrate models with a single line of code. This lets you use hyperparameters over many quantization schemes to find the best quality versus performance tradeoff.
  * **Federated with Other Libraries:** Qwix seamlessly integrates with the JAX AI stack. For example, Tokamax automatically adapts to use quantized versions of kernels, without additional user code, when the model is quantized with Qwix.
  * **Research Friendly:** Qwix's foundational APIs and extensible architecture empower researchers to explore new algorithms and facilitate straightforward comparisons with integrated benchmark and evaluation tools.



### The application layer: training and alignment

#### Foundation model training: MaxText and MaxDiffusion

[MaxText](https://maxtext.readthedocs.io/en/latest/) and [MaxDiffusion](https://github.com/AI-Hypercomputer/maxdiffusion) are Google's flagship LLM and Diffusion model training frameworks, respectively. These repositories contain a selection of highly optimized implementations of popular open-weights models. They serve a dual purpose: they function as both a ready to go model training codebase and as a reference that foundation model builders can use to build upon.

##### Motivation

There is rapid growth of interest across the industry in training GenAI models. The popularity of open models has accelerated this trend, providing proven architectures. Training and adapting these models requires high performance, efficiency, scalability to large numbers of chips, and clear, understandable code. MaxText and MaxDiffusion are comprehensive solutions which can be used on TPUs or GPUs and are designed to fulfill these needs.

##### Design

MaxText and MaxDiffusion are foundation model codebases designed with readability and performance in mind. They are structured with well-tested, reusable components: model definitions that use custom kernels (like Tokamax) for maximum performance, a training harness for orchestration and monitoring, and a powerful config system that lets you control details like sharding and quantization (using Qwix) through an intuitive interface. Advanced reliability features like multi-tier checkpointing are incorporated to ensure sustained goodput.

MaxText and MaxDiffusion use the best in class JAX libraries Qwix, Tunix, Orbax, and Optax to deliver core capabilities. These libraries provide robust, scalable infrastructure, reducing development overhead and letting you focus on the modeling task. For inference, the model code is shared to enable efficient and scalable serving.

##### Key strengths

  * **Performant by Design:** With training infrastructure set up for high "goodput" (useful throughput) and model implementations optimized for high MFU (Model Flops Utilization), MaxText and MaxDiffusion deliver high performance at scale out of the box.
  * **Built for Scale:** Leveraging the power of the JAX AI stack (especially Pathways), these frameworks lets you scale seamlessly from tens of chips to tens of thousands of chips.
  * **Solid Base for Foundation Model Builders:** The high-quality, readable implementations serve as a solid starting point for developers to either use as an end to end solution or as a reference implementation for their own customizations.



#### Post training and alignment: The Tunix Framework

[Tunix](https://tunix.readthedocs.io/en/latest/) offers state of the art open source reinforcement learning (RL) algorithms, along with a robust framework and infrastructure, providing a streamlined path for developers to experiment with LLM post-training techniques, including supervised fine tuning (SFT) and alignment using JAX and TPUs.

##### Motivation

Post-training is a critical step in unlocking the true power of LLMs. The reinforcement learning (RL) stage is particularly crucial for developing alignment and reasoning capabilities. Open-source development in this area has been almost exclusively based on PyTorch and GPUs, leaving a fundamental gap for JAX and TPU solutions. Tunix (Tune-in-JAX) is a high-performance, JAX-native library designed to fill this gap.

##### Design

![Tunix diagram](https://docs.cloud.google.com/static/tpu/docs/images/Tunix_diagram.png)

From a framework perspective, Tunix enables a state-of-the-art setup that **clearly separates RL algorithms from the infrastructure**. It offers a lightweight, client-like API that hides the complexity of the RL infrastructure, letting you develop new algorithms. Tunix provides out-of-the-box solutions for popular algorithms, including Proximal Policy Optimization (PPO), Direct Preference Optimization (DPO), and others.

On the infrastructure side, Tunix has integration with Pathways, enabling a single-controller architecture that makes multi-node RL training accessible. On the training side, Tunix natively supports parameter-efficient training (for example, LoRA) and leverages JAX sharding and XLA (General and Scalable Parallelization for ML Computation Graph (GSPMD)) to generate a performant compute graph. It supports popular open-source models like Gemma and Llama out of the box.

##### Key strengths

  * **Simplicity:** It provides a high-level, client-like API that abstracts away the complexities of the underlying distributed infrastructure.
  * **Developer Efficiency:** Tunix accelerates the R&D lifecycle with built-in algorithms and "recipes," giving you a working model and lets you iterate quickly.
  * **Performance and Scalability:** Tunix enables a highly efficient and horizontally scalable training infrastructure by leveraging Pathways as a single controller on the backend.



### The application layer: Production and inference

A historical challenge for JAX adoption has been the path from research to production. The JAX AI stack now provides a mature, two-pronged production story that offers both ecosystem compatibility and JAX performance.

#### High performance LLM inference: The vLLM-JAX solution

[vLLM-JAX](https://github.com/vllm-project/vllm-jax) is Google's high-performance inference backend designed to run JAX large language models (LLMs) efficiently on Cloud TPUs. It integrates the open-source vLLM framework with Google's JAX and TPU ecosystem. For serving PyTorch models with vLLM on TPUs, see [PyTorch on Cloud TPU](https://docs.cloud.google.com/tpu/docs/pytorch-on-tpu).

##### Motivation

The industry is rapidly evolving, with growing demand for seamless, high-performing, and easy-to-use inference solutions. Developers often face significant challenges from complex and inconsistent tooling, subpar performance, and limited model compatibility. The vLLM stack addresses these issues by providing a unified, performant, and intuitive platform.

##### Design

This solution extends the vLLM framework, rather than reinventing it. vLLM-JAX is a highly optimized open-source LLM serving engine known for its high throughput, achieved using key features like **PagedAttention** (which manages KV caches like virtual memory to minimize fragmentation) and **Continuous Batching** (which dynamically adds requests to the batch to improve utilization).

vLLM-JAX builds on this foundation and develops core components for request handling, scheduling, and memory management. It introduces a **JAX-based backend** that acts as a bridge, translating vLLM's computational graph and memory operations into TPU-executable code. This backend handles device interactions, JAX model execution, and the specifics of managing the KV cache on TPU hardware. It incorporates TPU-specific optimizations, such as efficient attention mechanisms (for example, leveraging JAX Pallas kernels for Ragged Paged Attention) and quantization, all tailored for the TPU architecture.

##### Key strengths

  * **Zero Onboarding/Offboarding Cost for Users:** Users can adopt this solution without significant friction. From a user-experience perspective, processing inference requests on TPUs should be the same on GPUs. The CLI to start the server, accept prompts, and return outputs are all shared.
  * **Fully Embrace the Ecosystem:** This approach utilizes and contributes to the vLLM interface and user experience, ensuring compatibility and ease of use.
  * **Fungibility between TPUs and GPUs:** The solution works efficiently on both TPUs and GPUs, giving you flexibility.
  * **Cost Efficient (Best Perf/$):** Optimizes performance to provide the best performance-to-cost ratio for popular models.



#### JAX serving: Orbax serialization and Neptune serving engine

For models other than LLMs, or for users desiring a fully JAX-native pipeline, the [Orbax](https://orbax.readthedocs.io/en/latest/index.html) serialization library and Neptune serving engine (NSE) system provide an end to end, high performance serving solution.

##### Motivation

Historically, JAX models often relied on a circuitous path to production, such as being wrapped in TensorFlow graphs and deployed using TensorFlow serving. This approach introduced significant limitations and inefficiencies, forcing developers to engage with a separate ecosystem and slowing down iteration. A dedicated JAX-native serving system is crucial for sustainability, reduced complexity, and optimized performance.

##### Design

This solution consists of two core components, as illustrated in the following diagram.

![JAX serving diagram](https://docs.cloud.google.com/static/tpu/docs/images/serving_orbax_nse.png)

  1. **Orbax Serialization Library:** Provides user-friendly APIs for serializing JAX models into a new, robust Orbax serialization format. This format is optimized for production deployment. It directly represents JAX model computations using **StableHLO** , allowing the computation graph to be represented natively. It also leverages **TensorStore** for storing weights, enabling fast checkpoint loading for serving.
  2. **Neptune Serving Engine (NSE):** This is the accompanying high-performance, flexible serving engine (typically deployed as a C++ binary) designed to natively run JAX models in the Orbax format. NSE offers production-essential capabilities, such as fast model loading, high-throughput concurrent serving with built-in batching, support for multiple model versions, and both single and multiple host serving (leveraging PJRT and Pathways). Use the Neptune Serving Engine for: 
     * Non-LLM models: It is a general-purpose solution ideal for workloads like recommender systems, diffusion models, and other AI models.
     * Small LLMs and "one-shot" serving: It is designed for non-autoregressive models or smaller models that are served in a "unary" fashion, where the entire output is generated in a single pass without the need for complex state management like a KV cache.



In short, Neptune Serving Engine fills the gap for serving the wide variety of models that are not large, autoregressive language models, providing a high performance TPU-native solution for the broader ML ecosystem.

##### Key strengths

  * **JAX Native Serving:** The solution is built natively for JAX, eliminating inter-framework overhead in model serialization and serving. This ensures fast model loading and optimized execution across CPUs, GPUs, and TPUs.
  * **Effortless Production Deployment:** Serialized models provide a **hermetic deployment path** that is unaffected by drift in Python dependencies and enables runtime model integrity checks. This provides a seamless, intuitive path for JAX model productionization.
  * **Enhanced Developer Experience:** By eliminating the need for cumbersome framework wrapping, this solution significantly reduces dependencies and system complexity, speeding up iteration for JAX developers.



### System wide analysis and profiling

#### XProf: Deep, hardware integrated performance profiling

[XProf](https://openxla.org/xprof) is a profiling and performance analysis tool that provides in depth visibility into various aspects of ML workload execution, letting you debug and optimize performance. It is deeply integrated into both the JAX and TPU ecosystems.

##### Motivation

On one hand, ML workloads are growing ever more complicated. On the other, there is an explosion of specialized hardware capabilities targeting these workloads. Matching the two effectively to ensure peak performance and efficiency is critical, given the enormous costs of ML infrastructure. This requires deep visibility into both the workload and the hardware, presented in a way that is quickly consumable. XProf excels at this.

##### Design

XProf consists of two primary components: collection and analysis.

  1. **Collection:** XProf captures information from various sources: annotations in your JAX code, cost models for operations within the XLA compiler, and **purpose built hardware profiling features within the TPU**. This collection can be triggered programmatically or on-demand, generating a comprehensive event artifact.
  2. **Analysis:** XProf post-processes the collected data and creates a suite of powerful visualizations, accessed with a browser.



##### Key strengths

The true power of XProf comes from its deep integration with the full stack, providing a breadth and depth of analysis that is a tangible benefit of the co-designed JAX/TPU ecosystem.

  * **Co-designed with the TPU:** XProf exploits hardware features specifically designed for seamless profile collection, enabling a collection overhead of **less than 1%**. This allows profiling to be a lightweight, iterative part of development.
  * **Breadth and Depth of Analysis:** XProf yields deep analysis across multiple axes. Its tools include: 
    * **Trace Viewer:** An operation timeline view of execution on different hardware units (for example, TensorCores).
    * **HLO Op Profile:** Breaks down the total time spent into different categories of operations.
    * **Memory Viewer:** Details memory allocations by different operations during the profiled window.
    * **Roofline Analysis:** Helps you identify whether specific operations are compute or memory bound and how far they are from the hardware's peak capabilities.
    * **Graph Viewer:** Provides a view into the full HLO graph executed by the hardware.



## A comparative perspective: The JAX/TPU stack as a compelling choice

The modern Machine Learning landscape offers many excellent, mature toolchains. The JAX AI Stack presents a unique and compelling set of advantages for developers focused on large-scale, high-performance ML, stemming directly from its modular design and deep hardware co-design.

While many frameworks offer a wide array of features, the JAX AI Stack provides specific, powerful differentiators in key areas of the development lifecycle:

  * **A Simpler, more powerful developer experience:** The chainable gradient transformation paradigm of Optax allows for more powerful and flexible optimization strategies that are declared once, rather than imperatively managed in the training loop. At the system level, the simpler single controller interface of **Pathways** abstracts away the complexity of multislice training, a significant simplification for researchers.
  * **Engineered for hero scale resilience:** The JAX stack is designed for extreme-scale training. Orbax provides "hero-scale training resilience" features like emergency and multi-tier checkpointing. This is complemented by Grain, which offers full support for reproducibility with deterministic global shuffles and checkpointable data loaders. The ability to atomically checkpoint the data pipeline state (Grain) with the model state (Orbax) is a critical capability for guaranteeing reproducibility in long-running jobs.
  * **A complete, end to end ecosystem:** The stack provides a cohesive, end to end solution. Developers can use MaxText as a SOTA reference for training, **Tunix** for alignment, and follow a clear, dual-path to production with **vLLM-JAX** (for vLLM compatibility) and **NSE** (for JAX performance).



While many stacks are similar from a high level software standpoint, the deciding factor often comes down to **Performance/TCO** , which is where the co design of JAX and TPUs provides a distinct advantage. This Performance/TCO benefit is a direct result of the vertical integration across software and TPU hardware. The ability of the **XLA** compiler to fuse operations specifically for the TPU architecture, or for the **XProf** profiler to use hardware hooks for <1% overhead profiling, are tangible benefits of this deep integration.

For organizations adopting this stack, the full featured nature of the JAX AI stack minimizes the cost of migration. For customers employing popular open model architectures, a shift from other frameworks to MaxText is often a matter of setting up config files. Furthermore, the stack's ability to ingest popular checkpoint formats like safetensors allows existing checkpoints to be migrated over without needing costly re-training.

The following table provides a mapping of the components provided by the JAX AI stack and their equivalents in other frameworks or libraries.

**Function** | **JAX** | **Alternatives/equivalents in other frameworks** 5  
---|---|---  
Compiler / runtime | XLA | Inductor, eager  
MultiPod training | Pathways | Torch lightning strategies, Ray Train, Monarch (new).  
Core framework | JAX | PyTorch  
Model authoring | Flax, Max* models | `torch.nn.*`, NVidia TransformerEngine, HuggingFace Transformers   
Optimizers & losses  | Optax | torch.optim.*, torch.nn.*Loss  
Data Loaders | Grain | Ray Data, HuggingFace dataloaders  
Checkpointing | Orbax | PyTorch distributed checkpointing, NeMo checkpointing  
Quantization | Qwix | TorchAO, bitsandbytes  
Kernel authoring & well known implementations | Pallas / Tokamax | Triton/Helion, Liger-kernel, TransformerEngine  
Post training / tuning | Tunix | VERL, NeMoRL  
Profiling | XProf | PyTorch profiler, NSight systems, NSight Compute  
Foundation model Training | MaxText, MaxDiffusion | NeMo-Megatron, DeepSpeed, TorchTitan  
LLM inference | vLLM | SGLang  
Non-LLM Inference | NSE | Triton Inference Server, RayServe  
  
* * *

5Some of the equivalents here are not always true comparisons because other frameworks draw API boundaries differently compared to JAX. The list of equivalents is not exhaustive and there are new libraries appearing frequently.

## Conclusion: A durable, production ready platform for the future of AI

The data provided in the previous table illustrates a self-evident conclusion - these stacks have their own strengths and weaknesses in a small number of areas but overall are vastly similar from the software standpoint. Both stacks provide turnkey solutions for pre-training, post-training adaptation and deployment of foundational models.

The JAX AI stack offers a compelling and robust solution for training and deploying ML models at any scale. It leverages deep vertical integration across software and TPU hardware to deliver class-leading performance and total cost of ownership.

By building on battle-tested internal systems, the stack has evolved to provide inherent reliability and scalability, enabling users to confidently develop and deploy even the largest models. Its modular and composable design, rooted in the JAX AI stack philosophy, grants users unparalleled freedom and control, allowing them to tailor the stack to their specific needs without the constraints of a monolithic framework.

With XLA and Pathways providing a scalable and fault-tolerant base, JAX providing a performant and expressive numerics library, powerful core development libraries like [Flax](https://flax.readthedocs.io/en/stable/), [Optax](https://optax.readthedocs.io/en/latest/), [Grain](https://google-grain.readthedocs.io/en/latest/), and [Orbax](https://orbax.readthedocs.io/en/latest/), advanced performance tools like [Pallas](https://docs.jax.dev/en/latest/pallas/index.html), [Tokamax](https://github.com/openxla/tokamax), and [Qwix](https://qwix.readthedocs.io/en/latest/), and a robust application and production layer in [MaxText](https://maxtext.readthedocs.io/en/latest/), vLLM, and NSE, the JAX AI stack provides a durable foundation for users to build on and rapidly bring state-of-the-art research to production.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
