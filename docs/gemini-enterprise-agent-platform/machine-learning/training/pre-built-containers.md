---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/pre-built-containers/
title: Prebuilt containers for serverless training \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:24:40.909101+00:00
---

# Prebuilt containers for serverless training  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/pre-built-containers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Prebuilt containers for serverless training Stay organized with collections  Save and categorize content based on your preferences. 

Gemini Enterprise Agent Platform provides Docker container images that you run as _prebuilt containers_ for serverless training. These containers, which are organized by machine learning (ML) framework and framework version, include common dependencies that you might want to use in training code. Often, using a prebuilt container is simpler than [creating your own custom container for training](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/create-custom-container).

This document lists the prebuilt containers for training, and it describes how to use them with a [Python training application](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/create-python-pre-built-container).

Gemini Enterprise Agent Platform supports each framework version based on a schedule to minimize security vulnerabilities. Review the [Agent Platform framework support policy](https://docs.cloud.google.com/gemini-enterprise-agent-platform//machine-learning/framework-support-policy) to understand the implications of the end-of-support and end-of-availability dates.

## Available container images

Each of the following container images is available in several [Artifact Registry repositories](https://docs.cloud.google.com/artifact-registry/docs/repositories), which [store data in various locations](https://docs.cloud.google.com/artifact-registry/docs/repo-locations). You can use any of the URIs for an image when you perform serverless training; each provides the same container image. When using Google Cloud console to perform serverless training, the Google Cloud console selects the URI that best matches the [location where you're using Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/locations). This reduces latency.

**Note:** Using image names without the `latest` tag isn't supported. You must use an image with the `latest` tag.

### TensorFlow

ML framework version | Supported accelerators (and CUDA version, if applicable) | End of patch and support date | End of availability | Supported images  
---|---|---|---|---  
2.17 (Python 3.10) | CPU only | Jul 11, 2025 | Jul 11, 2026 | 

  * `us-docker.pkg.dev/vertex-ai/training/tf-cpu.2-17.py310:latest`
  * `europe-docker.pkg.dev/vertex-ai/training/tf-cpu.2-17.py310:latest`
  * `asia-docker.pkg.dev/vertex-ai/training/tf-cpu.2-17.py310:latest`



#### Included dependencies

| PyPI packages | Ubuntu packages  
---|---  
tensorflow 2.17.x (latest patch)  
sympy 1.12  
pandas 2.2.3  
xgboost 2.1.3  
python-json-logger 3.2.1  
WebOb 1.8.7  
Paste 3.7.1  
webapp2 3.0.0b1  
mock 5.1.0  
google-cloud-resource-manager 1.6.1  
cloudml-hypertune  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software) |  ca-certificates-java  
libatlas-base-dev  
liblapack-dev  
gfortran  
gdb  
openjdk-8-jdk  
openjdk-8-jre-headless  
g++  
libio-all-perl  
libyaml-0-2  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software)  
  
2.17 (Python 3.10) | GPU (CUDA 12.x) | Jul 11, 2025 | Jul 11, 2026 | 

  * `us-docker.pkg.dev/vertex-ai/training/tf-gpu.2-17.py310:latest`
  * `europe-docker.pkg.dev/vertex-ai/training/tf-gpu.2-17.py310:latest`
  * `asia-docker.pkg.dev/vertex-ai/training/tf-gpu.2-17.py310:latest`



#### Included dependencies

| PyPI packages | Ubuntu packages  
---|---  
tensorflow 2.17.x (latest patch)  
sympy 1.12  
pandas 2.2.3  
xgboost 2.1.3  
python-json-logger 3.2.1  
WebOb 1.8.7  
Paste 3.7.1  
webapp2 3.0.0b1  
mock 5.1.0  
google-cloud-resource-manager 1.6.1  
cloudml-hypertune  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software) |  ca-certificates-java  
libatlas-base-dev  
liblapack-dev  
gfortran  
gdb  
openjdk-8-jdk  
openjdk-8-jre-headless  
g++  
libio-all-perl  
libyaml-0-2  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software)  
  
2.16 (Python 3.10) | CPU only | Jun 28, 2025 | Jun 28, 2026 | 

  * `us-docker.pkg.dev/vertex-ai/training/tf-cpu.2-16.py310:latest`
  * `europe-docker.pkg.dev/vertex-ai/training/tf-cpu.2-16.py310:latest`
  * `asia-docker.pkg.dev/vertex-ai/training/tf-cpu.2-16.py310:latest`



#### Included dependencies

| PyPI packages | Ubuntu packages  
---|---  
tensorflow 2.16.x (latest patch)  
sympy 1.12  
xgboost 2.0.3  
python-json-logger 2.0.7  
WebOb 1.8.7  
Paste 3.7.1  
webapp2 3.0.0b1  
mock 5.1.0  
google-cloud-resource-manager 1.6.1  
cloudml-hypertune  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software) |  ca-certificates-java  
libatlas-base-dev  
liblapack-dev  
gfortran  
gdb  
openjdk-8-jdk  
openjdk-8-jre-headless  
g++  
libio-all-perl  
libyaml-0-2  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software)  
  
2.16 (Python 3.10) | GPU (CUDA 12.x) | Jun 28, 2025 | Jun 28, 2026 | 

  * `us-docker.pkg.dev/vertex-ai/training/tf-gpu.2-16.py310:latest`
  * `europe-docker.pkg.dev/vertex-ai/training/tf-gpu.2-16.py310:latest`
  * `asia-docker.pkg.dev/vertex-ai/training/tf-gpu.2-16.py310:latest`



#### Included dependencies

| PyPI packages | Ubuntu packages  
---|---  
tensorflow 2.16.x (latest patch)  
sympy 1.12  
xgboost 2.0.3  
python-json-logger 2.0.7  
WebOb 1.8.7  
Paste 3.7.1  
webapp2 3.0.0b1  
mock 5.1.0  
google-cloud-resource-manager 1.6.1  
cloudml-hypertune  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software) |  ca-certificates-java  
libatlas-base-dev  
liblapack-dev  
gfortran  
gdb  
openjdk-8-jdk  
openjdk-8-jre-headless  
g++  
libio-all-perl  
libyaml-0-2  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software)  
  
2.15 (Python 3.10) | CPU only | Nov 14, 2024 | Nov 14, 2025 | 

  * `us-docker.pkg.dev/vertex-ai/training/tf-cpu.2-15.py310:latest`
  * `europe-docker.pkg.dev/vertex-ai/training/tf-cpu.2-15.py310:latest`
  * `asia-docker.pkg.dev/vertex-ai/training/tf-cpu.2-15.py310:latest`



#### Included dependencies

| PyPI packages | Ubuntu packages  
---|---  
tensorflow 2.15.x (latest patch)  
sympy 1.12  
xgboost 2.0.3  
python-json-logger 2.0.7  
WebOb 1.8.7  
Paste 3.7.1  
webapp2 3.0.0b1  
mock 5.1.0  
google-cloud-resource-manager 1.6.1  
cloudml-hypertune  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software) |  ca-certificates-java  
libatlas-base-dev  
liblapack-dev  
gfortran  
gdb  
openjdk-8-jdk  
openjdk-8-jre-headless  
g++  
libio-all-perl  
libyaml-0-2  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software)  
  
2.15 (Python 3.10) | GPU (CUDA 12.x) | Nov 14, 2024 | Nov 14, 2025 | 

  * `us-docker.pkg.dev/vertex-ai/training/tf-gpu.2-15.py310:latest`
  * `europe-docker.pkg.dev/vertex-ai/training/tf-gpu.2-15.py310:latest`
  * `asia-docker.pkg.dev/vertex-ai/training/tf-gpu.2-15.py310:latest`



#### Included dependencies

| PyPI packages | Ubuntu packages  
---|---  
tensorflow 2.15.x (latest patch)  
sympy 1.12  
xgboost 2.0.3  
python-json-logger 2.0.7  
WebOb 1.8.7  
Paste 3.7.1  
webapp2 3.0.0b1  
mock 5.1.0  
google-cloud-resource-manager 1.6.1  
cloudml-hypertune  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software) |  ca-certificates-java  
libatlas-base-dev  
liblapack-dev  
gfortran  
gdb  
openjdk-8-jdk  
openjdk-8-jre-headless  
g++  
libio-all-perl  
libyaml-0-2  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software)  
  
2.15 (Python 3.10) | TPU only | Oct 23, 2024 | Oct 23, 2025 | 

  * `us-docker.pkg.dev/vertex-ai/training/tf-tpu.2-15.cp310:latest`
  * `europe-docker.pkg.dev/vertex-ai/training/tf-tpu.2-15.cp310:latest`
  * `asia-docker.pkg.dev/vertex-ai/training/tf-tpu.2-15.cp310:latest`



#### Included dependencies

| PyPI packages | Ubuntu packages  
---|---  
tensorflow 2.15.x (latest patch)  
sympy 1.12  
xgboost 2.0.3  
python-json-logger 2.0.7  
WebOb 1.8.7  
Paste 3.7.1  
webapp2 3.0.0b1  
mock 5.1.0  
google-cloud-resource-manager 1.6.1  
cloudml-hypertune  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software) |  ca-certificates-java  
libatlas-base-dev  
liblapack-dev  
gfortran  
gdb  
openjdk-8-jdk  
openjdk-8-jre-headless  
g++  
libio-all-perl  
libyaml-0-2  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software)  
  
2.14 (Python 3.10) | CPU only | Sep 26, 2024 | Sep 26, 2025 | 

  * `us-docker.pkg.dev/vertex-ai/training/tf-cpu.2-14.py310:latest`
  * `europe-docker.pkg.dev/vertex-ai/training/tf-cpu.2-14.py310:latest`
  * `asia-docker.pkg.dev/vertex-ai/training/tf-cpu.2-14.py310:latest`



#### Included dependencies

| PyPI packages | Ubuntu packages  
---|---  
tensorflow 2.14.x (latest patch)  
sympy 1.12  
xgboost 2.0.3  
python-json-logger 2.0.7  
WebOb 1.8.7  
Paste 3.7.1  
webapp2 3.0.0b1  
mock 5.1.0  
google-cloud-resource-manager 1.6.1  
cloudml-hypertune  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software) |  ca-certificates-java  
libatlas-base-dev  
liblapack-dev  
gfortran  
gdb  
openjdk-8-jdk  
openjdk-8-jre-headless  
g++  
libio-all-perl  
libyaml-0-2  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software)  
  
2.14 (Python 3.10) | GPU (CUDA 11.x) | Sep 26, 2024 | Sep 26, 2025 | 

  * `us-docker.pkg.dev/vertex-ai/training/tf-gpu.2-14.py310:latest`
  * `europe-docker.pkg.dev/vertex-ai/training/tf-gpu.2-14.py310:latest`
  * `asia-docker.pkg.dev/vertex-ai/training/tf-gpu.2-14.py310:latest`



#### Included dependencies

| PyPI packages | Ubuntu packages  
---|---  
tensorflow 2.14.x (latest patch)  
sympy 1.12  
xgboost 2.0.3  
python-json-logger 2.0.7  
WebOb 1.8.7  
Paste 3.7.1  
webapp2 3.0.0b1  
mock 5.1.0  
google-cloud-resource-manager 1.6.1  
cloudml-hypertune  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software) |  ca-certificates-java  
libatlas-base-dev  
liblapack-dev  
gfortran  
gdb  
openjdk-8-jdk  
openjdk-8-jre-headless  
g++  
libio-all-perl  
libyaml-0-2  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software)  
  
2.13 (Python 3.10) | CPU only | Jul 5, 2024 | Jul 5, 2025 | 

  * `us-docker.pkg.dev/vertex-ai/training/tf-cpu.2-13.py310:latest`
  * `europe-docker.pkg.dev/vertex-ai/training/tf-cpu.2-13.py310:latest`
  * `asia-docker.pkg.dev/vertex-ai/training/tf-cpu.2-13.py310:latest`



#### Included dependencies

| PyPI packages | Ubuntu packages  
---|---  
tensorflow 2.13.x (latest patch)  
sympy 1.12  
xgboost 2.0.3  
python-json-logger 2.0.7  
WebOb 1.8.7  
Paste 3.7.1  
webapp2 3.0.0b1  
mock 5.1.0  
google-cloud-resource-manager 1.6.1  
cloudml-hypertune  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software) |  ca-certificates-java  
libatlas-base-dev  
liblapack-dev  
gfortran  
gdb  
openjdk-8-jdk  
openjdk-8-jre-headless  
g++  
libio-all-perl  
libyaml-0-2  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software)  
  
2.13 (Python 3.10) | GPU (CUDA 11.x) | Jul 5, 2024 | Jul 5, 2025 | 

  * `us-docker.pkg.dev/vertex-ai/training/tf-gpu.2-13.py310:latest`
  * `europe-docker.pkg.dev/vertex-ai/training/tf-gpu.2-13.py310:latest`
  * `asia-docker.pkg.dev/vertex-ai/training/tf-gpu.2-13.py310:latest`



#### Included dependencies

| PyPI packages | Ubuntu packages  
---|---  
tensorflow 2.13.x (latest patch)  
sympy 1.12  
xgboost 2.0.3  
python-json-logger 2.0.7  
WebOb 1.8.7  
Paste 3.7.1  
webapp2 3.0.0b1  
mock 5.1.0  
google-cloud-resource-manager 1.6.1  
cloudml-hypertune  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software) |  ca-certificates-java  
libatlas-base-dev  
liblapack-dev  
gfortran  
gdb  
openjdk-8-jdk  
openjdk-8-jre-headless  
g++  
libio-all-perl  
libyaml-0-2  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software)  
  
2.12 (Python 3.10) | CPU only | Jun 30, 2024 | Jun 30, 2025 | 

  * `us-docker.pkg.dev/vertex-ai/training/tf-cpu.2-12.py310:latest`
  * `europe-docker.pkg.dev/vertex-ai/training/tf-cpu.2-12.py310:latest`
  * `asia-docker.pkg.dev/vertex-ai/training/tf-cpu.2-12.py310:latest`



#### Included dependencies

| PyPI packages | Ubuntu packages  
---|---  
tensorflow 2.12.x (latest patch)  
sympy 1.10.1  
xgboost 1.6.2  
python-json-logger 2.0.4  
WebOb 1.8.7  
Paste 3.5.0  
webapp2 3.0.0b1  
mock 5.0.0  
google-cloud-resource-manager 1.6.1  
cloudml-hypertune  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software) |  ca-certificates-java  
libatlas-base-dev  
liblapack-dev  
gfortran  
gdb  
openjdk-8-jdk  
openjdk-8-jre-headless  
g++  
libio-all-perl  
libyaml-0-2  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software)  
  
2.12 (Python 3.10) | GPU (CUDA 11.x) | Jun 30, 2024 | Jun 30, 2025 | 

  * `us-docker.pkg.dev/vertex-ai/training/tf-gpu.2-12.py310:latest`
  * `europe-docker.pkg.dev/vertex-ai/training/tf-gpu.2-12.py310:latest`
  * `asia-docker.pkg.dev/vertex-ai/training/tf-gpu.2-12.py310:latest`



#### Included dependencies

