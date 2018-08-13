<img src="image/title.png" alt="subject_image" width="850" height="150">


### Aim of classification
- Segment 38 TripType of visiting custmoers in Walmart to improve customer's shopping experience.


### Data Description
- train.csv : 647054 rows, 7 columns(TripType, VisitNumber, Weekday, Upc, ScanCount DepartmentDescription, FinelineNumber)
- test.csv : 653646 rows, 6 columns(VisitNumber, Weekday, Upc, ScanCount DepartmentDescription, FinelineNumber)
- sample_submission.csv


### File description
- ++Walmart_Preprocessing.ipynb : Data preprocessing++

  **1. Fill in missing values and refining data**
  
    **- DepartmentDescription**
    
      - Number of missing value - 1361.
      - One of attribute of DepartmentDescription, "MENSWEAR" change to "MENS WEAR".
      - One of attribute of DepartmentDescription, "HEALTH AND BEAUTY AIDS"(only have train data) change to "BEUTY".
      
    **- FinelineNumber**
    
      - Number of missing value - 4129.
      
    **- Upc**
    
      - Number of missing value - 4129.
      - Range of the length of Upc is 3 to 12, so Restore the length of the Upc to 12.
      - Divide the Upc into manufacturer number and product number.
    
    
    <img src="image/UPC.png" alt="subject_image" width="600" height="100">
    
  **2. Data encode and derivation**
  
    **- Encode**
    
      - DepartmentDescription
      - Weekday
      - FinelineNumber
      - UPC(Manufacturer part)
      
    **- Derivation**
    
      - Divide by abs_scancount for each above columns were encoded.
      - Add "refund rate" column.


- ++preprocessing_functions.py : functions for preprocessing++
