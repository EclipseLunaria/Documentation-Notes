Thing is the most generic type of item

## Properties

|                                 **Property**                                 |                                          Expected Type                                          |                                          Description                                          | SuperProperty                                    |
| :--------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------: | :-------------------------------------------------------------------------------------------: | ------------------------------------------------ |
|            [[Schema.org Property additionalType\|additionalType]]            |                       [[Schema.org Text\|Text]], [[Schema.org URL\|URL]]                        |                Typically used for external Data RDF types using URI references                |                                                  |
|             [[Schema.org Property alternateName\|alternateName]]             |                                    [[Schema.org Text\|Text]]                                    |                                     An alias for an item                                      |                                                  |
|               [[Schema.org Property Description\|Description]]               |                [[Schema.org Text\|Text]], [[Schema.org TextObject\|TextObject]]                 |                                   A description of an item                                    |                                                  |
| [[Schema.org Property DisambiguatingDescription\|DisambiguatingDescription]] |                                    [[Schema.org Text\|Text]]                                    |                           Used to disambiguate from similar items.                            | [[Schema.org Property Description\|Description]] |
|                [[Schema.org Property Identifier\|Identifier]]                | [[Schema.org PropertyValue\|PropertyValue]], [[Schema.org Text\|Text]], [[Schema.org URL\|URL]] |      Represents any type of identifier for any type of thing. (I.E. ISBNs, UUIDs, etc.)       |                                                  |
|                     [[Schema.org Property Image\|Image]]                     |                [[Schema.org ImageObject\|ImageObject]], [[Schema.org URL\|URL]]                 |                                      An image of an item                                      |                                                  |
|          [[Schema.org Property MainEntityOfPage\|MainEntityOfPage]]          |               [[Schema.org CreativeWork\|CreativeWork]], [[Schema.org URL\|URL]]                |               Indicates a page or other creative work that the item is apart of               |                                                  |
|                      [[Schema.org Property Name\|Name]]                      |                                    [[Schema.org Text\|Text]]                                    |                                      The name of an item                                      | rdfs:label                                       |
|           [[Schema.org Property potentialAction\|potentialAction]]           |                                  [[Schema.org Action\|Action]]                                  |                  Indicates the idealized action that is taken by the object                   |                                                  |
|                    [[Schema.org Property sameAs\|sameAs]]                    |                                     [[Schema.org URL\|URL]]                                     | URL of a reference page that indicates the items identity like a companies social media pages |                                                  |
|                 [[Schema.org Property subjectOf\|subjectOf]]                 |             [[Schema.org CreativeWork\|CreativeWork]], [[Schema.org Event\|Event]]              |                             Creative work or event of this thing.                             |                                                  |
|                       [[Schema.org Propety Url\|Url]]                        |                                     [[Schema.org URL\|URL]]                                     |                                        URL of an item                                         |                                                  |

## Children
### [[Schema.org Action|Action]]
### [[Schema.org BioChemEntity|BioChemEntity]]

### [[Schema.org CreativeWork|CreativeWork]]

### [[Schema.org Event|Event]]

### [[Schema.org Intangible|Intangible]]
### [[Schema.org MedicalEntity|MedicalEntity]]

### [[Schema.org Organization|Organization]]

### [[Schema.org Person|Person]]

### [[Schema.org Place|Place]]
### [[Schema.org Product|Product]]


## Examples

### 1. Building
```JSON
{
	"context" : "http://schema.org",
	"@type" : "Thing",
	"name" : "Building"
}
```