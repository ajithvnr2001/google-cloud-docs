---
url: https://docs.cloud.google.com/python/docs/reference/optimization/latest/google.cloud.optimization_v1.types.InjectedSolutionConstraint.ConstraintRelaxation.Relaxation.Level
title: Class Level (1.16.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:34:53.565620+00:00
---

# Class Level (1.16.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/optimization/latest/google.cloud.optimization_v1.types.InjectedSolutionConstraint.ConstraintRelaxation.Relaxation.Level

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Level (1.16.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.16.0 (latest)  1.15.0  1.14.0  1.13.0  1.12.0  1.11.2  1.10.0  1.9.1  1.8.5  1.7.0  1.6.0  1.5.0  1.4.3  1.3.2  1.2.0  1.1.3  1.0.1  0.1.1 
    
    
    Level(value)

Expresses the different constraint relaxation levels, which are applied for a visit and those that follow when it satisfies the threshold conditions.

The enumeration below is in order of increasing relaxation.
    
    
        This value must not be explicitly used in `level`.
    RELAX_VISIT_TIMES_AFTER_THRESHOLD (1):
        Visit start times and vehicle start/end times
        will be relaxed, but each visit remains bound to
        the same vehicle and the visit sequence must be
        observed: no visit can be inserted between them
        or before them.
    RELAX_VISIT_TIMES_AND_SEQUENCE_AFTER_THRESHOLD (2):
        Same as `RELAX_VISIT_TIMES_AFTER_THRESHOLD`, but the visit
        sequence is also relaxed: visits can only be performed by
        this vehicle, but can potentially become unperformed.
    RELAX_ALL_AFTER_THRESHOLD (3):
        Same as `RELAX_VISIT_TIMES_AND_SEQUENCE_AFTER_THRESHOLD`,
        but the vehicle is also relaxed: visits are completely free
        at or after the threshold time and can potentially become
        unperformed.
    

## Enum  
  
---  
**Name** | **Description**  
`LEVEL_UNSPECIFIED` | Implicit default relaxation level: no constraints are relaxed, i.e., all visits are fully constrained.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
