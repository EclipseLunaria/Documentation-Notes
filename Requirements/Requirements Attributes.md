In requirements engineering there are many different types of attributes can have below are some important examples of such attributes:
## Important Attributes

### Identification
Identification is an attribute that has the following properties:
- Each requirement should be uniquely identified such as
	- Number - 10403
	- Name Tag - Physical System Limitation
	- Mnemonic - API-001
- Aid in requirements tracing
- May represent links and relationships if necessary or kept separate
- Identification is Immutable (Cannot be changed after assigned)
- Can not be reused (even if requirement is deleted


### Stakeholder Priority
The priority of each requirement **Should*** be identified. This should be through a consensus process among the different [[Stakeholders|stakeholders]]. Below are some potential scales that may be used to identify the priority of each requirement:
- Number scale - 1-5, 1-10, etc.
- Level scale - High, Medium, Low
Priority does not imply that requirements are not necessary. It only help facilitate making decisions when making trade offs to choose the requirement that best fits the [[stakeholders]] needs.


### Dependency
Used to define dependencies between requirements. Some priorities may have a low [[Requirements Attributes#Stakeholder Priority|stakeholder priority]] but be essential for the success of the overall system. This further helps the process of decision making and trade-offs between requirements. The relationship should indicate the relation between requirements such as when a primary requirement is removed then the requirement dependent on it may be removed as well.


### Risk
Risk analysis indicates how much of an impact requirements have on the greater system.  Major risks are related to:
- Potential financial loss
- Potential missed business opportunities
- Losing stakeholder confidence.
- Environmental impact
- Safety or Health issues
- National standards or laws


### Source
Each requirement should have an attribute that indicates where the requirement originates. Identifying the source indicates which organization to consult regarding the following requirements activities.
- Clarification
- Deconfliction
- Modification
- Deletion
Source implies ownership if the requirement indicating where it came from. When a stakeholder issues a requirement then they gain ownership. As requirements are further developed it will indicate which dev team to distribute ownership of the requirement to.


### Rationale
Each requirement should have the reason or justification for why it is needed. The rationale points any of the following materials:
- Supporting analysis
- Trade study
- Modelling simulation
- Other substantive objective evidence


### Difficulty
The difficulty of a requirement is assumed should be noted:
- Easy
- Nominal
- Difficult
Indicates additional context of the breadth and affordability of the requirement. It also helps with [[Cost Modelling|cost modelling]].


### Type
Requirements have different intents and properties which they represent. This classifies requirements into different groups for further analysis and allocation. The various existing type will be explored in more detail [[Requirements Attribute Types|here]]


