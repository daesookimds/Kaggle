<img src="image/title.png" alt="subject_image" width="850" height="150">


### Aim of classification
- Segment 38 TripType of visiting custmoers in Walmart to improve customer's shopping experience.


### Data Description
- train.csv : 647054 rows, 7 columns(TripType, VisitNumber, Weekday, Upc, ScanCount DepartmentDescription, FinelineNumber)
- test.csv : 653646 rows, 6 columns(VisitNumber, Weekday, Upc, ScanCount DepartmentDescription, FinelineNumber)
- sample_submission.csv


### File description

- ___Preprocessing - make X_train, y_train, X_test.ipynb : Data preprocessing___

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
      
  **3. Feature Selection**
  
      - DepartmentDescription : 67 columns
      - Weekday : 7 columns
      - FinelineNmber : 5045 columns ( exist in train and test data at the same time )
      - UPC(Manufacturer part) : 5304 columns ( exist in train and test data at the same time )
      - ScanCount : 1 column
      - Refund rate : 1 column
      
      total of columns : 10425 columns
      total of row : 95674 columns ( Group by 'VisitNumber" )
      train data shape : (95674, 10425)

- ___preprocessing_functions.py : functions for UPC preprocessing___


### Model

- ___Use a tree-based model.___

      - RandomForest
      - Xgboost

### Summary & Result

- ___Summary___

    - We classified customer types with information about product categories and customer purchase/refund records.
    
    - Assumptions through Domain Knowledge and Universal Knowledge for Classification
  
        - Use experience knowledge as a buyer
            - The best-selling items in the same category are likely to be sold.
            - The same customer will most likely buy the same things they used to buy.
        
        - Use all information within a category data(DepartmentDescription, FinelineNumber, UPC, Weekday)
            - Different customer types will have different product categories that customers purchase.
            - The more product categories are disaggregated, they can predict more precisely customer types.
            
        - Use tree-based model for interaction of features
      
      
- ___Result___

   - Last model selected : Xgboost
   - Parameter : need more time to Tuning...(now -ing...)
   
   ***Score***
   
   - top 20%
   
   <img src="image/score_01.png" alt="subject_image" width="800" height="100">
   
### Feedback

- Using too many features

      - The number of features is 10425.
      - Too many features cause overfitting.
      
- Did not consider walmart's own rules for dividing TripType

      - Did not consider walmart's own rules for dividing customer types.
      - Only focus the rules that the data shows us.