| PyPI packages | Ubuntu packages  
---|---  
tensorflow 2.12.x (latest patch)  
sympy 1.10.1  
xgboost 1.6.2  
python-json-logger 2.0.4  
WebOb 1.8.7  
Paste 3.5.0  
webapp2 3.0.0b1  
mock 5.0.0  
google-cloud-resource-manager 1.6.1  
cloudml-hypertune  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software) |  ca-certificates-java  
libatlas-base-dev  
liblapack-dev  
gfortran  
gdb  
openjdk-8-jdk  
openjdk-8-jre-headless  
g++  
libio-all-perl  
libyaml-0-2  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software)  
  
2.12 (Python 3.8) | TPU only | Jun 30, 2024 | Jun 30, 2025 | 

  * `us-docker.pkg.dev/vertex-ai/training/tf-tpu.2-12:latest`
  * `europe-docker.pkg.dev/vertex-ai/training/tf-tpu.2-12:latest`
  * `asia-docker.pkg.dev/vertex-ai/training/tf-tpu.2-12:latest`



#### Included dependencies

| PyPI packages | Ubuntu packages  
---|---  
tensorflow 2.12.x (latest patch)  
sympy 1.10.1  
xgboost 1.6.2  
python-json-logger 2.0.4  
WebOb 1.8.7  
Paste 3.5.0  
webapp2 3.0.0b1  
mock 5.0.0  
google-cloud-resource-manager 1.6.1  
cloudml-hypertune  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software) |  ca-certificates-java  
libatlas-base-dev  
liblapack-dev  
gfortran  
gdb  
openjdk-8-jdk  
openjdk-8-jre-headless  
g++  
libio-all-perl  
libyaml-0-2  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software)  
  
2.11 (Python 3.10) | CPU only | Nov 15, 2023 | Nov 15, 2024 | 

  * `us-docker.pkg.dev/vertex-ai/training/tf-cpu.2-11.py310:latest`
  * `europe-docker.pkg.dev/vertex-ai/training/tf-cpu.2-11.py310:latest`
  * `asia-docker.pkg.dev/vertex-ai/training/tf-cpu.2-11.py310:latest`



#### Included dependencies

| PyPI packages | Ubuntu packages  
---|---  
tensorflow 2.11.x (latest patch)  
sympy 1.10.1  
xgboost 1.6.2  
python-json-logger 2.0.4  
WebOb 1.8.7  
Paste 3.5.0  
webapp2 3.0.0b1  
mock 5.0.0  
google-cloud-resource-manager 1.6.1  
cloudml-hypertune  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software) |  ca-certificates-java  
libatlas-base-dev  
liblapack-dev  
gfortran  
gdb  
openjdk-8-jdk  
openjdk-8-jre-headless  
g++  
libio-all-perl  
libyaml-0-2  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software)  
  
2.11 (Python 3.10) | GPU (CUDA 11.x) | Nov 15, 2023 | Nov 15, 2024 | 

  * `us-docker.pkg.dev/vertex-ai/training/tf-gpu.2-11.py310:latest`
  * `europe-docker.pkg.dev/vertex-ai/training/tf-gpu.2-11.py310:latest`
  * `asia-docker.pkg.dev/vertex-ai/training/tf-gpu.2-11.py310:latest`



#### Included dependencies

| PyPI packages | Ubuntu packages  
---|---  
tensorflow 2.11.x (latest patch)  
sympy 1.10.1  
xgboost 1.6.2  
python-json-logger 2.0.4  
WebOb 1.8.7  
Paste 3.5.0  
webapp2 3.0.0b1  
mock 5.0.0  
google-cloud-resource-manager 1.6.1  
cloudml-hypertune  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software) |  ca-certificates-java  
libatlas-base-dev  
liblapack-dev  
gfortran  
gdb  
openjdk-8-jdk  
openjdk-8-jre-headless  
g++  
libio-all-perl  
libyaml-0-2  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software)  
  
2.11 (Python 3.7) | CPU only | Nov 15, 2023 | Nov 15, 2024 | 

  * `us-docker.pkg.dev/vertex-ai/training/tf-cpu.2-11:latest`
  * `europe-docker.pkg.dev/vertex-ai/training/tf-cpu.2-11:latest`
  * `asia-docker.pkg.dev/vertex-ai/training/tf-cpu.2-11:latest`



#### Included dependencies

| PyPI packages | Ubuntu packages  
---|---  
tensorflow 2.11.x (latest patch)  
sympy 1.10.1  
xgboost 1.6.2  
python-json-logger 2.0.4  
WebOb 1.8.7  
Paste 3.5.0  
webapp2 3.0.0b1  
mock 5.0.0  
google-cloud-resource-manager 1.6.1  
cloudml-hypertune  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software) |  ca-certificates-java  
libatlas-base-dev  
liblapack-dev  
gfortran  
gdb  
openjdk-8-jdk  
openjdk-8-jre-headless  
g++  
libio-all-perl  
libyaml-0-2  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software)  
  
2.11 (Python 3.7) | GPU (CUDA 11.x) | Nov 15, 2023 | Nov 15, 2024 | 

  * `us-docker.pkg.dev/vertex-ai/training/tf-gpu.2-11:latest`
  * `europe-docker.pkg.dev/vertex-ai/training/tf-gpu.2-11:latest`
  * `asia-docker.pkg.dev/vertex-ai/training/tf-gpu.2-11:latest`



#### Included dependencies

| PyPI packages | Ubuntu packages  
---|---  
tensorflow 2.11.x (latest patch)  
sympy 1.10.1  
xgboost 1.6.2  
python-json-logger 2.0.4  
WebOb 1.8.7  
Paste 3.5.0  
webapp2 3.0.0b1  
mock 5.0.0  
google-cloud-resource-manager 1.6.1  
cloudml-hypertune  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software) |  ca-certificates-java  
libatlas-base-dev  
liblapack-dev  
gfortran  
gdb  
openjdk-8-jdk  
openjdk-8-jre-headless  
g++  
libio-all-perl  
libyaml-0-2  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software)  
  
2.9 (Python 3.10) | CPU only | Nov 15, 2023 | Nov 15, 2024 | 

  * `us-docker.pkg.dev/vertex-ai/training/tf-cpu.2-9.py310:latest`
  * `europe-docker.pkg.dev/vertex-ai/training/tf-cpu.2-9.py310:latest`
  * `asia-docker.pkg.dev/vertex-ai/training/tf-cpu.2-9.py310:latest`



#### Included dependencies

| PyPI packages | Ubuntu packages  
---|---  
tensorflow 2.9.x (latest patch)  
sympy 1.10.1  
xgboost 1.6.1  
python-json-logger 2.0.2  
WebOb 1.8.7  
Paste 3.5.0  
webapp2 3.0.0b1  
mock 4.0.3  
google-cloud-resource-manager 1.5.0  
cloudml-hypertune  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software) |  ca-certificates-java  
libatlas-base-dev  
liblapack-dev  
gfortran  
gdb  
openjdk-8-jdk  
openjdk-8-jre-headless  
g++  
libio-all-perl  
libyaml-0-2  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software)  
  
2.9 (Python 3.10) | GPU (CUDA 11.x) | Nov 15, 2023 | Nov 15, 2024 | 

  * `us-docker.pkg.dev/vertex-ai/training/tf-gpu.2-9.py310:latest`
  * `europe-docker.pkg.dev/vertex-ai/training/tf-gpu.2-9.py310:latest`
  * `asia-docker.pkg.dev/vertex-ai/training/tf-gpu.2-9.py310:latest`



#### Included dependencies

| PyPI packages | Ubuntu packages  
---|---  
tensorflow 2.9.x (latest patch)  
sympy 1.10.1  
xgboost 1.6.1  
python-json-logger 2.0.2  
WebOb 1.8.7  
Paste 3.5.0  
webapp2 3.0.0b1  
mock 4.0.3  
google-cloud-resource-manager 1.5.0  
cloudml-hypertune  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software) |  ca-certificates-java  
libatlas-base-dev  
liblapack-dev  
gfortran  
gdb  
openjdk-8-jdk  
openjdk-8-jre-headless  
g++  
libio-all-perl  
libyaml-0-2  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software)  
  
2.9 (Python 3.7) | CPU only | Nov 15, 2023 | Nov 15, 2024 | 

  * `us-docker.pkg.dev/vertex-ai/training/tf-cpu.2-9:latest`
  * `europe-docker.pkg.dev/vertex-ai/training/tf-cpu.2-9:latest`
  * `asia-docker.pkg.dev/vertex-ai/training/tf-cpu.2-9:latest`



#### Included dependencies

| PyPI packages | Ubuntu packages  
---|---  
tensorflow 2.9.x (latest patch)  
sympy 1.10.1  
xgboost 1.6.1  
python-json-logger 2.0.2  
WebOb 1.8.7  
Paste 3.5.0  
webapp2 3.0.0b1  
mock 4.0.3  
google-cloud-resource-manager 1.5.0  
cloudml-hypertune  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software) |  ca-certificates-java  
libatlas-base-dev  
liblapack-dev  
gfortran  
gdb  
openjdk-8-jdk  
openjdk-8-jre-headless  
g++  
libio-all-perl  
libyaml-0-2  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software)  
  
2.9 (Python 3.7) | GPU (CUDA 11.x) | Nov 15, 2023 | Nov 15, 2024 | 

  * `us-docker.pkg.dev/vertex-ai/training/tf-gpu.2-9:latest`
  * `europe-docker.pkg.dev/vertex-ai/training/tf-gpu.2-9:latest`
  * `asia-docker.pkg.dev/vertex-ai/training/tf-gpu.2-9:latest`



#### Included dependencies

| PyPI packages | Ubuntu packages  
---|---  
tensorflow 2.9.x (latest patch)  
sympy 1.10.1  
xgboost 1.6.1  
python-json-logger 2.0.2  
WebOb 1.8.7  
Paste 3.5.0  
webapp2 3.0.0b1  
mock 4.0.3  
google-cloud-resource-manager 1.5.0  
cloudml-hypertune  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software) |  ca-certificates-java  
libatlas-base-dev  
liblapack-dev  
gfortran  
gdb  
openjdk-8-jdk  
openjdk-8-jre-headless  
g++  
libio-all-perl  
libyaml-0-2  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software)  
  
2.8 (Python 3.10) | CPU only | Nov 15, 2023 | Nov 15, 2024 | 

  * `us-docker.pkg.dev/vertex-ai/training/tf-cpu.2-8.py310:latest`
  * `europe-docker.pkg.dev/vertex-ai/training/tf-cpu.2-8.py310:latest`
  * `asia-docker.pkg.dev/vertex-ai/training/tf-cpu.2-8.py310:latest`



#### Included dependencies

| PyPI packages | Ubuntu packages  
---|---  
tensorflow 2.8.x (latest patch)  
sympy 1.9  
xgboost 1.5.2  
python-json-logger 2.0.2  
WebOb 1.8.7  
Paste 3.5.0  
webapp2 3.0.0b1  
mock 4.0.3  
google-cloud-resource-manager 1.3.3  
cloudml-hypertune  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software) |  ca-certificates-java  
libatlas-base-dev  
liblapack-dev  
gfortran  
gdb  
openjdk-8-jdk  
openjdk-8-jre-headless  
g++  
libio-all-perl  
libyaml-0-2  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software)  
  
2.8 (Python 3.10) | GPU (CUDA 11.x) | Nov 15, 2023 | Nov 15, 2024 | 

  * `us-docker.pkg.dev/vertex-ai/training/tf-gpu.2-8.py310:latest`
  * `europe-docker.pkg.dev/vertex-ai/training/tf-gpu.2-8.py310:latest`
  * `asia-docker.pkg.dev/vertex-ai/training/tf-gpu.2-8.py310:latest`



#### Included dependencies

| PyPI packages | Ubuntu packages  
---|---  
tensorflow 2.8.x (latest patch)  
sympy 1.9  
xgboost 1.5.2  
python-json-logger 2.0.2  
WebOb 1.8.7  
Paste 3.5.0  
webapp2 3.0.0b1  
mock 4.0.3  
google-cloud-resource-manager 1.3.3  
cloudml-hypertune  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software) |  ca-certificates-java  
libatlas-base-dev  
liblapack-dev  
gfortran  
gdb  
openjdk-8-jdk  
openjdk-8-jre-headless  
g++  
libio-all-perl  
libyaml-0-2  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software)  
  
2.8 (Python 3.7) | CPU only | Nov 15, 2023 | Nov 15, 2024 | 

  * `us-docker.pkg.dev/vertex-ai/training/tf-cpu.2-8:latest`
  * `europe-docker.pkg.dev/vertex-ai/training/tf-cpu.2-8:latest`
  * `asia-docker.pkg.dev/vertex-ai/training/tf-cpu.2-8:latest`



#### Included dependencies

| PyPI packages | Ubuntu packages  
---|---  
tensorflow 2.8.x (latest patch)  
sympy 1.9  
xgboost 1.5.2  
python-json-logger 2.0.2  
WebOb 1.8.7  
Paste 3.5.0  
webapp2 3.0.0b1  
mock 4.0.3  
google-cloud-resource-manager 1.3.3  
cloudml-hypertune  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software) |  ca-certificates-java  
libatlas-base-dev  
liblapack-dev  
gfortran  
gdb  
openjdk-8-jdk  
openjdk-8-jre-headless  
g++  
libio-all-perl  
libyaml-0-2  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software)  
  
2.8 (Python 3.7) | GPU (CUDA 11.x) | Nov 15, 2023 | Nov 15, 2024 | 

  * `us-docker.pkg.dev/vertex-ai/training/tf-gpu.2-8:latest`
  * `europe-docker.pkg.dev/vertex-ai/training/tf-gpu.2-8:latest`
  * `asia-docker.pkg.dev/vertex-ai/training/tf-gpu.2-8:latest`



#### Included dependencies

| PyPI packages | Ubuntu packages  
---|---  
tensorflow 2.8.x (latest patch)  
sympy 1.9  
xgboost 1.5.2  
python-json-logger 2.0.2  
WebOb 1.8.7  
Paste 3.5.0  
webapp2 3.0.0b1  
mock 4.0.3  
google-cloud-resource-manager 1.3.3  
cloudml-hypertune  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software) |  ca-certificates-java  
libatlas-base-dev  
liblapack-dev  
gfortran  
gdb  
openjdk-8-jdk  
openjdk-8-jre-headless  
g++  
libio-all-perl  
libyaml-0-2  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software)  
  
2.7 (Python 3.7) | CPU only | Sep 1, 2023 | Sep 1, 2024 | 

  * `us-docker.pkg.dev/vertex-ai/training/tf-cpu.2-7:latest`
  * `europe-docker.pkg.dev/vertex-ai/training/tf-cpu.2-7:latest`
  * `asia-docker.pkg.dev/vertex-ai/training/tf-cpu.2-7:latest`



#### Included dependencies

