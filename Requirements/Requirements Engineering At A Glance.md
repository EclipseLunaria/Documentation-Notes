

# Overview
This document is a landing page for navigating through the note about requirements fundamental Concept. The primary source for the notes can be found in [IEEE 29148](obsidian://open?vault=Documentation%20Notes&file=Docs%2Fiso-iec-ieee-29148.pdf) section **5.2**. 


## General
Requirements engineering aims to establish agreed upon requirements that must be met by the system, software or service.

Activities involving Requirements Engineering include the following:
* Discovering
* Eliciting
* Developing
* Analyzing
* Determining Verification Methods
* Validating
* Communicating
* Documenting
* Managing
These activities results in a hierarchy of requirements that:
* Enables an agreed understanding between *[[Stakeholders]]*
* Can be implemented and validated against real-world needs 
* Determining acceptance criterion with a basis for verifying designs
**Note:** One or more [[Requirements Specifications]] may be used to represent a hierarchy of requirements. See [[Guidelines for information items]] for templates and [[Information Item Content]] for more details within the documents.

## Transforming Needs Into Requirements
In order to define requirements you must start with [[Stakeholder Intentions]]. Intentions do not serve as Stakeholder Requirements. The following documents are used as aids for defining requirements for the following groups:
* Organization Level: [[Concept of Operations]]
* System Level: [[System Operational Concept]]
It is the engineers job to translate the stakeholder intentions into stakeholder requirement statements. These statements are both structured and formalized. It is important that the statements characteristics conform to a Well Formed Requirement. When a requirements are well formed it contributes to requirements validation. It also ensures that the requirements accurately align with the stakeholders needs.

An in-depth look for how to define a well formed requirement may be found at [[Requirements Construct]]

Requirements can be ranked or weighted indicating:
- Priority
- Timing
- Relative Importance
depicting the systems actions from the user's perspective.

## Characteristics of Individual Requirements
Each stakeholder, system and system element requirement shall possess the following characteristics:
### Necessary
Defined by an essential:
- Capability
- Characteristic
- Constraint
- Quality Factor
If removed a deficiency will exist because it cannot be fulfilled by other capabilities of the product or process. Requirement must be currently applicable. Requirements with planned expiration date or applicability are clearly identified
### Implementation Free
the requirement avoids placing unnecessary constraints on the architectural design. The objective is to be implementation independent. The requirement defines what needs to be met not how.

### Unambiguous
There is a single way that the requirement can be interpreted. The requirement should be simple and easy to understand.

### Consistent
The requirement should not conflict with any other requirement.

### Complete
The requirement should not need further elaboration. It should be measurable and fully describe the the traits to meet the stakeholders needs.

### Singular
The requirement statement should not include multiple requirements with use of conjunctions (eg. and, or)

### Feasible
The requirement should be achievable without major technological advances and fit within the systems constraints

### Traceable
All parent-child relationships are identified in tracing that the requirement traces to its source to implementation.
#### Upward Traceability
The requirement should be able to be traced to specific:
- [[stakeholder statements]] of need
- higher tier requirement
- other sources (e.g. trade or design study)
#### Downward Traceability
The requirement should also be able to be traced down to:
- Specific requirements in the lower tier
- other system definition artifacts

### Verifiable
The Requirement should have the means to prove that the system meets the requirement. It can be shown to be satisfied through evidence. If the requirement is measurable it improves verifiability.

## Characteristics of a set of requirements
certain characteristics that need to be considered for the set of requirements rather than any individual requirements. This ensures that the requirements as a set collectively provide a feasible solution to meet [[Stakeholder Intentions]] and constraints. Each set shall contain the following characteristics:
#### Complete
No further elaboration needed on requirements as they are fully specifying the system or system element being specified. The set contains no:
- To Be Defined (TBD)
- To Be Specified (TBS)
- To Be Resolved (TBR)
Resolution of the TBx designations may be iterative and there is an acceptable within a given timeframe. The timeframe is determined by riskes

#### Consistent
The for a set of requirements to be consistent the following conditions must be met:
- No contradictory requirements
- No duplicate requirements
- The same item is required to have the same term used across all requirements

#### Affordable
The requirements should be feasibly be able to be satisfied within the given development lifecycle constraints.

#### Bounded
Set of requirements maintain identified scope for intended solution without going beyond necessary to satisfy the user needs.

---

## Types of Requirements 
It is important to distinguish between the different [[Types of Requirements Information|types of requirements]]. There are different levels and types of abstraction at different levels of the project. in order to distinguish between them they will be defined [[Types of Requirements Information|here]] and be explored in greater detail. 

---

## Requirements Attributes
In order to support [[Requirements Analysis|requirements analysis]], [[Requirements Construct#Characteristics|well-formed requirements]] should have descriptive attributes defined to help in clarifying and managing requirements. The **[[Requirements Attributes|requirements attributes]]** should be associated with the requirements in a dedicated requirements repository such as Git or similar technologies. A more in depth dive into requirements attributes may be found [[Requirements Attributes|here]].

---
## Iterative Vs. Recursive Processes
Both iterative and recursive process application is essential for the development in requirements engineering.

### Iterative Applications

![[Pasted image 20240417091908.png]]
Iterative processes are defined by a process or set of processes that are repeated on the same system level. In requirements development the iterative process is essential. Often time certain requirement are impossible to determine in detail without getting feedback from the existing system from the previous iteration. New information with respect to requirements takes the form of questions with respect to the requirements. as a result, reapplying the process allows the questions that arose to be resolved.

### Recursive Applications
![[Pasted image 20240417092848.png]]
Recursive application processes are processes are processes that are applied at successive system levels. When the higher level application is applied to the system then the outcome is used at the next lower level processes of the system which repeats until the lowest level. The system outcomes are much more detailed thus adding value to successive systems. The above figure shows the application of processes from the top down. Stakeholder requirements requirements may only  be applied at the system of interest level (top level). This is because often times most stakeholders only are concerned with the overall system and not fine details. However, both requirements analysis and architectural designs will be applied recursively to the lower levels. 

## Iteration and Recursion in Requirements Engineering
### Different Stakeholders Different Levels of Abstraction
Different stakeholders will often have different system level abstractions that they care about. For example the CEO of an organization might only care about the top system level. Meanwhile, a systems engineer may care more about the details of the system at a lower level. Meaning that it is important to partition the requirements in more detailed levels of the system.

This is done using Iterative and Recursive processes of requirements analysis and partitioned at the architectural design level. This allows room to make trade-offs in the system between architectural decisions. This partitioning allows for new *[[derived requirements]]*  to be elicited. These requirements are used to define relationships between architectural elements of the system. This is necessary to provide context between:
- Lower levels of abstraction of system elements
- Defining system design constraints and performance levels of system elements
This is accomplished through the *recursive* application of the requirements analysis process

Some requirements are impossible to derive until another part of the system evolves. While other requirements define how system elements interoperate. Recursive and iterative processes are applied to the requirements analysis and architectural design are needed to capture these requirements.

It is fairly rare that the analysis process is applied uniformly. Experienced engineers may find an off the shelf solution for a problem than a junior engineer. Thus off the shelf solutions may require less analysis. However, other problems require much more analysis in order to solve. *[[Critical Requirements]]* those which have high risk or impact public safety should always be rigorously analyzed.


## Requirement Information Items
This section will describe the relationships between [[Requirements Processes|requirements processes]] and [[Requirements Information Items|requirement information items]] in a typical application project.

![[Pasted image 20240417125226.png]]

There are multiple scopes to any given system of which the requirements processes and the resultant requirements are defined. Requirements are defined at the business level and propagated down to the system while system requirements operate and affect lower level. This relationship is illustrated above.

The following are specification documents intended to represent different sets of requirement information:
- [[Stakeholder Requirements Specification]] - StRS
- [[System Requirements Specification]] - SyRS
- [[Software Requirements Specification]] - SRS
It is important to note that a SyRS can be used to represent both system or a system component and software requirements. At the same time the SRS can be used for lower level requirements for software specific elements of a system or system element.

An example of the a sequence of requirements processes and specifications is shown below:
![[Pasted image 20240417131610.png]]

### Concept of Operation (ConOps)
the concept of operation communicates with leadership of how the organization will operate in regards to the project.

### Operational Concept (OpsCon)
Operational concept documents are a good tool for eliciting requirements. It is also a means to communicate the organizations intentions with stakeholders.