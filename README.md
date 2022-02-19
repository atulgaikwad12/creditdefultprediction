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

`If using git bash then activate base using below command`
```buildoutcfg
source activate base
```

`Else for cmd use`
```
conda activate base
```

 `To Create Conda Enviroment and activate it` 
```buildoutcfg
conda create -n <envName> python=3.7 -y
conda env list
activate <envName>
```

`To install required libraries listed inside requirements.txt `
```buildoutcfg
pip install requirements.txt
conda list
```

`To freeze requirements.txt`
```buildoutcfg
pip freeze>requirements.txt
```

`Git commands to publish code (remote repo - "origin", local branch default name -  "master") `
```buildoutcfg 
git init 
git add .
git commit -m 'First Commit Msg'
git status 
git remote add origin git@github.com:username/new_repo
git push -u origin master
```

### Extra git commands just for reference
`Stash changes to clean working tree (so to work with new changes keeping old changes stored temporay aside)`
```
git status
git stash
```
`Clean stash & again apply to working tree`
```
git status
git stash pop
```
`Reapply stash without cleaning it`
```
git status
git stash apply
```

`Sync local repository with remote one (remote repo - origin)`
```
git diff
git fetch origin
git log --oneline main..origin/main
git checkout main
git log origin/main
git merge origin/main
```

`Remove file from stagging area`
```
git status
git rm --cached fileName
```

`To see last commit log (press q to quit)`
```
git log -p -1
```

`To see summarized status`
```
git status -s
```

`To create new branch and switch to it`
```
git branch <newbranchnaame>
git branch
git checkout <newbranchName>
```
`Alternate way to do same `
```
git checkout - b <newBranchName>
```

`To merge new branch changes to master`
```
git checkout master
git merge <newbranchname>
```

`Clone any repository in local`
```
git clone <repo_url> <optional_foldename>
``` 

`To see merged/Non merged branch`
```
git branch --merged
git branch --non-merged
```

`To delete merged branch`
```
git branch -d <BranchName>
```

`To delete non merged branch`
```
git branch -D <BranchName>
```

`To unstage files from staging area not changing working directory so to match last commit`
```
git reset
```

`To unstage files from staging area as well as from working directory so to match last commit`
```
git reset
```