| PyPI packages | Ubuntu packages  
---|---  
tensorflow 2.7.x (latest patch)  
sympy 1.9  
xgboost 1.5.0  
python-json-logger 2.0.2  
WebOb 1.8.7  
Paste 3.5.0  
webapp2 3.0.0b1  
mock 4.0.3  
google-cloud-resource-manager 1.3.1  
cloudml-hypertune  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software) |  curl  
libcurl3-dev  
wget  
zip  
unzip  
git  
vim  
build-essential  
ca-certificates  
pkg-config  
rsync  
ca-certificates-java  
libatlas-base-dev  
liblapack-dev  
gfortran  
libpng-dev  
libjpeg-dev  
python3.7  
python3-dev  
python3.7-dev  
python3-pip  
python3-setuptools  
python2.7  
python-dev  
python-setuptools  
gdb  
openjdk-8-jdk  
openjdk-8-jre-headless  
g++  
zlib1g-dev  
libio-all-perl  
module-init-tools  
libsnappy-dev  
libyaml-0-2  
python-opencv  
  
  
2.7 (Python 3.7) | GPU (CUDA 11.x) | Sep 1, 2023 | Sep 1, 2024 | 

  * `us-docker.pkg.dev/vertex-ai/training/tf-gpu.2-7:latest`
  * `europe-docker.pkg.dev/vertex-ai/training/tf-gpu.2-7:latest`
  * `asia-docker.pkg.dev/vertex-ai/training/tf-gpu.2-7:latest`



#### Included dependencies

| PyPI packages | Ubuntu packages  
---|---  
tensorflow 2.7.x (latest patch)  
sympy 1.9  
xgboost 1.5.0  
python-json-logger 2.0.2  
WebOb 1.8.7  
Paste 3.5.0  
webapp2 3.0.0b1  
mock 4.0.3  
google-cloud-resource-manager 1.3.1  
cloudml-hypertune  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software) |  curl  
libcurl3-dev  
wget  
zip  
unzip  
git  
vim  
build-essential  
ca-certificates  
pkg-config  
rsync  
ca-certificates-java  
libatlas-base-dev  
liblapack-dev  
gfortran  
libpng-dev  
libjpeg-dev  
python3.7  
python3-dev  
python3.7-dev  
python3-pip  
python3-setuptools  
python2.7  
python-dev  
python-setuptools  
gdb  
openjdk-8-jdk  
openjdk-8-jre-headless  
g++  
zlib1g-dev  
libio-all-perl  
module-init-tools  
libsnappy-dev  
libyaml-0-2  
python-opencv  
  
  
2.6 (Python 3.7) | CPU only | Sep 1, 2023 | Sep 1, 2024 | 

  * `us-docker.pkg.dev/vertex-ai/training/tf-cpu.2-6:latest`
  * `europe-docker.pkg.dev/vertex-ai/training/tf-cpu.2-6:latest`
  * `asia-docker.pkg.dev/vertex-ai/training/tf-cpu.2-6:latest`



#### Included dependencies

| PyPI packages | Ubuntu packages  
---|---  
tensorflow 2.6.x (latest patch)  
sympy 1.8  
xgboost 1.4.2  
python-json-logger 2.0.2  
WebOb 1.8.7  
Paste 3.5.0  
webapp2 3.0.0b1  
mock 4.0.3  
google-cloud-resource-manager 1.0.2  
cloudml-hypertune  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software) |  curl  
libcurl3-dev  
wget  
zip  
unzip  
git  
vim  
build-essential  
ca-certificates  
pkg-config  
rsync  
ca-certificates-java  
libatlas-base-dev  
liblapack-dev  
gfortran  
libpng-dev  
libjpeg-dev  
python3.7  
python3-dev  
python3.7-dev  
python3-pip  
python3-setuptools  
python2.7  
python-dev  
python-setuptools  
gdb  
openjdk-8-jdk  
openjdk-8-jre-headless  
g++  
zlib1g-dev  
libio-all-perl  
module-init-tools  
libsnappy-dev  
libyaml-0-2  
python-opencv  
  
  
2.6 (Python 3.7) | GPU (CUDA 11.x) | Sep 1, 2023 | Sep 1, 2024 | 

  * `us-docker.pkg.dev/vertex-ai/training/tf-gpu.2-6:latest`
  * `europe-docker.pkg.dev/vertex-ai/training/tf-gpu.2-6:latest`
  * `asia-docker.pkg.dev/vertex-ai/training/tf-gpu.2-6:latest`



#### Included dependencies

| PyPI packages | Ubuntu packages  
---|---  
tensorflow 2.6.x (latest patch)  
sympy 1.8  
xgboost 1.4.2  
python-json-logger 2.0.2  
WebOb 1.8.7  
Paste 3.5.0  
webapp2 3.0.0b1  
mock 4.0.3  
google-cloud-resource-manager 1.0.2  
cloudml-hypertune  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software) |  curl  
libcurl3-dev  
wget  
zip  
unzip  
git  
vim  
build-essential  
ca-certificates  
pkg-config  
rsync  
ca-certificates-java  
libatlas-base-dev  
liblapack-dev  
gfortran  
libpng-dev  
libjpeg-dev  
python3.7  
python3-dev  
python3.7-dev  
python3-pip  
python3-setuptools  
python2.7  
python-dev  
python-setuptools  
gdb  
openjdk-8-jdk  
openjdk-8-jre-headless  
g++  
zlib1g-dev  
libio-all-perl  
module-init-tools  
libsnappy-dev  
libyaml-0-2  
python-opencv  
  
  
2.5 (Python 3.7) | CPU only | Sep 1, 2023 | Sep 1, 2024 | 

  * `us-docker.pkg.dev/vertex-ai/training/tf-cpu.2-5:latest`
  * `europe-docker.pkg.dev/vertex-ai/training/tf-cpu.2-5:latest`
  * `asia-docker.pkg.dev/vertex-ai/training/tf-cpu.2-5:latest`



#### Included dependencies

| PyPI packages | Ubuntu packages  
---|---  
tensorflow 2.5.x (latest patch)  
sympy 1.8  
xgboost 1.4.0  
PyYAML 3.13  
python-json-logger 2.0.1  
WebOb 1.8.7  
Paste 3.5.0  
webapp2 3.0.0b1  
mock 4.0.3  
google-cloud-resource-manager 0.30.3  
cloudml-hypertune  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software) |  curl  
libcurl3-dev  
wget  
zip  
unzip  
git  
vim  
build-essential  
ca-certificates  
pkg-config  
rsync  
ca-certificates-java  
libatlas-base-dev  
liblapack-dev  
gfortran  
libpng-dev  
libjpeg-dev  
python3.7  
python3-dev  
python3.7-dev  
python3-pip  
python3-setuptools  
python2.7  
python-dev  
python-setuptools  
gdb  
openjdk-8-jdk  
openjdk-8-jre-headless  
g++  
zlib1g-dev  
libio-all-perl  
module-init-tools  
libsnappy-dev  
libyaml-0-2  
python-opencv  
  
  
2.5 (Python 3.7) | GPU (CUDA 11.x) | Sep 1, 2023 | Sep 1, 2024 | 

  * `us-docker.pkg.dev/vertex-ai/training/tf-gpu.2-5:latest`
  * `europe-docker.pkg.dev/vertex-ai/training/tf-gpu.2-5:latest`
  * `asia-docker.pkg.dev/vertex-ai/training/tf-gpu.2-5:latest`



#### Included dependencies

| PyPI packages | Ubuntu packages  
---|---  
tensorflow 2.5.x (latest patch)  
sympy 1.8  
xgboost 1.4.0  
PyYAML 3.13  
python-json-logger 2.0.1  
WebOb 1.8.7  
Paste 3.5.0  
webapp2 3.0.0b1  
mock 4.0.3  
google-cloud-resource-manager 0.30.3  
cloudml-hypertune  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software) |  curl  
libcurl3-dev  
wget  
zip  
unzip  
git  
vim  
build-essential  
ca-certificates  
pkg-config  
rsync  
ca-certificates-java  
libatlas-base-dev  
liblapack-dev  
gfortran  
libpng-dev  
libjpeg-dev  
python3.7  
python3-dev  
python3.7-dev  
python3-pip  
python3-setuptools  
python2.7  
python-dev  
python-setuptools  
gdb  
openjdk-8-jdk  
openjdk-8-jre-headless  
g++  
zlib1g-dev  
libio-all-perl  
module-init-tools  
libsnappy-dev  
libyaml-0-2  
python-opencv  
  
  
2.4 (Python 3.7) | CPU only | Sep 1, 2023 | Sep 1, 2024 | 

  * `us-docker.pkg.dev/vertex-ai/training/tf-cpu.2-4:latest`
  * `europe-docker.pkg.dev/vertex-ai/training/tf-cpu.2-4:latest`
  * `asia-docker.pkg.dev/vertex-ai/training/tf-cpu.2-4:latest`



#### Included dependencies

| PyPI packages | Ubuntu packages  
---|---  
tensorflow 2.4.x (latest patch)  
numpy 1.19.4  
pandas 1.1.5  
scipy 1.5.4  
scikit-learn 0.24.0  
sympy 1.7.1  
statsmodels 0.12.1  
xgboost 1.3.1  
oauth2client 4.1.3  
httplib2 0.15.0  
python-dateutil 2.8.1  
six 1.15.0  
future 0.18.2  
PyYAML 3.13  
wrapt 1.12.1  
crcmod 1.7  
google-api-python-client 1.9.0  
python-json-logger 2.0.1  
wheel 0.36.2  
WebOb 1.8.6  
Paste 3.5.0  
tornado 5.1.1  
grpcio 1.32.0  
requests 2.25.1  
webapp2 3.0.0b1  
mock 4.0.3  
google-cloud-bigquery 2.6.1  
google-cloud-bigtable 1.6.1  
google-cloud-datastore 2.1.0  
google-cloud-logging 1.15.0  
google-cloud-pubsub 2.2.0  
google-cloud-resource-manager 0.30.3  
google-cloud-storage 1.35.0  
joblib 1.0.0  
cloudml-hypertune  
psutil 5.8.0  |  curl  
libcurl3-dev  
wget  
zip  
unzip  
git  
vim  
build-essential  
ca-certificates  
pkg-config  
rsync  
ca-certificates-java  
libatlas-base-dev  
liblapack-dev  
gfortran  
libpng-dev  
libjpeg-dev  
python3.7  
python3-dev  
python3.7-dev  
python3-pip  
python3-setuptools  
python2.7  
python-dev  
python-setuptools  
gdb  
openjdk-8-jdk  
openjdk-8-jre-headless  
g++  
zlib1g-dev  
libio-all-perl  
module-init-tools  
libsnappy-dev  
libyaml-0-2  
python-opencv  
  
  
2.4 (Python 3.7) | GPU (CUDA 11.x) | Sep 1, 2023 | Sep 1, 2024 | 

  * `us-docker.pkg.dev/vertex-ai/training/tf-gpu.2-4:latest`
  * `europe-docker.pkg.dev/vertex-ai/training/tf-gpu.2-4:latest`
  * `asia-docker.pkg.dev/vertex-ai/training/tf-gpu.2-4:latest`



#### Included dependencies

| PyPI packages | Ubuntu packages  
---|---  
tensorflow 2.4.x (latest patch)  
numpy 1.19.4  
pandas 1.1.5  
scipy 1.5.4  
scikit-learn 0.24.0  
sympy 1.7.1  
statsmodels 0.12.1  
xgboost 1.3.1  
oauth2client 4.1.3  
httplib2 0.15.0  
python-dateutil 2.8.1  
six 1.15.0  
future 0.18.2  
PyYAML 3.13  
wrapt 1.12.1  
crcmod 1.7  
google-api-python-client 1.9.0  
python-json-logger 2.0.1  
wheel 0.36.2  
WebOb 1.8.6  
Paste 3.5.0  
tornado 5.1.1  
grpcio 1.32.0  
requests 2.25.1  
webapp2 3.0.0b1  
mock 4.0.3  
google-cloud-bigquery 2.6.1  
google-cloud-bigtable 1.6.1  
google-cloud-datastore 2.1.0  
google-cloud-logging 1.15.0  
google-cloud-pubsub 2.2.0  
google-cloud-resource-manager 0.30.3  
google-cloud-storage 1.35.0  
joblib 1.0.0  
cloudml-hypertune  
psutil 5.8.0  |  curl  
libcurl3-dev  
wget  
zip  
unzip  
git  
vim  
build-essential  
ca-certificates  
pkg-config  
rsync  
ca-certificates-java  
libatlas-base-dev  
liblapack-dev  
gfortran  
libpng-dev  
libjpeg-dev  
python3.7  
python3-dev  
python3.7-dev  
python3-pip  
python3-setuptools  
python2.7  
python-dev  
python-setuptools  
gdb  
openjdk-8-jdk  
openjdk-8-jre-headless  
g++  
zlib1g-dev  
libio-all-perl  
module-init-tools  
libsnappy-dev  
libyaml-0-2  
python-opencv  
  
  
2.3 (Python 3.7) | CPU only | Sep 1, 2023 | Sep 1, 2024 | 

  * `us-docker.pkg.dev/vertex-ai/training/tf-cpu.2-3:latest`
  * `europe-docker.pkg.dev/vertex-ai/training/tf-cpu.2-3:latest`
  * `asia-docker.pkg.dev/vertex-ai/training/tf-cpu.2-3:latest`



#### Included dependencies

| PyPI packages | Ubuntu packages  
---|---  
tensorflow 2.3.x (latest patch)  
numpy 1.18.5  
pandas 1.1.3  
scipy 1.4.1  
scikit-learn 0.23.2  
sympy 1.6.2  
statsmodels 0.12.0  
xgboost 1.2.1  
oauth2client 4.1.3  
httplib2 0.15.0  
python-dateutil 2.8.1  
six 1.15.0  
future 0.18.2  
PyYAML 3.13  
wrapt 1.12.1  
crcmod 1.7  
google-api-python-client 1.9.0  
python-json-logger 2.0.1  
wheel 0.35.1  
WebOb 1.8.6  
Paste 3.5.0  
tornado 5.1.1  
grpcio 1.33.1  
requests 2.24.0  
webapp2 3.0.0b1  
mock 4.0.2  
google-cloud-bigquery 2.2.0  
google-cloud-bigtable 1.5.1  
google-cloud-datastore 1.15.3  
google-cloud-logging 1.15.0  
google-cloud-pubsub 2.1.0  
google-cloud-resource-manager 0.30.2  
google-cloud-storage 1.32.0  
joblib 0.17.0  
cloudml-hypertune  
psutil 5.7.2  |  curl  
libcurl3-dev  
wget  
zip  
unzip  
git  
vim  
build-essential  
ca-certificates  
pkg-config  
rsync  
ca-certificates-java  
libatlas-base-dev  
liblapack-dev  
gfortran  
libpng-dev  
libjpeg-dev  
python3.7  
python3-dev  
python3.7-dev  
python3-pip  
python3-setuptools  
python2.7  
python-dev  
python-setuptools  
gdb  
openjdk-8-jdk  
openjdk-8-jre-headless  
g++  
zlib1g-dev  
libio-all-perl  
module-init-tools  
libsnappy-dev  
libyaml-0-2  
python-opencv  
  
  
2.3 (Python 3.7) | GPU (CUDA 11.x) | Sep 1, 2023 | Sep 1, 2024 | 

  * `us-docker.pkg.dev/vertex-ai/training/tf-gpu.2-3:latest`
  * `europe-docker.pkg.dev/vertex-ai/training/tf-gpu.2-3:latest`
  * `asia-docker.pkg.dev/vertex-ai/training/tf-gpu.2-3:latest`



#### Included dependencies

