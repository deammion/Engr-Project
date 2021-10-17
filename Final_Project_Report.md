# Final Project Report

**Project _Name_:** Shield all the things<br>
**Client:** Kirk Jackson<br>
**Date:** 18 October 2021<br>

## Project Objective(s)

The objective of this project is to create a working prototype of a proxy plugin program which will prevent cross site scripting (XSS) on websites. This plugin will be used with MITMproxy to collect, process, analyse and categorise scripts on a webpage to allow for the filtering of unsafe scripts. Filtering will be achieved through the use of Content Security Polciy (CSP) headers and Nonce Tags. Filtered/Blocked scripts should be blocked from execution and reported through report-uri. 

## Summary of Project Results

Full functionality achieved as per the objective stated above. The system is capable of watching traffic and collecting scripts as they pass through the plugin, then analysing them to learn which are common and/or safe. Then, the program can apply this information to add CSP headers and assign nonces to safe script tags. This will result in unsafe script tags being blocked from executing, hence preventing XSS. Blocked scripts are also reported as per the objective.

## Original and Delivered Scope

_The things that are within scope of the delivered project; the things that the delivered project can do. This should convey to the reader those aspects of the project results which are not obvious from other documents. If the project has a significant Issue backlog on delivery, a summary of the pending features, why these features were not completed and how they could be picked up by others if project work was to resume._

## Original and Actual Schedule

_A summary of the original timelines and a summary of deviations from the original plan. This should convey to the reader those aspects of the project results which are not obvious from other documents._

### Original Scope
|  Project Deliverables  | Date     |
| ---------------------- |  ------  |
| Architectural Prototype|   14th May|
| Collection Phase Implementation|   20th July |
| Analysis Phase Implementation |   3rd August |
| Operational Phase Implementation |   17th August |
| Application - Minimum Viable Product |   17th August  |
| Documentation - Minimum Viable Product |  13th August |
| Further Releases       |   8th October |
| Final Project          |   6th November |

Dates are subject to change as the project continues

### Delivered Scope
There were some deviations from the original plan in respect to implemtning each phase. This then resulted in the timeline of the minimum viable product to also be delayed. Furthermore, the minimum viable product, the further releases and final project all resulted in the same outcome. 

The following table depcits the deviations from the original timeline plan.

|  Project Deliverables  | Date     |
| ---------------------- |  ------  |
| Collection Phase Implementation|   3rd August |
| Analysis Phase Implementation |   17th August |
| Operational Phase Implementation |   28th Septemeber |
| Application - Minimum Viable Product |   7th October  |
| Documentation - Minimum Viable Product |  7th October  |
| Further Releases       |   7th October |
| Final Project          |   8th October |

## Delivered Expenditure

No expenditure

## Project Self-Assessment

_A short statement of the team’s assessment of the delivered project, with a focus on the technical aspects. This should convey to the reader those aspects of the project results which are not obvious from other documents._

## Lessons Learned

_Lessons learned which are of significance, impact and priority to the client. The focus here is on the lessons-learned at the intersection of the technical and management aspects of your project which are relevant to the client. Projects which have encountered significant technical or non-technical issues which will be of particular relevance to the client or the client's organisation should document these in this section._

## Procurement Summary

No procurements

---
