---
url: https://docs.cloud.google.com/data-studio/blending-example-classes-students-and-grades/
title: Blending example: Classes, students, and grades \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:08:58.509715+00:00
---

# Blending example: Classes, students, and grades  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/blending-example-classes-students-and-grades/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)



Send feedback 

#  Blending example: Classes, students, and grades Stay organized with collections  Save and categorize content based on your preferences. 

Suppose you are a school administrator and that you store information about the classes offered, the students who enroll in those classes, and the grades they receive in each class. You can use Data Studio to track and visualize this information by using data blending.

**See a demonstration report** : Copy and edit a [live demonstration report](https://datastudio.google.com/reporting/edb8c110-6946-4054-a287-8fe65fcce8f6/page/r7vQ) to see how blending works. (This report is available only in English.) 

## Questions to answer

This example answers the following questions that you might have about the data:

  * Which students took which classes, and what grade did each student receive in each class?
  * What was the highest grade received in each class?
  * Which student received the highest grade in each class?



## Sample data

Here's the data used in the examples.

**Classes** :

class_id  |  class_name   
---|---  
c1  |  Underwater basket weaving   
c2  |  Home fusion made easy   
c3  |  How to train an attack iguana   
c4  |  Learn SQL for fun and profit   
  
**Students** :

student_id  |  student_name   
---|---  
s1  |  Brett   
s2  |  Rick   
s3  |  Susanna   
s4  |  Jennifer   
  
**Grades** :

student_id  |  class_id  |  grade   
---|---|---  
s1  |  c1  |  2   
s2  |  c1  |  99   
s3  |  c1  |  65   
s4  |  c1  |  3   
s2  |  c2  |  38   
s3  |  c2  |  88   
s4  |  c2  |  48   
s1  |  c3  |  7   
s4  |  c3  |  32   
s1  |  c4  |  94   
s2  |  c4  |  63   
s3  |  c4  |  75   
s4  |  c4  |  20   
**Tip:** Follow along with the examples in this document by making a copy of this data using [Google Sheets](https://docs.google.com/spreadsheets/d/1v74etUJflbLMfrfmlyAH2wFS99rcsVJrrRF6YmIAsW4/edit?usp=sharing).

## Setup

The first step is to connect to your data by creating data sources in Data Studio. The demonstration report uses Sheets for the underlying data, but you could also store this data in a database, such as BigQuery or MySQL.

  1. Create a new report.
  2. Add 3 data sources corresponding to the sample data: 
     1. Classes
     2. Students
     3. Grades



Learn how to [create and edit data sources](https://docs.cloud.google.com/data-studio/about-data-sources).

## Question 1: Students, classes, and grades received

**Question** : "Which students took which classes, and what grade did each student receive in each class?"

To answer this question, follow these steps:

  1. Create a new blend.
  2. Add a **Grades** table with the following dimensions: 
     1. `student_id`
     2. `class_id`
     3. `grade`
  3. Add a **Students** table with the following dimensions: 
     1. `student_id`
     2. `student_name`
  4. Add a **Classes** table with the following dimensions: 
     1. `class_id`
     2. `class_name`
  5. Join **Grades** to **Students** with `student_id`.
  6. Join **Grades** to **Classes** with `class_id`.
  7. Set both join operations to left outer. ![A blend configuration displays left outer join conditions selected between the Grades and Students tables, and between the Students and Classes tables.](https://docs.cloud.google.com/static/data-studio/images/grades-blend-2022-02-15.png)
  8. Save the blend and close the editor.
  9. Add a table to the report with the `student_name`, `class_name`, and `grade` fields.
  10. Sort the table by `student_name`, descending.



Your table should look like this:

student_name | class_name | grade  
---|---|---  
Brett | Underwater basket weaving | 2  
Brett | How to train an attack iguana | 7  
Brett | Learn SQL for fun and profit | 94  
Jennifer | Underwater basket weaving | 3  
Jennifer | Home fusion made easy | 48  
Jennifer | How to train an attack iguana | 32  
Jennifer | Learn SQL for fun and profit | 20  
Rick | Underwater basket weaving | 99  
Rick | Home fusion made easy | 38  
Rick | Learn SQL for fun and profit | 63  
Susanna | Underwater basket weaving | 65  
Susanna | Home fusion made easy | 88  
Susanna | Learn SQL for fun and profit | 75  
  
## Question 2: Highest grade by class

**Question** : "What was the highest grade received in each class?"

To answer this question, follow these steps:

  1. Use the same blend as in Question 1.
  2. Add a table to the report.
  3. Add `class_name` as a dimension and `grade` as a metric.
  4. Edit the `grade` field as follows: 
     1. Change the name to `max_grade`.
     2. Set the aggregation to **MAX**.
  5. Sort the table by `max_grade`, descending.

![Table Setup tab with Blended Data as the Data source, class_name as a Dimension, and max_grade as a Metric.](https://docs.cloud.google.com/static/data-studio/images/max-grade-table-2022-02-15.png)




Your table should look like this:

class_name | max_grade  
---|---  
Underwater basket weaving | 99  
Learn SQL for fun and profit | 94  
How to train an attack iguana | 32  
Home fusion made easy | 88  
  
## Question 3: Highest grade by student by class

**Question** :"Which student received the highest grade in each class?"

To answer this question, follow these steps:

  1. Create a new blend.
  2. Add a **Classes** table with the following dimensions: 
     1. `class_id`
     2. `class_name`
  3. Add a **Grades** table, name it **Grades 1** , and add dimension `class_id`.
  4. Add `grade` as a metric, and set the aggregation to **MAX**.
  5. Rename `grade` to `max_grade`.
  6. Add the **Grades** table again, name it **Grades 2** , and add dimensions: 
     1. `student_id`
     2. `class_id`
     3. `grade`
  7. Add a **Students** table, with dimensions: 
     1. `student_id`
     2. `student_name`
  8. Use **left outer** for each join.
  9. Join **Classes** to **Grades** with `class_id`.
  10. Join **Grades** to **Grades 2** with: 
     1. `class_id = class_id`
     2. `max_grade = grade`
  11. Join **Grades 2** to **Students** with `student_id`.

![A blend configuration displays left outer join conditions selected between the Classes and Grades 1 tables, the Grades 1 and Grades 2 tables, and the Grades 2 and Students tables.](https://docs.cloud.google.com/static/data-studio/images/max-grade-student-class-2022-02-15.png)

  12. Save the blend and close the editor.

  13. Add a table to the report with the `student_name`, `class_name`, and `max_grade` fields.

![The Setup tab for a blended data table chart with the student_name, class_name, and max_grade dimensions and the max_grade metric selected.](https://docs.cloud.google.com/static/data-studio/images/max-grade-student-class-table-2022-02-15.png)




Your table should look like this:

student_name | class_name | max_grade  
---|---|---  
Rick | Underwater basket weaving | 99  
Brett | Learn SQL for fun and profit | 94  
Susanna | Home fusion made easy | 88  
Jennifer | How to train an attack iguana | 32  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
