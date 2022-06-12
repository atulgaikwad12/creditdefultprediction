# Credit Defult Prediction
  ML Project to predict probability of credit default by  cardholder, based on  various characteristics 
  and payment behavior of cardholder.  
---
***
     
## Raw Data Description

> This dataset contains information on default payments, demographic factors, credit data, history of payment, and bill statements of credit card clients in Taiwan from April 2005 to September 2005.


* **ID**: ID of each client

* **LIMIT_BAL**: Amount of given credit in NT dollars (includes individual and family/supplementary credit

* **SEX**: Gender (1=male, 2=female)

* **EDUCATION**: (1=graduate school, 2=university, 3=high school, 4=others, 5=unknown, 6=unknown)

* **MARRIAGE**: Marital status (1=married, 2=single, 3=others)

* **AGE**: Age in years

* **PAY_0 to PAY_6**
  * PAY_0: Repayment status in September, 2005
    1. "-1" = pay duly, 1=payment delay for one month
    2. "2" = payment delay for two months.....
    3. "8" = payment delay for eight months 
    4. "9" = payment delay for nine months and above  
     

  * PAY_2: Repayment status in August, 2005 (scale same as above)
  * PAY_3: Repayment status in July, 2005 (scale same as above)
  * PAY_4: Repayment status in June, 2005 (scale same as above)
  * PAY_5: Repayment status in May, 2005 (scale same as above)
  * PAY_6: Repayment status in April, 2005 (scale same as above)

* **BILL_AMT1 to BILL_AMT6** 
  * BILL_AMT1: Amount of bill statement in September, 2005 (NT dollar)
  * BILL_AMT2: Amount of bill statement in August, 2005 (NT dollar)
  * BILL_AMT3: Amount of bill statement in July, 2005 (NT dollar)
  * BILL_AMT4: Amount of bill statement in June, 2005 (NT dollar)
  * BILL_AMT5: Amount of bill statement in May, 2005 (NT dollar)
  * BILL_AMT6: Amount of bill statement in April, 2005 (NT dollar)

* **PAY_AMT1 to PAY_AMT6**
  * PAY_AMT1: Amount of previous payment in September, 2005 (NT dollar)
  * PAY_AMT2: Amount of previous payment in August, 2005 (NT dollar)
  * PAY_AMT3: Amount of previous payment in July, 2005 (NT dollar)
  * PAY_AMT4: Amount of previous payment in June, 2005 (NT dollar)
  * PAY_AMT5: Amount of previous payment in May, 2005 (NT dollar)
  * PAY_AMT6: Amount of previous payment in April, 2005 (NT dollar)

* **default.payment.next.month** : Default payment (1=yes, 0=no)
***
## Acknowledgement for dataset -
>*The original dataset can be found here at the UCI Machine Learning Repository.*\
Lichman, M. (2013). [UCI Machine Learning Repository](http://archive.ics.uci.edu/ml). Irvine, CA: University of California, School of Information and Computer Science.

---
## Project Installation Steps :-
`Conda command to create virtual env inside current directory`
```
conda create --prefix ./env python=3.7 -y && conda activate ./env
```

`To install required libraries listed inside requirements.txt `
```buildoutcfg
pip install requirements.txt
conda list
```

`To create conda.yaml file which will be used by mlflow`
```bash
conda env export > conda.yaml
```

`Git commands to publish code (remote repo - "origin", local branch default name -  "master", renamed to "main") `
```buildoutcfg 
git init 
git add .
git commit -m 'First Commit Msg'
git status 
git remote add origin git@github.com:username/new_repo
git branch -m master main
git push -u origin main
```

`MlFlow command to run Project`
`To consider default entry point main`
```bash
mlflow run . --no-conda
```
`run any specific entry point in MLproject file`
```bash
mlflow run . -e get_data --no-conda
```
`Passing config file overriding the defult defined inside MLproject file`
```bash
mlflow run . -e get_data -P config=configs/your_config.yaml --no-conda
```
`Defining experiment name` 
```bash
mlflow run . -e main --experiment-name firstime --no-conda
```