| PyPI packages | Ubuntu packages  
---|---  
tensorflow 2.3.x (latest patch)  
numpy 1.18.5  
pandas 1.1.3  
scipy 1.4.1  
scikit-learn 0.23.2  
sympy 1.6.2  
statsmodels 0.12.0  
xgboost 1.2.1  
oauth2client 4.1.3  
httplib2 0.15.0  
python-dateutil 2.8.1  
six 1.15.0  
future 0.18.2  
PyYAML 3.13  
wrapt 1.12.1  
crcmod 1.7  
google-api-python-client 1.9.0  
python-json-logger 2.0.1  
wheel 0.35.1  
WebOb 1.8.6  
Paste 3.5.0  
tornado 5.1.1  
grpcio 1.33.1  
requests 2.24.0  
webapp2 3.0.0b1  
mock 4.0.2  
google-cloud-bigquery 2.2.0  
google-cloud-bigtable 1.5.1  
google-cloud-datastore 1.15.3  
google-cloud-logging 1.15.0  
google-cloud-pubsub 2.1.0  
google-cloud-resource-manager 0.30.2  
google-cloud-storage 1.32.0  
joblib 0.17.0  
cloudml-hypertune  
psutil 5.7.2  |  curl  
libcurl3-dev  
wget  
zip  
unzip  
git  
vim  
build-essential  
ca-certificates  
pkg-config  
rsync  
ca-certificates-java  
libatlas-base-dev  
liblapack-dev  
gfortran  
libpng-dev  
libjpeg-dev  
python3.7  
python3-dev  
python3.7-dev  
python3-pip  
python3-setuptools  
python2.7  
python-dev  
python-setuptools  
gdb  
openjdk-8-jdk  
openjdk-8-jre-headless  
g++  
zlib1g-dev  
libio-all-perl  
module-init-tools  
libsnappy-dev  
libyaml-0-2  
python-opencv  
  
  
2.2 (Python 3.7) | CPU only | Sep 1, 2023 | Sep 1, 2024 | 

  * `us-docker.pkg.dev/vertex-ai/training/tf-cpu.2-2:latest`
  * `europe-docker.pkg.dev/vertex-ai/training/tf-cpu.2-2:latest`
  * `asia-docker.pkg.dev/vertex-ai/training/tf-cpu.2-2:latest`



#### Included dependencies

| PyPI packages | Ubuntu packages  
---|---  
tensorflow 2.2.x (latest patch)  
numpy 1.18.5  
pandas 1.0.4  
scipy 1.4.1  
scikit-learn 0.23.1  
sympy 1.6  
statsmodels 0.11.1  
xgboost 1.1.1  
oauth2client 4.1.3  
httplib2 0.18.1  
python-dateutil 2.8.1  
six 1.15.0  
future 0.18.2  
PyYAML 5.3.1  
wrapt 1.12.1  
crcmod 1.7  
google-api-python-client 1.9.3  
python-json-logger 0.1.11  
wheel 0.34.2  
WebOb 1.8.6  
Paste 3.4.1  
tornado 5.1.1  
grpcio 1.29.0  
requests 2.23.0  
webapp2 3.0.0b1  
mock 4.0.2  
google-cloud-bigquery 1.25.0  
google-cloud-bigtable 1.2.1  
google-cloud-datastore 1.12.0  
google-cloud-logging 1.15.0  
google-cloud-pubsub 1.6.0  
google-cloud-resource-manager 0.30.2  
google-cloud-storage 1.29.0  
joblib 0.15.1  
cloudml-hypertune  
psutil 5.7.0  |  curl  
libcurl3-dev  
wget  
zip  
unzip  
git  
vim  
build-essential  
ca-certificates  
pkg-config  
rsync  
ca-certificates-java  
libatlas-base-dev  
liblapack-dev  
gfortran  
libpng-dev  
libjpeg-dev  
python3.7  
python3-dev  
python3.7-dev  
python3-pip  
python3-setuptools  
python2.7  
python-dev  
python-setuptools  
gdb  
openjdk-8-jdk  
openjdk-8-jre-headless  
g++  
zlib1g-dev  
libio-all-perl  
module-init-tools  
libsnappy-dev  
libyaml-0-2  
python-opencv  
  
  
2.2 (Python 3.7) | GPU (CUDA 11.x) | Sep 1, 2023 | Sep 1, 2024 | 

  * `us-docker.pkg.dev/vertex-ai/training/tf-gpu.2-2:latest`
  * `europe-docker.pkg.dev/vertex-ai/training/tf-gpu.2-2:latest`
  * `asia-docker.pkg.dev/vertex-ai/training/tf-gpu.2-2:latest`



#### Included dependencies

| PyPI packages | Ubuntu packages  
---|---  
tensorflow 2.2.x (latest patch)  
numpy 1.18.5  
pandas 1.0.4  
scipy 1.4.1  
scikit-learn 0.23.1  
sympy 1.6  
statsmodels 0.11.1  
xgboost 1.1.1  
oauth2client 4.1.3  
httplib2 0.18.1  
python-dateutil 2.8.1  
six 1.15.0  
future 0.18.2  
PyYAML 5.3.1  
wrapt 1.12.1  
crcmod 1.7  
google-api-python-client 1.9.3  
python-json-logger 0.1.11  
wheel 0.34.2  
WebOb 1.8.6  
Paste 3.4.1  
tornado 5.1.1  
grpcio 1.29.0  
requests 2.23.0  
webapp2 3.0.0b1  
mock 4.0.2  
google-cloud-bigquery 1.25.0  
google-cloud-bigtable 1.2.1  
google-cloud-datastore 1.12.0  
google-cloud-logging 1.15.0  
google-cloud-pubsub 1.6.0  
google-cloud-resource-manager 0.30.2  
google-cloud-storage 1.29.0  
joblib 0.15.1  
cloudml-hypertune  
psutil 5.7.0  |  curl  
libcurl3-dev  
wget  
zip  
unzip  
git  
vim  
build-essential  
ca-certificates  
pkg-config  
rsync  
ca-certificates-java  
libatlas-base-dev  
liblapack-dev  
gfortran  
libpng-dev  
libjpeg-dev  
python3.7  
python3-dev  
python3.7-dev  
python3-pip  
python3-setuptools  
python2.7  
python-dev  
python-setuptools  
gdb  
openjdk-8-jdk  
openjdk-8-jre-headless  
g++  
zlib1g-dev  
libio-all-perl  
module-init-tools  
libsnappy-dev  
libyaml-0-2  
python-opencv  
  
  
2.1 (Python 3.7) | CPU only | Sep 1, 2023 | Sep 1, 2024 | 

  * `us-docker.pkg.dev/vertex-ai/training/tf-cpu.2-1:latest`
  * `europe-docker.pkg.dev/vertex-ai/training/tf-cpu.2-1:latest`
  * `asia-docker.pkg.dev/vertex-ai/training/tf-cpu.2-1:latest`



#### Included dependencies

| PyPI packages | Ubuntu packages  
---|---  
tensorflow 2.1.0  
numpy 1.18.0  
pandas 0.25.3  
scipy 1.4.1  
scikit-learn 0.22.1  
sympy 1.5  
statsmodels 0.10.2  
xgboost 0.90  
oauth2client 4.1.3  
httplib2 0.15.0  
python-dateutil 2.8.1  
six 1.13.0  
future 0.18.2  
PyYAML 5.2  
wrapt 1.11.2  
crcmod 1.7  
google-api-python-client 1.7.11  
python-json-logger 0.1.11  
wheel 0.33.6  
WebOb 1.8.5  
Paste 3.2.3  
tornado 5.1.1  
grpcio 1.26.0  
requests 2.22.0  
webapp2 3.0.0b1  
mock 3.0.5  
google-cloud-bigquery 1.23.1  
google-cloud-bigtable 1.2.0  
google-cloud-datastore 1.10.0  
google-cloud-logging 1.14.0  
google-cloud-pubsub 1.1.0  
google-cloud-resource-manager 0.30.0  
google-cloud-storage 1.23.0  
joblib 0.14.1  
cloudml-hypertune  
psutil 5.7.0  
|  curl  
libcurl3-dev  
wget  
zip  
unzip  
git  
vim  
build-essential  
ca-certificates  
pkg-config  
rsync  
ca-certificates-java  
libatlas-base-dev  
liblapack-dev  
gfortran  
libpng-dev  
libjpeg-dev  
python3.7  
python3-dev  
python3.7-dev  
python3-pip  
python3-setuptools  
python2.7  
python-dev  
python-setuptools  
gdb  
openjdk-8-jdk  
openjdk-8-jre-headless  
g++  
zlib1g-dev  
libio-all-perl  
module-init-tools  
libsnappy-dev  
libyaml-0-2  
python-opencv  
  
  
2.1 (Python 3.7) | GPU (CUDA 11.x) | Sep 1, 2023 | Sep 1, 2024 | 

  * `us-docker.pkg.dev/vertex-ai/training/tf-gpu.2-1:latest`
  * `europe-docker.pkg.dev/vertex-ai/training/tf-gpu.2-1:latest`
  * `asia-docker.pkg.dev/vertex-ai/training/tf-gpu.2-1:latest`



#### Included dependencies

| PyPI packages | Ubuntu packages  
---|---  
tensorflow 2.1.0  
numpy 1.18.0  
pandas 0.25.3  
scipy 1.4.1  
scikit-learn 0.22.1  
sympy 1.5  
statsmodels 0.10.2  
xgboost 0.90  
oauth2client 4.1.3  
httplib2 0.15.0  
python-dateutil 2.8.1  
six 1.13.0  
future 0.18.2  
PyYAML 5.2  
wrapt 1.11.2  
crcmod 1.7  
google-api-python-client 1.7.11  
python-json-logger 0.1.11  
wheel 0.33.6  
WebOb 1.8.5  
Paste 3.2.3  
tornado 5.1.1  
grpcio 1.26.0  
requests 2.22.0  
webapp2 3.0.0b1  
mock 3.0.5  
google-cloud-bigquery 1.23.1  
google-cloud-bigtable 1.2.0  
google-cloud-datastore 1.10.0  
google-cloud-logging 1.14.0  
google-cloud-pubsub 1.1.0  
google-cloud-resource-manager 0.30.0  
google-cloud-storage 1.23.0  
joblib 0.14.1  
cloudml-hypertune  
psutil 5.7.0  
|  curl  
libcurl3-dev  
wget  
zip  
unzip  
git  
vim  
build-essential  
ca-certificates  
pkg-config  
rsync  
ca-certificates-java  
libatlas-base-dev  
liblapack-dev  
gfortran  
libpng-dev  
libjpeg-dev  
python3.7  
python3-dev  
python3.7-dev  
python3-pip  
python3-setuptools  
python2.7  
python-dev  
python-setuptools  
gdb  
openjdk-8-jdk  
openjdk-8-jre-headless  
g++  
zlib1g-dev  
libio-all-perl  
module-init-tools  
libsnappy-dev  
libyaml-0-2  
python-opencv  
  
  
1.15 (Python 3.7) | CPU only | Sep 1, 2023 | Sep 1, 2024 | 

  * `us-docker.pkg.dev/vertex-ai/training/tf-cpu.1-15:latest`
  * `europe-docker.pkg.dev/vertex-ai/training/tf-cpu.1-15:latest`
  * `asia-docker.pkg.dev/vertex-ai/training/tf-cpu.1-15:latest`



#### Included dependencies

| PyPI packages | Ubuntu packages  
---|---  
tensorflow 1.15.0  
numpy 1.16.5  
pandas 0.24.2  
scipy 1.2.2  
scikit-learn 0.20.4  
sympy 1.4  
statsmodels 0.10.1  
xgboost 0.82  
oauth2client 4.1.3  
httplib2 0.12.0  
python-dateutil 2.7.5  
argparse 1.4.0  
six 1.12.0  
future 0.17.1  
PyYAML 3.13  
wrapt 1.11.1  
crcmod 1.7  
google-api-python-client 1.7.8  
python-json-logger 0.1.10  
wheel 0.32.3  
WebOb 1.8.5  
Paste 3.0.6  
tornado 5.1.1  
grpcio 1.18.0  
requests 2.19.0  
webapp2 3.0.0b1  
mock 2.0.0  
google-cloud-bigquery 1.20.0  
google-cloud-bigtable 1.0.0  
google-cloud-datastore 1.9.0  
google-cloud-logging 1.12.1  
google-cloud-pubsub 1.0.0  
google-cloud-resource-manager 0.29.2  
google-cloud-storage 1.19.1  
joblib 0.13.0  
cloudml-hypertune  
psutil 5.7.0  
|  curl  
libcurl3-dev  
wget  
zip  
unzip  
git  
vim  
build-essential  
ca-certificates  
pkg-config  
rsync  
ca-certificates-java  
libatlas-base-dev  
liblapack-dev  
gfortran  
libpng-dev  
libjpeg-dev  
python3.7  
python3-dev  
python3.7-dev  
python3-pip  
python3-setuptools  
python2.7  
python-dev  
python-setuptools  
gdb  
openjdk-8-jdk  
openjdk-8-jre-headless  
g++  
zlib1g-dev  
libio-all-perl  
module-init-tools  
libsnappy-dev  
libyaml-0-2  
python-opencv  
  
  
1.15 (Python 3.7) | GPU (CUDA 11.x) | Sep 1, 2023 | Sep 1, 2024 | 

  * `us-docker.pkg.dev/vertex-ai/training/tf-gpu.1-15:latest`
  * `europe-docker.pkg.dev/vertex-ai/training/tf-gpu.1-15:latest`
  * `asia-docker.pkg.dev/vertex-ai/training/tf-gpu.1-15:latest`



#### Included dependencies

| PyPI packages | Ubuntu packages  
---|---  
tensorflow 1.15.0  
numpy 1.16.5  
pandas 0.24.2  
scipy 1.2.2  
scikit-learn 0.20.4  
sympy 1.4  
statsmodels 0.10.1  
xgboost 0.82  
oauth2client 4.1.3  
httplib2 0.12.0  
python-dateutil 2.7.5  
argparse 1.4.0  
six 1.12.0  
future 0.17.1  
PyYAML 3.13  
wrapt 1.11.1  
crcmod 1.7  
google-api-python-client 1.7.8  
python-json-logger 0.1.10  
wheel 0.32.3  
WebOb 1.8.5  
Paste 3.0.6  
tornado 5.1.1  
grpcio 1.18.0  
requests 2.19.0  
webapp2 3.0.0b1  
mock 2.0.0  
google-cloud-bigquery 1.20.0  
google-cloud-bigtable 1.0.0  
google-cloud-datastore 1.9.0  
google-cloud-logging 1.12.1  
google-cloud-pubsub 1.0.0  
google-cloud-resource-manager 0.29.2  
google-cloud-storage 1.19.1  
joblib 0.13.0  
cloudml-hypertune  
psutil 5.7.0  
|  curl  
libcurl3-dev  
wget  
zip  
unzip  
git  
vim  
build-essential  
ca-certificates  
pkg-config  
rsync  
ca-certificates-java  
libatlas-base-dev  
liblapack-dev  
gfortran  
libpng-dev  
libjpeg-dev  
python3.7  
python3-dev  
python3.7-dev  
python3-pip  
python3-setuptools  
python2.7  
python-dev  
python-setuptools  
gdb  
openjdk-8-jdk  
openjdk-8-jre-headless  
g++  
zlib1g-dev  
libio-all-perl  
module-init-tools  
libsnappy-dev  
libyaml-0-2  
python-opencv  
  
  
### PyTorch

