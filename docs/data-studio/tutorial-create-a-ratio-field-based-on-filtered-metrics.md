---
url: https://docs.cloud.google.com/data-studio/tutorial-create-a-ratio-field-based-on-filtered-metrics/
title: Tutorial: Create a ratio field based on filtered metrics \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:43:54.161733+00:00
---

# Tutorial: Create a ratio field based on filtered metrics  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/tutorial-create-a-ratio-field-based-on-filtered-metrics/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Tutorial: Create a ratio field based on filtered metrics Stay organized with collections  Save and categorize content based on your preferences. 

A common use case in reporting and data visualization is to display key performance indicators (KPI) as ratios of one indicator as compared to another. For example, suppose you are measuring the completion rate of an online coding academy. A KPI for the course is completion rate, which we'll define here as:

`Course completions / Course registrations`

If your dataset already contains this data then you can display the result in Data Studio. But what if you need to calculate it in your report, or need to display completion rates based on filtered data? The solution is to use data blending.

Say your data looks like this:

**Event Category** |  **Event Action** |  **Course Number** |  **Unique Events**  
---|---|---|---  
Course Certificate  |  Download  |  9  |  299   
Course Complete  |  Fail  |  8  |  21   
Course Complete  |  Fail  |  9  |  86   
Course Complete  |  Pass  |  9  |  337   
Course Complete  |  Fail  |  6  |  34   
Course Complete  |  Pass  |  7  |  363   
Course Complete  |  Fail  |  7  |  17   
Registration  |  Register  |  8  |  814   
Registration  |  Register  |  7  |  475   
Registration  |  Register  |  5  |  574   
Registration  |  Register  |  9  |  1078   
Registration  |  Unregister  |  6  |  22   
  
## Step 1: Calculate the course completions

  1. Add a scorecard to your report. Call it **Course Completions**.
  2. Set the metric to _Unique Events_.
  3. Add a filter to the scorecard to ignore non-completion events:

`Include`**`Event Category`**`= "Course Complete"`

`AND`

`Include`**`Event Action`**`= "Pass"`




Based on the sample data, the scorecard would look like this:

Course Completions700  
---  
  
## Step 2: Calculate the course registrations

  1. Add a scorecard to your report. Call it **Course Registrations**.
  2. Set the metric to _Unique Events_.
  3. Add a filter to the scorecard to ignore non-registration events:

`Include`**`Event Category`**`= "Registration"`

`AND`

`Include`**`Event Action`**`= "Register"`




Based on the sample data, the scorecard would look like this:

Course Registrations2,941  
---  
  
## Step 3: Blend the data from the scorecards

  1. Select the _Course Registrations_ scorecard, then select the _Course Completions_ scorecard.
  2. Right-click, then select **Blend data**.



This creates a new scorecard that automatically calculates the ratio between those metrics:

Course Completion Rate23.80%  
---  
**Tip:**

To create more complex calculated fields or change the number display:

  1. Select the blended scorecard.
  2. Edit the metric.
  3. Enter a new formula and/or change the field **Type** to match the data.

![A user selects a scorecard chart that displays 72.76% Users/Sessions and then edits the Users/Sessions metric definition by selecting the Type icon next to the field name.](https://docs.cloud.google.com/static/data-studio/images/edit-scorecard-2019-09-12-rge.png)

## Related resources

Learn more about how blending works:

  * [About data blending](https://docs.cloud.google.com/data-studio/how-blends-work)
  * [Use blending to re-aggregate data](https://docs.cloud.google.com/data-studio/use-blending-to-reaggregate-data)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
