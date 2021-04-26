# ENGR 301: Architectural Design and Proof-of-Concept

## Proof-of-Concept

The aim of an architectural proof-of-concept (spike or walking skeleton) is to demonstrate the technical feasibility of your chosen architecture, to mitigate technical and project risks, and to plan and validate your technical and team processes (e.g., build systems, story breakdown, Kanban boards, acceptance testing, deployment).

A walking skeleton is an initial technical attempt that will form the architectural foundation of your product. Since a walking skeleton is expected to be carried into your product, it must be completed to the quality standards expected for your final product. A walking skeleton should demonstrate all the technologies your program will rely on "end-to-end" &mdash; from the user interface down to the hardware.

In the context of ENGR 301, a walking skeleton does not need to deliver any business value to your project: the aim is technical validation and risk mitigation.


## Document

The aim of the architectural design document is to describe the architecture and high-level design of the system your group is to build, to identify any critical technical issues with your design, and to explain how you have addressed the highest rated technical and architectural risks. The architecture document should also demonstrate your understanding of architectural techniques and architectural quality, using tools and associated notations as necessary to communicate the architecture precisely, unambiguously and clearly in a written technical document.

Page specifications below are *limits not targets* and refer to the pages in the PDF generated from the markdown. Because the size of your document is necessarily limited, you should ensure that you focus your efforts on those architectural concerns that are most important to completing a successful system: if sections are at their page limit, indicate how many items would be expected in a complete specification.