ML framework version | Supported accelerators (and CUDA version, if applicable) | End of patch and support date | End of availability | Supported images  
---|---|---|---|---  
2.4 (Python 3.10) | CPU only | Jul 24, 2025 | Jul 24, 2026 | 

  * `us-docker.pkg.dev/vertex-ai/training/pytorch-xla.2-4.py310:latest`
  * `europe-docker.pkg.dev/vertex-ai/training/pytorch-xla.2-4.py310:latest`
  * `asia-docker.pkg.dev/vertex-ai/training/pytorch-xla.2-4.py310:latest`



#### Included dependencies

| PyPI packages | Ubuntu packages  
---|---  
PyTorch 2.4.x (latest patch)  
pandas 2.2.3  
absl-py 2.1.0  
cloud-tpu-client 0.10  
python-json-logger 3.2.1  
scikit-learn 1.6.1  
cloudml-hypertune  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software) |  curl  
libcurl3-dev  
wget  
zip  
unzip  
git  
vim  
build-essential  
ca-certificates  
pkg-config  
rsync  
ca-certificates-java  
libatlas-base-dev  
liblapack-dev  
gfortran  
libpng-dev  
libjpeg-dev  
python3.8  
python3-dev  
python3.7-dev  
python3-pip  
python3-setuptools  
gdb  
openjdk-8-jdk  
openjdk-8-jre-headless  
g++  
zlib1g-dev  
libio-all-perl  
module-init-tools  
libsnappy-dev  
libyaml-0-2  
python-opencv  
  
  
2.4 (Python 3.10) | GPU only (CUDA 12.x) | Jul 24, 2025 | Jul 24, 2026 | 

  * `us-docker.pkg.dev/vertex-ai/training/pytorch-gpu.2-4.py310:latest`
  * `europe-docker.pkg.dev/vertex-ai/training/pytorch-gpu.2-4.py310:latest`
  * `asia-docker.pkg.dev/vertex-ai/training/pytorch-gpu.2-4.py310:latest`



#### Included dependencies

| PyPI packages | Ubuntu packages  
---|---  
PyTorch 2.4.x (latest patch)  
pandas 2.2.3  
absl-py 2.1.0  
cloud-tpu-client 0.10  
python-json-logger 3.2.1  
scikit-learn 1.6.1  
cloudml-hypertune  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software) |  curl  
libcurl3-dev  
wget  
zip  
unzip  
git  
vim  
build-essential  
ca-certificates  
pkg-config  
rsync  
ca-certificates-java  
libatlas-base-dev  
liblapack-dev  
gfortran  
libpng-dev  
libjpeg-dev  
python3.8  
python3-dev  
python3.7-dev  
python3-pip  
python3-setuptools  
gdb  
openjdk-8-jdk  
openjdk-8-jre-headless  
g++  
zlib1g-dev  
libio-all-perl  
module-init-tools  
libsnappy-dev  
libyaml-0-2  
python-opencv  
  
  
2.3 (Python 3.10) | CPU only | Apr 24, 2025 | Apr 24, 2026 | 

  * `us-docker.pkg.dev/vertex-ai/training/pytorch-xla.2-3.py310:latest`
  * `europe-docker.pkg.dev/vertex-ai/training/pytorch-xla.2-3.py310:latest`
  * `asia-docker.pkg.dev/vertex-ai/training/pytorch-xla.2-3.py310:latest`



#### Included dependencies

| PyPI packages | Ubuntu packages  
---|---  
PyTorch 2.3.x (latest patch)  
absl-py 2.1.0  
cloud-tpu-client 0.10  
python-json-logger 2.0.7  
cloudml-hypertune  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software) |  curl  
libcurl3-dev  
wget  
zip  
unzip  
git  
vim  
build-essential  
ca-certificates  
pkg-config  
rsync  
ca-certificates-java  
libatlas-base-dev  
liblapack-dev  
gfortran  
libpng-dev  
libjpeg-dev  
python3.8  
python3-dev  
python3.7-dev  
python3-pip  
python3-setuptools  
gdb  
openjdk-8-jdk  
openjdk-8-jre-headless  
g++  
zlib1g-dev  
libio-all-perl  
module-init-tools  
libsnappy-dev  
libyaml-0-2  
python-opencv  
  
  
2.3 (Python 3.10) | GPU only (CUDA 12.x) | Apr 24, 2025 | Apr 24, 2026 | 

  * `us-docker.pkg.dev/vertex-ai/training/pytorch-gpu.2-3.py310:latest`
  * `europe-docker.pkg.dev/vertex-ai/training/pytorch-gpu.2-3.py310:latest`
  * `asia-docker.pkg.dev/vertex-ai/training/pytorch-gpu.2-3.py310:latest`



#### Included dependencies

| PyPI packages | Ubuntu packages  
---|---  
PyTorch 2.3.x (latest patch)  
absl-py 2.1.0  
cloud-tpu-client 0.10  
python-json-logger 2.0.7  
cloudml-hypertune  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software) |  curl  
libcurl3-dev  
wget  
zip  
unzip  
git  
vim  
build-essential  
ca-certificates  
pkg-config  
rsync  
ca-certificates-java  
libatlas-base-dev  
liblapack-dev  
gfortran  
libpng-dev  
libjpeg-dev  
python3.8  
python3-dev  
python3.7-dev  
python3-pip  
python3-setuptools  
gdb  
openjdk-8-jdk  
openjdk-8-jre-headless  
g++  
zlib1g-dev  
libio-all-perl  
module-init-tools  
libsnappy-dev  
libyaml-0-2  
python-opencv  
  
  
2.2 (Python 3.10) | CPU only | Jan 30, 2025 | Oct 23, 2026 | 

  * `us-docker.pkg.dev/vertex-ai/training/pytorch-xla.2-2.py310:latest`
  * `europe-docker.pkg.dev/vertex-ai/training/pytorch-xla.2-2.py310:latest`
  * `asia-docker.pkg.dev/vertex-ai/training/pytorch-xla.2-2.py310:latest`



#### Included dependencies

| PyPI packages | Ubuntu packages  
---|---  
PyTorch 2.2.x (latest patch)  
absl-py 2.1.0  
cloud-tpu-client 0.10  
python-json-logger 2.0.7  
cloudml-hypertune  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software) |  curl  
libcurl3-dev  
wget  
zip  
unzip  
git  
vim  
build-essential  
ca-certificates  
pkg-config  
rsync  
ca-certificates-java  
libatlas-base-dev  
liblapack-dev  
gfortran  
libpng-dev  
libjpeg-dev  
python3.8  
python3-dev  
python3.7-dev  
python3-pip  
python3-setuptools  
gdb  
openjdk-8-jdk  
openjdk-8-jre-headless  
g++  
zlib1g-dev  
libio-all-perl  
module-init-tools  
libsnappy-dev  
libyaml-0-2  
python-opencv  
  
  
2.2 (Python 3.10) | GPU only (CUDA 12.x) | Jan 30, 2025 | Jan 30, 2026 | 

  * `us-docker.pkg.dev/vertex-ai/training/pytorch-gpu.2-2.py310:latest`
  * `europe-docker.pkg.dev/vertex-ai/training/pytorch-gpu.2-2.py310:latest`
  * `asia-docker.pkg.dev/vertex-ai/training/pytorch-gpu.2-2.py310:latest`



#### Included dependencies

| PyPI packages | Ubuntu packages  
---|---  
PyTorch 2.2.x (latest patch)  
absl-py 2.1.0  
cloud-tpu-client 0.10  
python-json-logger 2.0.7  
cloudml-hypertune  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software) |  curl  
libcurl3-dev  
wget  
zip  
unzip  
git  
vim  
build-essential  
ca-certificates  
pkg-config  
rsync  
ca-certificates-java  
libatlas-base-dev  
liblapack-dev  
gfortran  
libpng-dev  
libjpeg-dev  
python3.8  
python3-dev  
python3.7-dev  
python3-pip  
python3-setuptools  
gdb  
openjdk-8-jdk  
openjdk-8-jre-headless  
g++  
zlib1g-dev  
libio-all-perl  
module-init-tools  
libsnappy-dev  
libyaml-0-2  
python-opencv  
  
  
2.2 (Python 3.10) | TPU only | Nov 6, 2024 | Nov 6, 2025 | 

  * `us-docker.pkg.dev/vertex-ai/training/pytorch-tpu.2-2.cp310:latest`
  * `europe-docker.pkg.dev/vertex-ai/training/pytorch-tpu.2-2.cp310:latest`
  * `asia-docker.pkg.dev/vertex-ai/training/pytorch-tpu.2-2.cp310:latest`



#### Included dependencies

| PyPI packages | Ubuntu packages  
---|---  
PyTorch 2.2.x (latest patch)  
absl-py 2.1.0  
cloud-tpu-client 0.10  
python-json-logger 2.0.7  
tpu-info  
cloudml-hypertune  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software) |  curl  
libcurl3-dev  
wget  
zip  
unzip  
git  
vim  
build-essential  
ca-certificates  
pkg-config  
rsync  
ca-certificates-java  
libatlas-base-dev  
liblapack-dev  
gfortran  
libpng-dev  
libjpeg-dev  
python3.8  
python3-dev  
python3.7-dev  
python3-pip  
python3-setuptools  
gdb  
openjdk-8-jdk  
openjdk-8-jre-headless  
g++  
zlib1g-dev  
libio-all-perl  
module-init-tools  
libsnappy-dev  
libyaml-0-2  
python-opencv  
  
  
2.1 (Python 3.10) | CPU only | Oct 4, 2024 | Oct 4, 2025 | 

  * `us-docker.pkg.dev/vertex-ai/training/pytorch-xla.2-1.py310:latest`
  * `europe-docker.pkg.dev/vertex-ai/training/pytorch-xla.2-1.py310:latest`
  * `asia-docker.pkg.dev/vertex-ai/training/pytorch-xla.2-1.py310:latest`



#### Included dependencies

| PyPI packages | Ubuntu packages  
---|---  
PyTorch 2.1.x (latest patch)  
absl-py 2.1.0  
cloud-tpu-client 0.10  
python-json-logger 2.0.7  
cloudml-hypertune  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software) |  curl  
libcurl3-dev  
wget  
zip  
unzip  
git  
vim  
build-essential  
ca-certificates  
pkg-config  
rsync  
ca-certificates-java  
libatlas-base-dev  
liblapack-dev  
gfortran  
libpng-dev  
libjpeg-dev  
python3.8  
python3-dev  
python3.7-dev  
python3-pip  
python3-setuptools  
gdb  
openjdk-8-jdk  
openjdk-8-jre-headless  
g++  
zlib1g-dev  
libio-all-perl  
module-init-tools  
libsnappy-dev  
libyaml-0-2  
python-opencv  
  
  
2.1 (Python 3.10) | GPU only (CUDA 12.x) | Oct 4, 2024  | Oct 4, 2025 | 

  * `us-docker.pkg.dev/vertex-ai/training/pytorch-gpu.2-1.py310:latest`
  * `europe-docker.pkg.dev/vertex-ai/training/pytorch-gpu.2-1.py310:latest`
  * `asia-docker.pkg.dev/vertex-ai/training/pytorch-gpu.2-1.py310:latest`



#### Included dependencies

| PyPI packages | Ubuntu packages  
---|---  
PyTorch 2.1.x (latest patch)  
absl-py 2.1.0  
cloud-tpu-client 0.10  
python-json-logger 2.0.7  
cloudml-hypertune  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software) |  curl  
libcurl3-dev  
wget  
zip  
unzip  
git  
vim  
build-essential  
ca-certificates  
pkg-config  
rsync  
ca-certificates-java  
libatlas-base-dev  
liblapack-dev  
gfortran  
libpng-dev  
libjpeg-dev  
python3.8  
python3-dev  
python3.7-dev  
python3-pip  
python3-setuptools  
gdb  
openjdk-8-jdk  
openjdk-8-jre-headless  
g++  
zlib1g-dev  
libio-all-perl  
module-init-tools  
libsnappy-dev  
libyaml-0-2  
python-opencv  
  
  
2.1 (Python 3.8) | TPU only | Oct 23, 2024 | Oct 23, 2025 | 

  * `us-docker.pkg.dev/vertex-ai/training/pytorch-tpu.2-1.cp310:latest`
  * `europe-docker.pkg.dev/vertex-ai/training/pytorch-tpu.2-1.cp310:latest`
  * `asia-docker.pkg.dev/vertex-ai/training/pytorch-tpu.2-1.cp310:latest`



#### Included dependencies

| PyPI packages | Ubuntu packages  
---|---  
PyTorch 2.3.x (latest patch)  
absl-py 2.1.0  
cloud-tpu-client 0.10  
python-json-logger 2.0.7  
tpu-info  
cloudml-hypertune  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software) |  curl  
libcurl3-dev  
wget  
zip  
unzip  
git  
vim  
build-essential  
ca-certificates  
pkg-config  
rsync  
ca-certificates-java  
libatlas-base-dev  
liblapack-dev  
gfortran  
libpng-dev  
libjpeg-dev  
python3.8  
python3-dev  
python3.7-dev  
python3-pip  
python3-setuptools  
gdb  
openjdk-8-jdk  
openjdk-8-jre-headless  
g++  
zlib1g-dev  
libio-all-perl  
module-init-tools  
libsnappy-dev  
libyaml-0-2  
python-opencv  
  
  
2.0 (Python 3.10) | CPU only | Mar 15, 2024 | Mar 15, 2025 | 

  * `us-docker.pkg.dev/vertex-ai/training/pytorch-xla.2-0.py310:latest`
  * `europe-docker.pkg.dev/vertex-ai/training/pytorch-xla.2-0.py310:latest`
  * `asia-docker.pkg.dev/vertex-ai/training/pytorch-xla.2-0.py310:latest`



#### Included dependencies

| PyPI packages | Ubuntu packages  
---|---  
PyTorch 2.0.x (latest patch)  
absl-py 2.1.0  
cloud-tpu-client 0.10  
python-json-logger 2.0.7  
cloudml-hypertune  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software) |  curl  
libcurl3-dev  
wget  
zip  
unzip  
git  
vim  
build-essential  
ca-certificates  
pkg-config  
rsync  
ca-certificates-java  
libatlas-base-dev  
liblapack-dev  
gfortran  
libpng-dev  
libjpeg-dev  
python3.8  
python3-dev  
python3.7-dev  
python3-pip  
python3-setuptools  
gdb  
openjdk-8-jdk  
openjdk-8-jre-headless  
g++  
zlib1g-dev  
libio-all-perl  
module-init-tools  
libsnappy-dev  
libyaml-0-2  
python-opencv  
  
  
2.0 (Python 3.10) | GPU only (CUDA 11.x) | Mar 15, 2024 | Mar 15, 2025 | 

  * `us-docker.pkg.dev/vertex-ai/training/pytorch-gpu.2-0.py310:latest`
  * `europe-docker.pkg.dev/vertex-ai/training/pytorch-gpu.2-0.py310:latest`
  * `asia-docker.pkg.dev/vertex-ai/training/pytorch-gpu.2-0.py310:latest`



