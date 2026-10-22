---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/vizier/overview/
title: Agent Platform Vizier overview \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:14:14.586891+00:00
---

# Agent Platform Vizier overview  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/vizier/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Agent Platform Vizier overview Stay organized with collections  Save and categorize content based on your preferences. 

Agent Platform Vizier is a tool for optimizing any system with configurable parameters where evaluating any given parameter settings is an expensive task. When ML models have many different hyperparameters, it can be difficult and time consuming to tune them manually. Agent Platform Vizier optimizes your model's output by tuning the hyperparameters for you.

_Black-box optimization_ is the optimization of a system that meets either of the following criteria:

  * Doesn't have a known [objective function](https://developers.google.com/machine-learning/glossary#objective-function) to evaluate.

  * Is too costly to evaluate by using the objective function, usually due to the complexity of the system.




## Additional Agent Platform Vizier functionality

Agent Platform Vizier optimizes hyperparameters of ML models, but it can also perform other optimization tasks.

### Tune parameters

You can use Agent Platform Vizier to effectively tune parameters in a function. For example, use Agent Platform Vizier to determine the most effective combination of background color, font size, and link color on a news website Subscription button. For more examples, see the use cases.

[Read about the difference between hyperparameters and parameters](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/hyperparameter-tuning-overview).

### Optimize any evaluable system

Agent Platform Vizier works with any system that you can evaluate, including systems that can't be expressed as a closed-form analytical function. For example, use Agent Platform Vizier to find the best neural network depth, width, and learning rate for a TensorFlow model.

## How Agent Platform Vizier works

The following sections define terms, behavior, and available values that you can use with Agent Platform Vizier to optimize your ML model or function. Start by determining a [study configuration](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.studies).

### Study configurations

A _study configuration_ is the definition of the optimization problem that you are trying to solve. It includes the result you would like to optimize and the hyperparameters or parameters that affect that result.

### Studies and trials

A _study_ is the implementation of a study configuration. A study uses the study configuration goals (metrics) and input values (hyperparameters or parameters) to conduct experiments, called trials. A _trial_ is a specific set of input values that produce a measured outcome relative to your goals.

Agent Platform Vizier suggests input values to use for each trial but it does not run trials for you.

A study continues until it reaches a set limit of trials, or you interrupt the study. A trial continues until you indicate that it is either finished or infeasible.

### Measurements

A _measurement_ is the measured outcome of your trial. Each measurement can contain one or more metrics, and each trial can contain one or more measurements taken over a period of time. You can add a new measurement to the trial at any point before the trial is completed.

### Search algorithms

If you don't specify an algorithm, Agent Platform Vizier uses the default algorithm. The default algorithm applies Bayesian optimization to arrive at the optimal solution with a more effective search over the parameter space.

The following values are available:

  * `ALGORITHM_UNSPECIFIED`: Same as not specifying an algorithm. Agent Platform chooses the best search algorithm between Gaussian process bandits, linear combination search, or their variants.

  * `GRID_SEARCH`: A grid search within the feasible space. This option is useful if you want to specify a quantity of trials that is greater than the number of points in the feasible space. In such cases, if you don't specify a grid search, the default algorithm can generate duplicate suggestions. To use grid search, all parameters must be of type `INTEGER`, `CATEGORICAL`, or `DISCRETE`.

  * `RANDOM_SEARCH`: A random search within the feasible space.




## How Agent Platform Vizier differs from custom training

Agent Platform Vizier is an independent service for optimizing complex models with many parameters. It can be used for both ML and non-ML use cases. It can be used with Training jobs or with other systems (even multi cloud). [Hyperparameter tuning for custom training](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/hyperparameter-tuning-overview) is a built-in feature that uses Agent Platform Vizier for training jobs. It helps determine the best hyperparameter settings for an ML model.

## Use cases

In the following scenarios, Agent Platform Vizier helps tune hyperparameters to optimize a model or tune parameters to optimize an outcome:

  * Optimize the learning rate, batch size, and other hyperparameters of a neural network recommendation engine.

  * Optimize usability of an application by testing different arrangements of user interface elements.

  * Minimize computing resources for a job by identifying an ideal buffer size and thread count.

  * Optimize the amounts of ingredients in a recipe to produce the most delicious version.




## What's next

  * To learn more about how Agent Platform Vizier tunes multi-objective functions, see [Random Hypervolume Scalarizations for Provable Multi-Objective Black Box Optimization](https://arxiv.org/abs/2006.04655).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
