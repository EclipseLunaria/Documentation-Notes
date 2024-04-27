
# RDF Predicates
### Type
**Reference URI:** http://www.w3.org/1999/02/22-rdf-syntax-ns#type
**Comment:** The subject is an instance of a class

### Comment
**Reference URI:** http://www.w3.org/2000/01/rdf-schema#comment
**Comment:** A description of the subject Resource
### RDF Schema
**Reference URI:** http://www.w3.org/2000/01/rdf-schema#label
**Comment:** A human-readable name for a subject

### Subclass Of
**Reference URI:** http://www.w3.org/2000/01/rdf-schema#subClassOf
**Comment:** The subject is a sub-class of a class.

### SubPropertyOf
**Reference URI:**  http://www.w3.org/2000/01/rdf-schema#subPropertyOf
**Comment:** The subject is a sub-property of a property.

### EquivalentClass
**Reference URI:** http://www.w3.org/2002/07/owl#equivalentClass'
**Comment:** The property that two given classes are equivalent, used in defining datatype definitions


### EquivalentProperty
**Reference URI:** http://www.w3.org/2002/07/owl#equivalentProperty'
**Comment:** The property that determines if two properties are equivalent


## SKOS predicates
*SKOS* stands for [[Simple Knowledge Organization System]] a common data model for sharing and linking knowledge organization systems via the [[Semantic Web]]
### SemanticRelation
**Resource URI:** http://www.w3.org/2004/02/skos/core#semanticRelation
**Comment:** is in semantic relationship with
**Super Property:** Concept

### MappingRelation
**Reference URI:** http://www.w3.org/2004/02/skos/core#mappingRelation
**Comment:** is in mapping relationship with
**Super Property:** Semantic Relation
### CloseMatch
**Reference URI:** http://www.w3.org/2004/02/skos/core#closeMatch
**Comment:** has close match
**Super Property:** Mapping Relation

### ExactMatch
**Reference URI:** http://www.w3.org/2004/02/skos/core#exactMatch
**Comment:** "has exact match"
**Super Property:** CloseMatch


## Schema.org Predicates

### Contributor
**Reference URI:** https://schema.org/contributor
**Comment:** A secondary contributor to the [[Schema.org CreativeWork|CreativeWork]] or [[Schema.org Event|Event]]
Values Expected: 
- [[Schema.org Organization|Organization]]
- [[Schema.org Person|Person]]
**Used on types:**
- [[Schema.org CreativeWork|CreativeWork]]
- [[Schema.org Event|Event]]

### DomainIncludes
**Reference URI:** https://schema.org/domainIncludes
**Comment:** Relates a property to a class that is (one of) the type(s) the property is expected to be used on
**Expected Values:** 
- [[Schema.org Class|Class]]
**Used on:**
- [[Schema.org Property|Property]]

### InverseOf
**Reference URI:** https://schema.org/inverseOf
**Comment:** Relates a property to a property that is its inverse.
**Expected Value:**
- [[Schema.org Property|Property]]
**Used on:**
- [[Schema.org Property|Property]]
**Note:** this property relates two properties to each other but one is in the reverse direction. For example [[Schema.org Alumni]] and [[Schema.org AlumniOf|AlumniOf]] are inverses of eachother

### IsPartOf
**Reference URI:** https://schema.org/isPartOf'
**Comment:** Indicates an item or [[Schema.org CreativeWork|CreativeWork]] that this item or [[Schema.org CreativeWork|CreativeWork]] (in some sense), is part of.
**Expected Value:** 
- [[Schema.org CreativeWork|CreativeWork]]
- [[Schema.org URL|URL]]
**Used on:** 
- [[Schema.org CreativeWork|CreativeWork]]
**Sub-Properties:**
- [[Schema.org inDefinedTermSet|inDefinedTermSet]]
- [[Schema.org partOfEpisode|partOfEpisode]]
- [[Schema.org partOfSeason|partOfSeason]]
- [[Schema.org partOfSeries|partOfSeries]]

### RangeIncludes
**Reference URI:** https://schema.org/rangeIncludes
**Expected Values:**
- [[Schema.org Class|Class]]
**Used on:**
- [[Schema.org Property|Property]]

### SameAs
**Referenced URI:** https://schema.org/sameAs
**Expected Values:**
- [[Schema.org URL|URL]]
**Used on:**
- [[Schema.org Thing|Thing]]

### Source
NOTE: The referenced url returns an error.
**Referenced URI:** https://schema.org/source
**Comments:**  These reference Objects that are sourced from external sources.

### SupersededBy
**Reference URI:** https://schema.org/supersededBy
**Comment:** Relates a term to one that supersedes it
**Expected Values:** 
- [[Schema.org Class|Class]]
- [[Schema.org Enumeration|Enumeration]]
- [[Schema.org Property|Property]]
**Used on:**
- [[Schema.org Class|Class]]
- [[Schema.org Enumeration|Enumeration]]
- [[Schema.org Property|Property]]