#### Included dependencies

| PyPI packages | Ubuntu packages  
---|---  
PyTorch 2.0.x (latest patch)  
absl-py 2.1.0  
cloud-tpu-client 0.10  
python-json-logger 2.0.7  
cloudml-hypertune  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software) |  curl  
libcurl3-dev  
wget  
zip  
unzip  
git  
vim  
build-essential  
ca-certificates  
pkg-config  
rsync  
ca-certificates-java  
libatlas-base-dev  
liblapack-dev  
gfortran  
libpng-dev  
libjpeg-dev  
python3.8  
python3-dev  
python3.7-dev  
python3-pip  
python3-setuptools  
gdb  
openjdk-8-jdk  
openjdk-8-jre-headless  
g++  
zlib1g-dev  
libio-all-perl  
module-init-tools  
libsnappy-dev  
libyaml-0-2  
python-opencv  
  
  
2.0 (Python 3.8) | TPU only | May 15, 2024 | May 15, 2025 | 

  * `us-docker.pkg.dev/vertex-ai/training/pytorch-tpu.2-0:latest`
  * `europe-docker.pkg.dev/vertex-ai/training/pytorch-tpu.2-0:latest`
  * `asia-docker.pkg.dev/vertex-ai/training/pytorch-tpu.2-0:latest`



#### Included dependencies

| PyPI packages | Ubuntu packages  
---|---  
PyTorch 2.0.x (latest patch)  
absl-py 2.1.0  
cloud-tpu-client 0.10  
python-json-logger 2.0.7  
cloudml-hypertune  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software) |  curl  
libcurl3-dev  
wget  
zip  
unzip  
git  
vim  
build-essential  
ca-certificates  
pkg-config  
rsync  
ca-certificates-java  
libatlas-base-dev  
liblapack-dev  
gfortran  
libpng-dev  
libjpeg-dev  
python3.8  
python3-dev  
python3.7-dev  
python3-pip  
python3-setuptools  
gdb  
openjdk-8-jdk  
openjdk-8-jre-headless  
g++  
zlib1g-dev  
libio-all-perl  
module-init-tools  
libsnappy-dev  
libyaml-0-2  
python-opencv  
  
  
1.13 (Python 3.10) | CPU or GPU (CUDA 11.x) | May 15, 2024 | May 15, 2025 | 

  * `us-docker.pkg.dev/vertex-ai/training/pytorch-gpu.1-13.py310:latest`
  * `europe-docker.pkg.dev/vertex-ai/training/pytorch-gpu.1-13.py310:latest`
  * `asia-docker.pkg.dev/vertex-ai/training/pytorch-gpu.1-13.py310:latest`



#### Included dependencies

| PyPI packages | Ubuntu packages  
---|---  
PyTorch 1.13.x (latest patch)  
absl-py 1.3.0  
cloud-tpu-client 0.10  
python-json-logger 2.0.4  
cloudml-hypertune  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software) |  ca-certificates-java  
libatlas-base-dev  
liblapack-dev  
gfortran  
gdb  
openjdk-8-jdk  
openjdk-8-jre-headless  
g++  
libio-all-perl  
libyaml-0-2  
  
  
1.13 (Python 3.7) | CPU or GPU (CUDA 11.x) | Dec 8, 2023 | Dec 8, 2024 | 

  * `us-docker.pkg.dev/vertex-ai/training/pytorch-gpu.1-13:latest`
  * `europe-docker.pkg.dev/vertex-ai/training/pytorch-gpu.1-13:latest`
  * `asia-docker.pkg.dev/vertex-ai/training/pytorch-gpu.1-13:latest`



#### Included dependencies

| PyPI packages | Ubuntu packages  
---|---  
PyTorch 1.13.x (latest patch)  
absl-py 1.3.0  
cloud-tpu-client 0.10  
python-json-logger 2.0.4  
cloudml-hypertune  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software) |  ca-certificates-java  
libatlas-base-dev  
liblapack-dev  
gfortran  
gdb  
openjdk-8-jdk  
openjdk-8-jre-headless  
g++  
libio-all-perl  
libyaml-0-2  
  
  
1.12 (Python 3.10) | CPU or GPU (CUDA 11.x) | May 15, 2024 | May 15, 2025 | 

  * `us-docker.pkg.dev/vertex-ai/training/pytorch-gpu.1-12.py310:latest`
  * `europe-docker.pkg.dev/vertex-ai/training/pytorch-gpu.1-12.py310:latest`
  * `asia-docker.pkg.dev/vertex-ai/training/pytorch-gpu.1-12.py310:latest`



#### Included dependencies

| PyPI packages | Ubuntu packages  
---|---  
PyTorch 1.12.x (latest patch)  
absl-py 1.3.0  
cloud-tpu-client 0.10  
python-json-logger 2.0.4  
cloudml-hypertune  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software) |  ca-certificates-java  
libatlas-base-dev  
liblapack-dev  
gfortran  
gdb  
openjdk-8-jdk  
openjdk-8-jre-headless  
g++  
libio-all-perl  
libyaml-0-2  
  
  
1.12 (Python 3.7) | CPU or GPU (CUDA 11.x) | Sep 1, 2023 | Sep 1, 2024 | 

  * `us-docker.pkg.dev/vertex-ai/training/pytorch-gpu.1-12:latest`
  * `europe-docker.pkg.dev/vertex-ai/training/pytorch-gpu.1-12:latest`
  * `asia-docker.pkg.dev/vertex-ai/training/pytorch-gpu.1-12:latest`



#### Included dependencies

| PyPI packages | Ubuntu packages  
---|---  
PyTorch 1.12.x (latest patch)  
absl-py 1.3.0  
cloud-tpu-client 0.10  
python-json-logger 2.0.4  
cloudml-hypertune  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software) |  ca-certificates-java  
libatlas-base-dev  
liblapack-dev  
gfortran  
gdb  
openjdk-8-jdk  
openjdk-8-jre-headless  
g++  
libio-all-perl  
libyaml-0-2  
  
  
1.11 (Python 3.7) | CPU only | Sep 1, 2023 | Sep 1, 2024 | 

  * `us-docker.pkg.dev/vertex-ai/training/pytorch-xla.1-11:latest`
  * `europe-docker.pkg.dev/vertex-ai/training/pytorch-xla.1-11:latest`
  * `asia-docker.pkg.dev/vertex-ai/training/pytorch-xla.1-11:latest`



#### Included dependencies

| PyPI packages | Ubuntu packages  
---|---  
PyTorch 1.11.x (latest patch)  
absl-py 1.0.0  
cloud-tpu-client 0.10  
python-json-logger 2.0.2  
cloudml-hypertune  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software) |  ca-certificates-java  
libatlas-base-dev  
liblapack-dev  
gfortran  
gdb  
openjdk-8-jdk  
openjdk-8-jre-headless  
g++  
libio-all-perl  
libyaml-0-2  
  
  
1.11 (Python 3.7) | GPU (CUDA 11.x) | Sep 1, 2023 | Sep 1, 2024 | 

  * `us-docker.pkg.dev/vertex-ai/training/pytorch-gpu.1-11:latest`
  * `europe-docker.pkg.dev/vertex-ai/training/pytorch-gpu.1-11:latest`
  * `asia-docker.pkg.dev/vertex-ai/training/pytorch-gpu.1-11:latest`



#### Included dependencies

| PyPI packages | Ubuntu packages  
---|---  
PyTorch 1.11.x (latest patch)  
absl-py 1.0.0  
cloud-tpu-client 0.10  
python-json-logger 2.0.2  
cloudml-hypertune  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software) |  ca-certificates-java  
libatlas-base-dev  
liblapack-dev  
gfortran  
gdb  
openjdk-8-jdk  
openjdk-8-jre-headless  
g++  
libio-all-perl  
libyaml-0-2  
  
  
1.10 (Python 3.7) | CPU only | Sep 1, 2023 | Sep 1, 2024 | 

  * `us-docker.pkg.dev/vertex-ai/training/pytorch-xla.1-10:latest`
  * `europe-docker.pkg.dev/vertex-ai/training/pytorch-xla.1-10:latest`
  * `asia-docker.pkg.dev/vertex-ai/training/pytorch-xla.1-10:latest`



#### Included dependencies

| PyPI packages | Ubuntu packages  
---|---  
PyTorch 1.10.x (latest patch)  
absl-py 1.0.0  
cloud-tpu-client 0.10  
python-json-logger 2.0.2  
cloudml-hypertune  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software) |  ca-certificates-java  
libatlas-base-dev  
liblapack-dev  
gfortran  
gdb  
openjdk-8-jdk  
openjdk-8-jre-headless  
g++  
libio-all-perl  
libyaml-0-2  
  
  
1.10 (Python 3.7) | GPU (CUDA 11.x) | Sep 1, 2023 | Sep 1, 2024 | 

  * `us-docker.pkg.dev/vertex-ai/training/pytorch-gpu.1-10:latest`
  * `europe-docker.pkg.dev/vertex-ai/training/pytorch-gpu.1-10:latest`
  * `asia-docker.pkg.dev/vertex-ai/training/pytorch-gpu.1-10:latest`



#### Included dependencies

| PyPI packages | Ubuntu packages  
---|---  
PyTorch 1.10.x (latest patch)  
absl-py 1.0.0  
cloud-tpu-client 0.10  
python-json-logger 2.0.2  
cloudml-hypertune  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software) |  ca-certificates-java  
libatlas-base-dev  
liblapack-dev  
gfortran  
gdb  
openjdk-8-jdk  
openjdk-8-jre-headless  
g++  
libio-all-perl  
libyaml-0-2  
  
  
1.9 (Python 3.7) | CPU only | Sep 1, 2023 | Sep 1, 2024 | 

  * `us-docker.pkg.dev/vertex-ai/training/pytorch-xla.1-9:latest`
  * `europe-docker.pkg.dev/vertex-ai/training/pytorch-xla.1-9:latest`
  * `asia-docker.pkg.dev/vertex-ai/training/pytorch-xla.1-9:latest`



#### Included dependencies

| PyPI packages | Ubuntu packages  
---|---  
PyTorch 1.9.x (latest patch)  
absl-py 0.13.0  
cloud-tpu-client 0.10  
python-json-logger 2.0.2  
cloudml-hypertune  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software) |  curl  
libcurl3-dev  
wget  
zip  
unzip  
git  
vim  
build-essential  
ca-certificates  
pkg-config  
rsync  
ca-certificates-java  
libatlas-base-dev  
liblapack-dev  
gfortran  
libpng-dev  
libjpeg-dev  
python3.7  
python3-dev  
python3.7-dev  
python3-pip  
python3-setuptools  
python2.7  
python-dev  
python-setuptools  
gdb  
openjdk-8-jdk  
openjdk-8-jre-headless  
g++  
zlib1g-dev  
libio-all-perl  
module-init-tools  
libsnappy-dev  
libyaml-0-2  
python-opencv  
  
  
1.9 (Python 3.7) | GPU (CUDA 11.x) | Sep 1, 2023 | Sep 1, 2024 | 

  * `us-docker.pkg.dev/vertex-ai/training/pytorch-gpu.1-9:latest`
  * `europe-docker.pkg.dev/vertex-ai/training/pytorch-gpu.1-9:latest`
  * `asia-docker.pkg.dev/vertex-ai/training/pytorch-gpu.1-9:latest`



#### Included dependencies

| PyPI packages | Ubuntu packages  
---|---  
PyTorch 1.9.x (latest patch)  
absl-py 0.13.0  
cloud-tpu-client 0.10  
python-json-logger 2.0.2  
cloudml-hypertune  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software) |  curl  
libcurl3-dev  
wget  
zip  
unzip  
git  
vim  
build-essential  
ca-certificates  
pkg-config  
rsync  
ca-certificates-java  
libatlas-base-dev  
liblapack-dev  
gfortran  
libpng-dev  
libjpeg-dev  
python3.7  
python3-dev  
python3.7-dev  
python3-pip  
python3-setuptools  
python2.7  
python-dev  
python-setuptools  
gdb  
openjdk-8-jdk  
openjdk-8-jre-headless  
g++  
zlib1g-dev  
libio-all-perl  
module-init-tools  
libsnappy-dev  
libyaml-0-2  
python-opencv  
  
  
1.7 (Python 3.7) | CPU only | Sep 1, 2023 | Sep 1, 2024 | 

  * `us-docker.pkg.dev/vertex-ai/training/pytorch-xla.1-7:latest`
  * `europe-docker.pkg.dev/vertex-ai/training/pytorch-xla.1-7:latest`
  * `asia-docker.pkg.dev/vertex-ai/training/pytorch-xla.1-7:latest`



#### Included dependencies

[Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software)  
1.7 (Python 3.7) | GPU (CUDA 11.x) | Sep 1, 2023 | Sep 1, 2024 | 

  * `us-docker.pkg.dev/vertex-ai/training/pytorch-gpu.1-7:latest`
  * `europe-docker.pkg.dev/vertex-ai/training/pytorch-gpu.1-7:latest`
  * `asia-docker.pkg.dev/vertex-ai/training/pytorch-gpu.1-7:latest`



#### Included dependencies

[Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software)  
1.6 (Python 3.7) | CPU only | Sep 1, 2023 | Sep 1, 2024 | 

  * `us-docker.pkg.dev/vertex-ai/training/pytorch-xla.1-6:latest`
  * `europe-docker.pkg.dev/vertex-ai/training/pytorch-xla.1-6:latest`
  * `asia-docker.pkg.dev/vertex-ai/training/pytorch-xla.1-6:latest`



#### Included dependencies

[Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software)  
1.6 (Python 3.7) | GPU (CUDA 11.x) | Sep 1, 2023 | Sep 1, 2024 | 

  * `us-docker.pkg.dev/vertex-ai/training/pytorch-gpu.1-6:latest`
  * `europe-docker.pkg.dev/vertex-ai/training/pytorch-gpu.1-6:latest`
  * `asia-docker.pkg.dev/vertex-ai/training/pytorch-gpu.1-6:latest`



#### Included dependencies

[Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software)  
1.4 (Python 3.7) | CPU only | Sep 1, 2023 | Sep 1, 2024 | 

  * `us-docker.pkg.dev/vertex-ai/training/pytorch-cpu.1-4:latest`
  * `europe-docker.pkg.dev/vertex-ai/training/pytorch-cpu.1-4:latest`
  * `asia-docker.pkg.dev/vertex-ai/training/pytorch-cpu.1-4:latest`



#### Included dependencies

[Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software)  
1.4 (Python 3.7) | GPU (CUDA 11.x) | Sep 1, 2023 | Sep 1, 2024 | 

  * `us-docker.pkg.dev/vertex-ai/training/pytorch-gpu.1-4:latest`
  * `europe-docker.pkg.dev/vertex-ai/training/pytorch-gpu.1-4:latest`
  * `asia-docker.pkg.dev/vertex-ai/training/pytorch-gpu.1-4:latest`



#### Included dependencies

[Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software)  
  
### scikit-learn

ML framework version | Supported accelerators (and CUDA version, if applicable) | End of patch and support date | End of availability | Supported images  
---|---|---|---|---  
1.6 (Python 3.10) | CPU only | Jul 11, 2025 | Jul 11, 2026 | 

  * `us-docker.pkg.dev/vertex-ai/training/sklearn-cpu.1-6:latest`
  * `europe-docker.pkg.dev/vertex-ai/training/sklearn-cpu.1-6:latest`
  * `asia-docker.pkg.dev/vertex-ai/training/sklearn-cpu.1-6:latest`



