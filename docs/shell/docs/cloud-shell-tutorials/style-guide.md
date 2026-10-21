---
url: https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/style-guide/
title: Tutorial style guide \u00a0|\u00a0 Cloud Shell \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:29:21.244141+00:00
---

# Tutorial style guide  |  Cloud Shell  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/style-guide/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Shell ](https://docs.cloud.google.com/shell/docs)



Send feedback 

#  Tutorial style guide Stay organized with collections  Save and categorize content based on your preferences. 

The following guidelines will help you present your content in tutorial form so that your users can effectively familiarize themselves with your project.

## Cloud Shell features

  * **Unique layout:** Tutorials are presented in a side panel on the right hand side of Google Cloud console.
  * **Navigation:** Users can move through the tutorial using the **Next** and **Previous** buttons in each step. They can also close the tutorial and resume from where they left off.
  * **Code to go:** Code snippets can be copied directly into Cloud Shell.



![Google Cloud console session with tutorial launched](https://docs.cloud.google.com/static/shell/docs/images/cloud-shell-tutorial-style-guide.png)

_A Cloud Shell Editor session with a tutorial pane open. Users can copy code directly into Cloud Shell by clicking a button, and can move between pages with the**Next** and **Previous** buttons._

## Writing style

  * **Keep it light:** Tutorials should be informative and helpful in tone, but not overly formal.
  * **You, the user:** Use second person pronouns (**do use** : you, your; **don't use** : we, I, our, and so on)
  * **Explain cause and effect:** When asking users to carry out a step, explain the reasoning behind the action and the expected result.
  * **Have focused goals:** Before writing the content for your tutorial, establish a well-defined goal you want your users to accomplish. Craft your tutorial keeping this goal in mind.

Original  | Revised  | Improvement   
---|---|---  
On the next page, you'll learn how to create a new tutorial.  | Continue on to the next step to start setting up your tutorial.  | Focus on the user; use of active voice  Use of relaxed language   
Run this command:  ``` gcloud projects list --format="table[box,title=Projects](name, projectId)" ```  | To display a tabulated list of all your projects and their ID numbers, titled 'Projects', run the following command: ``` gcloud projects list --format="table[box,title=Projects](name, projectId)" ```  | Explanation of reasoning upfront to set expectations about the output   
`Let's get started!` | `Let's get started!` This guide will show you how to build your own interactive tutorial. It'll also walk you through generating a button that users can use to launch your finished tutorial.  | Clear roadmap of lessons covered in the tutorial  Make sure to keep this focus when writing content!   
  
## Best practices

  * **Keep it short:** The unique space constraints of the tutorial pane mean that a limited amount of information can be presented to a user at a time. Avoid large chunks of text that are difficult to scan and require vertical scrolling; favor information presented in bite-sized chunks.

    * Aim for no more than 5 steps and 3 code snippets per page.

    * Paragraphs should ideally be 5 lines or fewer and should deal with a singular concept.

    * If a page must be long, aim to have it be a maximum of twice the length of the pane.

    * Code and terminal blocks should be small enough to read:

      * Aim for 10 lines or less.
      * Aim for 80 characters or less per line, to reduce horizontal scrolling.
      * Avoid multi-command code blocks to prevent users from having to do a bulk copy-execute.
  * **Introductory page:** Start your tutorial off with an introduction.

    * **Set expectations:** Briefly explain how your users will profit from completing this tutorial.
    * **Estimated time commitment:** Roughly estimate how long users can expect to spend on the tutorial. Aim to create a tutorial that can be finished under 15 minutes. If your tutorial is longer (or consists of more than 15 densely worded pages), consider breaking it into a series of smaller tutorials.
    * **Be upfront:** Clearly state any prerequisite resources or access that users might need to have set up to work through the tutorial uninterrupted.
Example |  ## Let's get started! Get your users up and running quickly with your project by including an interactive tutorial. This guide will show you how to build your own interactive tutorial (like this one). It'll also walk you through generating a button that users can use to launch your finished tutorial. **Time to complete**: About 10 minutes **Prerequisites**: A Cloud Billing account Click the **Continue** button to move to the next step.   
---|---  
  * **Background page**

    * **Set the scene:** It's often helpful, when writing a tutorial, to furnish it with context. This might mean providing a short overview of the product or quickly running through salient features of a UI.
Example |  ## What is Cloud Shell? Before you get started, let's briefly go over what Cloud Shell can do. Cloud Shell is a personal hosted Virtual Machine which comes pre-loaded with developer tools for Google Cloud products. This interactive shell environment comes with a built-in code editor, persistent disk storage, and web preview functionality. To use command-line access alone, visit [console.cloud.google.com/cloudshell](https://console.cloud.google.com/cloudshell). You can direct your users to Cloud Shell to help them quickly get started with your project; giving them an opportunity to step through a use case and familiarize themselves with your project's functionality. Continue on to the next step to start setting up your tutorial.   
---|---  
  * **Basic Examples:**

    * **Hello World:** The first example you provide should be simple enough for your user to test without much explanation. It should be your Hello World equivalent. Use this example as a base to keep building on to exemplify concepts through the tutorial.
Example |  ## In-context tutorials What you're looking at now is an in-context tutorial. The content is shown along with the Cloud Shell environment where you can carry out the tutorial steps. Having the tutorial and development environment open in the same place makes it easier for your users to start using your project through a straightforward single screen experience. Try running a command now: ```bash echo "Hello Cloud Shell" ``` **Tip**: Click the copy button on the side of the code box to paste the command in the Cloud Shell terminal to run it. Next, you'll write and launch a basic tutorial.   
---|---  
  * **Tutorial Content**

    * **Format with caution:** Text formatting (bold, italics, etc.) is distracting; use it only when necessary and to your advantage (for warnings, key learnings, etc.).
    * **Consistent grammar:** Use imperative tense when describing user action and be sure to end sentences with a period.
    * **Refer to links:** Where essential for context, include supplementary links ([link text](link URL)) so that users can do their own research.
    * **Choose spotlighting over screenshots:** Spotlighting, an action that highlights where UI elements are in the Google Cloud console, demonstrates position so that users can identify elements without searching an image.
    * **Alternate view:** If possible, provide a link to your tutorial content offered as static content; this gives users the freedom to pick how they'd like to consume the provided information.
    * **Tips appreciated:** Where applicable, add in tips (called out by "**Tip:**") to provide users with more intuitive solutions and best practices.
Example |  ## Writing in Markdown To write your tutorial, use [Markdown](https://en.wikipedia.org/wiki/Markdown) and follow these guidelines:  ### Edit the title Modify the title of this tutorial ('# Introduction to writing tutorials in Cloud Shell') by changing it to: ``` # Teach me to write a tutorial ```  ### Add a new step Next, add a step just after the title like this: ``` ## Step 1 This is a new step I've just added. ```  Each 'step' of a tutorial is displayed on one page. **Tip**: To move through steps, users will use the 'Back' and 'Continue/Forward' buttons.   
---|---  
  * **Summary**

    * **Congratulations:** Be sure to add in a trophy icon (<walkthrough-conclusion-trophy></walkthrough-conclusion-trophy>) to appreciate users taking the time to finish the tutorial.
    * **Wrap up:** Summarize important lessons that you'd like users to take away from the tutorial.
    * **What's next:** Help users along their journey by providing next steps - these might be recommended reading, supplementary resources, or even, another tutorial.
    * **Look out for your users:** Advise them to clean up any test resources they created for the purposes of the tutorial to avoid unwanted billing charges.
Example |  ## Congratulations <walkthrough-conclusion-trophy></walkthrough-conclusion-trophy> You're all set! You can now have users launch your tutorial in Cloud Shell and have them start using your project with ease. For a complete list of Cloud Shell tutorial writing tools, see the [Tutorial Markdown Reference](https://cloud.google.com/shell/docs/tutorial-markdown-reference). **Don't forget to clean up after yourself**: If you created test projects, be sure to delete them to avoid unnecessary charges. Use `gcloud projects delete <PROJECT-ID>`.   
---|---  



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
