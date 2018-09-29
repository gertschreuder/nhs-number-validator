# NHS number validator 
## A simple NHS number validator, following the process described in the NHS Data Dictionary.

The [NHS NUMBER](https://www.datadictionary.nhs.uk/data_dictionary/attributes/n/nhs/nhs_number_de.asp?shownav=1), the primary identifier of a [PERSON](https://www.datadictionary.nhs.uk/data_dictionary/classes/p/person_de.asp?shownav=1), is a unique identifier for a [PATIENT](https://www.datadictionary.nhs.uk/data_dictionary/classes/p/patient_de.asp?shownav=1) within the NHS in England and Wales.

This will not vary by any [Organisation](https://www.datadictionary.nhs.uk/data_dictionary/nhs_business_definitions/o/organisation_de.asp?shownav=1) of which a [PERSON](https://www.datadictionary.nhs.uk/data_dictionary/classes/p/person_de.asp?shownav=1) is a [PATIENT](https://www.datadictionary.nhs.uk/data_dictionary/classes/p/patient_de.asp?shownav=1).

It is mandatory to record the [NHS NUMBER](https://www.datadictionary.nhs.uk/data_dictionary/attributes/n/nhs/nhs_number_de.asp?shownav=1). There are exceptions, such as Accident and Emergency care, sexual health and major incidents, as defined in existing national policies.

The [NHS NUMBER](https://www.datadictionary.nhs.uk/data_dictionary/attributes/n/nhs/nhs_number_de.asp?shownav=1) is 10 numeric digits in length. The tenth digit is a check digit used to confirm its validity. The check digit is validated using the Modulus 11 algorithm and the use of this algorithm is mandatory. There are 5 steps in the validation of the check digit:

**Step 1**  Multiply each of the first nine digits by a weighting factor as follows:

**Digit Position**
(starting from the left) Factor:

| 1 | 10 |
| --- | --- |
| 2 | 9 |
| 3 | 8 |
| 4 | 7 |
| 5 | 6 |
| 6 | 5 |
| 7 | 4 |
| 8 | 3 |
| 9 | 2 |

**Step 2**  Add the results of each multiplication together.

**Step 3**  Divide the total by 11 and establish the remainder.

**Step 4**  Subtract the remainder from 11 to give the check digit.

If the result is 11 then a check digit of 0 is used. If the result is 10 then the [NHS NUMBER](https://www.datadictionary.nhs.uk/data_dictionary/attributes/n/nhs/nhs_number_de.asp?shownav=1) is invalid and not used.

**Step 5**  Check the remainder matches the check digit. If it does not, the [NHS NUMBER](https://www.datadictionary.nhs.uk/data_dictionary/attributes/n/nhs/nhs_number_de.asp?shownav=1) is invalid.