#### Included dependencies

| PyPI packages | Ubuntu packages  
---|---  
numpy 1.26.4  
pandas 2.2.3  
scipy 1.15.2  
scikit-learn 1.6.1  
sympy 1.12  
xgboost 2.1.3  
oauth2client 4.1.3  
httplib2 0.22.0  
python-dateutil 2.9.0.post0  
six 1.17.0  
wrapt 1.17.2  
google-api-python-client 2.162.0  
python-json-logger 3.2.1  
wheel 0.45.1  
WebOb 1.8.7  
Paste 3.7.1  
grpcio 1.71.0rc2  
requests 2.32.3  
webapp2 3.0.0b1  
mock 5.1.0  
google-cloud-bigquery 3.29.0  
google-cloud-datastore 1.15.5  
google-cloud-resource-manager 1.6.1  
google-cloud-storage 2.19.0  
joblib 1.4.2  
cloudml-hypertune  
|  ca-certificates-java  
libatlas-base-dev  
liblapack-dev  
gfortran  
gdb  
openjdk-8-jdk  
openjdk-8-jre-headless  
g++  
libio-all-perl  
libyaml-0-2  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software)  
  
1.6 (Python 3.10) | GPU (CUDA 12.x) | Jul 11, 2025 | Jul 11, 2026 | 

  * `us-docker.pkg.dev/vertex-ai/training/sklearn-gpu.1-6:latest`
  * `europe-docker.pkg.dev/vertex-ai/training/sklearn-gpu.1-6:latest`
  * `asia-docker.pkg.dev/vertex-ai/training/sklearn-gpu.1-6:latest`



#### Included dependencies

| PyPI packages | Ubuntu packages  
---|---  
numpy 1.26.4  
pandas 2.2.3  
scipy 1.15.2  
scikit-learn 1.6.1  
sympy 1.12  
xgboost 2.1.3  
oauth2client 4.1.3  
httplib2 0.22.0  
python-dateutil 2.9.0.post0  
six 1.17.0  
wrapt 1.17.2  
google-api-python-client 2.162.0  
python-json-logger 3.2.1  
wheel 0.45.1  
WebOb 1.8.7  
Paste 3.7.1  
grpcio 1.71.0rc2  
requests 2.32.3  
webapp2 3.0.0b1  
mock 5.1.0  
google-cloud-bigquery 3.29.0  
google-cloud-datastore 1.15.5  
google-cloud-resource-manager 1.6.1  
google-cloud-storage 2.19.0  
joblib 1.4.2  
cloudml-hypertune  
|  ca-certificates-java  
libatlas-base-dev  
liblapack-dev  
gfortran  
gdb  
openjdk-8-jdk  
openjdk-8-jre-headless  
g++  
libio-all-perl  
libyaml-0-2  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software)  
  
1.0 (Python 3.10) | CPU only | June 30, 2024 | June 30, 2025 | 

  * `us-docker.pkg.dev/vertex-ai/training/sklearn-cpu.1-0:latest`
  * `europe-docker.pkg.dev/vertex-ai/training/sklearn-cpu.1-0:latest`
  * `asia-docker.pkg.dev/vertex-ai/training/sklearn-cpu.1-0:latest`



#### Included dependencies

| PyPI packages | Ubuntu packages  
---|---  
numpy 1.18.5  
pandas 1.0.4  
scipy 1.4.1  
scikit-learn 1.0  
sympy 1.6  
statsmodels 0.11.1  
xgboost 1.6.2  
oauth2client 4.1.3  
httplib2 0.18.1  
python-dateutil 2.8.1  
six 1.15.0  
future 0.18.2  
PyYAML 5.3.1  
wrapt 1.12.1  
crcmod 1.7  
google-api-python-client 1.9.3  
python-json-logger 0.1.11  
wheel 0.34.2  
WebOb 1.8.6  
Paste 3.4.1  
tornado 5.1.1  
grpcio 1.29.0  
requests 2.23.0  
webapp2 3.0.0b1  
mock 4.0.2  
google-cloud-bigquery 1.25.0  
google-cloud-bigtable 1.2.1  
google-cloud-datastore 1.12.0  
google-cloud-logging 1.15.0  
google-cloud-pubsub 1.6.0  
google-cloud-resource-manager 0.30.2  
google-cloud-storage 1.29.0  
joblib 0.15.1  
cloudml-hypertune  
|  curl  
libcurl3-dev  
wget  
zip  
unzip  
git  
vim  
build-essential  
ca-certificates  
pkg-config  
rsync  
ca-certificates-java  
libatlas-base-dev  
liblapack-dev  
gfortran  
libpng-dev  
libjpeg-dev  
python3.10  
python3-dev  
python3.10-dev  
python3-pip  
python3-setuptools  
python2.7  
python-dev  
python-setuptools  
gdb  
openjdk-8-jdk  
openjdk-8-jre-headless  
g++  
zlib1g-dev  
libio-all-perl  
module-init-tools  
libsnappy-dev  
libyaml-0-2  
python-opencv  
  
  
1.0 (Python 3.10) | GPU (CUDA 11.x) | June 30, 2024 | June 30, 2025 | 

  * `us-docker.pkg.dev/vertex-ai/training/sklearn-gpu.1-0:latest`
  * `europe-docker.pkg.dev/vertex-ai/training/sklearn-gpu.1-0:latest`
  * `asia-docker.pkg.dev/vertex-ai/training/sklearn-gpu.1-0:latest`



#### Included dependencies

| PyPI packages | Ubuntu packages  
---|---  
numpy 1.18.5  
pandas 1.0.4  
scipy 1.4.1  
scikit-learn 1.0  
sympy 1.6  
statsmodels 0.11.1  
xgboost 1.6.2  
oauth2client 4.1.3  
httplib2 0.18.1  
python-dateutil 2.8.1  
six 1.15.0  
future 0.18.2  
PyYAML 5.3.1  
wrapt 1.12.1  
crcmod 1.7  
google-api-python-client 1.9.3  
python-json-logger 0.1.11  
wheel 0.34.2  
WebOb 1.8.6  
Paste 3.4.1  
tornado 5.1.1  
grpcio 1.29.0  
requests 2.23.0  
webapp2 3.0.0b1  
mock 4.0.2  
google-cloud-bigquery 1.25.0  
google-cloud-bigtable 1.2.1  
google-cloud-datastore 1.12.0  
google-cloud-logging 1.15.0  
google-cloud-pubsub 1.6.0  
google-cloud-resource-manager 0.30.2  
google-cloud-storage 1.29.0  
joblib 0.15.1  
cloudml-hypertune  
|  curl  
libcurl3-dev  
wget  
zip  
unzip  
git  
vim  
build-essential  
ca-certificates  
pkg-config  
rsync  
ca-certificates-java  
libatlas-base-dev  
liblapack-dev  
gfortran  
libpng-dev  
libjpeg-dev  
python3.10  
python3-dev  
python3.10-dev  
python3-pip  
python3-setuptools  
python2.7  
python-dev  
python-setuptools  
gdb  
openjdk-8-jdk  
openjdk-8-jre-headless  
g++  
zlib1g-dev  
libio-all-perl  
module-init-tools  
libsnappy-dev  
libyaml-0-2  
python-opencv  
  
  
0.23 (Python 3.7) | CPU only | Sep 1, 2023 | Sep 1, 2024 | 

  * `us-docker.pkg.dev/vertex-ai/training/scikit-learn-cpu.0-23:latest`
  * `europe-docker.pkg.dev/vertex-ai/training/scikit-learn-cpu.0-23:latest`
  * `asia-docker.pkg.dev/vertex-ai/training/scikit-learn-cpu.0-23:latest`



#### Included dependencies

| PyPI packages | Ubuntu packages  
---|---  
numpy 1.18.5  
pandas 1.0.4  
scipy 1.4.1  
scikit-learn 0.23.1  
sympy 1.6  
statsmodels 0.11.1  
xgboost 1.1.1  
oauth2client 4.1.3  
httplib2 0.18.1  
python-dateutil 2.8.1  
six 1.15.0  
future 0.18.2  
PyYAML 5.3.1  
wrapt 1.12.1  
crcmod 1.7  
google-api-python-client 1.9.3  
python-json-logger 0.1.11  
wheel 0.34.2  
WebOb 1.8.6  
Paste 3.4.1  
tornado 5.1.1  
grpcio 1.29.0  
requests 2.23.0  
webapp2 3.0.0b1  
mock 4.0.2  
google-cloud-bigquery 1.25.0  
google-cloud-bigtable 1.2.1  
google-cloud-datastore 1.12.0  
google-cloud-logging 1.15.0  
google-cloud-pubsub 1.6.0  
google-cloud-resource-manager 0.30.2  
google-cloud-storage 1.29.0  
joblib 0.15.1  
cloudml-hypertune  
|  curl  
libcurl3-dev  
wget  
zip  
unzip  
git  
vim  
build-essential  
ca-certificates  
pkg-config  
rsync  
ca-certificates-java  
libatlas-base-dev  
liblapack-dev  
gfortran  
libpng-dev  
libjpeg-dev  
python3.7  
python3-dev  
python3.7-dev  
python3-pip  
python3-setuptools  
python2.7  
python-dev  
python-setuptools  
gdb  
openjdk-8-jdk  
openjdk-8-jre-headless  
g++  
zlib1g-dev  
libio-all-perl  
module-init-tools  
libsnappy-dev  
libyaml-0-2  
python-opencv  
  
  
### XGBoost

ML framework version | Supported accelerators (and CUDA version, if applicable) | End of patch and support date | End of availability | Supported images  
---|---|---|---|---  
2.1 (Python 3.10) | CPU only | Jul 11, 2025 | Jul 11, 2026 | 

  * `us-docker.pkg.dev/vertex-ai/training/xgboost-cpu.2-1:latest`
  * `europe-docker.pkg.dev/vertex-ai/training/xgboost-cpu.2-1:latest`
  * `asia-docker.pkg.dev/vertex-ai/training/xgboost-cpu.2-1:latest`



#### Included dependencies

| PyPI packages | Ubuntu packages  
---|---  
numpy 1.26.4  
pandas 2.2.3  
scipy 1.15.2  
scikit-learn 1.6.1  
sympy 1.12  
xgboost 2.1.3  
oauth2client 4.1.3  
httplib2 0.22.0  
python-dateutil 2.9.0.post0  
six 1.17.0  
wrapt 1.17.2  
google-api-python-client 2.162.0  
python-json-logger 3.2.1  
wheel 0.45.1  
WebOb 1.8.7  
Paste 3.7.1  
grpcio 1.71.0rc2  
requests 2.32.3  
webapp2 3.0.0b1  
mock 5.1.0  
google-cloud-bigquery 3.29.0  
google-cloud-datastore 1.15.5  
google-cloud-resource-manager 1.6.1  
google-cloud-storage 2.19.0  
joblib 1.4.2  
cloudml-hypertune  
|  ca-certificates-java  
libatlas-base-dev  
liblapack-dev  
gfortran  
gdb  
openjdk-8-jdk  
openjdk-8-jre-headless  
g++  
libio-all-perl  
libyaml-0-2  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software)  
  
2.1 (Python 3.10) | GPU (CUDA 12.x) | Jul 11, 2025 | Jul 11, 2026 | 

  * `us-docker.pkg.dev/vertex-ai/training/xgboost-gpu.2-1:latest`
  * `europe-docker.pkg.dev/vertex-ai/training/xgboost-gpu.2-1:latest`
  * `asia-docker.pkg.dev/vertex-ai/training/xgboost-gpu.2-1:latest`



#### Included dependencies

| PyPI packages | Ubuntu packages  
---|---  
numpy 1.26.4  
pandas 2.2.3  
scipy 1.15.2  
scikit-learn 1.6.1  
sympy 1.12  
xgboost 2.1.3  
oauth2client 4.1.3  
httplib2 0.22.0  
python-dateutil 2.9.0.post0  
six 1.17.0  
wrapt 1.17.2  
google-api-python-client 2.162.0  
python-json-logger 3.2.1  
wheel 0.45.1  
WebOb 1.8.7  
Paste 3.7.1  
grpcio 1.71.0rc2  
requests 2.32.3  
webapp2 3.0.0b1  
mock 5.1.0  
google-cloud-bigquery 3.29.0  
google-cloud-datastore 1.15.5  
google-cloud-resource-manager 1.6.1  
google-cloud-storage 2.19.0  
joblib 1.4.2  
cloudml-hypertune  
|  ca-certificates-java  
libatlas-base-dev  
liblapack-dev  
gfortran  
gdb  
openjdk-8-jdk  
openjdk-8-jre-headless  
g++  
libio-all-perl  
libyaml-0-2  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software)  
  
1.6 (Python 3.10) | CPU only | June 30, 2024 | June 30, 2025 | 

  * `us-docker.pkg.dev/vertex-ai/training/xgboost-cpu.1-6:latest`
  * `europe-docker.pkg.dev/vertex-ai/training/xgboost-cpu.1-6:latest`
  * `asia-docker.pkg.dev/vertex-ai/training/xgboost-cpu.1-6:latest`



#### Included dependencies

| PyPI packages | Ubuntu packages  
---|---  
numpy 1.18.5  
pandas 1.0.4  
scipy 1.4.1  
scikit-learn 0.23.1  
sympy 1.6  
statsmodels 0.11.1  
xgboost 1.6.2  
oauth2client 4.1.3  
httplib2 0.18.1  
python-dateutil 2.8.1  
six 1.15.0  
future 0.18.2  
PyYAML 5.3.1  
wrapt 1.12.1  
crcmod 1.7  
google-api-python-client 1.9.3  
python-json-logger 0.1.11  
wheel 0.34.2  
WebOb 1.8.6  
Paste 3.4.1  
tornado 5.1.1  
grpcio 1.29.0  
requests 2.23.0  
webapp2 3.0.0b1  
mock 4.0.2  
google-cloud-bigquery 1.25.0  
google-cloud-bigtable 1.2.1  
google-cloud-datastore 1.12.0  
google-cloud-logging 1.15.0  
google-cloud-pubsub 1.6.0  
google-cloud-resource-manager 0.30.2  
google-cloud-storage 1.29.0  
joblib 0.15.1  
cloudml-hypertune  
|  curl  
libcurl3-dev  
wget  
zip  
unzip  
git  
vim  
build-essential  
ca-certificates  
pkg-config  
rsync  
ca-certificates-java  
libatlas-base-dev  
liblapack-dev  
gfortran  
libpng-dev  
libjpeg-dev  
python3.10  
python3-dev  
python3.10-dev  
python3-pip  
python3-setuptools  
python2.7  
python-dev  
python-setuptools  
gdb  
openjdk-8-jdk  
openjdk-8-jre-headless  
g++  
zlib1g-dev  
libio-all-perl  
module-init-tools  
libsnappy-dev  
libyaml-0-2  
python-opencv  
  
  
1.6 (Python 3.10) | GPU (CUDA 11.x) | June 30, 2024 | June 30, 2025 | 

  * `us-docker.pkg.dev/vertex-ai/training/xgboost-gpu.1-6:latest`
  * `europe-docker.pkg.dev/vertex-ai/training/xgboost-gpu.1-6:latest`
  * `asia-docker.pkg.dev/vertex-ai/training/xgboost-gpu.1-6:latest`