The ENGR 301 project architecture design document should be based on the standard ISO/IEC/IEEE 42010:2011(E) _Systems and software engineering &mdash; Architecture description_, plus appropriate sections from ISO/IEC/IEEE 29148:2018(E) _Systems and software engineering &mdash; Life cycle processes &mdash; Requirements engineering_; ISO/IEC/IEEE 15289:2017 _Systems and software engineering &mdash; Content of life-cycle information items (documentation)_; ISO/IEC/IEEE 15288:2015 _Systems and software engineering &mdash; System life-cycle processes_; ISO/IEC/IEEE 12207:2017 _Systems and software engineering &mdash; Software life cycle processes_ and ISO 25010 SQuaRE; with notations from ISO/ISE 19501 (UML). In particular, Annex F of ISO/IEC/IEEE 15288 and Annex F of ISO/IEC/IEEE 12207. These standards are available through the Victoria University Library subscription to the [IEEE Xplore Digital Library](https://ieeexplore.ieee.org/) (e.g., by visiting IEEE Xplore from a computer connected to the University network).

The document should contain the sections listed below, and conform to the formatting rules listed at the end of this brief.

All team members are expected to contribute equally to the document and list their contributions in the last section of the document (please make sure that your continued contribution to this document can be traced in GitLab). You should work on your document in your team's GitLab repository in a directory called "M2_Architecture". If more than one team member has contributed to a particular commit, all those team member IDs should be included in the first line of the git commit message. ``git blame``, ``git diff``, file histories, etc. will be tools used to assess individual contributions, so everyone is encouraged to contribute individually (your contribution should be made to many sections of the document, rather than focusing on just a single section), commit early and commit often.

---

# ENGR 301 Project *NN* Architectural Design and Proof-of-Concept

**Authors:** a comma-separated list of the names of each member of the team.

## 1. Introduction

One page overall introduction including sections 1.1 and 1.2 (ISO/IEC/IEEE 42010:2011(E) clause 5.2)

### Client

Company: RedShield

Contact: Kirk Jackson <br>
Email: 	kirk@redshield.co <br>
Address: <br>
    RedShield <br>
    Level 12 <br>
    RedShield House <br>
    79 Boulcott St <br>


### 1.1 Purpose

One sentence describing the purpose of the system.

### 1.2 Scope

One paragraph describing the scope of the system.

### 1.3 Changes to requirements

If the requirement have changed significantly since the requirements document, outline the changes here. Changes must be justified and supported by evidences, i.e., they must be substantiated. (max one page, only if required)

## 2. References

References to other documents or standards. Follow the IEEE Citation Reference scheme, available from the [IEEE website](https://ieee-dataport.org/sites/default/files/analysis/27/IEEE%20Citation%20Guidelines.pdf) (PDF; 20 KB). (1 page, longer if required)

## 3. Architecture

Describe your system's architecture according to ISO/IEC/IEEE 42010:2011(E), ISO/IEC/IEEE 12207, ISO/IEC/IEEE 15289 and ISO/IEC/IEEE 15288.

Note in particular the note to clause 5 of 42010:

_"The verb include when used in Clause 5 indicates that either the information is present in the architecture description or reference to that information is provided therein."_

This means that you should refer to information (e.g. risks, requirements, models) in this or other documents rather than repeat information.

### 3.1 Stakeholders

See ISO/IEC/IEEE 42010 clause 5.3 and ISO/IEC/IEEE 12207 clause 6.4.4.3(2).

For most systems this will be about 2 pages, including a table mapping concerns to stakeholder.

### 3.2 Architectural Viewpoints
(1 page, 42010 5.4) 

Identify the architectural viewpoints you will use to present your system's architecture. Write one sentence to outline each viewpoint. Show which viewpoint frames which architectural concern.

### 4. Architectural Views

(5 sub-sections of 2 pages each sub-section, per 42010, 5.5, 5.6, with reference to Annex F of both 12207 and 15288) 

Describe your system's architecture in a series of architectural views, each view corresponding to one viewpoint.

You should include views from the following viewpoints (from Kruchten's 4+1 model):

 * Logical
 * Development
 * Process
 * Physical 
 * Scenarios - present scenarios illustrating how two of your most important use cases are supported by your architecture

As appropriate you should include the following viewpoints:

 * Circuit Architecture
 * Hardware Architecture

Each architectural view should include at least one architectural model. If architectural models are shared across views, refer back to the first occurrence of that model in your document, rather than including a separate section for the architectural models.

### 4.1 Logical
...

### 4.2 Development
...

### 4.3 Process
...

### 4.4 Physical 
...

### 4.5 Scenarios
...

## 5. Development Schedule

_For each subsection, make clear what (if anything) has changed from the requirements document._ If unchanged, these sections should be copied over from the requirements document, not simply cross-referenced.

Schedules must be justified and supported by evidences; they must be either direct client requirements or direct consequences of client requirements. If the requirements document did not contain justifications or supporting evidences, then both must be provided here.

### 5.1 Schedule

Identify dates for key project deliverables:

|  Project Deliverables  | Date     |
| ---------------------- |  ------  |
| Architectural Prototype|   Friday 7th May |
| Minimum Viable Product |   Monday 16th August |
| Further Releases       |   Friday 8th October |
| Final Project          |   Saturday 6th November |

Dates are subject to change as the project continues


### 5.2 Budget and Procurement

#### 5.2.1 Budget

| Item     | Amount |
| -------- |  ----- |
| Software |  nil   |
| Hardware |  nil   |
| Travel   |  nil   |

This project does not require a budget as it makes use of open-source programs such as MITM. Accessing this can be done using personal computers or the computers available at Victoria University of Wellington.<br>

The client is local and has indicated they can travel to Victoria University of Wellington for meetings.<br>

#### 5.2.2 Procurement

As Stated in Section 5.2.1, as of writing this document, there is no budget requirements for this project. Therefore, there are no procurement requirements. <br> 

### 5.3 Risks 

Identify the ten most important project risks: their type, likelihood, impact, and mitigation strategies (3 pages).

### 5.4 Health and Safety

**Occupational Overuse**
Occupational Overuse is a type of overuse injury that may result in Muscle pains, hot or cold flushes, numbness or a restricted range of movement. To prevent this from happening team members will be encouraged to take regular breaks away from their work and personal devices. Furthermore realistic deadlines and workloads will be set to discourage overworking, alongside getting the team to practice good time management to prevent overuse to meet deadlines.
Additionally, team members will have ergonomic workspaces so that any required equipment will be nearby and easily accessible. This will also encompass ensuring desks are at the correct height to encourage correct posture and reduce straining. Correct postures will be promoted and ensured for all team members and the team will use comfortable chairs which if possible, will have back support. This will reduce straining and incorrect postures in a work environment, mitigating occupational overuse and its potential symptoms.
https://www.southerncross.co.nz/group/medical-library/occupational-overuse-syndrome-oos

**Eye Strain**
Eye strain occurs when a person has been staring at a computer for large periods without having any breaks away from technology. Insufficient lighting and screen flickering can also contribute to eye strain. As with the Occupational Overuse, the team will be encouraged to take regular breaks away from their work and personal devices. The team will also be encouraged to work in environments that have a sufficient level of lighting, for example not working in the dark with the screen as your only light. The team will also make sure that text displayed in any of the work produced is easily readable to avoid eye strain from having to read small text.

**Electrical Saftey**
Since we are dealing with technology there is the risk of receiving electrical shocks from any appliances that are used in the process of working on this project. This could pose a small risk to the health of team members when they are dealing with electrical appliances such as laptops, desktop computers, monitors, electrical jugs, and the associated cables for these appliances.  As per the AS/NZS 3760 Standard, to minimise the risk of any electrical shocks the team should be encouraged to only use appliances which have been through the Test and Tag process in the last 12 months.

**Cable Management**
Unmanaged cables are a safety risk as team members or nearby people can get caught on them and/or trip on them. To manage this risk, all team members will ensure that any cables they use will be kept underneath their desk, mitigating the possibility of someone getting caught on them. Furthermore, all cables which are not being used will be stored away in a cupboard or bag to further mitigate the risk unmanaged cables pose.

**COVID-19 Outbreak and/or Lockdown**
To manage the safety risk of another Covid-19 outbreak or lockdown, team members will ensure all work is saved online using Gitlab so access to the University labs is not mandatory. Furthermore, everyone involved in the project will ensure they have a way to contact each other online. This will ensure all members of the team can work from home. This will mitigate this safety risk as it ensures that if there was a Covid-19 outbreak or lockdown, members do not need to expose themselves to any additional Covid-19 risks to do this project.

**Natural Disaster**
To manage the safety risk of earthquakes, cyclones, or tsunamis team members will ensure that they each have an understanding of the basic Natural Disaster responses that should be carried out in the event of any of the above mentioned natural disasters so that our team maximises their chances of getting through the disasters without injury. This basic knowledge should include what to do in the initial stage of a natural disaster as well as where to go and what to do after a natural disaster has occurred.

**Health and Safety at External Workplaces**
The project does not require any work or testing to be held off-campus. However, there is a possibility that some meetings will be held at Red Shield’s office. To receive a Health and Safety induction for this external workplace, team members will get in contact with the client to arrange this, before any work being done at the clients' office.

**Human or Animal Test Subjects**

This project does not include any human or animal subjects. This is because all testing can and will be done by the team, using different web applications.

#### 5.4.1 Safety Plans

Safety Plans may be required for some projects, depending on project requirements.


## 6. Appendices

### 6.1 Assumptions and dependencies 

One page on assumptions and dependencies (9.5.7) 
Below is a list of assumptions and dependencies for this project:<br>

* It is assumed that during the collection phase, the websites scanned (HTML being parsed) will be clean. <br>
* It is assumed that if the scripts are hosted on a different domain, they have not been modified after the original application developer determining they are safe to include in their application. <br>
* It is assumed that users of this program will have access to either of the following browsers: Edge, Chrome or Firefox.<br>
* It is assumed that users have access to a technological device (i.e. computer, cellular phone, tablet).<br>
* It is assumed that users have internet access to run this program.<br>
* A dependency is that the browsers used must either be Edge, Chrome or Firefox to gain the full benefits of security from CSP being inforced client-side. <br>

### 6.2 Acronyms and abbreviations

One page glossary as required 

## 7. Contributions

An one page statement of contributions, including a list of each member of the group and what they contributed to this document.

| Contributors  | Sections    |
| ------        |  ---------- |
|    Dylan      |             |
|    Isabella   |             |
|    Damien     |             |
|    James      |             |
|    Jaya       |             |
|    Nathan     |             |
|    Timothy    |             |

---

## Formatting Rules 

 * Write your document using [Markdown](https://gitlab.ecs.vuw.ac.nz/help/user/markdown#gitlab-flavored-markdown-gfm) in your team's GitLab repository.
 * Major sections should be separated by a horizontal rule.


## Assessment 

This document will be weighted at 20% on the architectural proof-of-concept(s), and 80% on the architecture design.

The proof-of-concept will be assessed for coverage (does it demonstrate all the technologies needed to build your project?) and quality (with an emphasis on simplicity, modularity, and modifiability).

The document will be assessed by considering both presentation and content. Group and individual group members will be assessed by identical criteria, the group mark for the finished PDF and the individual mark on the contributions visible through `git blame`, `git diff`, file histories, etc. 

The presentation will be based on how easy it is to read, correct spelling, grammar, punctuation, clear diagrams, and so on.

The content will be assessed according to its clarity, consistency, relevance, critical engagement and a demonstrated understanding of the material in the course. We look for evidence these traits are represented and assess the level of performance against these traits. Inspection of the GitLab Group is the essential form of assessing this document. While being comprehensive and easy to understand, this document must be reasonably concise too. You will be affected negatively by writing a report with too many pages (far more than what has been suggested for each section above).

---
