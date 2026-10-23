---
url: https://docs.cloud.google.com/gemini/enterprise/docs/use-cases/brainstorm-new-content/
title: Brainstorm new content \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:13:37.029815+00:00
---

# Brainstorm new content  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/use-cases/brainstorm-new-content/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ App user guide ](https://docs.cloud.google.com/gemini/enterprise/docs/get-started)



Send feedback 

#  Brainstorm new content Stay organized with collections  Save and categorize content based on your preferences. 

Go from a blank page to a working outline in one turn, and then ground that outline in what your organization has already published so the draft sounds like you rather than like a template.

## Before you begin

The grounded prompt draws on your own material. Either attach your style guide and prior content, or make sure the relevant Google Drive folder or content source is connected and indexed, then reference the files by name in the prompt.

## Example prompt

To get a first outline quickly, enter a prompt in the chat box such as the following:
    
    
    Give me a 5-point outline for a blog post about why inventory forecasts break
    down during promotional periods. The audience is supply chain managers at
    mid-size retailers who own the forecast but don't build the models themselves.
    
    For each point, give the claim, why this audience cares, and the one example or
    number that would make it land. Flag any point where I'd need data I probably
    don't have.
    

To ground the outline in your own material, enter a prompt such as the following:
    
    
    You are a content strategist. Attached are our style guide and our ten
    highest-performing posts from the last year, with their pageview and
    engaged-time numbers.
    
    I want to write about why inventory forecasts break down during promotional
    periods, for supply chain managers at mid-size retailers.
    
    1. **What we've already said on this topic.** Any of our existing posts that
    overlap, what each one covers, and whether the new post should replace it,
    link to it, or be narrowed to avoid repeating it.
    
    2. **What actually performs for us.** Looking only at the attached numbers,
    what do our top posts have in common: length, structure, whether they lead with
    a claim or a story, use of data, headline pattern. Say which of these the
    numbers support and which is your impression.
    
    3. **Three angles** on the topic, each differentiated from what we've already
    published. For each: the argument, who it's aimed at, and why it's ours to make
    rather than anyone's.
    
    4. **An outline for the strongest angle**, following the structural pattern the
    data supports.
    
    5. **Voice check:** three phrases from the outline that don't match the style
    guide, quoted, with replacements.
    
    Rules:
    - Base the performance observations on the attached numbers only. Ten posts is
      a small sample; say where a pattern is thin.
    - Don't propose an angle that requires proprietary data we haven't published.
      If an angle needs data, say what data and who would have it.
    

## Example output

In response to the grounded prompt, Gemini Enterprise produces output similar to the following:

> ### What we've already said
> 
> Existing post | Overlap | Recommendation  
> ---|---|---  
> "Five forecasting mistakes" (Mar) | Section 3 covers promotional lift in two paragraphs | Link to it; the new post is the long version of that section  
> "Peak season readiness checklist" (Aug) | Operational, not analytical. No real overlap | Cross-link  
> "What good demand data looks like" (Jan) | Assumes clean baseline demand, which is exactly what the new post questions | Narrow the new post so it doesn't contradict this one without acknowledging it  
>   
> ### What performs for us
> 
> Supported by the numbers:
> 
>   * **Length.** The five highest engaged-time posts are 1,400-1,900 words. The three shortest posts in the set are also the three lowest. The pattern holds across all ten.
>   * **Leading with a claim.** Seven of the ten open with an assertion rather than a scenario. Those seven average roughly double the engaged time.
> 

> 
> My impression, not supported by the numbers:
> 
>   * Posts with a table seem to do better, but only three of the ten have one, and one of those is the weakest post in the set. Ten posts is too small a sample to call this.
> 

> 
> ### Three angles
> 
>   1. **"Your forecast isn't wrong during promotions; it's answering a different question."** Argues that baseline models are being asked to predict an event they were never fitted on. Aimed at managers who inherited a model they didn't build. Ours to make because our March post already established credibility on model diagnostics.
>   2. **"The markdown is the forecast error."** Reframes promotional markdowns as the visible cost of a forecast the organization already knows is wrong. Aimed at managers who need to make the case upward. Strongest angle for a finance-adjacent reader.
>   3. **"Stop measuring forecast accuracy in aggregate."** Argues that promotional weeks get averaged away in MAPE. Aimed at the analyst layer. Narrower audience, but nobody in our space has written it.
> 

> 
> ### Outline for angle 2
> 
> Following the pattern the data supports: open with the claim, 1,400-1,700 words, no scenario lead.
> 
>   1. **Open with the claim.** Markdown budgets are a forecast error line item that has been reclassified as a marketing cost.
>   2. **Why the two get separated.** Different owners, different systems, different review cycles. Nobody adds them up.
>   3. **What the combined number looks like.** [NEEDS DATA - a worked example with real figures. We have not published anything like this. Ask the analytics team whether an anonymized customer example can be used.]
>   4. **Why more safety stock doesn't fix it.** Moves the cost, doesn't remove it. Ties back to the March post.
>   5. **What to change.** Decompose promotional lift from baseline; measure accuracy on promotional weeks separately.
>   6. **Close on the reframe** , not on a product mention.
> 

> 
> ### Voice check
> 
> Phrase in the outline | Style guide says | Replacement  
> ---|---|---  
> "reclassified as a marketing cost" | Avoid nominalizations; prefer verbs | "gets counted as marketing spend"  
> "leverage the decomposition" | "leverage" is on the banned-words list | "separate promotional lift from baseline"  
> "in today's dynamic retail environment" | Style guide: cut throat-clearing openers | Delete; start with the claim  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