#### Included dependencies

| PyPI packages | Ubuntu packages  
---|---  
numpy 1.18.5  
pandas 1.0.4  
scipy 1.4.1  
scikit-learn 0.23.1  
sympy 1.6  
statsmodels 0.11.1  
xgboost 1.6.2  
oauth2client 4.1.3  
httplib2 0.18.1  
python-dateutil 2.8.1  
six 1.15.0  
future 0.18.2  
PyYAML 5.3.1  
wrapt 1.12.1  
crcmod 1.7  
google-api-python-client 1.9.3  
python-json-logger 0.1.11  
wheel 0.34.2  
WebOb 1.8.6  
Paste 3.4.1  
tornado 5.1.1  
grpcio 1.29.0  
requests 2.23.0  
webapp2 3.0.0b1  
mock 4.0.2  
google-cloud-bigquery 1.25.0  
google-cloud-bigtable 1.2.1  
google-cloud-datastore 1.12.0  
google-cloud-logging 1.15.0  
google-cloud-pubsub 1.6.0  
google-cloud-resource-manager 0.30.2  
google-cloud-storage 1.29.0  
joblib 0.15.1  
cloudml-hypertune  
|  curl  
libcurl3-dev  
wget  
zip  
unzip  
git  
vim  
build-essential  
ca-certificates  
pkg-config  
rsync  
ca-certificates-java  
libatlas-base-dev  
liblapack-dev  
gfortran  
libpng-dev  
libjpeg-dev  
python3.10  
python3-dev  
python3.10-dev  
python3-pip  
python3-setuptools  
python2.7  
python-dev  
python-setuptools  
gdb  
openjdk-8-jdk  
openjdk-8-jre-headless  
g++  
zlib1g-dev  
libio-all-perl  
module-init-tools  
libsnappy-dev  
libyaml-0-2  
python-opencv  
  
  
1.1 (Python 3.7) | CPU only | Nov 15, 2023 | Nov 15, 2024 | 

  * `us-docker.pkg.dev/vertex-ai/training/xgboost-cpu.1-1:latest`
  * `europe-docker.pkg.dev/vertex-ai/training/xgboost-cpu.1-1:latest`
  * `asia-docker.pkg.dev/vertex-ai/training/xgboost-cpu.1-1:latest`



#### Included dependencies

| PyPI packages | Ubuntu packages  
---|---  
numpy 1.18.5  
pandas 1.0.4  
scipy 1.4.1  
scikit-learn 0.23.1  
sympy 1.6  
statsmodels 0.11.1  
xgboost 1.1.1  
oauth2client 4.1.3  
httplib2 0.18.1  
python-dateutil 2.8.1  
six 1.15.0  
future 0.18.2  
PyYAML 5.3.1  
wrapt 1.12.1  
crcmod 1.7  
google-api-python-client 1.9.3  
python-json-logger 0.1.11  
wheel 0.34.2  
WebOb 1.8.6  
Paste 3.4.1  
tornado 5.1.1  
grpcio 1.29.0  
requests 2.23.0  
webapp2 3.0.0b1  
mock 4.0.2  
google-cloud-bigquery 1.25.0  
google-cloud-bigtable 1.2.1  
google-cloud-datastore 1.12.0  
google-cloud-logging 1.15.0  
google-cloud-pubsub 1.6.0  
google-cloud-resource-manager 0.30.2  
google-cloud-storage 1.29.0  
joblib 0.15.1  
cloudml-hypertune  
|  curl  
libcurl3-dev  
wget  
zip  
unzip  
git  
vim  
build-essential  
ca-certificates  
pkg-config  
rsync  
ca-certificates-java  
libatlas-base-dev  
liblapack-dev  
gfortran  
libpng-dev  
libjpeg-dev  
python3.7  
python3-dev  
python3.7-dev  
python3-pip  
python3-setuptools  
python2.7  
python-dev  
python-setuptools  
gdb  
openjdk-8-jdk  
openjdk-8-jre-headless  
g++  
zlib1g-dev  
libio-all-perl  
module-init-tools  
libsnappy-dev  
libyaml-0-2  
python-opencv  
  
  
### Supported versions of Ray on Vertex AI

[Ray on Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/open-source/ray) container images are available. The following versions of prebuilt containers are supported:

Ray version | Supported accelerators (and CUDA version, if applicable) | End of patch and support date | End of availability | Supported images  
---|---|---|---|---  
2.47.1 (Python 3.11) | CPU only | Jul 28, 2026 | Jul 28, 2027 | 

  * `us-docker.pkg.dev/vertex-ai/training/ray-cpu.2-47.py311:latest`
  * `europe-docker.pkg.dev/vertex-ai/training/ray-cpu.2-47.py311:latest`
  * `asia-docker.pkg.dev/vertex-ai/training/ray-cpu.2-47.py311:latest`



#### Included dependencies

| PyPI packages | Ubuntu packages  
---|---  
absl-py 2.3.0  
cloud-tpu-client 0.10  
cloudml-hypertune  
python-json-logger 3.3.0  
google-cloud-resource-manager 1.14.2  
setuptools 69.5.1  
kubernetes  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software) |  ca-certificates-java  
libatlas-base-dev  
liblapack-dev  
g++  
libio-all-perl  
libyaml-0-2  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software)  
  
2.47.1 (Python 3.11) | GPU (CUDA 11.x) | Jul 28, 2026 | Jul 28, 2027 | 

  * `us-docker.pkg.dev/vertex-ai/training/ray-gpu.2-47.py311:latest`
  * `europe-docker.pkg.dev/vertex-ai/training/ray-gpu.2-47.py311:latest`
  * `asia-docker.pkg.dev/vertex-ai/training/ray-gpu.2-47.py311:latest`



#### Included dependencies

| PyPI packages | Ubuntu packages  
---|---  
absl-py 2.3.0  
cloud-tpu-client 0.10  
cloudml-hypertune  
python-json-logger 3.3.0  
google-cloud-resource-manager 1.14.2  
setuptools 69.5.1  
kubernetes  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software) |  ca-certificates-java  
libatlas-base-dev  
liblapack-dev  
g++  
libio-all-perl  
libyaml-0-2  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software)  
  
2.42.0 (Python 3.11) | CPU only | Mar 1, 2026 | Mar 1, 2027 | 

  * `us-docker.pkg.dev/vertex-ai/training/ray-cpu.2-42.py311:latest`
  * `europe-docker.pkg.dev/vertex-ai/training/ray-cpu.2-42.py311:latest`
  * `asia-docker.pkg.dev/vertex-ai/training/ray-cpu.2-42.py311:latest`



#### Included dependencies

| PyPI packages | Ubuntu packages  
---|---  
absl-py 2.1.0  
cloud-tpu-client 0.10  
cloudml-hypertune  
python-json-logger 3.2.1  
google-cloud-resource-manager 1.12.4  
setuptools 69.5.1  
kubernetes  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software) |  ca-certificates-java  
libatlas-base-dev  
liblapack-dev  
g++  
libio-all-perl  
libyaml-0-2  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software)  
  
2.42.0 (Python 3.11) | GPU (CUDA 11.x) | Mar 1, 2026 | Mar 1, 2027 | 

  * `us-docker.pkg.dev/vertex-ai/training/ray-gpu.2-42.py311:latest`
  * `europe-docker.pkg.dev/vertex-ai/training/ray-gpu.2-42.py311:latest`
  * `asia-docker.pkg.dev/vertex-ai/training/ray-gpu.2-42.py311:latest`



#### Included dependencies

| PyPI packages | Ubuntu packages  
---|---  
absl-py 2.1.0  
cloud-tpu-client 0.10  
cloudml-hypertune  
python-json-logger 3.2.1  
google-cloud-resource-manager 1.12.4  
setuptools 69.5.1  
kubernetes  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software) |  ca-certificates-java  
libatlas-base-dev  
liblapack-dev  
g++  
libio-all-perl  
libyaml-0-2  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software)  
  
2.42.0 (Python 3.10) | CPU only | Mar 1, 2026 | Mar 1, 2027 | 

  * `us-docker.pkg.dev/vertex-ai/training/ray-cpu.2-42.py310:latest`
  * `europe-docker.pkg.dev/vertex-ai/training/ray-cpu.2-42.py310:latest`
  * `asia-docker.pkg.dev/vertex-ai/training/ray-cpu.2-42.py310:latest`



#### Included dependencies

| PyPI packages | Ubuntu packages  
---|---  
absl-py 2.1.0  
cloud-tpu-client 0.10  
cloudml-hypertune  
python-json-logger 3.2.1  
google-cloud-resource-manager 1.12.4  
setuptools 69.5.1  
kubernetes  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software) |  ca-certificates-java  
libatlas-base-dev  
liblapack-dev  
g++  
libio-all-perl  
libyaml-0-2  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software)  
  
2.42.0 (Python 3.10) | GPU (CUDA 11.x) | Mar 1, 2026 | Mar 1, 2027 | 

  * `us-docker.pkg.dev/vertex-ai/training/ray-gpu.2-42.py310:latest`
  * `europe-docker.pkg.dev/vertex-ai/training/ray-gpu.2-42.py310:latest`
  * `asia-docker.pkg.dev/vertex-ai/training/ray-gpu.2-42.py310:latest`



#### Included dependencies

| PyPI packages | Ubuntu packages  
---|---  
absl-py 2.1.0  
cloud-tpu-client 0.10  
cloudml-hypertune  
python-json-logger 3.2.1  
google-cloud-resource-manager 1.12.4  
setuptools 69.5.1  
kubernetes  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software) |  ca-certificates-java  
libatlas-base-dev  
liblapack-dev  
g++  
libio-all-perl  
libyaml-0-2  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software)  
  
2.33.0 (Python 3.10) | CPU only | September 16, 2025 | September 16, 2026 | 

  * `us-docker.pkg.dev/vertex-ai/training/ray-cpu.2-33.py310:latest`
  * `europe-docker.pkg.dev/vertex-ai/training/ray-cpu.2-33.py310:latest`
  * `asia-docker.pkg.dev/vertex-ai/training/ray-cpu.2-33.py310:latest`



#### Included dependencies

| PyPI packages | Ubuntu packages  
---|---  
absl-py 2.1.0  
cloud-tpu-client 0.10  
cloudml-hypertune  
python-json-logger 2.0.7  
google-cloud-resource-manager 1.12.4  
setuptools 69.5.1  
kubernetes  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software) |  ca-certificates-java  
libatlas-base-dev  
liblapack-dev  
g++  
libio-all-perl  
libyaml-0-2  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software)  
  
2.33.0 (Python 3.10) | GPU (CUDA 11.x) | September 16, 2025 | September 16, 2026 | 

  * `us-docker.pkg.dev/vertex-ai/training/ray-gpu.2-33.py310:latest`
  * `europe-docker.pkg.dev/vertex-ai/training/ray-gpu.2-33.py310:latest`
  * `asia-docker.pkg.dev/vertex-ai/training/ray-gpu.2-33.py310:latest`



#### Included dependencies

| PyPI packages | Ubuntu packages  
---|---  
absl-py 2.1.0  
cloud-tpu-client 0.10  
cloudml-hypertune  
python-json-logger 2.0.7  
google-cloud-resource-manager 1.12.4  
setuptools 69.5.1  
kubernetes  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software) |  ca-certificates-java  
libatlas-base-dev  
liblapack-dev  
g++  
libio-all-perl  
libyaml-0-2  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software)  
  
2.9.3 (Python 3.10) | CPU only | May 7, 2025 | May 7, 2026 | 

  * `us-docker.pkg.dev/vertex-ai/training/ray-cpu.2-9.py310:latest`
  * `europe-docker.pkg.dev/vertex-ai/training/ray-cpu.2-9.py310:latest`
  * `asia-docker.pkg.dev/vertex-ai/training/ray-cpu.2-9.py310:latest`



#### Included dependencies

| PyPI packages | Ubuntu packages  
---|---  
absl-py 2.0.0  
cloud-tpu-client 0.10  
cloudml-hypertune  
python-json-logger 2.0.7  
google-cloud-resource-manager 1.11.0  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software) |  ca-certificates-java  
libatlas-base-dev  
liblapack-dev  
g++  
libio-all-perl  
libyaml-0-2  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software)  
  
2.9.3 (Python 3.10) | GPU (CUDA 11.x) | May 7, 2025 | May 7, 2026 | 

  * `us-docker.pkg.dev/vertex-ai/training/ray-gpu.2-9.py310:latest`
  * `europe-docker.pkg.dev/vertex-ai/training/ray-gpu.2-9.py310:latest`
  * `asia-docker.pkg.dev/vertex-ai/training/ray-gpu.2-9.py310:latest`



#### Included dependencies

| PyPI packages | Ubuntu packages  
---|---  
absl-py 2.0.0  
cloud-tpu-client 0.10  
cloudml-hypertune  
python-json-logger 2.0.7  
google-cloud-resource-manager 1.11.0  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software) |  ca-certificates-java  
libatlas-base-dev  
liblapack-dev  
g++  
libio-all-perl  
libyaml-0-2  
Other [ Deep Learning Containers dependencies](https://docs.cloud.google.com/deep-learning-containers/docs/overview#pre-installed_software)  
  
## Train with a prebuilt container

To see an example of using a prebuilt container for training as part of a more comprehensive workflow, run the "Custom training and online inference" notebook in one of the following environments: 

[![](https://docs.cloud.google.com/static/vertex-ai/images/colab-logo-32px.png)Open in Colab](https://colab.research.google.com/github/GoogleCloudPlatform/vertex-ai-samples/blob/main/notebooks/official/custom/sdk-custom-image-classification-online.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/colab-enterprise-logo-32px.png)Open in Colab Enterprise](https://console.cloud.google.com/agent-platform/colab/import/https%3A%2F%2Fraw.githubusercontent.com%2FGoogleCloudPlatform%2Fvertex-ai-samples%2Fmain%2Fnotebooks%2Fofficial%2Fcustom%2Fsdk-custom-image-classification-online.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/vertex-ai-workbench-logo-32px.png)Open in Agent Platform Workbench](https://console.cloud.google.com/agent-platform/workbench/deploy-notebook?download_url=https%3A%2F%2Fraw.githubusercontent.com%2FGoogleCloudPlatform%2Fvertex-ai-samples%2Fmain%2Fnotebooks%2Fofficial%2Fcustom%2Fsdk-custom-image-classification-online.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/github-logo-32px.png)View on GitHub](https://github.com/GoogleCloudPlatform/vertex-ai-samples/blob/main/notebooks/official/custom/sdk-custom-image-classification-online.ipynb)

To use a prebuilt container, read the [guide to configuring container settings](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/configure-container-settings).

If you're using a container image that supports GPUs, make sure to specify the [`machineSpec.acceleratorType` and `machineSpec.acceleratorCount`](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/MachineSpec) fields when you create your `CustomJob`, `HyperparameterTuningJob`, or `TrainingPipeline` resource.

## What's next

  * Learn how to [create a Python training application](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/create-python-pre-built-container) to use with a prebuilt container. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
