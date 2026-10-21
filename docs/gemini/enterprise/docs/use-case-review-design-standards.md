---
url: https://docs.cloud.google.com/gemini/enterprise/docs/use-case-review-design-standards/
title: Review design standards \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T11:27:09.206251+00:00
---

# Review design standards  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/use-case-review-design-standards/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ App user guide ](https://docs.cloud.google.com/gemini/enterprise/docs/get-started)



Send feedback 

#  Review design standards Stay organized with collections  Save and categorize content based on your preferences. 

Verify design standards or existing product specifications, drawing on integrated enterprise data.

## Example prompt

In the chat box, enter a prompt such as the following:
    
    
    What is the acceptable tolerance for the diameter of [COMPONENT]?
    

## Example output

In response to this prompt, Gemini Enterprise produces output similar to the following:

> The acceptable tolerance for a 25 mm steel drive shaft depends entirely on its application and the type of "fit" required with its mating components, such as bearings or gears. There is no single universal tolerance. Instead, engineers use a standardized system, ISO 286, to define these tolerances.
> 
> This system specifies different "fits," which are categorized into three main types:
> 
>   * **Clearance Fits:** The shaft is always smaller than the hole, allowing for rotation or sliding.
>   * **Transition Fits:** There can be either a small clearance or a slight interference, used for precise location where disassembly might be needed.
>   * **Interference Fits:** The shaft is intentionally larger than the hole, creating a solid, press-fit assembly that transmits torque.
> 

> 
> * * *
> 
> ### Factors That Determine the Right Tolerance
> 
> Several key factors must be considered to select the appropriate tolerance for a drive shaft:
> 
>   * **Mating Components:** The primary factor is what the shaft connects to. For instance, the fit for a ball bearing will be different from that for a gear or a pulley.
>   * **Operating Conditions:** High speeds, heavy loads, and significant temperature variations all demand tighter and more specific tolerances to prevent failure.
>   * **Rotational Component:** As a general rule, the part that rotates (usually the shaft) requires a tighter, interference fit with its mating component to prevent slipping or "creep."
>   * **Material:** The material of both the shaft and the housing is important. For example, an aluminum housing expands more with heat than a steel one and may require a tighter initial fit.
> 

> 
> * * *
> 
> ### Common ISO Tolerances for a 25 mm Shaft
> 
> For a nominal 25 mm diameter shaft, here are some common ISO tolerance "classes" and their corresponding dimensions. These classes are designated by a letter (which sets the tolerance position relative to the nominal size) and a number (which indicates the tolerance magnitude).
> 
> Fit Type | ISO Class | Upper Limit (mm) | Lower Limit (mm) | Application Examples  
> ---|---|---|---|---  
> **Clearance (Loose)** | h11 | 25.000 | 24.870 | Used where high accuracy is not needed, suitable for large temperature variations.  
> **Clearance (Running)** | g6 | 24.993 | 24.980 | For sliding parts and guiding shafts that need to move and turn freely with high accuracy.  
> **Clearance (Sliding)** | ... |  |  |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
