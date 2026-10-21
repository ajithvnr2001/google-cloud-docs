---
url: https://docs.cloud.google.com/architecture/guidelines-for-developing-high-quality-ml-solutions/
title: Guidelines for developing high-quality, predictive ML solutions \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:22:18.918294+00:00
---

# Guidelines for developing high-quality, predictive ML solutions  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/guidelines-for-developing-high-quality-ml-solutions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Guidelines for developing high-quality, predictive ML solutions Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2024-07-08 UTC

This document collates some guidelines to help you assess, ensure, and control quality in building predictive machine learning (ML) solutions. It provides suggestions for every step of the process, from developing your ML models to deploying your training systems and serving systems to production. The document extends the information that's discussed in [Practitioners Guide to MLOps](https://cloud.google.com/resources/mlops-whitepaper) by highlighting and distilling the quality aspects in each process of the MLOps lifecycle.

This document is intended for anyone who is involved in building, deploying, and operating ML solutions. The document assumes that you're familiar with MLOps in general. It does not assume that you have knowledge of any specific ML platform.

## Overview of machine learning solution quality

In software engineering, many standards, processes, tools, and practices have been developed to ensure [software quality](https://en.wikipedia.org/wiki/Software_quality). The goal is to make sure that the software works as intended in production, and that it meets both functional and non-functional requirements. These practices cover topics like software [testing](https://en.wikipedia.org/wiki/Software_testing), software [verification and validation](https://en.wikipedia.org/wiki/Software_verification_and_validation), and software [logging](https://en.wikipedia.org/wiki/Logging_\(software\)) and [monitoring](https://en.wikipedia.org/wiki/Application_performance_management). In [DevOps](https://en.wikipedia.org/wiki/DevOps), these practices are typically integrated and automated in [CI/CD](https://en.wikipedia.org/wiki/CI/CD) processes.

[MLOps](https://cloud.google.com/blog/products/ai-machine-learning/google-cloud-launches-vertex-ai-unified-platform-for-mlops) is a set of standardized processes and capabilities for building, deploying, and operating ML systems rapidly and reliably. As with other software solutions, ML software solutions require you to integrate these software quality practices and apply them throughout the MLOps lifecycle. By applying these practices, you help make sure the trustworthiness and predictability of your models, and that the models conform to your requirements.

However, the tasks of building, deploying, and operating ML systems present additional challenges that require certain quality practices that might not be relevant to other software systems. In addition to the characteristics of most of the other software systems, ML systems have the following characteristics:

  * **Data-dependent systems**. The quality of the trained models and of their predictions depends on the validity of the data that's used for training and that's submitted for prediction requests. Any software system depends on valid data, but ML systems deduce the logic for decision-making from the data automatically, so they are particularly dependent on the quality of the data.

  * **Dual training-serving systems**. ML workloads typically consist of two distinct but related production systems: the training system and the serving system. A continuous training pipeline produces newly trained models that are then deployed for prediction serving. Each system requires a different set of quality practices that balance effectiveness and efficiency in order to produce and maintain a performant model in production. In addition, inconsistencies between these two systems result in errors and poor predictive performance.

  * **Prone to staleness**. Models often degrade after they're deployed in production because the models fail to adapt to changes in the environment that they represent, such as seasonal changes in purchase behavior. The models can also fail to adapt to changes in data, such as new products and locations. Thus, keeping track of the effectiveness of the model in production is an additional challenge for ML systems.

  * **Automated decision-making systems**. Unlike other software systems, where actions are carefully hand-coded for a set of requirements and business rules, ML models learn rules from data to make a decision. Implicit bias in the data can lead models to produce unfair outcomes.




When a deployed ML model produces bad predictions, the poor ML quality can be the result of a wide range of problems. Some of these problems can arise from the typical bugs that are in any program. But ML-specific problems can also include data skews and anomalies, along with the absence of proper model evaluation and validation procedures as a part of the training process. Another potential issue is inconsistent data format between the model's built-in interface and the serving API. In addition, model performance degrades over time even without these problems, and it can fail silently if it's not properly monitored. Therefore, you should include different kinds of testing and monitoring for ML models and systems during development, during deployment, and in production.

## Quality guidelines for model development

When you develop an ML model during the experimentation phase, you have the following two sets of target metrics that you can use to assess the model's performance:

  * **The model's optimizing metrics**. This metric reflects the model's predictive effectiveness. The metric includes [accuracy](https://en.wikipedia.org/wiki/Accuracy_and_precision) and [f-measure](https://en.wikipedia.org/wiki/F-score) in classification tasks, [mean absolute percentage error](https://en.wikipedia.org/wiki/Mean_absolute_percentage_error) in regression and forecasting tasks, [discounted cumulative gain](https://en.wikipedia.org/wiki/Discounted_cumulative_gain) in ranking tasks, and [perplexity](https://en.wikipedia.org/wiki/Perplexity) and [BLEU](https://en.wikipedia.org/wiki/BLEU) scores in language models. The better the value of this metric, the better the model is for a given task. In some use cases, to ensure fairness, it's important to achieve similar predictive effectiveness on different slices of the data—for example, on different customer demographics.
  * **The model's satisficing metrics**. This metric reflects an operational constraint that the model needs to satisfy, such as prediction latency. You set a latency threshold to a particular value, such as 200 milliseconds. Any model that doesn't meet the threshold is not accepted. Another example of a satisficing metric is the size of the model, which is important when you want to deploy your model to low-powered hardware like mobile and embedded devices.



During experimentation, you develop, train, evaluate, and debug your model to improve its effectiveness with respect to the optimizing metrics, without violating the satisficing metric thresholds.

### Guidelines for experimentation

  * Have predefined and fixed thresholds for optimizing metrics and for satisficing metrics.
  * Implement a streamlined evaluation routine that takes a model and data and produces a set of evaluation metrics. Implement the routine so it works regardless of the type of the model (for example, decision trees or neural networks) or the model's framework (for example, TensorFlow or Scikit-learn).
  * Make sure that you have a baseline model to compare with. This baseline can consist of hardcoded heuristics or it can be a simple model that predicts the mean or the mode target value. Use the baseline model to check the performance of the ML model. If the ML model isn't better than the baseline model, there is a fundamental problem in the ML model.
  * Track every experiment that has been done to help you with reproducibility and incremental improvement. For each experiment, store hyperparameter values, feature selection, and random seeds.



### Guidelines for data quality

  * Address any imbalanced classes early in your experiments by choosing the right evaluation metric. In addition, apply techniques like upweighting minority class instances or downsampling majority class instances.
  * Make sure that you understand the data source at hand, and perform the relevant [data preprocessing and feature engineering](https://developers.google.com/machine-learning/data-prep/process) to prepare the training dataset. This type of process needs to be repeatable and automatable.
  * Make sure that you have a separate [testing data split](https://en.wikipedia.org/wiki/Training,_validation,_and_test_sets) (holdout) for the final evaluation of the model. The test split should not be seen during training, and don't use it for hyperparameter tuning.
  * Make sure that training, validation, and test splits are equally representative of your input data. Sampling such a test split depends on the nature of the data and of the ML task at hand. For example, stratified splitting is relevant to classification tasks, while chronological splitting is relevant to time-series tasks.
  * Make sure that the validation and test splits are preprocessed separately from the training data split. If the splits are preprocessed in a mixture, it leads to [data leakage](https://en.wikipedia.org/wiki/Leakage_\(machine_learning\)). For example, when you use statistics to transform data for normalization or for bucketizing numerical features, compute the statistics from the training data and apply them to normalize the validation and test splits.
  * Generate a dataset schema that includes the data types and some statistical properties of the features. You can use this schema to find anomalous or invalid data during experimentation and training.
  * Make sure that your training data is properly shuffled in batches but that it also still meets the model training requirements. For example, this task can apply to positive and negative instance distributions.
  * Have a separate validation dataset for hyperparameter tuning and model selection. You can also use the validation dataset to perform early stopping. Otherwise, you can let the model train for the entirety of the given set of maximum iterations. However, only save a new snapshot of the model if its performance on the validation dataset improves relative to the previous snapshot.



### Guidelines for model quality

  * Make sure that your models don't have any fundamental problems that prevent them from learning any relationship between the inputs and the outputs. You can achieve this goal by training the model with very few examples. If the model doesn't achieve high accuracy for these examples, there might be a bug in your model implementation or training routine.
  * When you're training neural networks, monitor for `NaN` values in your loss and for the percentage of weights that have zero values throughout your model training. These `NaN` or zero values can be indications of erroneous arithmetic calculations, or of vanishing or exploding gradients. Visualizing changes in weight-values distribution over time can help you detect the [internal covariate shifts](https://arxiv.org/abs/1502.03167) that slow down the training. You can apply batch normalization to alleviate this reduction in speed.
  * Compare your model performance on the training data and on the test data to understand if your model is overfitting or underfitting. If you see either of these issues, perform the relevant improvements. For example, if there is underfitting, you might increase the model's learning capacity. If there was overfitting, you might apply regularization.
  * Analyze misclassified instances, especially the instances that have high prediction confidence and the most-confused classes in the multi-class [confusion matrix](https://developers.google.com/machine-learning/glossary#confusion-matrix). These errors can be an indication of mislabeled training examples. The errors can also identify an opportunity for data preprocessing, such as removing outliers, or for creating new features to help discriminate between such classes.
  * Analyze feature importance scores and clean up features that don't add enough improvement to the model's quality. [Parsimonious models](https://en.wikipedia.org/wiki/Occam%27s_razor) are preferred over complex ones.



## Quality guidelines for training pipeline deployment

As you implement your model and model training pipeline, you need to create a set of tests in a CI/CD routine. These tests run automatically as you push new code changes, or they run before you deploy your training pipeline to the target environment.

### Guidelines

  * Unit-test the feature engineering functionality.
  * Unit-test the encoding of the inputs to the model.
  * Unit-test user-implemented (custom) modules of the models independently—for example, unit-test custom graph convolution and pooling layers, or custom attention layers.
  * Unit-test any custom loss or evaluation functions.
  * Unit-test the output types and shapes of your model against expected inputs.
  * Unit-test that the `fit` function of the model works without any errors on a couple of small batches of data. The tests should make sure that the loss decreases and that the execution time of the training step is as expected. You make these checks because changes in model code can introduce bugs that slow down the training process.
  * Unit-test the model's save and load functionality.
  * Unit-test the exported model-serving interfaces against raw inputs and against expected outputs.
  * Test the components of the pipeline steps with mock inputs and with output artifacts.
  * Deploy the pipeline to a test environment and perform integration testing of the end-to-end pipeline. For this process, use some testing data to make sure that the workflow executes properly throughout and that it produces the expected artifacts.
  * Use [shadow deployment](https://thenewstack.io/deployment-strategies/) when you deploy a new version of the training pipeline to the production environment. A shadow deployment helps you make sure that the newly deployed pipeline version is executed on live data in parallel to the previous pipeline version.



## Quality guidelines for continuous training

The continuous training process is about orchestrating and automating the execution of training pipelines. Typical training workflows include steps like data ingestion and splitting, data transformation, model training, model evaluation, and model registration. Some training pipelines consist of more complex workflows. Additional tasks can include performing self-supervised model training that uses unlabeled data, or building an approximate nearest neighbor index for embeddings. The main input of any training pipeline is new training data, and the main output is a new candidate model to deploy in production.

The training pipeline runs in production automatically, based on a schedule (for example, daily or weekly) or based on a trigger (for example, when new labeled data is available). Therefore, you need to add quality-control steps to the training workflow, specifically data-validation steps and model-validation steps. These steps validate the inputs and the outputs of the pipelines.

You add the data-validation step after the data-ingestion step in the training workflow. The data-validation step profiles the new input training data that's ingested into the pipeline. During profiling, the pipeline uses a predefined data schema, which was created during the ML development process, to detect anomalies. Depending on the use case, you can ignore or just remove some invalid records from the dataset. However, other issues in the newly ingested data might halt the execution of the training pipeline, so you must identify and address those issues.

### Guidelines for data validation

  * Verify that the features of the extracted training data are complete and that they match the expected schema—that is, there are no missing features and no added ones. Also verify that features match the projected volumes.
  * Validate the data types and the shapes of the features in the dataset that are ingested into the training pipeline.
  * Verify that the formats of particular features (for example, dates, times, URLs, postcodes, and IP addresses) match the expected regular expressions. Also verify that features fall within valid ranges.
  * Validate the maximum fraction of the missing values for each feature. A large fraction of missing values in a particular feature can affect the model training. Missing values usually indicate an unreliable feature source.
  * Validate the domains of the input features. For example, check if there are changes in a vocabulary of categorical features or changes in the range of numerical features, and adjust data preprocessing accordingly. As another example, ranges for numerical features might change if an update in the upstream system that populates the features uses different units of measure. For example, the upstream system might change currency from dollars to yen, or it might change distances from kilometers to meters.
  * Verify that the distributions of each feature match your expectations. For example, you might test that the most common value of a feature for payment type is `cash` and that this payment type accounts for 50% of all values. However, this test can fail if there's a change in the most common payment type to `credit_card`. An external change like this might require changes in your model.



You add a model validation step before the model registration step to make sure that only models that pass the validation criteria are registered for production deployment.

### Guidelines for model validation

  * For the final model evaluation, use a separate test split that hasn't been used for model training or for hyperparameter tuning.
  * Score the candidate model against the test data split, compute the relevant evaluation metrics, and verify that the candidate model surpasses predefined quality thresholds.
  * Make sure that the test data split is representative of the data as a whole to account for varying data patterns. For time-series data, make sure that the test split contains more recent data than the training split.
  * Test model quality on important data slices like users by country or movies by genre. By testing on sliced data, you avoid a problem where fine-grained performance issues are masked by a global summary metric.
  * Evaluate the current (champion) model against the test data split, and compare it to the candidate (challenger) model that the training pipeline produces.
  * Validate the model against fairness indicators to detect implicit bias—for example, implicit bias might be induced by insufficient diversity in the training data. Fairness indicators can reveal root-cause issues that you must address before you deploy the model to production.



During continuous training, you can validate the model against both optimizing metrics and satisficing metrics. Alternatively, you might validate the model only against the optimizing metrics and defer validating against the satisficing metric until the model deployment phase. If you plan to deploy variations of the same model to different serving environments or workloads, it can be more suitable to defer validation against the satisficing metric. Different serving environments or workloads (such as cloud environments versus on-device environments, or real-time environments versus batch serving environments) might require different satisficing metric thresholds. If you're deploying to multiple environments, your continuous training pipeline might train two or more models, where each model is optimized for its target deployment environment.

As you put more continuous-training pipelines with complex workflows into production, you must track the metadata and the artifacts that the pipeline runs produce. Tracking this information helps you trace and debug any issue that might arise in production. Tracking the information also helps you reproduce the outputs of the pipelines so that you can improve their implementation in subsequent ML development iterations.

### Guidelines for tracking ML metadata and artifacts

  * Track lineage of the source code, deployed pipelines, components of the pipelines, pipeline runs, the dataset in use, and the produced artifacts.
  * Track the hyperparameters and the configurations of the pipeline runs.
  * Track key inputs and output artifacts of the pipeline steps, like dataset statistics, dataset anomalies (if any), transformed data and schemas, model checkpoints, and model evaluation results.
  * Track that conditional pipeline steps run in response to the conditions, and ensure observability by adding altering mechanisms in case key steps don't run or if they fail.



## Quality guidelines for model deployment

Assume that you have a trained model that's been validated from an optimizing metrics perspective, and that the model is approved from a model governance perspective (as described later in the model governance section). The model is stored in the model registry and is ready to be deployed to production. At this point, you need to implement a set of tests to verify that the model is fit to serve in its target environment. You also need to automate these tests in a model CI/CD routine.

### Guidelines

  * Verify that the model artifact can be loaded and invoked successfully with its runtime dependencies. You can perform this verification by staging the model in a sandboxed version of the serving environment. This verification helps you make sure that the operations and binaries that are used by the model are present in the environment.
  * Validate satisficing metrics of the model (if any) in a staging environment, like model size and latency.
  * Unit-test the model-artifact-serving interfaces in a staging environment against raw inputs and against expected outputs.
  * Unit-test the model artifact in a staging environment for a set of typical and edge cases of prediction requests. For example, unit-test for a request instance where all features are set to `None`.
  * Smoke-test the model service API after it's been deployed to its target environment. To perform this test, send a single instance or a batch of instances to the model service and validate the service response.
  * Canary-test the newly deployed model version on a small stream of live serving data. This test makes sure that the new model service doesn't produce errors before the model is exposed to a large number of users.
  * Test in a staging environment that you can roll back to a previous serving model version quickly and safely.
  * Perform online experimentation to test the newly trained model using a small subset of the serving population. This test measures the performance of the new model compared to the current one. After you compare the new model's performance to the performance of the current model, you might decide to fully release the new model to serve all of your live prediction requests. Online experimentation techniques include [A/B testing](https://en.wikipedia.org/wiki/A/B_testing) and [Multi-Armed Bandit (MAB)](https://www.tensorflow.org/agents/tutorials/intro_bandit).



## Quality guidelines for model serving

The predictive performance of the ML models that are deployed and are serving in production usually degrades over time. This degradation can be due to inconsistencies that have been introduced between the serving features and the features that are expected by the model. These inconsistencies are called _training-serving skew_. For example, a recommendation model might be expecting an alphanumeric input value for a feature like a most-recently-viewed product code. But instead, the product name rather than the product code is passed during serving, due to an update to the application that's consuming the model service.

In addition, the model can go stale as the statistical properties of the serving data drift over time, and the patterns that were learned by the current deployed model are no longer accurate. In both cases, the model can no longer provide accurate predictions.

To avoid this degradation of the model's predictive performance, you must perform continuous monitoring of the model's effectiveness. Monitoring lets you regularly and proactively verify that the model's performance doesn't degrade.

### Guidelines

  * Log a sample of the serving request-response payloads in a data store for regular analysis. The request is the input instance, and the response is the prediction that's produced by the model for that data instance.
  * Implement an automated process that profiles the stored request-response data by computing descriptive statistics. Compute and store these serving statistics at regular intervals.
  * Identify training-serving skew that's caused by data shift and drift by comparing the serving data statistics to the baseline statistics of the training data. In addition, analyze how the serving data statistics change over time.
  * Identify [concept drift](https://en.wikipedia.org/wiki/Concept_drift) by analyzing how feature attributions for the predictions change over time.
  * Identify serving data instances that are considered outliers with respect to the training data. To find these outliers, use novelty detection techniques and track how the percentage of outliers in the serving data changes over time.
  * Set alerts for when the model reaches skew-score thresholds on the key predictive features in your dataset.
  * If labels are available (that is, ground truth), join the true labels with the predicted labels of the serving instances to perform continuous evaluation. This approach is similar to the evaluation system that you implement as A/B testing during online experimentation. Continuous evaluation can identify not only the predictive power of your model in production, but also identify which type of request it performs well with and performs poorly with.
  * Set objectives for system metrics that are important to you, and measure the performance of the models according to those objectives.
  * Monitor service efficiency to make sure that your model can serve in production at scale. This monitoring also helps you predict and manage capacity planning, and it helps you estimate the cost of your serving infrastructure. Monitor efficiency metrics, including CPU utilization, GPU utilization, memory utilization, service latency, throughputs, and error rate.



## Model governance

Model governance is a core function in companies that provides guidelines and processes to help employees implement the company's AI principles. These principles can include avoiding models that create or enforce bias, and being able to justify AI-made decisions. The model governance function makes sure that there is a human in the loop. Having human review is particularly important for sensitive and high-impact workloads (often user-facing ones). Workloads like this can include scoring credit risk, ranking job candidates, approving insurance policies, and propagating information on social media.

### Guidelines

  * Have a [responsibility assignment matrix](https://en.wikipedia.org/wiki/Responsibility_assignment_matrix) for each model by task. The matrix should consider cross-functional teams (lines of business, data engineering, data science, ML engineering, risk and compliance, and so on) along the entire organization hierarchy.
  * Maintain model documentation and reporting in the model registry that's linked to a model's version—for example, by using [model cards](https://modelcards.withgoogle.com/). Such metadata includes information about the data that was used to train the model, about model performance, and about any known limitations.
  * Implement a review process for the model before you approve it for deployment in production. In this type of process, you keep versions of the model's checklist, supplementary documentation, and any additional information that stakeholders might request.
  * Evaluate the model on benchmark datasets (also known as _golden datasets_), which cover both standard cases and edge cases. In addition, validate the model against fairness indicators to help detect implicit bias.
  * Explain to the model's users the model predictive behavior as a whole and on specific sample input instances. Providing this information helps you understand important features and possible undesirable behavior of the model.
  * Analyze the model's predictive behavior using [what-if analysis tools](https://pair-code.github.io/what-if-tool/) to understand the importance of different data features. This analysis can also help you visualize model behavior across multiple models and subsets of input data.
  * Test the model against [adversarial attacks](https://openai.com/blog/adversarial-example-research/) to help make sure that the model is robust against exploitation in production.
  * Track alerts on the predictive performance of models that are in production, on dataset shifts, and on drift. Configure the alerts to notify model stakeholders.
  * Manage online experimentation, rollout, and rollback of the models.



## What's next

  * Read [The ML Test Score: A Rubric for ML Production Readiness and Technical Debt Reduction](https://research.google/pubs/pub46555/) from Google Research.
  * Read [A Brief Guide to Running ML Systems in Production](https://www.oreilly.com/content/a-brief-guide-to-running-ml-systems-in-production/) from O'Reilly.
  * Read [Rules for Machine Learning](https://developers.google.com/machine-learning/guides/rules-of-ml).
  * Try the [Testing and Debugging in Machine learning](https://developers.google.com/machine-learning/testing-debugging) training.
  * Read the [Data Validation in Machine Learning](https://mlsys.org/Conferences/2019/doc/2019/167.pdf) paper.
  * See the [E2E MLOps on Google Cloud](https://github.com/GoogleCloudPlatform/vertex-ai-samples/tree/main/notebooks/community/ml_ops) code repository.
  * For an overview of architectural principles and recommendations that are specific to AI and ML workloads in Google Cloud, see the [AI and ML perspective](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml) in the Well-Architected Framework. 
  * For more reference architectures, diagrams, and best practices, explore the [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



## Contributors

Author: [Mike Styer](https://www.linkedin.com/in/mstyer) | Generative AI Solution Architect

Other contributor: [Amanda Brinhosa](https://www.linkedin.com/in/amandafbri) | Customer Engineer

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-07-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-07-08 UTC."],[],[]] 
