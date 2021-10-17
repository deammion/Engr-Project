# Final Project Report

**Project _Name_:** Shield all the things<br>
**Client:** Kirk Jackson<br>
**Date:** 18 October 2021<br>

## Project Objective(s)

The objective of this project is to create a working prototype of a proxy plugin program which will prevent cross site scripting (XSS) on websites. This plugin is an add-on for MITMproxy. Which will collect, process, analyse and categorise scripts on a webpage to allow for the filtering of unsafe scripts. Filtering will be achieved through the use of Content Security Polciy (CSP) headers and Nonce Tags. Filtered/Blocked scripts should be blocked from execution and reported through report-uri.

## Summary of Project Results

Full functionality was achieved as per the objective stated above. The plugin is capable of monitoring traffic and collecting HTTP flows and analysing scripts as they pass through the proxy. This process will allow the plugin to learn which scripts are common and/or safe. The program will use this information to apply CSP headers and assign nonces to safe script tags. This will result in unsafe script tags being blocked from executing, hence preventing XSS. Blocked scripts are also reported as per the objective.

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

The team was able to achieve all the objectives set by the client. The plugin can monitor traffic, capture and store HTTP flows (Collection class). From these flows the plugin can read these HTTP files, analyse the scripts within these files and produce a database of safe scripts (Analysis class). The plugin can then use this database to apply the CSP to the HTTP response (Operational class).<br>

The Analysis class is desgined in a way that it can be called each time a HTTP response is captured, or independently. Meaning the class will function correctly whether it is analysing one HTTP file or thousands of files. It does this by, first reading from the Database file (if it exists), then reading and analyising the new HTTP files.<br>

## Lessons Learned
Throughout this project, as a group we learnt how to use Python. Only one member from the group had expereince using Python, so the rest of us
had to learn. This was a challenge at the start because despite Python being similar to Java (a langauge we are all fimilar with) i.e., it is an object oriented langauge, with different syntax, it was still a hurdle to get around.<br>
Furthermore we learnt how to use the Man-in-the-Middle proxy. This was an entirely new piece of software that we were directed to use by the client, Kirk at RedShield.
It was originally very difficult to get it working on all members of the groups' laptops. We found that the documentation was somewhat confusing
however we managed to get it done in the end.<br>
We also learnt how to use deadlines/Scheduling and produce deliverables for a client. It was beneficial that we were ahead of Schedule, which allowed for refactoring and polishing the program. <br>


## Procurement Summary

No procurements

---
