## Overview
This page will go into detail into the construction of a well formed requirement. It will start with the characteristics of a well formed requirement. followed with the structure and examples.

---
## Characteristics
A well-formed requirement is a statement that:
- Can be verified
- must be met or possessed by a system
- Solves a [[Stakeholders]] problem or achieve a goal.
- Is qualified by measurable conditions
- Is bounded by [[Requirements Construct#Constraints|constraints]])
- defines the systems performance when used by specific [[stakeholders]] or capability of the system
These characteristics provide a means of distinguishing between requirements and their [[Requirements Attributes|attributes]] such as:
- Conditions
- Assumptions
- Design Decisions
- Constraints
------------------
## Construction Guidance
A requirement is a statement expressing a need with associated constraints and conditions. When constructed in natural-language the statement should comprise of a:
#### Subject
- The System
- The Software
#### Verb
- Operate at a power level
- Provide a field for

#### Compliment

------------------------
### Common Approaches
The signal if a requirement should be agreed upon in advance. The following examples such as:
#### Shall:
- Mandatory
- Binding Provisions
#### Will:
- Non-Mandatory
- Statements of Fact, Futurity, or Declaration of Purpose
- Establish context or limitations of use
- May be construed as **legally binding**
- best to avoid for using it in requirements
#### Should
- Non-Mandatory
- Non-Binding Provisions 
- Preference or goals are desired
### Avoid
- Non-requirements such as descriptive text (e.g. are, is, was)
- Must as it may be misinterpreted as a requirement
- Avoid negative requirements such as **"Shall Not"**
- Avoid passive voice such as **"shall be able to select"**
All terms specific to requirements should be formally defined and applied consistently throughout all system requirements.

--------------------------------
## Requirement Language Criteria
the following considerations will help ensure that good requirement characteristic are employed.

### What not How
Requirements should state *what* is needed for the system not *how* it should be implemented such as design decisions. However, design decisions / solutions architectures are defined at a higher level. This is part of the iterative and recursive application of requirements analysis and architectural design process.

### Terms to Avoid:
When terms in requirements are vague or ambiguous it can lead to the requirements being extremely difficult even impossible to verify or have multiple interpretations. the following types of unbound and ambiguous terms:
#### Superlatives
- best
- most
#### Subjective Language
- user friendly
- easy to use
- cost effective
#### Vague Pronouns
- it
- this
- that
#### Ambiguous Adverbs and Adjectives
- almost always
- significant
- minimal
#### Open-ended, Non-verifiable Terms
- provide support
- but not limited to
- as a minimum
#### Comparative Phrases
- better than
- higher quality
#### Loopholes
- if possible
- as appropriate
- as applicable 
#### Incomplete References
- not specifying the reference with its date and version number.
- not specifying just the applicable parts of the reference to restrict verification work
#### Negative Statements
such as statement of "system capability not to be provided"

### Requirement Assumptions
All assumptions regarding the requirement should be documented and validated in one of the [[Requirements Attributes|requirements attributes]] associated with a requirement or in an accompanying document. Include definitions as declarative statements, not requirements.

---

## Examples of Requirement Syntax

#### **{Condition} {Subject} {Action} {Object} {Constraint}**

**Example:** when Signal x is recieved *{Condition}*, the system *{Subject}* shall set *{Action}* the signal x received bit *{Object}*

#### {Condition}{Action or Constraint}{Value}

**Example:** At sea state 1 *{Condition}*, the Radar System shall detect targets at ranges out to *{Action or Constraint}* 100 nautical miles *{Value}*.

#### {Subject} {Action} {Value}
**Example:** The Invoice System *{Subject}*, shall display pending customer invoices *{Action}* in which invoices are to be paid.

---
## Conditions
Condition are measurable qualitative or quantitative attributes that are stipulated for a requirement. They allow a requirement to be validated and verified by further qualifying the requirement. It is important to note that conditions may limit choices a designer can make.

## Constraints
Constraints impose restrictions on the design solution or implementation of the systems engineering process. Constraints may be applied in the following scenarios:
- Across all requirements
- specified in relationship to requirement or set of requirements
- standalone requirement

### Constraint Examples
- Interfaces to already existing systems where the interface cannot be changed such as
	- Format
	- Protocol
	- Content
- Physical Size Limitations
- Laws of a particular country
- available duration or budget
- pre-existing technology platform
- user or operator capabilities and limitations
